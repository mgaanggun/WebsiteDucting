import re

with open("d:/Constructify-pro/project-details.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Detail Proyek - Instalasi Ducting HVAC Menara Bursa</title>',
    content
)

content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Studi kasus instalasi menyeluruh sistem ducting HVAC terpadu (Exhaust, Fresh Air, dan AC Sentral) pada gedung perkantoran bertingkat 32 lantai.">',
    content
)

content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="detail proyek ducting hvac, instalasi ducting gedung tinggi, ducting ac perkantoran, smoke spill basement, air balancing gedung">',
    content
)

# 2. Breadcrumbs
content = re.sub(
    r'<li class="current">Menara Korporat Meridian</li>',
    '<li class="current">Sistem Ducting HVAC Menara Bursa</li>',
    content
)

# 3. Main Project Details Section
old_section_pattern = r'<!-- Project Details Section -->.*?<!-- /Project Details Section -->'
new_section = '''<!-- Project Details Section -->
    <section id="project-details" class="project-details section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-5">

          <div class="col-lg-8">

            <div class="hero-banner" data-aos="zoom-in">
              <div class="banner-slider swiper init-swiper">
                <script type="application/json" class="swiper-config">
                  {
                    "loop": true,
                    "speed": 700,
                    "autoplay": {
                      "delay": 4500
                    },
                    "effect": "slide",
                    "slidesPerView": 1,
                    "pagination": {
                      "el": ".swiper-pagination",
                      "type": "fraction"
                    },
                    "navigation": {
                      "nextEl": ".swiper-button-next",
                      "prevEl": ".swiper-button-prev"
                    }
                  }
                </script>
                <div class="swiper-wrapper">
                  <div class="swiper-slide">
                    <img src="assets/img/ducting/ducting-ac.jpg" alt="Instalasi Ducting AC Sentral Menara Bursa" class="img-fluid" loading="lazy">
                  </div>
                  <div class="swiper-slide">
                    <img src="assets/img/ducting/ducting-bjls.jpg" alt="Fabrikasi Saluran BJLS Smoke Spill" class="img-fluid" loading="lazy">
                  </div>
                  <div class="swiper-slide">
                    <img src="assets/img/ducting/ducting-pu.jpg" alt="Pemasangan Panel Ducting PU" class="img-fluid" loading="lazy">
                  </div>
                </div>
                <div class="slider-controls">
                  <div class="swiper-button-prev"></div>
                  <div class="swiper-pagination"></div>
                  <div class="swiper-button-next"></div>
                </div>
              </div><!-- End Banner Slider -->

              <div class="banner-overlay">
                <span class="tag">Ducting AC &amp; Exhaust Sentral</span>
                <h2>Sistem Ducting HVAC Menara Bursa (32 Lantai)</h2>
              </div>
            </div><!-- End Hero Banner -->

            <div class="detail-tabs mt-4" data-aos="fade-up" data-aos-delay="200">
              <ul class="nav nav-tabs" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#project-details-tab-1" type="button" role="tab" aria-selected="true">
                    <i class="bi bi-info-circle"></i> Ringkasan Proyek
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" data-bs-toggle="tab" data-bs-target="#project-details-tab-2" type="button" role="tab" aria-selected="false">
                    <i class="bi bi-exclamation-triangle"></i> Tantangan Teknis
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" data-bs-toggle="tab" data-bs-target="#project-details-tab-3" type="button" role="tab" aria-selected="false">
                    <i class="bi bi-gear"></i> Metodologi Pengerjaan
                  </button>
                </li>
              </ul>

              <div class="tab-content">
                <div class="tab-pane fade show active" id="project-details-tab-1" role="tabpanel">
                  <p class="summary">
                    Pemasangan menyeluruh sistem saluran udara (ducting) HVAC terpadu meliputi cerobong exhaust basement bertekanan tinggi (smoke spill), saluran suplai udara segar (fresh air) berfiltrasi, dan saluran ducting AC sentral AHU untuk gedung perkantoran 32 lantai.
                  </p>
                  <p>
                    Proyek ini mencakup luas total area lantai lebih dari 65.000 m² dengan kapasitas sirkulasi udara kumulatif mencapai 450.000 CFM. Menggunakan kombinasi saluran Ducting BJLS galvalum berspesifikasi tahan api untuk sistem exhaust dan smoke spill, serta panel Ducting PU pre-insulated berefisiensi termal tinggi pada area ruang kerja dan lantai eksekutif guna memastikan difusi pendinginan yang senyap dan hemat daya.
                  </p>
                </div><!-- End Tab 1 -->

                <div class="tab-pane fade" id="project-details-tab-2" role="tabpanel">
                  <p>
                    Ruang plafon antar-lantai yang sangat padat oleh pipa hidran, kabel elektrikal, dan jalur sprinkler menuntut akurasi pemodelan 3D BIM Clash Detection dengan toleransi milimeter. Selain itu, gedung perkantoran ini mensyaratkan kriteria kebisingan (Noise Criteria) sangat ketat di bawah NC-30 pada lantai eksekutif, sehingga memerlukan perancangan silencer duct dan insulasi akustik peredam suara turbulensi aliran udara yang sangat cermat.
                  </p>
                </div><!-- End Tab 2 -->

                <div class="tab-pane fade" id="project-details-tab-3" role="tabpanel">
                  <p>
                    Kami menerapkan proses fabrikasi otomatis CNC menggunakan Auto Duct Line modern di workshop kami untuk memproduksi segmen ducting berflange TDC kedap udara (leakage class 3 SMACNA). Di lapangan, tim MEP memasang gantungan pegas peredam getaran (spring vibration isolator) dan melakukan pengujian Testing, Adjusting &amp; Balancing (TAB) di setiap diffuser udara menggunakan anemometer terkalibrasi untuk menjamin keseragaman debit udara.
                  </p>
                </div><!-- End Tab 3 -->
              </div>
            </div><!-- End Detail Tabs -->

            <div class="photo-grid mt-4" data-aos="fade-up" data-aos-delay="300">
              <h4>Dokumentasi Visual Instalasi Ducting</h4>
              <div class="row g-3">
                <div class="col-4">
                  <a href="assets/img/ducting/ducting-exhaust.jpg" class="glightbox" data-gallery="detail-gallery">
                    <img src="assets/img/ducting/ducting-exhaust.jpg" alt="Instalasi Exhaust Shaft" class="img-fluid" loading="lazy">
                  </a>
                </div>
                <div class="col-4">
                  <a href="assets/img/ducting/ducting-fresh-air.jpg" class="glightbox" data-gallery="detail-gallery">
                    <img src="assets/img/ducting/ducting-fresh-air.jpg" alt="Saluran Suplai Fresh Air" class="img-fluid" loading="lazy">
                  </a>
                </div>
                <div class="col-4">
                  <a href="assets/img/ducting/ducting-bjls-2.jpg" class="glightbox" data-gallery="detail-gallery">
                    <img src="assets/img/ducting/ducting-bjls-2.jpg" alt="Ducting BJLS Basement" class="img-fluid" loading="lazy">
                  </a>
                </div>
                <div class="col-4">
                  <a href="assets/img/ducting/ducting-ac-2.jpg" class="glightbox" data-gallery="detail-gallery">
                    <img src="assets/img/ducting/ducting-ac-2.jpg" alt="Distribusi Ducting AC" class="img-fluid" loading="lazy">
                  </a>
                </div>
                <div class="col-4">
                  <a href="assets/img/ducting/ducting-pu-2.jpg" class="glightbox" data-gallery="detail-gallery">
                    <img src="assets/img/ducting/ducting-pu-2.jpg" alt="Panel PU Cleanroom" class="img-fluid" loading="lazy">
                  </a>
                </div>
                <div class="col-4">
                  <a href="assets/img/ducting/ducting-bjls-3.jpg" class="glightbox" data-gallery="detail-gallery">
                    <img src="assets/img/ducting/ducting-bjls-3.jpg" alt="Jalur Saluran Utama AHU" class="img-fluid" loading="lazy">
                  </a>
                </div>
              </div>
            </div><!-- End Photo Grid -->

          </div>

          <div class="col-lg-4">
            <div class="project-info-card" data-aos="fade-up" data-aos-delay="100">
              <h3>Spesifikasi Proyek</h3>
              <ul class="info-list">
                <li><strong>Kategori:</strong> <span>Ducting HVAC &amp; Tata Udara Sentral</span></li>
                <li><strong>Klien:</strong> <span>PT Pengelola Menara Bursa</span></li>
                <li><strong>Lokasi:</strong> <span>Kawasan Bisnis Sudirman, Jakarta</span></li>
                <li><strong>Waktu Pengerjaan:</strong> <span>6 Bulan (Selesai Tepat Waktu)</span></li>
                <li><strong>Total Kapasitas:</strong> <span>450.000 CFM (32 Lantai)</span></li>
                <li><strong>Material Utama:</strong> <span>BJLS Galvalum &amp; Panel PU Pre-Insulated</span></li>
                <li><strong>Standar Regulasi:</strong> <span>SMACNA &amp; SNI 03-6572</span></li>
              </ul>
              <div class="project-cta mt-4">
                <a href="contact.html" class="btn-main w-100 text-center">Konsultasikan Proyek Anda</a>
              </div>
            </div>

            <div class="help-box mt-4" data-aos="fade-up" data-aos-delay="200">
              <div class="help-icon">
                <i class="bi bi-fan"></i>
              </div>
              <h4>Butuh Solusi Ducting Gedung?</h4>
              <p>Konsultasikan kebutuhan saluran tata udara dan efisiensi HVAC gedung Anda bersama tim engineer spesialis kami.</p>
              <a href="tel:085210620252" class="help-phone"><i class="bi bi-telephone-fill"></i> 0852-1062-0252</a>
            </div>
          </div>

        </div>

      </div>

    </section><!-- /Project Details Section -->'''
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

with open("d:/Constructify-pro/project-details.html", "w", encoding="utf-8") as f:
    f.write(content)

print("project-details.html updated successfully!")
