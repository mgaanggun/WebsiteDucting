import glob
import re
import urllib.parse

files = sorted(glob.glob('produk-*.html'))
phone_number = "6285210620252"

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Extract title from <h2>
    m_h2 = re.search(r'<h2>(.*?)</h2>', content)
    title = m_h2.group(1).strip() if m_h2 else "Produk Ducting HVAC"
    # Clean HTML entities if any
    clean_title = title.replace('&amp;', '&').replace('&quot;', '"')
    
    msg = f"Halo Ducting HVAC, saya ingin minta penawaran harga untuk produk {clean_title}."
    wa_url = f"https://wa.me/{phone_number}?text={urllib.parse.quote(msg)}"
    
    # Replace CTA button
    old_btn_pattern = r'<a\s+href="contact\.html"\s+class="btn-main\s+w-100\s+text-center">Minta Penawaran Harga Produk</a>'
    new_btn = f'<a href="{wa_url}" target="_blank" rel="noopener noreferrer" class="btn-main w-100 text-center"><i class="bi bi-whatsapp me-2"></i>Minta Penawaran Harga Produk</a>'
    
    if re.search(old_btn_pattern, content):
        content = re.sub(old_btn_pattern, new_btn, content)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        print(f"Updated {f} with WhatsApp link for '{clean_title}'")
    else:
        print(f"Pattern not found in {f}")

# Also update scratch/build_product_pages.py
build_script = 'scratch/build_product_pages.py'
with open(build_script, 'r', encoding='utf-8') as fp:
    b_content = fp.read()

# In build_product_pages.py, find template
old_b_btn = '<a href="contact.html" class="btn-main w-100 text-center">Minta Penawaran Harga Produk</a>'
if old_b_btn in b_content:
    # Update to dynamic or template
    b_content = b_content.replace(
        old_b_btn,
        '<a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20penawaran%20harga%20untuk%20produk." target="_blank" rel="noopener noreferrer" class="btn-main w-100 text-center"><i class="bi bi-whatsapp me-2"></i>Minta Penawaran Harga Produk</a>'
    )
    with open(build_script, 'w', encoding='utf-8') as fp:
        fp.write(b_content)
    print("Updated build_product_pages.py")
