import glob
import re
import urllib.parse

files = sorted(glob.glob('produk-*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    m_h2 = re.search(r'<h2>(.*?)</h2>', content)
    h2 = m_h2.group(1) if m_h2 else ''
    m_btn = re.search(r'<div class="project-cta[^"]*">(.*?)</div>', content, re.DOTALL)
    btn = m_btn.group(1).strip() if m_btn else ''
    print(f"{f}: H2 = {h2}")
    print(f"  Current btn: {btn}")
