#!/usr/bin/env python3
"""Regenerate localized vCards using the exact portrait and explicit canonical URL."""
import base64
import json
from pathlib import Path
from urllib.parse import urlparse
ROOT = Path(__file__).resolve().parents[1] / 'maria'
c = json.loads((ROOT/'site-config.json').read_text('utf-8'))
url = c.get('publicCardUrl')
u = urlparse(url or '')
if u.scheme!='https' or not u.netloc or u.query or u.fragment:
    raise SystemExit('ERROR: explicit canonical HTTPS publicCardUrl is required')
photo = (ROOT/c['photo']).read_bytes()
if not(photo.startswith(b'\xff\xd8') and photo.endswith(b'\xff\xd9')):
    raise SystemExit('ERROR: portrait JPEG signature is invalid')
def escape(t):
    return str(t).replace('\\','\\\\').replace('\r','').replace('\n','\\n').replace(',','\\,').replace(';','\\;')
def fold(t):
    out=[]; line=''
    for ch in t:
        if len((line+ch).encode('utf-8'))>75:
            out.append(line)
            line=' '+ch
        else: line+=ch
    return out+[line]
all_links=c['socials']+c['contacts']
links=[]
for label,icon in [('Instagram','instagram'),('Telegram','telegram'),('WhatsApp','whatsapp'),('Viber','viber')]:
    a=[x['url'] for x in all_links if x.get('icon')==icon and x.get('url')]
    if len(a)!=1: raise SystemExit(f'ERROR: exactly one {icon} URL required, got {len(a)}')
    links.append(f'URL;TYPE={label}:{a[0]}')
encoded=base64.b64encode(photo).decode('ascii')
photo_lines=['PHOTO;ENCODING=b;TYPE=JPEG:'+encoded[:42]]
photo_lines+=[' '+encoded[i:i+72] for i in range(42,len(encoded),72)]
for language,firstname,surname in [('ru','Мария','Кравченко Артемьева'),('uk','Марія',"Кравченко Артем'єва")]:
    p=c['locales'][language]
    fields=['BEGIN:VCARD','VERSION:3.0',f'N:{escape(surname)};{escape(firstname)};;;',f'FN:{escape(p["name"])}',f'TITLE:{escape(p["title"])}',f'TEL;TYPE=CELL,VOICE:{c["phone"]}',f'URL:{url}',*links]
    lines=[l for field in fields for l in fold(field)]+photo_lines+['END:VCARD']
    content=('\r\n'.join(lines)+'\r\n').encode('utf-8')
    dest=ROOT/('contact-'+language+'.vcf')
    dest.write_bytes(content)
    print(language,len(content),'bytes',url)
