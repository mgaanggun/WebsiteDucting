import re

with open("d:/Constructify-pro/services.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Layanan Fabrikasi &amp; Instalasi Ducting HVAC</title>',
    content
)

content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Layanan spesialis Ducting HVAC terpadu: Ducting Exhaust dapur/industri, Fresh Air filtrasi O2, Ducting AC Sentral AHU/VRV, Ducting PU Cleanroom, dan BJLS Galvalum berstandar SMACNA.">',
    content
)

content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="layanan ducting hvac, fabrikasi ducting bjls, ducting pu polyurethane, instalasi cerobong exhaust, fresh air ventilation, duct cleaning air balancing">',
    content
)

# 2. Services Section
old_services_pattern = r'<!-- Services Section -->.*?<!-- /Services Section -->'
new_services = '''<!-- Services Section -->
    <section id="services" class="services section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Layanan Spesialis Ducting HVAC Kami</h2>
        <p>Solusi saluran tata udara terpadu dengan standar SMACNA, efisiensi aerodinamis tinggi, dan jaminan kualitas bebas kebocoran</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4 align-items-stretch">

          <div class="col-lg-4" data-aos="fade-right" data-aos-delay="100">
            <div class="services-image">
              <img src="assets/img/ducting/ducting-exhaust.jpg" alt="Layanan Fabrikasi Ducting HVAC" class="img-fluid">
              <div class="image-overlay">
                <h3>Keandalan Sirkulasi Udara &amp; Mutu Terbaik</h3>
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
                    <h4>Ducting Exhaust</h4>
                    <p>Cerobong khusus untuk menyalurkan udara kotor, panas, uap dapur restoran, dan asap industri dari dalam ruangan ke luar ruangan secara aman.</p>
                    <a href="ducting-exhaust.html" class="stretched-link text-decoration-none small text-muted mt-2 d-inline-block">Lihat Detail Produk <i class="bi bi-chevron-right"></i></a>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="200">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-cloud-sun"></i>
                  </div>
                  <div class="service-body">
                    <h4>Ducting Fresh Air</h4>
                    <p>Saluran suplai udara segar berfiltrasi dari luar gedung ke dalam ruangan, menjaga sirkulasi oksigen, tekanan positif, dan kualitas udara (IAQ).</p>
                    <a href="ducting-fresh-air.html" class="stretched-link text-decoration-none small text-muted mt-2 d-inline-block">Lihat Detail Produk <i class="bi bi-chevron-right"></i></a>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="300">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-snow2"></i>
                  </div>
                  <div class="service-body">
                    <h4>Ducting AC Sentral</h4>
                    <p>Pipa dan cerobong distribusi udara dingin dari sistem AC Sentral (AHU, FCU, VRV) ke seluruh zona ruangan secara merata, efisien, dan senyap.</p>
                    <a href="ducting-ac.html" class="stretched-link text-decoration-none small text-muted mt-2 d-inline-block">Lihat Detail Produk <i class="bi bi-chevron-right"></i></a>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="400">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-layers-half"></i>
                  </div>
                  <div class="service-body">
                    <h4>Ducting PU (Polyurethane)</h4>
                    <p>Cerobong berbahan Pre-Insulated Polyurethane yang ringan, higienis, anti-jamur, bebas kondensasi, ideal untuk rumah sakit, farmasi, dan cleanroom.</p>
                    <a href="ducting-pu.html" class="stretched-link text-decoration-none small text-muted mt-2 d-inline-block">Lihat Detail Produk <i class="bi bi-chevron-right"></i></a>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="500">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-shield-check"></i>
                  </div>
                  <div class="service-body">
                    <h4>Ducting BJLS (Galvalum)</h4>
                    <p>Cerobong baja lapis seng tahan benturan dan tekanan statis tinggi, sangat kokoh untuk industri, basement, dan sistem smoke-spill darurat.</p>
                    <a href="ducting-bjls.html" class="stretched-link text-decoration-none small text-muted mt-2 d-inline-block">Lihat Detail Produk <i class="bi bi-chevron-right"></i></a>
                  </div>
                </div>
              </div><!-- End Service -->

              <div class="col-md-6" data-aos="fade-up" data-aos-delay="600">
                <div class="service-item">
                  <div class="service-icon">
                    <i class="bi bi-tools"></i>
                  </div>
                  <div class="service-body">
                    <h4>Maintenance &amp; Duct Cleaning</h4>
                    <p>Pembersihan kerak minyak &amp; debu saluran udara, perbaikan kebocoran isolasi, penggantian filter HEPA, serta pengujian Air Balancing (TAB).</p>
                    <a href="service-details.html" class="stretched-link text-decoration-none small text-muted mt-2 d-inline-block">Lihat Detail Layanan <i class="bi bi-chevron-right"></i></a>
                  </div>
                </div>
              </div><!-- End Service -->

            </div>
          </div>

        </div>

      </div>

    </section><!-- /Services Section -->'''
content = re.sub(old_services_pattern, new_services, content, flags=re.DOTALL)

# 3. Process Section
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
              <h3>Survei Beban &amp; CFM</h3>
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
              <p>Penyusunan shop drawing 3D/BIM, kalkulasi ukuran penampang saluran, posisi diffuser, dan pemilihan damper pengatur.</p>
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
              <p>Pemasangan gantungan antivibrasi, sealing kedap udara, dan pengujian Test Adjust Balance (TAB) aliran udara.</p>
            </div>
          </div><!-- End Step -->

        </div>

      </div>

    </section><!-- /Process Section -->'''
content = re.sub(old_process_pattern, new_process, content, flags=re.DOTALL)

# 4. Faq Section
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

# 5. Call To Action Section
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

# 6. Footer links
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

with open("d:/Constructify-pro/services.html", "w", encoding="utf-8") as f:
    f.write(content)

print("services.html updated successfully!")
