import re

with open("d:/Constructify-pro/about.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Tentang Kami - Ducting HVAC</title>',
    content
)

content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Pelajari tentang Ducting HVAC, pengalaman lebih dari 25 tahun dalam fabrikasi dan instalasi cerobong saluran udara berstandar SMACNA di Indonesia.">',
    content
)

content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="tentang ducting hvac, spesialis ducting, pabrik ducting, teknisi hvac, cerobong udara indonesia">',
    content
)

# 2. About section
old_about_pattern = r'<!-- About Section -->.*?<!-- /About Section -->'
new_about = '''<!-- About Section -->
    <section id="about" class="about section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-5 align-items-center">

          <div class="col-lg-6" data-aos="fade-right" data-aos-delay="200">
            <div class="about-gallery">
              <div class="gallery-main">
                <img src="assets/img/ducting/ducting-ac.jpg" alt="Instalasi Saluran Ducting AC Sentral" class="img-fluid" loading="lazy">
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
              <h2>Kami Menghadirkan Rekayasa Tata Udara dengan Presisi &amp; Mutu Terbaik</h2>
              <p class="lead">Sejak tahun 1998, kami telah menyediakan layanan fabrikasi dan instalasi ducting HVAC berstandar internasional SMACNA. Komitmen kami terhadap keahlian aerodinamis aliran udara, efisiensi termal tanpa kondensasi, dan kepuasan klien menjadi landasan dari setiap proyek yang kami kerjakan.</p>

              <div class="about-highlights">
                <div class="row g-4">
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-shield-check"></i>
                      </div>
                      <h4>Resmi &amp; Standar SMACNA</h4>
                      <p>Kepatuhan penuh pada standar kebocoran udara minimal dan regulasi teknis keselamatan tata udara.</p>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-clock-history"></i>
                      </div>
                      <h4>Penyelesaian Tepat Waktu</h4>
                      <p>Fabrikasi cepat dengan mesin CNC modern serta koordinasi instalasi lapangan yang disiplin.</p>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-people"></i>
                      </div>
                      <h4>Teknisi &amp; MEP Berpengalaman</h4>
                      <p>Didukung oleh lebih dari 120 tenaga kerja profesional di bidang airflow sizing, mekanikal, dan isolasi.</p>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="highlight-item">
                      <div class="highlight-icon">
                        <i class="bi bi-trophy"></i>
                      </div>
                      <h4>Material Bersertifikasi</h4>
                      <p>Memakai lembaran BJLS pilihan berstandar SNI dan panel Polyurethane (PU) fire-retardant.</p>
                    </div>
                  </div>
                </div>
              </div>

              <div class="about-cta">
                <a href="contact.html" class="btn-about">Konsultasi Sistem Ducting <i class="bi bi-arrow-right"></i></a>
                <a href="projects.html" class="btn-about-outline">Lihat Portofolio Kami</a>
              </div>
            </div>
          </div>

        </div>

      </div>

    </section><!-- /About Section -->'''
content = re.sub(old_about_pattern, new_about, content, flags=re.DOTALL)

# 3. Stats section
old_stats_pattern = r'<!-- Stats Section -->.*?<!-- /Stats Section -->'
new_stats = '''<!-- Stats Section -->
    <section id="stats" class="stats section light-background">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row align-items-center gy-5">

          <div class="col-lg-5" data-aos="fade-right" data-aos-delay="100">
            <div class="stats-content">
              <span class="label-tag">Rekam Jejak Terpercaya</span>
              <h2>Angka Nyata Komitmen &amp; Mutu Tata Udara Kami</h2>
              <p>Dengan pengalaman lebih dari dua dekade di industri HVAC dan tata udara, portofolio riil kami mencerminkan standar rekayasa presisi, penghematan konsumsi daya sistem pendingin, dan kepuasan berkelanjutan dari para klien.</p>
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
                    <p>Proyek Ducting Terselesaikan</p>
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
                    <p>Klien Gedung &amp; Pabrik</p>
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

# 4. Process Section
old_process_pattern = r'<!-- Process Section -->.*?<!-- /Process Section -->'
new_process = '''<!-- Process Section -->
    <section id="process" class="process section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Tahapan Kerja Sistematis</h2>
        <p>Alur kerja terstruktur dan transparan yang menjamin efisiensi sistem ducting dari survei beban udara hingga pengujian balancing</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4">

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="100">
            <div class="process-step">
              <div class="step-number">01</div>
              <div class="step-icon">
                <i class="bi bi-speedometer2"></i>
              </div>
              <h3>Survei Beban &amp; CFM</h3>
              <p>Kami menganalisis volume ruangan, kebutuhan laju udara (CFM), hambatan statis, dan spesifikasi unit pendingin/exhaust.</p>
            </div>
          </div><!-- End Step -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="200">
            <div class="process-step">
              <div class="step-number">02</div>
              <div class="step-icon">
                <i class="bi bi-diagram-3"></i>
              </div>
              <h3>Desain CAD &amp; Sizing</h3>
              <p>Penyusunan gambar kerja 3D/BIM, kalkulasi ukuran penampang saluran, posisi volume damper, dan pemilihan material PU/BJLS.</p>
            </div>
          </div><!-- End Step -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="300">
            <div class="process-step">
              <div class="step-number">03</div>
              <div class="step-icon">
                <i class="bi bi-gear-wide-connected"></i>
              </div>
              <h3>Fabrikasi &amp; Instalasi</h3>
              <p>Fabrikasi otomatis presisi di workshop dilanjutkan pemasangan di lapangan oleh tim MEP dengan standar keselamatan K3 ketat.</p>
            </div>
          </div><!-- End Step -->

          <div class="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay="400">
            <div class="process-step">
              <div class="step-number">04</div>
              <div class="step-icon">
                <i class="bi bi-check2-circle"></i>
              </div>
              <h3>Testing &amp; Air Balancing</h3>
              <p>Pengukuran debit udara di setiap diffuser dengan anemometer, uji kebocoran ducting, dan penyerahan sertifikat garansi resmi.</p>
            </div>
          </div><!-- End Step -->

        </div>

      </div>

    </section><!-- /Process Section -->'''
content = re.sub(old_process_pattern, new_process, content, flags=re.DOTALL)

# 5. Testimonials Section
old_testi_pattern = r'<!-- Testimonials Section -->.*?<!-- /Testimonials Section -->'
new_testi = '''<!-- Testimonials Section -->
    <section id="testimonials" class="testimonials section light-background">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Testimoni Klien</h2>
        <p>Simak kepuasan para pengelola gedung, tim manajemen rumah sakit, dan pimpinan pabrik yang mempercayakan sistem ducting HVAC mereka kepada kami</p>
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
                <p>"Ducting HVAC menyelesaikan pemasangan saluran AC sentral gedung kami lebih cepat dari target. Kerapian isolasi dan hasil penyeimbangan udaranya sangat dingin merata."</p>
                <div class="client-info d-flex align-items-center gap-16">
                  <img src="assets/img/person/person-m-3.webp" alt="James Harrison" class="img-fluid">
                  <div>
                    <h4>James Harrison</h4>
                    <span>Building Manager Gedung Komersial</span>
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
                <p>"Kualitas ducting PU untuk ruang steril rumah sakit kami terbukti sangat higienis, anti-jamur, dan tidak berembun sama sekali. Sangat direkomendasikan untuk fasilitas medis."</p>
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
                <p>"Sistem exhaust dapur restoran kami yang sebelumnya panas dan berasap kini menjadi sangat nyaman. Tim teknisinya sangat paham kalkulasi CFM dan static pressure."</p>
                <div class="client-info d-flex align-items-center gap-16">
                  <img src="assets/img/person/person-m-9.webp" alt="Michael Torres" class="img-fluid">
                  <div>
                    <h4>Michael Torres</h4>
                    <span>Pengelola Restoran &amp; Food Court</span>
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
                <p>"Ketahanan ducting BJLS galvalum di area pabrik kami sangat luar biasa. Tahan getaran, sambungan kedap udara, dan instalasi sangat kokoh memenuhi regulasi industri."</p>
                <div class="client-info d-flex align-items-center gap-16">
                  <img src="assets/img/person/person-f-12.webp" alt="Olivia Nguyen" class="img-fluid">
                  <div>
                    <h4>Olivia Nguyen</h4>
                    <span>Manager Fasilitas Industri</span>
                  </div>
                </div>
              </div>
            </div><!-- End Testimonial -->

          </div>
          <div class="swiper-pagination"></div>
        </div>

      </div>

    </section><!-- /Testimonials Section -->'''
content = re.sub(old_testi_pattern, new_testi, content, flags=re.DOTALL)

# 6. Call To Action Section
old_cta_pattern = r'<!-- Call To Action Section -->.*?<!-- /Call To Action Section -->'
new_cta = '''<!-- Call To Action Section -->
    <section id="call-to-action" class="call-to-action section dark-background">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row align-items-center gy-5">

          <div class="col-lg-6" data-aos="fade-right" data-aos-delay="150">
            <div class="info-block">
              <span class="tagline">Bermitra dengan Spesialis Tata Udara</span>
              <h2>Optimalkan Kualitas Sirkulasi Udara Gedung Anda Hari Ini</h2>
              <p>Siap merealisasikan sistem saluran ducting HVAC yang efisien, senyap, dan bebas kebocoran? Bekerjasamalah dengan tim teknisi berpengalaman yang berkomitmen pada standar kualitas tertinggi, keselamatan kerja, dan ketepatan waktu.</p>

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
                    <h5>Material Bersertifikasi SNI</h5>
                    <p>Kepatuhan ketat terhadap spesifikasi teknis dan anti-karat</p>
                  </div>
                </div><!-- End Highlight Card -->

                <div class="highlight-card" data-aos="zoom-in" data-aos-delay="340">
                  <div class="card-icon">
                    <i class="bi bi-graph-up-arrow"></i>
                  </div>
                  <div class="card-body-content">
                    <h5>Efisiensi Anggaran &amp; Energi</h5>
                    <p>Estimasi biaya transparan dan desain airflow hemat listrik</p>
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
                <img src="assets/img/ducting/ducting-bjls.jpg" alt="Instalasi Saluran Ducting HVAC" class="img-fluid">
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

# 7. Footer links
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

with open("d:/Constructify-pro/about.html", "w", encoding="utf-8") as f:
    f.write(content)

print("about.html updated successfully!")
