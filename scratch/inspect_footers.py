import glob
import re

files = sorted(glob.glob('*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.search(r'<footer\s+id="footer"[^>]*>(.*?)</footer>', c, re.DOTALL)
    if m:
        footer_content = m.group(1)
        has_newsletter = 'footer-newsletter' in footer_content
        has_sudirman = 'Sudirman' in footer_content
        has_dark = 'dark-background' in c[m.start():m.start()+50]
        print(f"{f:35s}: dark={has_dark}, sudirman={has_sudirman}, newsletter={has_newsletter}")
    else:
        print(f"{f:35s}: NO FOOTER FOUND")
