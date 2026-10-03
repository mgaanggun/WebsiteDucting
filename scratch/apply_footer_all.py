import glob
import re

# Read the standard footer directly from ducting-bjls.html
with open('ducting-bjls.html', 'r', encoding='utf-8') as fp:
    bjls_content = fp.read()

m_footer = re.search(r'(<footer\s+id="footer"[^>]*>.*?</footer>)', bjls_content, re.DOTALL)
if not m_footer:
    print("ERROR: Could not find footer in ducting-bjls.html")
    exit(1)

target_footer = m_footer.group(1)
print(f"Target footer length: {len(target_footer)} characters")

# Check all HTML files
html_files = sorted(glob.glob('*.html'))
updated_count = 0
already_matched = 0

footer_regex = re.compile(r'<footer\s+id="footer"[^>]*>.*?</footer>', re.DOTALL)

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    m = footer_regex.search(content)
    if not m:
        print(f"WARNING: No footer found in {fname}")
        continue
    
    current_footer = m.group(0)
    if current_footer.strip() == target_footer.strip():
        already_matched += 1
        print(f"Already matching: {fname}")
    else:
        new_content = footer_regex.sub(target_footer, content)
        with open(fname, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        updated_count += 1
        print(f"UPDATED: {fname}")

print(f"\nSummary: {updated_count} files updated, {already_matched} files already matched out of {len(html_files)} total.")
