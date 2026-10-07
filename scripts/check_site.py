"""Check generated routes, translations, local assets and anchors; stdlib only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / 'public'

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.ids=set(); self.lang=None; self.translation=None; self.h1=0; self.text=[]; self.prose_text=[]; self.in_prose=0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag == 'div' and 'prose' in attrs.get('class','').split(): self.in_prose += 1
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag == 'html': self.lang=attrs.get('lang')
        if tag == 'h1': self.h1 += 1
        if tag == 'a' and 'language-switch' in attrs.get('class',''): self.translation=attrs.get('href')
        for attribute in ('href','src'):
            if attribute in attrs: self.links.append((tag,attrs[attribute],attrs))
    def handle_data(self, data):
        self.text.append(data)
        if self.in_prose: self.prose_text.append(data)
    def handle_endtag(self, tag):
        if tag == 'div' and self.in_prose: self.in_prose -= 1

files=list(output.rglob('*.html'))
documents={p:Document(p.read_text(encoding='utf-8')) for p in files}
errors=[]; count=0; referenced_css=set()
config=(root/'hugo.toml').read_text(encoding='utf-8')
default_base=re.search(r"baseURL\s*=\s*'([^']+)'", config).group(1)
# Detect the canonical base URL in built output, including project-site subpaths.
home=(output/'index.html').read_text(encoding='utf-8')
base_match=re.search(r'<link[^>]*rel=["\']?canonical["\']?[^>]*href=["\']?([^"\' >]+)',home)
base=urlsplit(base_match.group(1) if base_match else default_base)
prefix=base.path.rstrip('/')

def resolve(url, origin):
    parsed=urlsplit(url)
    if parsed.scheme and (parsed.scheme not in ('https','http') or parsed.netloc != base.netloc): return None
    if parsed.netloc and parsed.netloc != base.netloc: return None
    path=unquote(parsed.path)
    if path.startswith('/'):
        if prefix and not (path == prefix or path.startswith(prefix+'/')):
            errors.append(f'{origin.relative_to(output)}: outside site base path: {url}')
            return None
        path=path[len(prefix):].lstrip('/')
        dest=output/path
    elif path: dest=origin.parent/path
    else: dest=origin
    if dest.is_dir() or path.endswith('/'): dest=dest/'index.html'
    if not dest.exists(): errors.append(f'{origin.relative_to(output)}: missing {url}')
    elif parsed.fragment and dest.suffix=='.html' and unquote(parsed.fragment) not in documents.get(dest,Document(dest.read_text(encoding='utf-8'))).ids:
        errors.append(f'{origin.relative_to(output)}: missing anchor {url}')
    return dest

for path,doc in documents.items():
    # Hugo's /en/ redirect is a generated alias, not a content page.
    if path == output/'en/index.html': continue
    if not doc.lang: errors.append(f'{path}: missing language')
    if not doc.h1: errors.append(f'{path}: missing main heading')
    if '**' in ''.join(doc.prose_text): errors.append(f'{path}: unrendered Markdown emphasis')
    if 'Liu YuChen' not in ''.join(doc.text) or 'LYC' not in ''.join(doc.text): errors.append(f'{path}: incorrect brand')
    if path.name != '404.html' and not doc.translation: errors.append(f'{path}: missing language switch')
    for tag,url,attrs in doc.links:
        if not url: errors.append(f'{path}: empty URL'); continue
        if tag=='link' and attrs.get('rel') in ('canonical','alternate'): continue
        resolved=resolve(url,path); count+=1
        if tag == 'link' and attrs.get('rel') == 'stylesheet' and resolved: referenced_css.add(resolved)
    if doc.translation:
        target=resolve(doc.translation,path)
        if target in documents:
            if documents[target].lang == doc.lang: errors.append(f'{path}: switch points to same language')
            back=documents[target].translation
            if not back or resolve(back,target) != path: errors.append(f'{path}: translation does not link back')

for css in referenced_css:
    for url in re.findall(r'url\(["\']?([^\)"\']+)',css.read_text(encoding='utf-8')):
        resolve(url,css); count+=1
research_routes=('lifestyle-networks','literature-intelligence','gastric-gist','cervical-transcriptomics','xiamen-nev-market')
for route in ('','about','research','gallery','notes',*(f'research/{slug}' for slug in research_routes)):
    for lang in ('','zh'):
        if not (output/lang/route/'index.html').exists(): errors.append(f'Missing route: {lang}/{route}')
en=json.loads((root/'i18n/en.json').read_text(encoding='utf-8'))
zh=json.loads((root/'i18n/zh.json').read_text(encoding='utf-8'))
if en.keys() != zh.keys(): errors.append('Translation keys differ')
for path in (root/'layouts').rglob('*.html'):
    for key in re.findall(r'i18n\s+"([^"]+)"',path.read_text(encoding='utf-8')):
        if key not in en: errors.append(f'{path}: missing translation {key}')
for slug in research_routes:
    for lang in ('en','zh'):
        source=root/'content'/lang/'research'/f'{slug}.md'
        route=output/('' if lang=='en' else 'zh')/'research'/slug/'index.html'
        if not source.exists() or not route.exists(): errors.append(f'Missing research project: {lang}/{slug}')
        elif not any(marker in route.read_text(encoding='utf-8') for marker in ('class="results-figure"','class=results-figure')):
            errors.append(f'{lang}/{slug} has no results chart')
        if route.exists() and '**' in ''.join(documents.get(route,Document(route.read_text(encoding='utf-8'))).prose_text):
            errors.append(f'{lang}/{slug}: unrendered Markdown emphasis')
for path in files:
    if any(term in path.as_posix().lower() for term in ('campus-cats','multi-omics')): errors.append(f'Deleted project remains: {path.relative_to(output)}')
for path in (root/'content').rglob('*.md'):
    if 'campus-cats' in path.name or 'multi-omics' in path.name: errors.append(f'Deleted source content remains: {path.relative_to(root)}')
if (output/'files/CV.pdf').read_bytes() != (root/'static/files/CV.pdf').read_bytes(): errors.append('CV changed during build')
if not (output/'.nojekyll').exists(): errors.append('.nojekyll missing')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'PASS: {len(documents)} HTML files; {count} local/link references; 22 content routes; reciprocal language switching; {len(en)} bilingual UI keys; 10 research result charts; CV and .nojekyll.')
