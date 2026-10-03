import re

with open("d:/Constructify-pro/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Ducting HVAC - Spesialis Fabrikasi &amp; Instalasi Saluran Udara Profesional</title>',
    content
)

content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Ducting HVAC adalah spesialis fabrikasi dan instalasi ducting exhaust, fresh air, AC sentral, ducting PU polyurethane, dan ducting BJLS galvalum standar SMACNA bergaransi.">',
    content
)

content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="ducting hvac, ducting exhaust, ducting fresh air, ducting ac sentral, ducting pu, ducting bjls, saluran udara, cerobong hvac, fabrikasi ducting">',
    content
)

# 2. Update Hero Section
old_hero_pattern = r'<!-- Hero Section -->.*?<!-- /Hero Section -->'
new_hero = '''<!-- Hero Section -->
    <section id="hero" class="hero section">

      <div class="hero-bg">
        <img src="assets/img/ducting/ducting-bjls.jpg" alt="Instalasi Ducting HVAC Profesional">
      </div>

      <div class="container position-relative">
        <div class="row">
          <div class="col-lg-8" data-aos="fade-up" data-aos-delay="100">
            <span class="badge-label"><i class="bi bi-fan"></i> Spesialis Fabrikasi &amp; Instalasi Ducting HVAC</span>
            <h1>Solusi Distribusi Udara &amp; Ducting HVAC <span class="accent">Presisi Tinggi</span></h1>
            <p class="lead">Kami menghadirkan solusi fabrikasi dan instalasi ducting HVAC terpadu (Exhaust, Fresh Air, AC Sentral, PU, dan BJLS) dengan standar rekayasa presisi tinggi untuk gedung perkantoran, rumah sakit, pusat perbelanjaan, dan pabrik industri di seluruh Indonesia.</p>
            <div class="hero-actions d-flex flex-wrap gap-3">
              <a href="projects.html" class="btn-main">Jelajahi Proyek Kami</a>
              <a href="contact.html" class="btn-outline">Minta Penawaran Biaya <i class="bi bi-arrow-right"></i></a>
            </div>
          </div>
        </div>

        <div class="row hero-counters" data-aos="fade-up" data-aos-delay="200">
          <div class="col-6 col-lg-3">
            <div class="counter-item">
              <h3><span data-purecounter-start="0" data-purecounter-end="25" data-purecounter-duration="1" class="purecounter"></span>+</h3>
              <p>Tahun Pengalaman</p>
            </div>
          </div>
          <div class="col-6 col-lg-3">
            <div class="counter-item">
              <h3><span data-purecounter-start="0" data-purecounter-end="850" data-purecounter-duration="1" class="purecounter"></span>+</h3>
              <p>Proyek Ducting Selesai</p>
            </div>
          </div>
          <div class="col-6 col-lg-3">
            <div class="counter-item">
              <h3><span data-purecounter-start="0" data-purecounter-end="120" data-purecounter-duration="1" class="purecounter"></span>+</h3>
              <p>Teknisi &amp; MEP Engineer</p>
            </div>
          </div>
          <div class="col-6 col-lg-3">
            <div class="counter-item">
              <h3><span data-purecounter-start="0" data-purecounter-end="35" data-purecounter-duration="1" class="purecounter"></span>+</h3>
              <p>Sertifikasi Standar Mutu</p>
            </div>
          </div>
        </div>

      </div>

    </section><!-- /Hero Section -->'''

content = re.sub(old_hero_pattern, new_hero, content, flags=re.DOTALL)

# 3. Update About Section
old_about_pattern = r'<!-- About Section -->.*?<!-- /About Section -->'
new_about = '''<!-- About Section -->
    <section id="about" class="about section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-5 align-items-center">

          <div class="col-lg-6" data-aos="fade-right" data-aos-delay="200">
            <div class="about-gallery">
              <div class="gallery-main">
                <img src="assets/img/ducting/ducting-ac.jpg" alt="Instalasi Saluran Ducting AC" class="img-fluid" loading="lazy">
              </div>
              <div class="gallery-secondary">
                <img src="assets/img/ducting/ducting-pu.jpg" alt="Fabrikasi Ducting PU Higienis" class="img-fluid" loading="lazy">
              </div>
              <div class="experience-badge">
                <span class="number">25+</span>
                <span class="text">Tahun<br>Pengalaman</span>
              </div>
            </div>
          </div>

          <div class="col-lg-6" data-aos="fade-left" data-aos-delay="300">
            <div class="about-content">
              <span class="section-label"><i class="bi bi-fan"></i> Tentang Ducting HVAC</span>
              <h2>Rekayasa Tata Udara Berkualitas dengan Presisi Fabrikasi Terbaik</h2>
              <p class="lead">Sejak 1998, kami mendedikasikan keahlian dalam perancangan, fabrikasi otomatis CNC, dan instalasi sistem ducting HVAC. Kami memastikan sirkulasi udara bersih, pembuangan udara panas optimal, serta efisiensi pendinginan maksimal untuk kenyamanan dan keselamatan gedung Anda.</p>

              <div class="about-highlights">
                <div class="row g-4">
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-shield-check"></i>
                      </div>
                      <h4>Standar Mutu SMACNA</h4>
                      <p>Kepatuhan penuh pada standar SMACNA &amp; SNI untuk kebocoran udara minimal dan efisiensi termal.</p>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-clock-history"></i>
                      </div>
                      <h4>Selesai Tepat Waktu</h4>
                      <p>Manajemen proyek MEP disiplin dengan instalasi bertahap yang rapi dan tepat waktu.</p>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-people"></i>
                      </div>
                      <h4>Teknisi &amp; MEP Ahli</h4>
                      <p>Lebih dari 120 insinyur mekanikal, perancang airflow, dan teknisi isolasi bersertifikasi.</p>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-trophy"></i>
                      </div>
                      <h4>Material Bersertifikasi</h4>
                      <p>Menggunakan BJLS tebal berkualitas tinggi dan panel Polyurethane (PU) fire-retardant.</p>
                    </div>
                  </div>
                </div>
              </div>

              <div class="about-cta">
                <a href="contact.html" class="btn-about">Konsultasi Sistem Ducting <i class="bi bi-arrow-right"></i></a>
                <a href="projects.html" class="btn-about-outline">Lihat Proyek Kami</a>
              </div>
            </div>
          </div>

        </div>

      </div>

    </section><!-- /About Section -->'''

content = re.sub(old_about_pattern, new_about, content, flags=re.DOTALL)

# 4. Update Services Section
old_services_pattern = r'<!-- Services Section -->.*?<!-- /Services Section -->'
new_services = '''<!-- Services Section -->
    <section id="services" class="services section light-background">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Layanan Spesialis Ducting HVAC</h2>
        <p>Solusi fabrikasi dan instalasi cerobong saluran udara dengan standar SMACNA, efisiensi airflow aerodinamis, dan ketahanan jangka panjang</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4 align-items-stretch">

          <div class="col-lg-4" data-aos="fade-right" data-aos-delay="100">
            <div class="services-image">
              <img src="assets/img/ducting/ducting-exhaust.jpg" alt="Layanan Fabrikasi Ducting HVAC" class="img-fluid">
              <div class="image-overlay">
                <h3>Sirkulasi Udara Bersih &amp; Efisien untuk Gedung Anda</h3>
                <a href="contact.html" class="overlay-link">Dapatkan Konsultasi Gratis <i class="bi bi-arrow-right"></i></a>
              </div>
            </div>
          </div>

          <div class="col-lg-8">
            <div class="row g-4">

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="100">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-wind"></i>
                  </div>
                  <div class="service-body">
                    <h4><a href="ducting-exhaust.html" class="text-dark">Ducting Exhaust</a></h4>
                    <p>Cerobong khusus untuk menyalurkan udara kotor, panas, uap dapur komersial, dan asap industri dari dalam ruangan ke luar ruangan secara aman.</p>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="200">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-cloud-sun"></i>
                  </div>
                  <div class="service-body">
                    <h4><a href="ducting-fresh-air.html" class="text-dark">Ducting Fresh Air</a></h4>
                    <p>Saluran suplai udara segar berfiltrasi dari luar gedung ke dalam ruangan, menjaga sirkulasi oksigen, tekanan positif, dan kualitas udara (IAQ).</p>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="300">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-snow2"></i>
                  </div>
                  <div class="service-body">
                    <h4><a href="ducting-ac.html" class="text-dark">Ducting AC Sentral</a></h4>
                    <p>Pipa dan cerobong distribusi udara dingin dari sistem AC Sentral (AHU, FCU, VRV) ke seluruh zona ruangan secara merata, efisien, dan senyap.</p>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="400">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-layers-half"></i>
                  </div>
                  <div class="service-body">
                    <h4><a href="ducting-pu.html" class="text-dark">Ducting PU (Polyurethane)</a></h4>
                    <p>Cerobong berbahan Pre-Insulated Polyurethane yang ringan, higienis, anti-jamur, bebas kondensasi, ideal untuk rumah sakit, farmasi, dan cleanroom.</p>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="500">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-shield-check"></i>
                  </div>
                  <div class="service-body">
                    <h4><a href="ducting-bjls.html" class="text-dark">Ducting BJLS (Galvalum)</a></h4>
                    <p>Cerobong baja lapis seng tahan benturan dan tekanan statis tinggi, sangat kokoh untuk industri, basement, dan sistem smoke-spill darurat.</p>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="600">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-tools"></i>
                  </div>
                  <div class="service-body">
                    <h4><a href="service-details.html" class="text-dark">Maintenance &amp; Duct Cleaning</a></h4>
                    <p>Pembersihan kerak minyak &amp; debu saluran udara, perbaikan kebocoran isolasi, penggantian filter HEPA, serta pengujian Air Balancing (TAB).</p>
                  </div>
                </div>
              </div><!-- End Service -->

            </div>
          </div>

        </div>

      </div>

    </section><!-- /Services Section -->'''

content = re.sub(old_services_pattern, new_services, content, flags=re.DOTALL)

# 5. Update Stats Section
old_stats_pattern = r'<!-- Stats Section -->.*?<!-- /Stats Section -->'
new_stats = '''<!-- Stats Section -->
    <section id="stats" class="stats section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row align-items-center gy-5">

          <div class="col-lg-5" data-aos="fade-right" data-aos-delay="100">
            <div class="stats-content">
              <span class="label-tag">Rekam Jejak Terpercaya</span>
              <h2>Angka Nyata Komitmen &amp; Mutu Tata Udara Kami</h2>
              <p>Dengan pengalaman lebih dari dua dekade, portofolio sistem ducting HVAC kami menjamin distribusi airflow presisi, minim resistensi tekanan, dan hemat konsumsi energi pendinginan.</p>
              <a href="projects.html" class="stats-link">Lihat Portofolio Proyek <i class="bi bi-arrow-right"></i></a>
            </div>
          </div>

          <div class="col-lg-7" data-aos="fade-left" data-aos-delay="200">
            <div class="row g-4">

              <div class="col-sm-6">
                <div class="counter-card">
                  <div class="counter-icon">
                    <i class="bi bi-fan"></i>
                  </div>
                  <div class="counter-data">
                    <h3><span data-purecounter-start="0" data-purecounter-end="850" data-purecounter-duration="1" class="purecounter"></span>+</h3>
                    <p>Proyek Ducting Selesai</p>
                  </div>
                </div>
              </div><!-- End Counter -->

              <div class="col-sm-6">
                <div class="counter-card">
                  <div class="counter-icon">
                    <i class="bi bi-emoji-smile"></i>
                  </div>
                  <div class="counter-data">
                    <h3><span data-purecounter-start="0" data-purecounter-end="620" data-purecounter-duration="1" class="purecounter"></span>+</h3>
                    <p>Klien Gedung &amp; Industri</p>
                  </div>
                </div>
              </div><!-- End Counter -->

              <div class="col-sm-6">
                <div class="counter-card">
                  <div class="counter-icon">
                    <i class="bi bi-people"></i>
                  </div>
                  <div class="counter-data">
                    <h3><span data-purecounter-start="0" data-purecounter-end="120" data-purecounter-duration="1" class="purecounter"></span>+</h3>
                    <p>Teknisi MEP Bersertifikat</p>
                  </div>
                </div>
              </div><!-- End Counter -->

              <div class="col-sm-6">
                <div class="counter-card">
                  <div class="counter-icon">
                    <i class="bi bi-award"></i>
                  </div>
                  <div class="counter-data">
                    <h3><span data-purecounter-start="0" data-purecounter-end="35" data-purecounter-duration="1" class="purecounter"></span>+</h3>
                    <p>Sertifikasi Standar Mutu</p>
                  </div>
                </div>
              </div><!-- End Counter -->

            </div>
          </div>

        </div>

      </div>

    </section><!-- /Stats Section -->'''

content = re.sub(old_stats_pattern, new_stats, content, flags=re.DOTALL)

# 6. Update Projects Section
old_projects_pattern = r'<!-- Projects Section -->.*?<!-- /Projects Section -->'
new_projects = '''<!-- Projects Section -->
    <section id="projects" class="projects section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Portofolio Proyek Ducting HVAC</h2>
        <p>Bukti dedikasi kami dalam menghadirkan sistem ducting saluran udara berkualitas tinggi dengan efisiensi sirkulasi optimal di berbagai sektor</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="isotope-layout" data-default-filter="*" data-layout="fitRows" data-sort="original-order">

          <ul class="portfolio-filters isotope-filters" data-aos="fade-up" data-aos-delay="100">
            <li data-filter="*" class="filter-active">Semua Proyek</li>
            <li data-filter=".filter-exhaust">Exhaust &amp; Fresh Air</li>
            <li data-filter=".filter-ac">Ducting AC &amp; PU</li>
            <li data-filter=".filter-bjls">Ducting BJLS &amp; Industri</li>
          </ul><!-- End Portfolio Filters -->

          <div class="row g-4 isotope-container" data-aos="fade-up" data-aos-delay="200">

            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-exhaust">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-exhaust.jpg" alt="Exhaust Hood Kitchen Mall" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Exhaust &amp; Fresh Air</span>
                    <h3>Sistem Exhaust Hood Dapur Komersial</h3>
                    <p>Instalasi cerobong exhaust uap dan asap bertekanan tinggi di food court pusat perbelanjaan</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-exhaust.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Exhaust Hood Dapur Komersial"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-ac">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-ac.jpg" alt="Ducting AC Sentral Gedung Kantor" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting AC &amp; PU</span>
                    <h3>Ducting AC Sentral Gedung Perkantoran</h3>
                    <p>Sistem distribusi pendingin AHU bertingkat dengan insulasi termal prima dan difusi merata</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-ac.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting AC Sentral Gedung Perkantoran"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-bjls">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-bjls.jpg" alt="Ducting BJLS Basement" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting BJLS &amp; Industri</span>
                    <h3>Ducting BJLS Smoke Spill Basement</h3>
                    <p>Fabrikasi saluran baja lapis seng tebal tahan api untuk evakuasi asap darurat basement</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting BJLS Smoke Spill Basement"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-ac">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-pu.jpg" alt="Ducting PU Cleanroom" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting AC &amp; PU</span>
                    <h3>Cleanroom Ducting PU Farmasi &amp; RS</h3>
                    <p>Pemasangan panel Polyurethane higienis bebas serat partikel untuk ruang operasi dan laboratorium</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-pu.jpg" class="card-action glightbox" data-gallery="projects" title="Cleanroom Ducting PU Farmasi &amp; RS"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-exhaust">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-fresh-air.jpg" alt="Ducting Fresh Air Filtrasi" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Exhaust &amp; Fresh Air</span>
                    <h3>Sistem Fresh Air &amp; Tekanan Positif</h3>
                    <p>Saluran suplai udara segar berfiltrasi HEPA menjaga kemurnian sirkulasi oksigen gedung bertingkat</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-fresh-air.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Fresh Air &amp; Tekanan Positif"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-bjls">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-bjls-2.jpg" alt="Ventilasi Pabrik Industri" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting BJLS &amp; Industri</span>
                    <h3>Sistem Ventilasi Pabrik Industri Manufaktur</h3>
                    <p>Saluran udara volume besar bertekanan tinggi untuk pembuangan polutan dan pendinginan lini produksi</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls-2.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Ventilasi Pabrik Industri Manufaktur"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

          </div><!-- End Portfolio Items Container -->

        </div>

      </div>

    </section><!-- /Projects Section -->'''

content = re.sub(old_projects_pattern, new_projects, content, flags=re.DOTALL)

# 7. Update Process Section
old_process_pattern = r'<!-- Process Section -->.*?<!-- /Process Section -->'
new_process = '''<!-- Process Section -->
    <section id="process" class="process section light-background">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Tahapan Kerja Sistematis</h2>
        <p>Alur kerja rekayasa HVAC profesional yang menjamin sistem ducting efisien, kedap udara, dan sesuai standar SMACNA</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4">

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="100">
            <div class="process-step">
              <div class="step-number">01</div>
              <div class="step-icon">
                <i class="bi bi-speedometer2"></i>
              </div>
              <h3>Survey CFM &amp; Tekanan</h3>
              <p>Pengukuran beban termal ruangan, perhitungan laju aliran udara (CFM), dan estimasi hambatan tekanan statis (SP).</p>
            </div>
          </div><!-- End Step -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="200">
            <div class="process-step">
              <div class="step-number">02</div>
              <div class="step-icon">
                <i class="bi bi-diagram-3"></i>
              </div>
              <h3>Desain CAD &amp; Sizing</h3>
              <p>Penyusunan shop drawing 3D/BIM, kalkulasi ukuran penampang ducting, posisi diffuser, serta damper pengatur.</p>
            </div>
          </div><!-- End Step -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="300">
            <div class="process-step">
              <div class="step-number">03</div>
              <div class="step-icon">
                <i class="bi bi-gear-wide-connected"></i>
              </div>
              <h3>Fabrikasi Otomatis CNC</h3>
              <p>Pemotongan lembaran BJLS atau panel PU menggunakan mesin presisi modern untuk hasil sambungan flange yang kedap.</p>
            </div>
          </div><!-- End Step -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="400">
            <div class="process-step">
              <div class="step-number">04</div>
              <div class="step-icon">
                <i class="bi bi-check2-circle"></i>
              </div>
              <h3>Instalasi &amp; Air Balancing</h3>
              <p>Pemasangan gantungan antivibrasi, sealing sambungan, dan pengujian Test Adjust Balance (TAB) aliran udara.</p>
            </div>
          </div><!-- End Step -->

        </div>

      </div>

    </section><!-- /Process Section -->'''

content = re.sub(old_process_pattern, new_process, content, flags=re.DOTALL)

# 8. Update Team Section
old_team_pattern = r'<!-- Team Section -->.*?<!-- /Team Section -->'
new_team = '''<!-- Team Section -->
    <section id="team" class="team section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Tim Ahli Tata Udara &amp; MEP Kami</h2>
        <p>Dipimpin oleh praktisi profesional berpengalaman di bidang rekayasa HVAC, perancangan sirkulasi airflow, dan manajemen proyek MEP</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4">

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="100">
            <div class="member-card">
              <div class="member-img">
                <img src="assets/img/construction/team-2.webp" alt="Robert Anderson" class="img-fluid" loading="lazy">
                <div class="social-links">
                  <a href="#"><i class="bi bi-twitter-x"></i></a>
                  <a href="#"><i class="bi bi-facebook"></i></a>
                  <a href="#"><i class="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div class="member-info">
                <h4>Robert Anderson</h4>
                <span>Direktur Teknik &amp; MEP Specialist</span>
              </div>
            </div>
          </div><!-- End Team Member -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="200">
            <div class="member-card">
              <div class="member-img">
                <img src="assets/img/construction/team-5.webp" alt="Sarah Mitchell" class="img-fluid" loading="lazy">
                <div class="social-links">
                  <a href="#"><i class="bi bi-twitter-x"></i></a>
                  <a href="#"><i class="bi bi-facebook"></i></a>
                  <a href="#"><i class="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div class="member-info">
                <h4>Sarah Mitchell</h4>
                <span>Kepala Desain Airflow &amp; Sizing</span>
              </div>
            </div>
          </div><!-- End Team Member -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="300">
            <div class="member-card">
              <div class="member-img">
                <img src="assets/img/construction/team-7.webp" alt="David Thompson" class="img-fluid" loading="lazy">
                <div class="social-links">
                  <a href="#"><i class="bi bi-twitter-x"></i></a>
                  <a href="#"><i class="bi bi-facebook"></i></a>
                  <a href="#"><i class="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div class="member-info">
                <h4>David Thompson</h4>
                <span>Manajer Fabrikasi &amp; Instalasi</span>
              </div>
            </div>
          </div><!-- End Team Member -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="400">
            <div class="member-card">
              <div class="member-img">
                <img src="assets/img/construction/team-9.webp" alt="Emily Carter" class="img-fluid" loading="lazy">
                <div class="social-links">
                  <a href="#"><i class="bi bi-twitter-x"></i></a>
                  <a href="#"><i class="bi bi-facebook"></i></a>
                  <a href="#"><i class="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div class="member-info">
                <h4>Emily Carter</h4>
                <span>Pengawas Mutu K3 &amp; Air Balancing</span>
              </div>
            </div>
          </div><!-- End Team Member -->

        </div>

      </div>

    </section><!-- /Team Section -->'''

content = re.sub(old_team_pattern, new_team, content, flags=re.DOTALL)

# 9. Update Testimonials Section
old_testimonials_pattern = r'<!-- Testimonials Section -->.*?<!-- /Testimonials Section -->'
new_testimonials = '''<!-- Testimonials Section -->
    <section id="testimonials" class="testimonials section light-background">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Apa Kata Klien Kami</h2>
        <p>Kepercayaan pengelola gedung, rumah sakit, restoran, dan fasilitas industri adalah bukti kualitas sistem ducting kami</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="testimonials-slider swiper init-swiper">
          <script type="application/json" class="swiper-config">
            {
              "loop": true,
              "speed": 600,
              "autoplay": {
                "delay": 5000
              },
              "slidesPerView": 1,
              "spaceBetween": 24,
              "breakpoints": {
                "768": {
                  "slidesPerView": 2
                },
                "1200": {
                  "slidesPerView": 3
                }
              },
              "pagination": {
                "el": ".swiper-pagination",
                "type": "bullets",
                "clickable": true
              }
            }
          </script>
          <div class="swiper-wrapper">

            <div class="swiper-slide">
              <div class="testimonial-card">
                <div class="stars">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                </div>
                <p>"Instalasi Ducting AC Sentral dan Fresh Air untuk menara perkantoran kami selesai tepat waktu dengan hasil pengujian Air Balancing yang sangat presisi. Suhu ruangan merata dan minim desis suara."</p>
                <div class="client-info d-flex align-items-center gap-16">
                  <img src="assets/img/person/person-m-3.webp" alt="James Harrison" class="img-fluid">
                  <div>
                    <h4>James Harrison</h4>
                    <span>Building Manager Menara Sudirman</span>
                  </div>
                </div>
              </div>
            </div><!-- End Testimonial -->

            <div class="swiper-slide">
              <div class="testimonial-card">
                <div class="stars">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                </div>
                <p>"Pemasangan ducting PU pre-insulated di area cleanroom laboratorium kami sangat rapi, steril, dan bebas serat partikel. Lolos verifikasi uji kebersihan dan standar regulasi farmasi dengan memuaskan."</p>
                <div class="client-info d-flex align-items-center gap-16">
                  <img src="assets/img/person/person-f-7.webp" alt="Rebecca Collins" class="img-fluid">
                  <div>
                    <h4>dr. Rebecca Collins</h4>
                    <span>Direktur Operasional Rumah Sakit</span>
                  </div>
                </div>
              </div>
            </div><!-- End Testimonial -->

            <div class="swiper-slide">
              <div class="testimonial-card">
                <div class="stars">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-half"></i>
                </div>
                <p>"Sistem exhaust hood dapur restoran kami sebelumnya sering bermasalah dengan asap dan uap panas. Tim Ducting HVAC merombak total dengan ducting BJLS kokoh dan blower bertenaga, dapur kini sangat sejuk."</p>
                <div class="client-info d-flex align-items-center gap-16">
                  <img src="assets/img/person/person-m-9.webp" alt="Michael Torres" class="img-fluid">
                  <div>
                    <h4>Michael Torres</h4>
                    <span>Head of Culinary &amp; Restaurant Operations</span>
                  </div>
                </div>
              </div>
            </div><!-- End Testimonial -->

            <div class="swiper-slide">
              <div class="testimonial-card">
                <div class="stars">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                </div>
                <p>"Fabrikasi ducting BJLS untuk sistem ventilasi pabrik kami dikerjakan sangat cepat dan rapi. Perhitungan static pressure-nya sangat akurat sehingga efisiensi energi blower meningkat signifikan."</p>
                <div class="client-info d-flex align-items-center gap-16">
                  <img src="assets/img/person/person-f-12.webp" alt="Olivia Nguyen" class="img-fluid">
                  <div>
                    <h4>Olivia Nguyen</h4>
                    <span>Kepala Fasilitas Pabrik Industri</span>
                  </div>
                </div>
              </div>
            </div><!-- End Testimonial -->

          </div>
          <div class="swiper-pagination"></div>
        </div>

      </div>

    </section><!-- /Testimonials Section -->'''

content = re.sub(old_testimonials_pattern, new_testimonials, content, flags=re.DOTALL)

# 10. Update Faq Section
old_faq_pattern = r'<!-- Faq Section -->.*?<!-- /Faq Section -->'
new_faq = '''<!-- Faq Section -->
    <section id="faq" class="faq section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Pertanyaan yang Sering Diajukan (FAQ)</h2>
        <p>Jawaban lengkap seputar produk ducting, pemilihan material PU vs BJLS, estimasi biaya, dan garansi pengujian airflow</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row justify-content-center">
          <div class="col-lg-8">

            <div class="faq-item" data-aos="fade-up" data-aos-delay="100">
              <h3>Apa saja jenis ducting HVAC yang diproduksi dan dipasang?</h3>
              <div class="faq-content">
                <p>Kami memproduksi dan menginstalasi seluruh jenis saluran udara HVAC, meliputi Ducting Exhaust (pembuangan udara kotor/panas), Ducting Fresh Air (suplai udara segar), Ducting AC Sentral (distribusi pendingin AHU/FCU), Ducting PU (Pre-Insulated Polyurethane), serta Ducting BJLS (Baja Lapis Seng Galvalum) dengan standar SMACNA.</p>
              </div>
              <i class="faq-toggle bi bi-chevron-right"></i>
            </div><!-- End FAQ Item -->

            <div class="faq-item" data-aos="fade-up" data-aos-delay="200">
              <h3>Apa perbedaan mendasar antara Ducting PU dan Ducting BJLS?</h3>
              <div class="faq-content">
                <p>Ducting PU terbuat dari busa rigid polyurethane yang dilapisi aluminium foil di kedua sisi; sudah memiliki isolasi termal bawaan, sangat ringan, higienis, dan tidak melepaskan serat (sangat ideal untuk rumah sakit, cleanroom, perkantoran). Sedangkan Ducting BJLS terbuat dari lembaran baja lapis seng; sangat kuat, tahan benturan fisik, tahan panas tinggi, dan mampu menahan tekanan udara sangat tinggi (sangat cocok untuk exhaust dapur, pabrik berat, basement, dan jalur evakuasi asap smoke spill).</p>
              </div>
              <i class="faq-toggle bi bi-chevron-right"></i>
            </div><!-- End FAQ Item -->

            <div class="faq-item" data-aos="fade-up" data-aos-delay="300">
              <h3>Berapa lama waktu yang dibutuhkan untuk fabrikasi dan instalasi ducting?</h3>
              <div class="faq-content">
                <p>Fabrikasi saluran ducting di workshop kami menggunakan mesin CNC dan Auto Duct Line otomatis, sehingga pesanan dapat diselesaikan dalam hitungan hari. Waktu instalasi di lapangan bergantung pada luas bangunan dan ketinggian plafon, biasanya berkisar antara 1 hingga 3 minggu dengan koordinasi terpadu bersama tim kontraktor sipil/MEP lainnya.</p>
              </div>
              <i class="faq-toggle bi bi-chevron-right"></i>
            </div><!-- End FAQ Item -->

            <div class="faq-item" data-aos="fade-up" data-aos-delay="400">
              <h3>Apakah tersedia layanan survei lokasi dan perhitungan CFM gratis?</h3>
              <div class="faq-content">
                <p>Ya, tim engineer kami menyediakan survei teknis ke lokasi proyek dan perhitungan debit udara (CFM) serta kebutuhan static pressure tanpa dipungut biaya. Kami akan memberikan estimasi Rencana Anggaran Biaya (RAB) yang transparan dan terperinci.</p>
              </div>
              <i class="faq-toggle bi bi-chevron-right"></i>
            </div><!-- End FAQ Item -->

            <div class="faq-item" data-aos="fade-up" data-aos-delay="500">
              <h3>Bagaimana dengan jaminan garansi dan pengujian Air Balancing (TAB)?</h3>
              <div class="faq-content">
                <p>Setiap proyek instalasi kami dilengkapi dengan jaminan garansi bebas kebocoran udara dan pengujian Testing, Adjusting, &amp; Balancing (TAB) menggunakan alat ukur anemometer digital bersertifikat untuk memastikan volume udara di setiap diffuser atau grille sesuai dengan perencanaan kapasitas pendinginan.</p>
              </div>
              <i class="faq-toggle bi bi-chevron-right"></i>
            </div><!-- End FAQ Item -->

          </div>
        </div>

      </div>

    </section><!-- /Faq Section -->'''

content = re.sub(old_faq_pattern, new_faq, content, flags=re.DOTALL)

# 11. Update Call to Action Section
old_cta_pattern = r'<!-- Call To Action Section -->.*?<!-- /Call To Action Section -->'
new_cta = '''<!-- Call To Action Section -->
    <section id="call-to-action" class="call-to-action section dark-background">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row align-items-center gy-5">

          <div class="col-lg-6" data-aos="fade-right" data-aos-delay="150">
            <div class="info-block">
              <span class="tagline">Bermitra dengan Spesialis Tata Udara</span>
              <h2>Optimalkan Sirkulasi Udara &amp; Efisiensi HVAC Gedung Anda</h2>
              <p>Siap mengoptimalkan sistem saluran udara dan efisiensi ducting HVAC gedung Anda? Hubungi para insinyur dan spesialis ducting kami hari ini untuk konsultasi teknis, survei CFM, serta penawaran biaya yang transparan.</p>

              <div class="highlight-cards">
                <div class="highlight-card" data-aos="zoom-in" data-aos-delay="200">
                  <div class="card-icon">
                    <i class="bi bi-fan"></i>
                  </div>
                  <div class="card-body-content">
                    <h5>Kualitas Fabrikasi Presisi</h5>
                    <p>Standar SMACNA dengan tingkat kebocoran udara minimal</p>
                  </div>
                </div><!-- End Highlight Card -->

                <div class="highlight-card" data-aos="zoom-in" data-aos-delay="270">
                  <div class="card-icon">
                    <i class="bi bi-shield-check"></i>
                  </div>
                  <div class="card-body-content">
                    <h5>Material Berkualitas SNI</h5>
                    <p>Pilihan BJLS tebal anti-karat &amp; panel PU fire-retardant</p>
                  </div>
                </div><!-- End Highlight Card -->

                <div class="highlight-card" data-aos="zoom-in" data-aos-delay="340">
                  <div class="card-icon">
                    <i class="bi bi-graph-up-arrow"></i>
                  </div>
                  <div class="card-body-content">
                    <h5>Efisiensi Konsumsi Energi</h5>
                    <p>Aliran udara aerodinamis menghemat daya chiller &amp; fan</p>
                  </div>
                </div><!-- End Highlight Card -->
              </div>

              <div class="action-row" data-aos="fade-up" data-aos-delay="400">
                <a href="contact.html" class="btn-get-started">
                  <span>Minta Penawaran Gratis</span>
                  <i class="bi bi-arrow-right"></i>
                </a>
                <div class="phone-block">
                  <div class="phone-icon">
                    <i class="bi bi-telephone-fill"></i>
                  </div>
                  <div class="phone-details">
                    <span class="phone-label">Hubungi Spesialis Ducting</span>
                    <a href="tel:085210620252" class="phone-number">0852-1062-0252</a>
                  </div>
                </div>
              </div>

            </div>
          </div>

          <div class="col-lg-6" data-aos="fade-left" data-aos-delay="200">
            <div class="image-block">
              <div class="main-image">
                <img src="assets/img/ducting/ducting-bjls.jpg" alt="Instalasi Ducting HVAC Profesional" class="img-fluid">
              </div>
              <div class="counter-badge" data-aos="fade-down" data-aos-delay="350">
                <div class="counter-inner">
                  <span class="counter-value">850+</span>
                  <span class="counter-text">Proyek Sukses</span>
                </div>
              </div>
              <div class="accent-badge" data-aos="fade-up" data-aos-delay="400">
                <i class="bi bi-patch-check-fill"></i>
                <span>Standar Mutu SMACNA</span>
              </div>
            </div>
          </div>

        </div>

      </div>

    </section><!-- /Call To Action Section -->'''

content = re.sub(old_cta_pattern, new_cta, content, flags=re.DOTALL)

# 12. Update Contact Section
old_contact_pattern = r'<!-- Contact Section -->.*?<!-- /Contact Section -->'
new_contact = '''<!-- Contact Section -->
    <section id="contact" class="contact section light-background">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Hubungi Kami</h2>
        <p>Sampaikan kebutuhan sistem ducting dan sirkulasi tata udara gedung Anda, dapatkan konsultasi teknis serta estimasi biaya terbaik dari tim kami</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4">

          <div class="col-lg-4">
            <div class="info-cards">

              <div class="info-card d-flex align-items-start gap-3" data-aos="fade-up" data-aos-delay="100">
                <div class="icon-box">
                  <i class="bi bi-geo-alt"></i>
                </div>
                <div>
                  <h4>Kantor &amp; Workshop</h4>
                  <p>Workshop Fabrikasi Ducting HVAC<br>Jakarta &amp; Sekitarnya, Indonesia</p>
                </div>
              </div><!-- End Info Card -->

              <div class="info-card d-flex align-items-start gap-3" data-aos="fade-up" data-aos-delay="200">
                <div class="icon-box">
                  <i class="bi bi-telephone"></i>
                </div>
                <div>
                  <h4>Telepon / WhatsApp</h4>
                  <p><a href="tel:085210620252" class="text-dark">0852-1062-0252</a></p>
                </div>
              </div><!-- End Info Card -->

              <div class="info-card d-flex align-items-start gap-3" data-aos="fade-up" data-aos-delay="300">
                <div class="icon-box">
                  <i class="bi bi-envelope"></i>
                </div>
                <div>
                  <h4>Email Konsultasi</h4>
                  <p>info@ductinghvac.co.id<br>proyek@ductinghvac.co.id</p>
                </div>
              </div><!-- End Info Card -->

              <div class="info-card d-flex align-items-start gap-3" data-aos="fade-up" data-aos-delay="400">
                <div class="icon-box">
                  <i class="bi bi-clock"></i>
                </div>
                <div>
                  <h4>Jam Operasional</h4>
                  <p>Senin - Jumat: 08:00 - 18:00<br>Sabtu: 08:30 - 15:00</p>
                </div>
              </div><!-- End Info Card -->

            </div>
          </div>

          <div class="col-lg-8" data-aos="fade-up" data-aos-delay="200">
            <div class="contact-form-wrap">
              <form action="forms/contact.php" method="post" class="php-email-form">
                <div class="row gy-4">
                  <div class="col-md-6">
                    <input type="text" name="name" class="form-control" placeholder="Nama Lengkap Anda" required="" autocomplete="name">
                  </div>
                  <div class="col-md-6">
                    <input type="email" name="email" class="form-control" placeholder="Alamat Email Aktif" required="" autocomplete="email">
                  </div>
                  <div class="col-md-6">
                    <input type="tel" name="phone" class="form-control" placeholder="Nomor Telepon / WhatsApp" autocomplete="tel">
                  </div>
                  <div class="col-md-6">
                    <select name="service" class="form-control" required="">
                      <option value="" disabled="" selected="">Pilih Kebutuhan Layanan Ducting</option>
                      <option value="exhaust">Ducting Exhaust (Pembuangan Udara Panas &amp; Asap)</option>
                      <option value="fresh-air">Ducting Fresh Air (Suplai Udara Segar &amp; O2)</option>
                      <option value="ac">Ducting AC Sentral (Pipa Saluran Udara Pendingin)</option>
                      <option value="pu">Ducting PU (Polyurethane Pre-Insulated)</option>
                      <option value="bjls">Ducting BJLS (Galvalum / Baja Lapis Seng)</option>
                      <option value="maintenance">Maintenance &amp; Duct Cleaning / Air Balancing</option>
                      <option value="other">Konsultasi Sistem HVAC Lengkap</option>
                    </select>
                  </div>
                  <div class="col-12">
                    <input type="text" name="subject" class="form-control" placeholder="Subjek / Nama Proyek Gedung" required="">
                  </div>
                  <div class="col-12">
                    <textarea name="message" class="form-control" rows="5" placeholder="Jelaskan kebutuhan ducting, jenis gedung (kantor/mall/restoran/pabrik), perkiraan dimensi, atau jadwal survei yang diinginkan..." required=""></textarea>
                  </div>
                  <div class="col-12">
                    <div class="loading">Memuat...</div>
                    <div class="error-message"></div>
                    <div class="sent-message">Pesan Anda telah berhasil dikirimkan. Tim spesialis Ducting HVAC kami akan segera menghubungi Anda!</div>
                    <button type="submit" class="btn-submit">Kirim Pesan Sekarang</button>
                  </div>
                </div>
              </form>
            </div>
          </div>

        </div>

      </div>

    </section><!-- /Contact Section -->'''

content = re.sub(old_contact_pattern, new_contact, content, flags=re.DOTALL)

# 13. Update Footer Links to point to Ducting products
footer_links_pattern = r'<h4>Layanan Kami</h4>\s*<ul>.*?</ul>'
new_footer_links = '''<h4>Produk Ducting</h4>
          <ul>
            <li><a href="ducting-exhaust.html">Ducting Exhaust</a></li>
            <li><a href="ducting-fresh-air.html">Ducting Fresh Air</a></li>
            <li><a href="ducting-ac.html">Ducting AC Sentral</a></li>
            <li><a href="ducting-pu.html">Ducting PU</a></li>
            <li><a href="ducting-bjls.html">Ducting BJLS</a></li>
            <li><a href="service-details.html">Maintenance &amp; Cleaning</a></li>
          </ul>'''

content = re.sub(footer_links_pattern, new_footer_links, content, flags=re.DOTALL)

with open("d:/Constructify-pro/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("index.html successfully updated!")
