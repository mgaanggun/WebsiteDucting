import re

with open("d:/Constructify-pro/projects.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Portofolio Proyek - Ducting HVAC</title>',
    content
)

content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Jelajahi portofolio proyek ducting HVAC terbaik kami: instalasi ducting exhaust restoran, fresh air rumah sakit, ducting AC sentral perkantoran, PU cleanroom, dan BJLS industri.">',
    content
)

content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="portofolio ducting hvac, proyek ducting exhaust, proyek ducting ac sentral, ducting pu farmasi, ducting bjls pabrik, instalasi saluran udara">',
    content
)

# 2. Section Title and Filter Categories
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

            <!-- Project 1 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-exhaust">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-exhaust.jpg" alt="Exhaust Hood Dapur Mall" class="img-fluid" loading="lazy">
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

            <!-- Project 2 -->
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

            <!-- Project 3 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-bjls">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-bjls.jpg" alt="Ducting BJLS Smoke Spill Basement" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting BJLS &amp; Industri</span>
                    <h3>Ducting BJLS Smoke Spill Basement</h3>
                    <p>Fabrikasi saluran baja lapis seng tebal tahan api untuk evakuasi asap darurat basement gedung</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting BJLS Smoke Spill Basement"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 4 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-ac">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-pu.jpg" alt="Cleanroom Ducting PU Farmasi & RS" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting AC &amp; PU</span>
                    <h3>Cleanroom Ducting PU Farmasi &amp; RS</h3>
                    <p>Pemasangan panel Polyurethane higienis bebas serat partikel untuk ruang operasi dan lab steril</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-pu.jpg" class="card-action glightbox" data-gallery="projects" title="Cleanroom Ducting PU Farmasi &amp; RS"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 5 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-exhaust">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-fresh-air.jpg" alt="Sistem Fresh Air & Tekanan Positif RS" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Exhaust &amp; Fresh Air</span>
                    <h3>Sistem Fresh Air &amp; Tekanan Positif RS</h3>
                    <p>Saluran suplai udara segar berfiltrasi HEPA menjaga kemurnian sirkulasi oksigen rumah sakit</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-fresh-air.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Fresh Air &amp; Tekanan Positif RS"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 6 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-bjls">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-bjls-2.jpg" alt="Ventilasi Pabrik Manufaktur Otomotif" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting BJLS &amp; Industri</span>
                    <h3>Ventilasi Pabrik Manufaktur Otomotif</h3>
                    <p>Saluran udara volume besar bertekanan tinggi untuk pembuangan polutan dan pendinginan produksi</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls-2.jpg" class="card-action glightbox" data-gallery="projects" title="Ventilasi Pabrik Manufaktur Otomotif"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 7 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-exhaust">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-exhaust-2.jpg" alt="Exhaust Shaft Restoran Hotel Bintang 5" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Exhaust &amp; Fresh Air</span>
                    <h3>Exhaust Shaft Restoran Hotel Bintang 5</h3>
                    <p>Sistem cerobong pembuangan minyak dan asap vertikal 18 lantai bebas kebocoran aroma</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-exhaust-2.jpg" class="card-action glightbox" data-gallery="projects" title="Exhaust Shaft Restoran Hotel Bintang 5"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 8 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-ac">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-ac-2.jpg" alt="Instalasi Ducting VRV Hunian Mewah" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting AC &amp; PU</span>
                    <h3>Instalasi Ducting VRV Hunian Mewah</h3>
                    <p>Sistem saluran pendingin tersembunyi ceiling konsil dengan difuser linier minimalis dan senyap</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-ac-2.jpg" class="card-action glightbox" data-gallery="projects" title="Instalasi Ducting VRV Hunian Mewah"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 9 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-bjls">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-bjls-3.jpg" alt="Ducting Galvanis Gudang Logistik" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting BJLS &amp; Industri</span>
                    <h3>Ducting Galvanis Gudang Logistik</h3>
                    <p>Jaringan distribusi udara berjangkauan panjang untuk menjaga temperatur stabil ruang kargo</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls-3.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting Galvanis Gudang Logistik"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 10 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-ac">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-pu-2.jpg" alt="Ducting PU Menara Perbankan" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting AC &amp; PU</span>
                    <h3>Ducting PU Pre-Insulated Gedung Bank</h3>
                    <p>Instalasi saluran pendingin ringan berefisiensi energi tinggi tanpa resiko kondensasi tetesan air</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-pu-2.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting PU Pre-Insulated Gedung Bank"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 11 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-exhaust">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-fresh-air-2.jpg" alt="Sirkulasi Fresh Air Bioskop" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Exhaust &amp; Fresh Air</span>
                    <h3>Sirkulasi Fresh Air Gedung Bioskop</h3>
                    <p>Pengaturan suplai oksigen konstan di ruang auditorium teater kedap suara tanpa desis bising</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-fresh-air-2.jpg" class="card-action glightbox" data-gallery="projects" title="Sirkulasi Fresh Air Gedung Bioskop"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Project -->

            <!-- Project 12 -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-bjls">
              <div class="project-card">
                <img src="assets/img/ducting/ducting-ac-3.jpg" alt="Ducting AHU Utama Bandara" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">Ducting BJLS &amp; Industri</span>
                    <h3>Ducting AHU Utama Concourse Bandara</h3>
                    <p>Sistem distribusi tata udara volume masif di area concourse dan terminal keberangkatan</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-ac-3.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting AHU Utama Concourse Bandara"><i class="bi bi-arrows-fullscreen"></i></a>
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

# 3. Call To Action Section
old_cta_pattern = r'<!-- Call To Action Section -->.*?<!-- /Call To Action Section -->'
new_cta = '''<!-- Call To Action Section -->
    <section id="call-to-action" class="call-to-action section dark-background">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row align-items-center gy-5">

          <div class="col-lg-6" data-aos="fade-right" data-aos-delay="150">
            <div class="info-block">
              <span class="tagline">Bermitra dengan Tim Profesional</span>
              <h2>Optimalkan Sirkulasi Tata Udara &amp; Efisiensi Gedung Anda</h2>
              <p>Siap memulai proyek instalasi saluran ducting HVAC Anda? Hubungi spesialis teknik dan penaksir biaya kami hari ini untuk konsultasi menyeluruh dan penawaran resmi.</p>

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
                    <h5>Jaminan Keselamatan Kerja</h5>
                    <p>Kepatuhan ketat terhadap regulasi K3 dan standar keselamatan</p>
                  </div>
                </div><!-- End Highlight Card -->

                <div class="highlight-card" data-aos="zoom-in" data-aos-delay="340">
                  <div class="card-icon">
                    <i class="bi bi-graph-up-arrow"></i>
                  </div>
                  <div class="card-body-content">
                    <h5>Optimalisasi Anggaran</h5>
                    <p>Penetapan harga transparan tanpa ada biaya tak terduga</p>
                  </div>
                </div><!-- End Highlight Card -->
              </div>

              <div class="action-row" data-aos="fade-up" data-aos-delay="400">
                <a href="contact.html" class="btn-get-started">
                  <span>Minta Penawaran Biaya</span>
                  <i class="bi bi-arrow-right"></i>
                </a>
                <div class="phone-block">
                  <div class="phone-icon">
                    <i class="bi bi-telephone-fill"></i>
                  </div>
                  <div class="phone-details">
                    <span class="phone-label">Konsultasi dengan Tenaga Ahli</span>
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
                  <span class="counter-text">Proyek Terselesaikan</span>
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

with open("d:/Constructify-pro/projects.html", "w", encoding="utf-8") as f:
    f.write(content)

print("projects.html updated successfully!")
