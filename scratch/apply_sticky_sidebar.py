import glob
import re

files = sorted(glob.glob('produk-*.html')) + ['project-details.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # We want to replace:
    # <div class="col-lg-4">
    #   <div class="project-info-card" ...>
    #     ...
    #   </div>
    #   <div class="help-box mt-4" ...>
    #     ...
    #   </div>
    # </div>
    # with:
    # <div class="col-lg-4">
    #   <div class="product-sticky-sidebar">
    #     <div class="project-info-card">
    #       ...
    #     </div>
    #     <div class="help-box mt-3">
    #       ...
    #     </div>
    #   </div>
    # </div>
    
    # Regex pattern to match the col-lg-4 content
    pattern = re.compile(
        r'<div class="col-lg-4">\s*<div class="project-info-card"[^>]*>(.*?)</div>\s*<div class="help-box mt-4"[^>]*>(.*?)</div>\s*</div>',
        re.DOTALL
    )
    
    match = pattern.search(content)
    if match:
        card_inner = match.group(1)
        help_inner = match.group(2)
        
        replacement = f'''<div class="col-lg-4">
            <div class="product-sticky-sidebar">
              <div class="project-info-card">
{card_inner.rstrip()}
              </div>

              <div class="help-box mt-3">
{help_inner.rstrip()}
              </div>
            </div>
          </div>'''
        
        content = pattern.sub(replacement, content)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        print(f"Updated sticky sidebar in {f}")
    else:
        print(f"Pattern NOT matched in {f}")

# Also update scratch/build_product_pages.py
b_file = 'scratch/build_product_pages.py'
with open(b_file, 'r', encoding='utf-8') as fp:
    b_content = fp.read()

old_b_sidebar = '''          <div class="col-lg-4">
            <div class="project-info-card" data-aos="fade-up" data-aos-delay="100">
              <h3>Spesifikasi Produk</h3>
              <ul class="info-list">
                {specs_html}
              </ul>
              <div class="project-cta mt-4">
                <a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20penawaran%20harga%20untuk%20produk." target="_blank" rel="noopener noreferrer" class="btn-main w-100 text-center"><i class="bi bi-whatsapp me-2"></i>Minta Penawaran Harga Produk</a>
              </div>
            </div>

            <div class="help-box mt-4" data-aos="fade-up" data-aos-delay="200">
              <div class="help-icon">
                <i class="bi bi-fan"></i>
              </div>
              <h4>Konsultasi Spesifikasi Produk</h4>
              <p>Diskusikan kebutuhan dimensi saluran, perhitungan CFM, atau kustomisasi fabrikasi bersama tim engineer kami.</p>
              <a href="tel:085210620252" class="help-phone"><i class="bi bi-telephone-fill"></i> 0852-1062-0252</a>
            </div>
          </div>'''

new_b_sidebar = '''          <div class="col-lg-4">
            <div class="product-sticky-sidebar">
              <div class="project-info-card">
                <h3>Spesifikasi Produk</h3>
                <ul class="info-list">
                  {specs_html}
                </ul>
                <div class="project-cta mt-4">
                  <a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20penawaran%20harga%20untuk%20produk." target="_blank" rel="noopener noreferrer" class="btn-main w-100 text-center"><i class="bi bi-whatsapp me-2"></i>Minta Penawaran Harga Produk</a>
                </div>
              </div>

              <div class="help-box mt-3">
                <div class="help-icon">
                  <i class="bi bi-fan"></i>
                </div>
                <h4>Konsultasi Spesifikasi Produk</h4>
                <p>Diskusikan kebutuhan dimensi saluran, perhitungan CFM, atau kustomisasi fabrikasi bersama tim engineer kami.</p>
                <a href="tel:085210620252" class="help-phone"><i class="bi bi-telephone-fill"></i> 0852-1062-0252</a>
              </div>
            </div>
          </div>'''

if old_b_sidebar in b_content:
    b_content = b_content.replace(old_b_sidebar, new_b_sidebar)
    with open(b_file, 'w', encoding='utf-8') as fp:
        fp.write(b_content)
    print("Updated build_product_pages.py")
