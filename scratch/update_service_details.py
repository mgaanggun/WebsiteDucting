import re

with open("d:/Constructify-pro/service-details.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Detail Layanan - Fabrikasi &amp; Instalasi Ducting HVAC</title>',
    content
)

content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Informasi mendalam tentang layanan fabrikasi dan instalasi ducting HVAC terpadu: spesifikasi teknis, standar SMACNA, pengujian air balancing, dan garansi kebocoran.">',
    content
)

content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="detail layanan ducting hvac, instalasi saluran udara, fabrikasi ducting bjls, ducting pu, air balancing tab">',
    content
)

# 2. Breadcrumbs
content = re.sub(
    r'<li class="current">Konstruksi Residensial</li>',
    '<li class="current">Instalasi &amp; Fabrikasi Ducting HVAC</li>',
    content
)

# 3. Main Service Details Section
old_section_pattern = r'<!-- Service Details Section -->.*?<!-- /Service Details Section -->'
new_section = '''<!-- Service Details Section -->
    <section id="service-details" class="service-details section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-5">

          <div class="col-lg-5">
            <div class="service-sidebar">

              <div class="service-overview" data-aos="fade-up" data-aos-delay="100">
                <div class="overview-header">
                  <i class="bi bi-fan"></i>
                  <h3>Ringkasan Layanan</h3>
                </div>
                <div class="overview-content">
                  <h2>Sistem Ducting HVAC Terpadu</h2>
                  <p>Kami merancang, memproduksi, dan menginstalasi sistem saluran udara (ducting) HVAC terpadu untuk gedung komersial, rumah sakit, restoran, dan fasilitas industri. Mengedepankan efisiensi aliran aerodinamis, isolasi termal anti-kondensasi, dan standar SMACNA.</p>
                  <div class="cta-button">
                    <a href="contact.html" class="btn-get-started">Minta Penawaran Biaya</a>
                  </div>
                </div>
              </div>

              <div class="key-benefits" data-aos="fade-up" data-aos-delay="200">
                <h4>Keunggulan Utama</h4>
                <ul>
                  <li><i class="bi bi-check-circle-fill"></i> Perhitungan CFM &amp; Static Pressure presisi tinggi</li>
                  <li><i class="bi bi-check-circle-fill"></i> Fabrikasi otomatis CNC dengan flange kedap udara</li>
                  <li><i class="bi bi-check-circle-fill"></i> Material bersertifikasi standar SMACNA &amp; SNI</li>
                  <li><i class="bi bi-check-circle-fill"></i> Pilihan material fleksibel: BJLS Galvalum &amp; PU Panel</li>
                  <li><i class="bi bi-check-circle-fill"></i> Pengujian Testing, Adjusting &amp; Balancing (TAB) resmi</li>
                </ul>
              </div>

              <div class="contact-card" data-aos="fade-up" data-aos-delay="300">
                <div class="contact-header">
                  <i class="bi bi-headset"></i>
                  <h4>Butuh Konsultasi Teknis?</h4>
                </div>
                <div class="contact-info">
                  <div class="info-row">
                    <i class="bi bi-telephone"></i>
                    <div>
                      <span>Hubungi Kami</span>
                      <p><a href="tel:085210620252" class="text-white">0852-1062-0252</a></p>
                    </div>
                  </div>
                  <div class="info-row">
                    <i class="bi bi-envelope"></i>
                    <div>
                      <span>Email Konsultasi</span>
                      <p>info@ductinghvac.co.id</p>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>

          <div class="col-lg-7">
            <div class="service-content">

              <div class="image-gallery" data-aos="zoom-in" data-aos-delay="100">
                <div class="service-details-slider swiper init-swiper">
                  <script type="application/json" class="swiper-config">
                    {
                      "loop": true,
                      "speed": 800,
                      "autoplay": {
                        "delay": 5000
                      },
                      "slidesPerView": 1,
                      "effect": "fade",
                      "navigation": {
                        "nextEl": ".swiper-button-next",
                        "prevEl": ".swiper-button-prev"
                      },
                      "pagination": {
                        "el": ".swiper-pagination",
                        "type": "bullets",
                        "clickable": true
                      }
                    }
                  </script>
                  <div class="swiper-wrapper align-items-center">
                    <div class="swiper-slide">
                      <img src="assets/img/ducting/ducting-ac.jpg" alt="Instalasi Saluran Ducting AC Sentral" class="img-fluid" loading="lazy">
                    </div>
                    <div class="swiper-slide">
                      <img src="assets/img/ducting/ducting-pu.jpg" alt="Fabrikasi Panel Ducting PU" class="img-fluid" loading="lazy">
                    </div>
                    <div class="swiper-slide">
                      <img src="assets/img/ducting/ducting-bjls.jpg" alt="Fabrikasi Saluran Baja Ducting BJLS" class="img-fluid" loading="lazy">
                    </div>
                  </div>
                  <div class="swiper-pagination"></div>
                  <div class="swiper-button-next"></div>
                  <div class="swiper-button-prev"></div>
                </div>
              </div>

              <div class="details-content" data-aos="fade-up" data-aos-delay="200">
                <div class="section-header">
                  <h3>Membangun Sistem Sirkulasi Udara Bersih &amp; Efisien</h3>
                  <div class="divider"></div>
                </div>
                <p>
                  Layanan sistem ducting HVAC kami mencakup setiap fase proyek tata udara, mulai dari perhitungan beban pendinginan, kalkulasi debit aliran udara (CFM), pemodelan 3D BIM, fabrikasi otomatis CNC, hingga pengujian Air Balancing (TAB) di lapangan. Kami memastikan setiap ruangan memperoleh distribusi udara segar dan pendinginan yang merata tanpa desis kebisingan turbulensi.
                </p>
                <p>
                  Berbekal pengalaman lebih dari 25 tahun di dunia MEP dan tata udara industri, tim kami menguasai standar internasional SMACNA dan ASHRAE. Setiap saluran udara yang kami pasang diuji secara ketat terhadap batas kebocoran (leakage class), penurunan tekanan (pressure drop), serta integritas termal guna mencegah kondensasi atau tetesan air embun pada plafon bangunan.
                </p>
              </div>

              <div class="service-features" data-aos="fade-up" data-aos-delay="300">
                <div class="section-header">
                  <h3>Cakupan Keunggulan Teknis</h3>
                  <div class="divider"></div>
                </div>
                <div class="row g-4">
                  <div class="col-md-6">
                    <div class="feature-card">
                      <div class="icon-wrapper">
                        <i class="bi bi-diagram-3"></i>
                      </div>
                      <h4>Desain &amp; Sizing Aerodinamis</h4>
                      <p>Kalkulasi dimensi saluran udara presisi untuk meminimalkan friksi dan turbulensi aliran udara.</p>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="feature-card">
                      <div class="icon-wrapper">
                        <i class="bi bi-shield-check"></i>
                      </div>
                      <h4>Fabrikasi Kedap Udara</h4>
                      <p>Penggunaan sambungan Flange TDC/TDF dengan sealant tahan panas berdaya rekat kedap udara tinggi.</p>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="feature-card">
                      <div class="icon-wrapper">
                        <i class="bi bi-layers-half"></i>
                      </div>
                      <h4>Insulasi Termal Bebas Embun</h4>
                      <p>Aplikasi insulasi Glasswool berkepadatan tinggi atau busa Polyurethane (PU) pencegah kondensasi.</p>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="feature-card">
                      <div class="icon-wrapper">
                        <i class="bi bi-speedometer2"></i>
                      </div>
                      <h4>Air Balancing (TAB) Bersertifikat</h4>
                      <p>Pengukuran laju aliran udara akhir di setiap diffuser/grille menggunakan anemometer digital terkalibrasi.</p>
                    </div>
                  </div>
                </div>
              </div>

              <div class="implementation-steps" data-aos="fade-up" data-aos-delay="400">
                <div class="section-header">
                  <h3>Tahapan Implementasi Proyek</h3>
                  <div class="divider"></div>
                </div>
                <div class="steps-grid">
                  <div class="step-card">
                    <span class="step-num">01</span>
                    <h4>Survei &amp; Analisis CFM</h4>
                    <p>Peninjauan lokasi, pengukuran beban kalor ruangan, dan penentuan static pressure blower.</p>
                  </div>
                  <div class="step-card">
                    <span class="step-num">02</span>
                    <h4>Shop Drawing &amp; Sizing</h4>
                    <p>Pembuatan gambar koordinasi MEP 3D BIM untuk mencegah benturan dengan instalasi pipa/kabel lain.</p>
                  </div>
                  <div class="step-card">
                    <span class="step-num">03</span>
                    <h4>Fabrikasi &amp; Pemasangan</h4>
                    <p>Pemotongan presisi di workshop dan perakitan di langit-langit gedung oleh teknisi bersertifikat.</p>
                  </div>
                  <div class="step-card">
                    <span class="step-num">04</span>
                    <h4>Komisioning &amp; Balancing</h4>
                    <p>Penyetelan volume damper, pengujian debit udara merata di setiap titik, dan serah terima garansi.</p>
                  </div>
                </div>
              </div>

            </div>
          </div>

        </div>

      </div>

    </section><!-- /Service Details Section -->'''
content = re.sub(old_section_pattern, new_section, content, flags=re.DOTALL)

# 4. Footer links
content = re.sub(
    r'<h4>Layanan Kami</h4>\s*<ul>.*?</ul>',
    '''<h4>Produk Ducting</h4>
          <ul>
            <li><a href="ducting-exhaust.html">Ducting Exhaust</a></li>
            <li><a href="ducting-fresh-air.html">Ducting Fresh Air</a></li>
            <li><a href="ducting-ac.html">Ducting AC Sentral</a></li>
            <li><a href="ducting-pu.html">Ducting PU</a></li>
            <li><a href="ducting-bjls.html">Ducting BJLS</a></li>
            <li><a href="service-details.html">Maintenance &amp; Cleaning</a></li>
          </ul>''',
    content,
    flags=re.DOTALL
)

with open("d:/Constructify-pro/service-details.html", "w", encoding="utf-8") as f:
    f.write(content)

print("service-details.html updated successfully!")
