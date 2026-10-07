"""Build, verify and package the website without uploading; stdlib only."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
delivery=root/'delivery'
delivery.mkdir(exist_ok=True)
build=root/'tmp/package-site'
subprocess.run(['hugo','--cleanDestinationDir','--minify','--destination',str(build)],cwd=root,check=True)
subprocess.run([sys.executable,str(root/'scripts/check_site.py'),str(build)],cwd=root,check=True)
static_zip=delivery/'Liu-YuChen-GitHub-Pages.zip'
with ZipFile(static_zip,'w',ZIP_DEFLATED) as archive:
    for path in sorted(build.rglob('*')):
        if path.is_file(): archive.write(path,path.relative_to(build).as_posix())
source_zip=delivery/'Liu-YuChen-Website-Source.zip'
excluded={'delivery','tmp','public','resources','node_modules','.git'}
with ZipFile(source_zip,'w',ZIP_DEFLATED) as archive:
    for path in sorted(root.rglob('*')):
        relative=path.relative_to(root)
        if any(part in excluded or part=='__pycache__' for part in relative.parts): continue
        if path.is_file() and path.name != '.hugo_build.lock': archive.write(path,relative.as_posix())
    archive.write(delivery/'VERIFICATION.md','VERIFICATION.md')
for path in (static_zip,source_zip):
    with ZipFile(path) as archive:
        corrupt=archive.testzip()
        if corrupt: raise RuntimeError(f'Corrupt ZIP member: {corrupt}')
        names=set(archive.namelist())
        required={'index.html','zh/index.html','.nojekyll','files/CV.pdf'} if path==static_zip else {'hugo.toml','.github/workflows/pages.yml','README.md','themes/tella-master/LICENSE'}
        if not required <= names: raise RuntimeError(f'Missing ZIP members: {required-names}')
        print(f'{path.name}: {len(names)} files, {path.stat().st_size:,} bytes, ZIP integrity verified')
manifest='\n'.join(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}' for path in (static_zip,source_zip))+'\n'
(delivery/'SHA256SUMS.txt').write_text(manifest,encoding='utf-8')
