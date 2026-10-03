import re

# ----------------- 1. UPDATE team.html -----------------
with open("d:/Constructify-pro/team.html", "r", encoding="utf-8") as f:
    team_content = f.read()

team_content = re.sub(
    r'<title>.*?</title>',
    '<title>Tim Ahli - Ducting HVAC</title>',
    team_content
)
team_content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Kenali tim insinyur MEP, desainer tata udara, dan tenaga ahli fabrikasi ducting HVAC berpengalaman lebih dari 25 tahun di Indonesia.">',
    team_content
)
team_content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="tim ducting hvac, insinyur mep, teknisi ducting bjls, ahli tata udara, teknisi air balancing">',
    team_content
)
team_content = re.sub(
    r'<h1 class="mb-2 mb-lg-0">Tim Ahli Konstruksi</h1>',
    '<h1 class="mb-2 mb-lg-0">Tim Ahli Tata Udara &amp; MEP</h1>',
    team_content
)
team_content = re.sub(
    r'<p>Jajaran profesional berdedikasi dengan pengalaman puluhan tahun di bidang rekayasa teknik, perancangan arsitektur, dan manajemen lapangan</p>',
    '<p>Jajaran profesional berdedikasi dengan pengalaman puluhan tahun di bidang rekayasa HVAC, perancangan airflow, fabrikasi presisi, dan instalasi lapangan</p>',
    team_content
)

# Replace roles in team.html
team_content = team_content.replace('<span>Direktur Utama (CEO)</span>', '<span>Direktur Teknik &amp; MEP Specialist</span>')
team_content = team_content.replace('<span>Arsitek Utama</span>', '<span>Kepala Desain Airflow &amp; Sizing</span>')
team_content = team_content.replace('<span>Kepala Arsitek</span>', '<span>Kepala Desain Airflow &amp; Sizing</span>')
team_content = team_content.replace('<span>Manajer Proyek Senior</span>', '<span>Manajer Fabrikasi &amp; Instalasi</span>')
team_content = team_content.replace('<span>Pengawas Lapangan &amp; K3</span>', '<span>Pengawas Mutu K3 &amp; Air Balancing</span>')
team_content = team_content.replace('<span>Insinyur Struktur Utama</span>', '<span>Insinyur Mekanikal &amp; Ducting BJLS</span>')
team_content = team_content.replace('<span>Manajer Operasional Proyek</span>', '<span>Spesialis Cleanroom &amp; Ducting PU</span>')
team_content = team_content.replace('<span>Kepala Penaksir Biaya (Estimator)</span>', '<span>Estimator Biaya &amp; Konsultan CFM</span>')
team_content = team_content.replace('<span>Manajer Pengadaan &amp; Logistik</span>', '<span>Koordinator Pengadaan Material &amp; QC</span>')

# Replace Testimonials & CTA in team.html
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
team_content = re.sub(old_cta_pattern, new_cta, team_content, flags=re.DOTALL)

# Testimonials in team.html
team_content = team_content.replace('Simak pengakuan para pengembang properti, pelaku bisnis, dan pemilik hunian yang telah membuktikan kualitas pengerjaan dan integritas Constructify', 'Simak pengakuan para pengelola gedung, tim manajemen rumah sakit, dan pimpinan pabrik yang telah membuktikan kualitas sistem ducting HVAC kami')
team_content = team_content.replace('"Standar keselamatan kerja dan kualitas pengerjaan tertinggi. Kami telah bermitra dengan Constructify dalam 4 proyek infrastruktur wilayah dan selalu puas dengan hasilnya."', '"Ketahanan ducting BJLS galvalum di area pabrik kami sangat luar biasa. Tahan getaran, sambungan kedap udara, dan instalasi sangat kokoh memenuhi regulasi industri."')
team_content = team_content.replace('"Constructify menyelesaikan pembangunan gedung perkantoran komersial kami tiga minggu lebih awal dari jadwal. Integritas struktur dan detail finishing arsitekturnya sungguh luar biasa."', '"Ducting HVAC menyelesaikan pemasangan saluran AC sentral gedung kami lebih cepat dari target. Kerapian isolasi dan hasil penyeimbangan udaranya sangat dingin merata."')

# Footer links
team_content = re.sub(
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
    team_content,
    flags=re.DOTALL
)

with open("d:/Constructify-pro/team.html", "w", encoding="utf-8") as f:
    f.write(team_content)
print("team.html updated!")


# ----------------- 2. UPDATE contact.html -----------------
with open("d:/Constructify-pro/contact.html", "r", encoding="utf-8") as f:
    contact_content = f.read()

contact_content = re.sub(
    r'<title>.*?</title>',
    '<title>Kontak Kami - Ducting HVAC</title>',
    contact_content
)
contact_content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Hubungi spesialis Ducting HVAC untuk konsultasi teknis, survei laju aliran udara (CFM), dan estimasi penawaran biaya resmi.">',
    contact_content
)
contact_content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="kontak ducting hvac, konsultasi ducting, survei ducting, nomor telepon ducting hvac, pabrik ducting jakarta">',
    contact_content
)
contact_content = contact_content.replace(
    '<p>Konsultasikan kebutuhan proyek konstruksi Anda bersama tim estimator biaya dan insinyur profesional Constructify</p>',
    '<p>Konsultasikan kebutuhan sistem saluran udara dan estimasi biaya instalasi ducting HVAC gedung Anda bersama tim spesialis kami</p>'
)
contact_content = contact_content.replace(
    '742 Evergreen Terrace<br>Springfield, IL 62701',
    'Workshop Fabrikasi Ducting HVAC<br>Jakarta &amp; Sekitarnya, Indonesia'
)
contact_content = contact_content.replace(
    'contact@example.com<br>projects@example.com',
    'info@ductinghvac.co.id<br>proyek@ductinghvac.co.id'
)

# Update Select options in contact.html
old_select = r'<select name="service" class="form-control" required="">.*?</select>'
new_select = '''<select name="service" class="form-control" required="">
                      <option value="" disabled="" selected="">Pilih Kebutuhan Layanan Ducting</option>
                      <option value="exhaust">Ducting Exhaust (Pembuangan Udara Panas &amp; Asap)</option>
                      <option value="fresh-air">Ducting Fresh Air (Suplai Udara Segar &amp; O2)</option>
                      <option value="ac">Ducting AC Sentral (Pipa Saluran Udara Pendingin)</option>
                      <option value="pu">Ducting PU (Polyurethane Pre-Insulated)</option>
                      <option value="bjls">Ducting BJLS (Galvalum / Baja Lapis Seng)</option>
                      <option value="maintenance">Maintenance &amp; Duct Cleaning / Air Balancing</option>
                      <option value="other">Konsultasi Sistem HVAC Lengkap</option>
                    </select>'''
contact_content = re.sub(old_select, new_select, contact_content, flags=re.DOTALL)
contact_content = contact_content.replace(
    'placeholder="Jelaskan kebutuhan proyek, lokasi lahan, dan target waktu pengerjaan Anda..."',
    'placeholder="Jelaskan kebutuhan ducting, jenis gedung (kantor/mall/restoran/pabrik), perkiraan dimensi, atau jadwal survei yang diinginkan..."'
)
contact_content = contact_content.replace(
    'placeholder="Subjek / Judul Rencana Proyek"',
    'placeholder="Subjek / Nama Proyek Gedung"'
)

# Footer links
contact_content = re.sub(
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
    contact_content,
    flags=re.DOTALL
)

with open("d:/Constructify-pro/contact.html", "w", encoding="utf-8") as f:
    f.write(contact_content)
print("contact.html updated!")


# ----------------- 3. UPDATE blog.html -----------------
with open("d:/Constructify-pro/blog.html", "r", encoding="utf-8") as f:
    blog_content = f.read()

blog_content = re.sub(
    r'<title>.*?</title>',
    '<title>Blog &amp; Artikel Tata Udara - Ducting HVAC</title>',
    blog_content
)
blog_content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Temukan artikel mendalam seputar sistem ducting HVAC, perbandingan ducting PU vs BJLS, efisiensi sirkulasi udara, dan standar SMACNA dari para ahli Ducting HVAC.">',
    blog_content
)
blog_content = re.sub(
    r'<meta name="keywords" content=".*?">',
    '<meta name="keywords" content="blog ducting hvac, artikel tata udara, tips ducting pu, ducting bjls, exhaust dapur restoran, air balancing hvac">',
    blog_content
)
blog_content = blog_content.replace('<h1 class="mb-2 mb-lg-0">Blog &amp; Berita Konstruksi</h1>', '<h1 class="mb-2 mb-lg-0">Blog &amp; Artikel Tata Udara</h1>')
blog_content = blog_content.replace('<h2>Wawasan Industri Konstruksi Terkini</h2>', '<h2>Wawasan Sistem Tata Udara &amp; Ducting HVAC Terkini</h2>')
blog_content = blog_content.replace(
    '<p>Analisis teknis, inovasi rekayasa arsitektur berkelanjutan, dan standar konstruksi modern dari tim ahli Constructify</p>',
    '<p>Analisis teknis, efisiensi sirkulasi udara, pemilihan material saluran ducting, dan standar SMACNA dari tim ahli Ducting HVAC</p>'
)

# Update CTA in blog.html
blog_content = re.sub(old_cta_pattern, new_cta, blog_content, flags=re.DOTALL)

# Footer links
blog_content = re.sub(
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
    blog_content,
    flags=re.DOTALL
)

with open("d:/Constructify-pro/blog.html", "w", encoding="utf-8") as f:
    f.write(blog_content)
print("blog.html updated!")


# ----------------- 4. UPDATE blog-details*.html -----------------
for blog_file in ["blog-details.html", "blog-details-1.html", "blog-details-2.html"]:
    with open(f"d:/Constructify-pro/{blog_file}", "r", encoding="utf-8") as f:
        bd = f.read()

    bd = re.sub(
        r'<title>.*?</title>',
        '<title>Wawasan Tata Udara &amp; Ducting HVAC - Ducting HVAC</title>',
        bd
    )
    bd = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="Pelajari standar efisiensi energi ducting HVAC, perancangan sirkulasi udara, dan isolasi termal anti-kondensasi dari para ahli Ducting HVAC.">',
        bd
    )
    bd = re.sub(
        r'<meta name="keywords" content=".*?">',
        '<meta name="keywords" content="artikel ducting hvac, efisiensi energi tata udara, ducting pu, ducting bjls, air balancing">',
        bd
    )

    # Clean author bio and text
    bd = bd.replace("jurnalis konstruksi di Constructify", "jurnalis tata udara di Ducting HVAC")
    bd = bd.replace("Konstruksi berkelanjutan bukan lagi sekadar pemanis citra", "Efisiensi tata udara bukan lagi sekadar pelengkap gedung")
    bd = bd.replace("spesifikasi baku konstruksi hijau Constructify", "standar baku tata udara Ducting HVAC")
    bd = bd.replace("Diakui secara luas atas mutu pengerjaan konstruksi dan keselamatan kerja tinggi.", "Diakui secara luas atas mutu pengerjaan ducting HVAC dan standar SMACNA presisi.")
    bd = bd.replace("Merencanakan Konstruksi Gedung Tinggi atau Fasilitas Komersial?", "Merencanakan Sistem Ducting HVAC Gedung atau Fasilitas Komersial?")
    bd = bd.replace("Konsultasikan kebutuhan rekayasa struktur, analisis geoteknik, dan manajemen konstruksi Anda langsung dengan dewan ahli Constructify.", "Konsultasikan kebutuhan sistem saluran ducting, kalkulasi CFM, dan efisiensi tata udara Anda langsung dengan spesialis Ducting HVAC.")
    bd = bd.replace("konstruksi fasilitas bertingkat tinggi", "sistem tata udara gedung bertingkat tinggi")
    bd = bd.replace("Di Constructify, para insinyur struktur kami", "Di Ducting HVAC, para engineer tata udara kami")

    # Footer links
    bd = re.sub(
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
        bd,
        flags=re.DOTALL
    )

    with open(f"d:/Constructify-pro/{blog_file}", "w", encoding="utf-8") as f:
        f.write(bd)
    print(f"{blog_file} updated!")


# ----------------- 5. UPDATE ducting-*.html files (fix stray konstruksi/constructify) -----------------
for d_file in ["ducting-exhaust.html", "ducting-fresh-air.html", "ducting-ac.html", "ducting-pu.html", "ducting-bjls.html"]:
    with open(f"d:/Constructify-pro/{d_file}", "r", encoding="utf-8") as f:
        dc = f.read()

    dc = dc.replace("saluran cerobong berkonstruksi kedap udara", "saluran cerobong berstruktur kedap udara")
    dc = dc.replace("dalam industri konstruksi mekanikal elektrikal gedung (MEP)", "dalam industri tata udara dan mekanikal elektrikal gedung (MEP)")
    dc = dc.replace("konstruksi ducting AC Constructify", "fabrikasi ducting AC kami")
    dc = dc.replace("Jaminan Kualitas Konstruksi AC", "Jaminan Kualitas Fabrikasi Ducting AC")
    dc = dc.replace("Constructify", "Ducting HVAC")

    # Footer links
    dc = re.sub(
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
        dc,
        flags=re.DOTALL
    )

    with open(f"d:/Constructify-pro/{d_file}", "w", encoding="utf-8") as f:
        f.write(dc)
    print(f"{d_file} cleaned!")


# ----------------- 6. UPDATE privacy.html, terms.html, starter-page.html, 404.html -----------------
for o_file in ["privacy.html", "terms.html", "starter-page.html", "404.html"]:
    with open(f"d:/Constructify-pro/{o_file}", "r", encoding="utf-8") as f:
        oc = f.read()

    oc = oc.replace("layanan konstruksi resmi dari Constructify", "layanan resmi dari Ducting HVAC")
    oc = oc.replace("perjanjian konstruksi", "perjanjian layanan ducting hvac")
    oc = oc.replace("layanan konstruksi kami", "layanan ducting HVAC kami")
    oc = oc.replace("layanan konstruksi yang lebih baik", "layanan sistem ducting HVAC yang lebih baik")
    oc = oc.replace("detail rencana proyek konstruksi", "detail rencana proyek ducting HVAC")
    oc = oc.replace("layanan konstruksi", "layanan ducting HVAC")
    oc = oc.replace("Constructify", "Ducting HVAC")

    # Footer links
    oc = re.sub(
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
        oc,
        flags=re.DOTALL
    )

    with open(f"d:/Constructify-pro/{o_file}", "w", encoding="utf-8") as f:
        f.write(oc)
    print(f"{o_file} cleaned!")

print("All remaining files processed successfully!")
