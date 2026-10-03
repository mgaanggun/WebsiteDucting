import re

articles = [
    {
        "id": 1,
        "file": "blog-details-1.html",
        "title": "Efisiensi Energi Sistem Ducting HVAC pada Bangunan Komersial Modern",
        "short_title": "Efisiensi Energi HVAC",
        "badge": "Ducting AC Sentral & Energi",
        "date": "12 Oktober 2026",
        "read_time": "5 mnt baca",
        "comments": "14 Komentar",
        "image": "assets/img/ducting/ducting-ac.jpg",
        "excerpt": "Pelajari bagaimana rancangan saluran ducting aerodinamis, pemilihan insulasi termal tertutup, dan komisioning airflow mampu memangkas konsumsi listrik chiller gedung komersial hingga 30%.",
        "lead": "Seiring dengan melonjaknya biaya energi dan target dekarbonisasi global, sistem tata udara (HVAC) pada gedung perkantoran, pusat perbelanjaan, dan perhotelan modern menuntut efisiensi operasional tanpa mengorbankan kenyamanan termal para penghuninya.",
        "p1": "Saluran udara (ducting) merupakan urat nadi dari seluruh sistem pendingin sentral. Kehilangan tekanan statis (static pressure drop) dan turbulensi akibat desain saluran yang buruk memaksa motor fan pada Air Handling Unit (AHU) bekerja jauh melampaui kapasitas idealnya, yang berujung pada lonjakan tagihan listrik operasional gedung.",
        "h2_1": "Rekayasa Aerodinamis & Sambungan Flange Kedap Udara",
        "p2": "Di Ducting HVAC, tim rekayasa kami merancang jalur saluran udara dengan memperhitungkan radius belokan aerodinamis serta memasang double-thickness turning vanes pada setiap elbow 90 derajat. Penggunaan sambungan Flange TDF/TDC dengan mastic sealant berkualitas tinggi memastikan tingkat kebocoran udara berada jauh di bawah 1%, melampaui standar ketat SMACNA Air Duct Leakage Class 3.",
        "h2_2": "Proteksi Termal Menyeluruh Anti-Kondensasi",
        "p3": "Selain aliran udara, isolasi termal menjadi faktor penentu efisiensi. Kami menerapkan insulasi glasswool berdensitas tinggi 24-32 kg/m³ atau closed-cell elastomeric foam dengan barrier aluminium foil berdaya rekat kuat. Isolasi presisi ini memutus jembatan termal (thermal bridging), mencegah kondensasi titik embun (sweating) yang merusak plafon, serta memastikan temperatur udara dingin tidak terbuang sia-sia di sepanjang jalur distribusi.",
        "features": [
            "Pengurangan friksi aliran udara hingga 25% dengan turning vanes aerodinamis presisi.",
            "Tingkat kebocoran udara teruji di bawah 1% sesuai standar SMACNA Air Duct Leakage Test.",
            "Proteksi termal anti-kondensasi yang menjamin stabilitas suhu dingin dari AHU ke diffuser.",
            "Penghematan konsumsi daya listrik chiller dan motor fan gedung komersial hingga 30% per tahun."
        ],
        "related": [2, 3, 4]
    },
    {
        "id": 2,
        "file": "blog-details-2.html",
        "title": "Standar Mutu SMACNA & Uji Kebocoran Udara pada Fabrikasi Ducting BJLS",
        "short_title": "Standar Mutu SMACNA BJLS",
        "badge": "Ducting BJLS & Rekayasa",
        "date": "28 September 2026",
        "read_time": "7 mnt baca",
        "comments": "18 Komentar",
        "image": "assets/img/ducting/ducting-bjls.jpg",
        "excerpt": "Pembahasan mendalam mengenai standar SMACNA HVAC Duct Construction, teknik sambungan TDF bersealant, serta metode pengujian pressure test guna meminimalkan kebocoran udara statis.",
        "lead": "Dalam industri rekayasa mekanikal gedung bertingkat, standar SMACNA (Sheet Metal and Air Conditioning Contractors' National Association) menjadi acuan baku internasional yang menentukan kekuatan struktural, ketahanan getaran, dan integritas saluran udara berbahan BJLS.",
        "p1": "Pemilihan ketebalan pelat baja lapis seng (BJLS) harus disesuaikan secara matematis dengan dimensi penampang ducting serta tekanan statis operasional (static pressure water gauge). Menggunakan pelat yang terlalu tipis berisiko menimbulkan deformasi 'oil-canning' dan desis bising getaran saat blower berkecepatan tinggi beroperasi.",
        "h2_1": "Fabrikasi Otomatisasi dengan Auto Duct Line 5",
        "p2": "Workshop Ducting HVAC mengoperasikan mesin terotomatisasi Auto Duct Line 5 dan CNC Plasma Cutting untuk membentuk profil sambungan TDF (Transverse Duct Flange) langsung dari lembaran baja tanpa proses pelipatan manual. Hasilnya adalah ketepatan dimensi sudut 90 derajat yang presisi, penguncian corner lock yang kokoh, dan sambungan yang seragam di setiap segmen.",
        "h2_2": "Prosedur Uji Kebocoran (Duct Leakage Testing)",
        "p3": "Sebelum saluran diinsulasi dan ditutup plafon, wajib dilakukan pengetesan kebocoran udara (duct leakage test) dengan memberikan tekanan positif 500 Pa menggunakan calibrated orifice blower. Pengujian ini memastikan tidak ada celah udara yang lolos, menjamin volume udara (CFM) yang dihembuskan sampai seutuhnya ke titik ruangan yang dituju.",
        "features": [
            "Pemilihan spesifikasi BJLS 50 hingga BJLS 120 sesuai tabel standar SMACNA HVAC.",
            "Sambungan Flange TDF terintegrasi dengan sealing gasket dan klip corner berdaya cengkeram tinggi.",
            "Toleransi dimensi fabrikasi di bawah 0,5 mm dengan pemotongan CNC plasma otomatis.",
            "Laporan uji tekan resmi (pressure test report) disertakan untuk setiap fase instalasi gedung."
        ],
        "related": [1, 3, 5]
    },
    {
        "id": 3,
        "file": "blog-details-3.html",
        "title": "Perbandingan Material Saluran Udara: Keunggulan Ducting PU vs Ducting BJLS",
        "short_title": "Perbandingan PU vs BJLS",
        "badge": "Material & Fabrikasi",
        "date": "18 September 2026",
        "read_time": "6 mnt baca",
        "comments": "11 Komentar",
        "image": "assets/img/ducting/ducting-pu.jpg",
        "excerpt": "Panduan komprehensif membandingkan panel Polyurethane (PU) pre-insulated yang ringan dan bebas kondensasi dengan BJLS galvanis berkekuatan struktural tinggi untuk berbagai kebutuhan proyek.",
        "lead": "Menentukan material saluran udara adalah salah satu keputusan rekayasa paling menentukan dalam proyek HVAC. Memilih antara panel Polyurethane (PU) pre-insulated dan Baja Lapis Seng (BJLS) konvensional menuntut pemahaman mendalam atas karakteristik fisik, beban struktur, dan kondisi lingkungan.",
        "p1": "Panel Ducting PU memiliki keunggulan luar biasa dalam aspek bobot dan kemudahan instalasi. Dengan berat hanya sekitar 1,4 hingga 1,8 kg/m² (sekitar 70% lebih ringan daripada BJLS berinsulasi), ducting PU meminimalkan beban gantung pada dak beton dan struktur atap gedung, menjadikannya pilihan sempurna untuk gedung tua, ruang renovasi, maupun fasilitas cleanroom.",
        "h2_1": "Kinerja Termal & Kehigienisan Panel Polyurethane",
        "p2": "Busa kaku polyurethane berkepadatan 45-50 kg/m³ yang diapit lembaran aluminium foil timbul memiliki konduktivitas termal sangat rendah (λ = 0,022 W/m.K). Karena bersifat pre-insulated dan closed-cell, ducting PU tahan 100% terhadap kelembapan dan tidak melepaskan partikel serat (fiber-free), memenuhi syarat kebersihan ruang operasi rumah sakit dan industri farmasi.",
        "h2_2": "Keandalan Mekanis BJLS untuk Area Beban Berat",
        "p3": "Di sisi lain, BJLS tetap menjadi primadona tak tergantikan untuk area bertekanan statis tinggi di atas 2.000 Pa, cerobong pembuangan asap dapur komersial, instalasi shaft vertikal bertingkat banyak, serta ruang luar (outdoor) yang terpapar cuaca. BJLS menawarkan ketahanan mekanis terhadap benturan dan memenuhi regulasi proteksi kebakaran (fire-rated smoke spill).",
        "features": [
            "Ducting PU memangkas beban gantung dak hingga 70% dan mempercepat waktu instalasi 40%.",
            "Insulasi terintegrasi tanpa serat lepas, ideal untuk standar higienitas rumah sakit dan cleanroom.",
            "Ducting BJLS unggul dalam ketahanan mekanis, tekanan statis tinggi, dan tahan api pada zona darurat.",
            "Kombinasi kedua material sering diterapkan untuk efisiensi biaya dan fungsionalitas optimal gedung."
        ],
        "related": [1, 2, 4]
    },
    {
        "id": 4,
        "file": "blog-details-4.html",
        "title": "Sistem Exhaust Hood Dapur Komersial & Regulasi Keselamatan NFPA 96",
        "short_title": "Exhaust Hood Dapur NFPA 96",
        "badge": "Exhaust Hood & Keselamatan",
        "date": "10 September 2026",
        "read_time": "8 mnt baca",
        "comments": "23 Komentar",
        "image": "assets/img/ducting/ducting-exhaust.jpg",
        "excerpt": "Kupas tuntas desain cerobong hood dapur komersial, instalasi stainless grease baffle filter, drainase minyak terpadu, dan perhitungan CFM untuk menciptakan dapur aman dan bebas asap pekat.",
        "lead": "Dapur restoran komersial, katering industri, dan food court hotel beroperasi di bawah temperatur tinggi dengan produksi uap minyak (grease vapors) pekat. Kegagalan sistem ventilasi exhaust dapur bukan hanya merusak kenyamanan kerja koki, melainkan menjadi pemicu utama kebakaran fatal di gedung komersial.",
        "p1": "Regulasi internasional NFPA 96 (Standard for Ventilation Control and Fire Protection of Commercial Cooking Operations) mewajibkan saluran exhaust dapur dibangun menggunakan material tahan karat tebal dengan sambungan las kontinu kedap cairan (liquid-tight welded seams) guna mencegah minyak panas merembes ke plafon.",
        "h2_1": "Baffle Grease Filter & Talang Drainase Minyak",
        "p2": "Tudung hisap (exhaust hood) Ducting HVAC dilengkapi filter baffle baja tahan karat SUS 304 yang dirancang dengan sudut lekukan khusus. Gaya sentrifugal memisahkan partikel minyak dari udara panas dan mengalirkannya ke talang penampung grease cup yang mudah dilepas dan dibersihkan, mencegah penumpukan jelaga di dinding dalam cerobong.",
        "h2_2": "Kalkulasi CFM & Motor Blower High-Static",
        "p3": "Penentuan laju aliran udara (CFM) dihitung secara presisi berdasarkan panjang permukaan kompor, jenis peralatan memasak (heavy duty atau extra heavy duty), serta jarak tudung hisap. Motor blower sentrifugal backward-curved ditempatkan di ujung cerobong (rooftop) dengan motor di luar aliran udara panas untuk menjamin keandalan operasional jangka panjang.",
        "features": [
            "Konstruksi Stainless Steel SUS 304 food-grade atau BJLS tebal G120 dengan las kedap minyak.",
            "Baffle filter stainless steel mudah dicopot untuk sanitasi rutin tanpa menurunkan performa hisap.",
            "Pintu akses clean-out doors kedap minyak setiap 3 meter untuk inspeksi dan pembersihan berkala.",
            "Kompatibel dengan sistem pemadam api otomatis (kitchen fire suppression system) dan fusible link damper."
        ],
        "related": [1, 3, 5]
    },
    {
        "id": 5,
        "file": "blog-details-5.html",
        "title": "Peran Vital Sistem Fresh Air & Tekanan Positif di Rumah Sakit & Cleanroom",
        "short_title": "Fresh Air & Tekanan Positif",
        "badge": "Fresh Air & Ruang Steril",
        "date": "2 September 2026",
        "read_time": "6 mnt baca",
        "comments": "9 Komentar",
        "image": "assets/img/ducting/ducting-fresh-air.jpg",
        "excerpt": "Menjaga kualitas udara steril, regulasi pergantian udara (Air Changes per Hour / ACH), dan sistem tekanan positif guna mencegah kontaminasi silang pada ruang operasi dan fasilitas farmasi.",
        "lead": "Di lingkungan fasilitas kesehatan dan manufaktur obat, tata udara merupakan komponen keselamatan kritis. Sistem Fresh Air bertekanan positif bertindak sebagai benteng pertahanan yang melindungi pasien dan produk obat steril dari partikel kontaminan eksternal.",
        "p1": "Prinsip tekanan positif (positive room pressure) bekerja dengan menjaga tekanan udara di dalam ruang steril (seperti ruang operasi / OK) berada sekitar 15 hingga 25 Pascal lebih tinggi dibanding koridor sekitarnya. Ketika pintu terbuka, udara bersih di dalam ruangan akan terdorong keluar, secara efektif menghalau kuman dan debu koridor menerobos masuk.",
        "h2_1": "Filtrasi Bertingkat dengan HEPA H14",
        "p2": "Udara segar luar ruangan diproses melalui 3 jenjang filtrasi: Pre-filter G4 untuk menangkap debu kasar, Medium filter F8/F9 untuk serbuk sari dan partikel mikro, serta Terminal HEPA Filter H14 dengan efisiensi penyaringan 99,995% terhadap mikroba hingga ukuran 0,3 mikron. Distribusi udara disalurkan lewat laminar air flow ceiling tepat di atas meja bedah.",
        "h2_2": "Regulasi Pergantian Udara (ACH) & Stabilitas Kelembapan",
        "p3": "Sistem kami mengontrol pertukaran udara minimal 20 hingga 25 kali per jam (ACH) guna terus mendilusi udara kotor di dalam ruangan. Sistem pendingin dilengkapi kontrol kelembapan relatif (RH) otomatis pada kisaran 45% - 55% untuk mematikan perkembangbiakan spora jamur dan meminimalkan timbulnya listrik statis di ruang medis.",
        "features": [
            "Pengendalian diferensial tekanan presisi +15 Pa hingga +25 Pa dengan sensor monitor digital.",
            "Filtrasi tiga lapis berstandar rumah sakit hingga efisiensi HEPA H14 99,995%.",
            "Konstruksi saluran ducting antibakteri yang bebas serat dan mudah disterilisasi.",
            "Kepatuhan ketat terhadap standar internasional ISO 14644 Class 5 - 8 dan CPOB BPOM."
        ],
        "related": [1, 2, 6]
    },
    {
        "id": 6,
        "file": "blog-details-6.html",
        "title": "Panduan Pemeliharaan & Duct Cleaning Berkala untuk Kualitas Udara (IAQ)",
        "short_title": "Pemeliharaan & Duct Cleaning",
        "badge": "Maintenance & Air Quality",
        "date": "24 Agustus 2026",
        "read_time": "5 mnt baca",
        "comments": "16 Komentar",
        "image": "assets/img/ducting/ducting-ac-2.jpg",
        "excerpt": "Mengapa pembersihan saluran ducting secara terjadwal sangat penting untuk mencegah sick building syndrome, pertumbuhan jamur mikroba, serta menjaga efisiensi kinerja blower motor AHU.",
        "lead": "Saluran udara HVAC yang tersembunyi di balik plafon sering kali luput dari perhatian pengelola gedung. Padahal, seiring berjalannya waktu, saluran ducting yang tidak dirawat menjadi perangkap debu pekat, tungau, dan koloni jamur yang disemburkan kembali ke area kerja.",
        "p1": "Fenomena *Sick Building Syndrome* (SBS) — ditandai dengan keluhan alergi, sakit kepala, bersin-bersin, dan kelelahan kronis di antara penghuni gedung — sebagian besar dipicu oleh buruknya kualitas udara dalam ruangan (Indoor Air Quality / IAQ) akibat kontaminasi saluran ducting.",
        "h2_1": "Metodologi Pembersihan Berstandar NADCA",
        "p2": "Ducting HVAC menerapkan protokol pembersihan berstandar internasional NADCA (National Air Duct Cleaners Association). Proses dimulai dengan inspeksi kamera robot digital beresolusi tinggi, dilanjutkan penyikatan dinding ducting menggunakan rotary brush elektrik, dan penyedotan kotoran dengan mesin negative air vacuum berdaya hisap besar yang dilengkapi filter HEPA.",
        "h2_2": "Air Balancing & Pemulihan Efisiensi Energi",
        "p3": "Endapan debu tebal di dalam saluran menambah tahanan gesek (friction drag) hingga 20%, memaksa motor blower AHU mengonsumsi daya listrik lebih besar. Setelah proses pembersihan dan sterilisasi desinfektan food-grade, dilakukan pengujian Test Adjust Balance (TAB) menggunakan anemometer digital untuk memastikan aliran CFM terdistribusi merata di setiap ruangan.",
        "features": [
            "Inspeksi visual digital komprehensif dengan laporan foto Before & After terverifikasi.",
            "Penyikatan mekanis dan penyedotan vakum bertekanan negatif dengan filtrasi HEPA.",
            "Sterilisasi sanitasi menggunakan formula desinfektan ramah lingkungan bebas bau menyengat.",
            "Pengujian air balancing (TAB) guna mengoptimalkan distribusi hembusan udara di seluruh lantai."
        ],
        "related": [1, 4, 5]
    }
]

# Quick map by ID
article_by_id = {a["id"]: a for a in articles}

# Read standard footer from ducting-bjls.html
with open("ducting-bjls.html", "r", encoding="utf-8") as fp:
    bjls_content = fp.read()

m_footer = re.search(r'(<footer\s+id="footer"[^>]*>.*?</footer>)', bjls_content, re.DOTALL)
standard_footer = m_footer.group(1) if m_footer else ""

def generate_related_cards_html(rel_ids):
    cards_html = []
    for rid in rel_ids:
        ra = article_by_id[rid]
        c = f"""              <div class="related-card">
                <img src="{ra['image']}" alt="{ra['title']}">
                <div class="related-content">
                  <span class="related-category">{ra['badge']}</span>
                  <h5>
                    <a href="{ra['file']}">{ra['title']}</a>
                  </h5>
                  <p class="small text-muted mb-2">
                    {ra['excerpt']}
                  </p>
                  <a href="{ra['file']}" class="btn-view-related">
                    Baca Artikel <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
              </div>"""
        cards_html.append(c)
    return "\n\n".join(cards_html)

def generate_article_page(art):
    rel_html = generate_related_cards_html(art["related"])
    features_html = "\n".join([f"""                  <li>
                    <i class="bi bi-check-circle-fill"></i>
                    <div>
                      <strong>Fitur Unggulan:</strong>
                      <span>{feat}</span>
                    </div>
                  </li>""" for feat in art["features"]])
    
    html = f"""<!DOCTYPE html>
<html lang="id">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{art['title']} - Ducting HVAC</title>
  <meta name="description" content="{art['excerpt']}">
  <meta name="keywords" content="artikel ducting hvac, {art['short_title'].lower()}, ducting pu, ducting bjls, air balancing">

  <!-- Favicons -->
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800&family=Nunito:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Main CSS File -->
  <link href="assets/css/main.css" rel="stylesheet">
</head>

<body class="blog-details-page">

  <header id="header" class="header d-flex align-items-center sticky-top">
    <div class="container-fluid container-xxl position-relative d-flex align-items-center justify-content-between">

      <a href="index.html" class="logo d-flex align-items-center">
        <span class="logo-icon d-flex align-items-center justify-content-center"><i class="bi bi-fan"></i></span>
        <h1 class="sitename">Ducting HVAC</h1>
      </a>

      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="index.html">Beranda</a></li>
          <li><a href="about.html">Tentang Kami</a></li>
          <li><a href="services.html">Layanan</a></li>
          <li><a href="products.html">Produk</a></li>
          <li><a href="blog.html" class="active">Blog</a></li>
          <li class="dropdown"><a href="#"><span>Ducting</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="ducting-exhaust.html">Ducting Exhaust</a></li>
              <li><a href="ducting-fresh-air.html">Ducting Fresh Air</a></li>
              <li><a href="ducting-ac.html">Ducting AC</a></li>
              <li><a href="ducting-pu.html">Ducting PU</a></li>
              <li><a href="ducting-bjls.html">Ducting BJLS</a></li>
            </ul>
          </li>
          <li><a href="contact.html">Kontak</a></li>
        </ul>
      </nav>

      <div class="header-right d-flex align-items-center">
        <div class="header-actions d-none d-xl-flex align-items-center">
          <a class="action-link" href="tel:085210620252"><i class="bi bi-telephone"></i><span>0852-1062-0252</span></a>
        </div>
        <a class="btn-quote d-none d-sm-inline-flex" href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20estimasi%20biaya." target="_blank" rel="noopener noreferrer"><i class="bi bi-whatsapp me-2"></i>Minta Estimasi</a>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </div>

    </div>
  </header>

  <main class="main">

    <!-- Page Title -->
    <div class="page-title light-background">
      <div class="container d-lg-flex justify-content-between align-items-center">
        <h1 class="mb-2 mb-lg-0">Detail Artikel</h1>
        <nav class="breadcrumbs">
          <ol>
            <li><a href="index.html">Beranda</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li class="current">{art['short_title']}</li>
          </ol>
        </nav>
      </div>
    </div><!-- End Page Title -->

    <!-- Article Content Section -->
    <section class="section py-5">
      <div class="container" data-aos="fade-up">
        <div class="row gy-5">

          <!-- Main Article Column -->
          <div class="col-lg-8">

            <article class="article-container" data-aos="fade-up">

              <!-- Article Hero Image -->
              <div class="article-hero-image">
                <img src="{art['image']}" alt="{art['title']}" class="img-fluid rounded w-100" style="max-height: 440px; object-fit: cover;" loading="eager">
              </div>

              <!-- Article Header & Meta -->
              <div class="article-header">
                <span class="article-badge"><i class="bi bi-tag-fill me-1"></i> {art['badge']}</span>
                <h1>{art['title']}</h1>
                <div class="article-meta-bar">
                  <span class="d-inline-flex align-items-center">
                    <img src="assets/img/author/Mega Anggun.webp" alt="Mega Anggun" class="rounded-circle me-2" style="width: 26px; height: 26px; object-fit: cover;">
                    <strong>Mega Anggun</strong>
                  </span>
                  <span><i class="bi bi-calendar3"></i> {art['date']}</span>
                  <span><i class="bi bi-clock"></i> {art['read_time']}</span>
                  <span><i class="bi bi-chat-dots"></i> {art['comments']}</span>
                </div>
              </div>

              <!-- Article Body Content -->
              <div class="article-content">
                <p class="lead">
                  {art['lead']}
                </p>

                <p>
                  {art['p1']}
                </p>

                <h3>{art['h2_1']}</h3>
                <p>
                  {art['p2']}
                </p>

                <h3>{art['h2_2']}</h3>
                <p>
                  {art['p3']}
                </p>

                <h3>Keunggulan Rekayasa &amp; Nilai Tambah Utama:</h3>
                <ul class="article-feature-list">
{features_html}
                </ul>

                <!-- Quote Highlight Box -->
                <div class="article-quote-box">
                  <i class="bi bi-quote quote-icon"></i>
                  <blockquote>
                    "Sistem tata udara dan fabrikasi ducting HVAC yang presisi bukan sekadar menghadirkan kesejukan ruang, melainkan investasi strategis yang memangkas beban operasional gedung serta menjamin kesehatan sirkulasi udara jangka panjang."
                  </blockquote>
                  <cite>— Mega Anggun, Lead MEP Engineering Consultant Ducting HVAC</cite>
                </div>

                <!-- Consultation CTA Box -->
                <div class="article-cta-box">
                  <h4>Tertarik Mengoptimalkan Sistem Ducting HVAC Gedung Anda?</h4>
                  <p>
                    Dapatkan survei laju aliran udara (CFM), analisis kebutuhan kapasitas ducting, dan estimasi penawaran harga transparan dari para spesialis Ducting HVAC.
                  </p>
                  <div class="d-flex flex-wrap justify-content-center gap-3">
                    <a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20konsultasi%20artikel%20{art['short_title']}." target="_blank" rel="noopener noreferrer" class="btn btn-quote px-4 py-2"><i class="bi bi-whatsapp me-2"></i>Minta Estimasi WhatsApp</a>
                    <a href="tel:085210620252" class="btn btn-outline-light px-4 py-2"><i class="bi bi-telephone me-1"></i> 0852-1062-0252</a>
                  </div>
                </div>

                <!-- Author Profile Box -->
                <div class="author-box" data-aos="fade-up">
                  <div class="author-avatar">
                    <img src="assets/img/author/Mega Anggun.webp" alt="Mega Anggun">
                  </div>
                  <div class="author-info">
                    <span class="author-label">Penulis Artikel</span>
                    <h4 class="author-name">Mega Anggun</h4>
                    <p class="author-bio">
                      Spesialis rekayasa mekanikal tata udara (HVAC) dan jurnalis teknis di Ducting HVAC. Berpengalaman dalam komisioning sistem distribusi udara gedung komersial, audit efisiensi energi, serta kepatuhan standar internasional SMACNA dan NFPA 96.
                    </p>
                  </div>
                </div>

              </div>

            </article>

            <!-- Related Articles Section (Artikel Terkait Lainnya - EXACTLY 3 ARTICLES) -->
            <div class="related-posts-section" data-aos="fade-up" data-aos-delay="100">
              <h4 class="related-posts-title">
                <i class="bi bi-journal-text"></i> Artikel Terkait Lainnya
              </h4>

{rel_html}

            </div><!-- End Related Articles Section -->

          </div><!-- End Main Column -->

          <!-- Sidebar Column -->
          <div class="col-lg-4">
            <div class="sidebar-sticky">

              <!-- CTA Widget -->
              <div class="sidebar-widget sidebar-cta-widget" data-aos="fade-up" data-aos-delay="100">
                <i class="bi bi-fan main-icon"></i>
                <h4>Siap Memulai Proyek Anda?</h4>
                <p>
                  Diskusikan rencana instalasi ducting komersial atau industri Anda bersama konsultan teknik bersertifikasi kami.
                </p>
                <a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20estimasi%20biaya%20proyek." target="_blank" rel="noopener noreferrer" class="btn btn-quote w-100 mb-2"><i class="bi bi-whatsapp me-2"></i>Minta Estimasi WhatsApp</a>
                <a href="tel:085210620252" class="btn btn-outline-light w-100 text-white"><i class="bi bi-telephone me-1"></i> Hubungi Tenaga Ahli</a>
              </div>

              <!-- Advantages Widget -->
              <div class="sidebar-widget" data-aos="fade-up" data-aos-delay="200">
                <h4 class="widget-title">Mengapa Ducting HVAC</h4>
                <ul class="advantages-list">
                  <li>
                    <i class="bi bi-shield-check"></i>
                    <div>
                      <strong>Standar Mutu SMACNA</strong>
                      <span>Fabrikasi berstandar presisi dengan tingkat kebocoran udara minimal di bawah 1%.</span>
                    </div>
                  </li>
                  <li>
                    <i class="bi bi-clock-history"></i>
                    <div>
                      <strong>Tepat Waktu Sesuai Jadwal</strong>
                      <span>Didukung workshop mesin Auto Duct Line kapasitas ratusan meter per hari.</span>
                    </div>
                  </li>
                  <li>
                    <i class="bi bi-patch-check"></i>
                    <div>
                      <strong>Teknisi MEP Bersertifikat</strong>
                      <span>Tim insinyur berpengalaman dalam kalkulasi airflow CFM dan pressure test resmi.</span>
                    </div>
                  </li>
                  <li>
                    <i class="bi bi-trophy"></i>
                    <div>
                      <strong>Garansi Kebocoran &amp; Material</strong>
                      <span>Jaminan kepuasan hasil instalasi rapi, kedap udara, dan bebas kondensasi.</span>
                    </div>
                  </li>
                </ul>
              </div>

              <!-- Categories Widget -->
              <div class="sidebar-widget" data-aos="fade-up" data-aos-delay="300">
                <h4 class="widget-title">Kategori Artikel</h4>
                <ul class="categories-list">
                  <li>
                    <a href="blog-details-1.html">
                      <span><i class="bi bi-chevron-right me-1"></i> Ducting AC &amp; Efisiensi Energi</span>
                      <span class="badge bg-light text-dark">01</span>
                    </a>
                  </li>
                  <li>
                    <a href="blog-details-2.html">
                      <span><i class="bi bi-chevron-right me-1"></i> Ducting BJLS &amp; Standar Mutu</span>
                      <span class="badge bg-light text-dark">02</span>
                    </a>
                  </li>
                  <li>
                    <a href="blog-details-3.html">
                      <span><i class="bi bi-chevron-right me-1"></i> Material Panel Polyurethane</span>
                      <span class="badge bg-light text-dark">03</span>
                    </a>
                  </li>
                  <li>
                    <a href="blog-details-4.html">
                      <span><i class="bi bi-chevron-right me-1"></i> Exhaust Hood Dapur Komersial</span>
                      <span class="badge bg-light text-dark">04</span>
                    </a>
                  </li>
                  <li>
                    <a href="blog-details-5.html">
                      <span><i class="bi bi-chevron-right me-1"></i> Fresh Air &amp; Tekanan Positif RS</span>
                      <span class="badge bg-light text-dark">05</span>
                    </a>
                  </li>
                  <li>
                    <a href="blog-details-6.html">
                      <span><i class="bi bi-chevron-right me-1"></i> Pemeliharaan &amp; Duct Cleaning</span>
                      <span class="badge bg-light text-dark">06</span>
                    </a>
                  </li>
                </ul>
              </div>

            </div>
          </div><!-- End Sidebar Column -->

        </div>
      </div>
    </section>

  </main>

{standard_footer}

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Preloader -->
  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/vendor/imagesloaded/imagesloaded.pkgd.min.js"></script>
  <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>

  <!-- Main JS File -->
  <script src="assets/js/main.js"></script>

</body>

</html>
"""
    return html

# Write each article detail file
for art in articles:
    content = generate_article_page(art)
    with open(art["file"], "w", encoding="utf-8") as fp:
        fp.write(content)
    print(f"Written article: {art['file']}")

# Also update blog-details.html to mirror blog-details-1.html
with open("blog-details.html", "w", encoding="utf-8") as fp:
    fp.write(generate_article_page(articles[0]))
print("Written blog-details.html")

# Now update blog.html with 3-column layout (col-lg-4 col-md-6)
cards_grid = []
for i, art in enumerate(articles):
    delay = ((i % 3) + 1) * 100
    card_html = f"""          <!-- Article {art['id']} -->
          <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="{delay}">
            <div class="blog-card">
              <div class="blog-img-wrapper">
                <img src="{art['image']}" alt="{art['title']}" loading="lazy">
                <span class="blog-category-badge">{art['badge']}</span>
              </div>
              <div class="blog-body">
                <div class="blog-meta">
                  <span><i class="bi bi-calendar3"></i> {art['date']}</span>
                  <span><i class="bi bi-clock"></i> {art['read_time']}</span>
                </div>
                <h3 class="blog-title">
                  <a href="{art['file']}">{art['title']}</a>
                </h3>
                <p class="blog-excerpt">
                  {art['excerpt']}
                </p>
                <div class="blog-footer">
                  <div class="blog-author">
                    <img src="assets/img/author/Mega Anggun.webp" alt="Mega Anggun">
                    <span>Mega Anggun</span>
                  </div>
                  <a href="{art['file']}" class="read-more-btn">
                    Baca Artikel <i class="bi bi-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          </div><!-- End Article {art['id']} -->"""
    cards_grid.append(card_html)

grid_html = "\n\n".join(cards_grid)

# Read blog.html
with open("blog.html", "r", encoding="utf-8") as fp:
    blog_content = fp.read()

# Replace the row gy-4 content inside blog section
# Pattern: find <section id="blog" class="blog section"> ... <div class="row gy-4"> ... </div>
pattern_blog = re.compile(
    r'(<section id="blog" class="blog section">.*?<div class="row [^"]*">)(.*?)(</div>\s*</div>\s*</section>)',
    re.DOTALL
)

match_b = pattern_blog.search(blog_content)
if match_b:
    new_blog_content = '<section id="blog" class="blog section">\n\n      <!-- Section Title -->\n      <div class="container section-title" data-aos="fade-up">\n        <h2>Wawasan Sistem Tata Udara &amp; Ducting HVAC Terkini</h2>\n        <p>Analisis teknis, efisiensi sirkulasi udara, pemilihan material saluran ducting, dan standar SMACNA dari tim ahli Ducting HVAC</p>\n      </div><!-- End Section Title -->\n\n      <div class="container" data-aos="fade-up" data-aos-delay="100">\n\n        <div class="row g-4">\n\n' + grid_html + '\n\n        </div>\n      </div>\n    </section>'
    blog_content = blog_content[:match_b.start()] + new_blog_content + blog_content[match_b.end():]
    with open("blog.html", "w", encoding="utf-8") as fp:
        fp.write(blog_content)
    print("Updated blog.html with 6 articles in col-lg-4 (3 per row)!")
else:
    print("Could not find blog grid section in blog.html")

print("\nAll blog files successfully generated and updated!")
