"""Print a small, decision-focused evidence summary of supplied project files."""
from pathlib import Path
import json,re
base=Path(__file__).resolve().parents[1]/'tmp/source_extracts'
rules={
'lifestyle':r'Abstract|105,138|107 displayed|SDS-score edge|stable|holdout|network has|direct SDS|31,013|29\.5%|r = -0\.125|does not|Figure [1234]\.',
'abm':r'29,139|134 papers|2,495|2,495 papers|1\.50%|5\.65%|59\.6%|40\.4%|communities increased|communities.*52|8 to 52|Cochran|Figure (1|6|9|12|16|18|21|22|23)\.',
'cisc':r'309 samples|14,794|TCGA-CESC|GTEx|baseline|survival|AUC|Figure|14 genes|WGCNA|top.*genes|Tumor|Normal',
'ev':r'8058|8,058|403份|368份|91\.32|LDA|续航|充电|Cronbach|0\.9[0-9]|随机森林.*重要性|K-means|Figure|信度|效度|下表|总计',
}
for key,pattern in rules.items():
    print(f'\n[{key.upper()}]')
    path=base/f'{key}.json'
    info=json.loads(path.read_text(encoding='utf-8'))
    print('FILE:',info['file'])
    print('HEADINGS:', ' | '.join(info.get('headings',[])[:40]))
    for t in info.get('tables',[]):
        samples=t['sample']
        headers=samples[0] if samples else []
        row_preview=[row for row in samples[1:] if any(re.search(pattern,str(cell),re.I) for cell in row)]
        if row_preview:print(f"TABLE {t['index']} {t['rows']} rows HEAD: {headers} RESULTS: {row_preview[:4]}")
    for i,line in enumerate(info['text']):
        if re.search(pattern,line,re.I):print(f'P{i}: {line[:250]}')
    if key=='ev':
        for i,t in enumerate(info.get('tables',[]),1):
            s=' '.join(' '.join(row) for row in t['sample'])
            print(f'TABLE {i} {t["rows"]}x{t["cols"]}: {s[:300]}')

print('\n[FOCUSED TABLES AND FIGURE CAPTIONS]')
for key,table_ids in {'lifestyle':(1,2,3),'abm':(1,2),'cisc':(1,2,3,4,5,6,7,8,9,10,11),'ev':(4,6,7,8,9,10,15,16,17)}.items():
 d=json.loads((base/f'{key}.json').read_text(encoding='utf-8'))
 for number in table_ids:
  table=d.get('tables',[])[number-1]
  print(f'{key} TABLE {number} {table["rows"]}x{table["cols"]}: '+json.dumps(table.get('sample',[]),ensure_ascii=False)[:800])
 for i,line in enumerate(d.get('text',[])):
  if re.match(r'Figure\s*\d+\.|Fig\.?\s*\d+|图\s*\d+|图\d+',line,re.I):print(f'{key} P{i}: {line[:300]}')
