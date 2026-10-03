import os
import re
import glob

# Data for 12 Products
products = [
    {
        "id": "produk-exhaust-hood",
        "file": "produk-exhaust-hood.html",
        "title": "Sistem Exhaust Hood Dapur Komersial",
        "category": "Exhaust & Fresh Air",
        "filter": "filter-exhaust",
        "tag": "Exhaust Dapur & Food Court",
        "summary": "Sistem tudung hisap (hood) dan cerobong exhaust dapur komersial bertekanan tinggi untuk restoran, hotel, katering, dan food court mall.",
        "p1": "Sistem Exhaust Hood Dapur Komersial kami dirancang khusus untuk menangkap dan menyedot uap panas, asap pekat, partikel minyak goreng (grease), dan aroma tajam yang dihasilkan oleh peralatan memasak komersial. Dibuat menggunakan material Stainless Steel SUS 304 food-grade atau BJLS tebal berkualitas tinggi dengan sambungan las kedap minyak guna mencegah risiko kebakaran sesuai regulasi NFPA 96.",
        "p2": "Dilengkapi dengan baffle grease filter baja anti-karat yang dapat dilepas untuk pencucian rutin, saluran drainase minyak terintegrasi, serta motor blower exhaust sentrifugal berkekuatan tinggi yang mampu mengatasi hambatan statis pada cerobong panjang vertikal. Menjadikan lingkungan kerja dapur tetap sejuk, higienis, dan nyaman bagi para koki.",
        "tab2_title": "Keunggulan Teknis & Keamanan Kebakaran",
        "tab2_text": "Sistem exhaust dapur kami mengadopsi standar SMACNA Kitchen Ventilation dan NFPA 96 Standard for Ventilation Control and Fire Protection of Commercial Cooking Operations. Memiliki sudut kemiringan talang minyak yang presisi agar minyak tidak menetes kembali ke atas wajan masakan, serta dilengkapi akses pintu pembersihan (clean-out access door) di setiap belokan saluran ducting.",
        "tab3_title": "Aplikasi & Rekomendasi Pemasangan",
        "tab3_text": "Sangat ideal untuk restoran cepat saji, dapur hotel berbintang, sentra kuliner mall/food court, pabrik pengolahan makanan beku, dan dapur katering berskala besar. Tim engineer kami menghitung kebutuhan laju aliran udara (CFM) secara presisi berdasarkan panjang kompor dan jenis masakan (light, medium, atau extra heavy duty).",
        "slider_imgs": ["assets/img/ducting/ducting-exhaust.jpg", "assets/img/ducting/ducting-exhaust-2.jpg", "assets/img/ducting/ducting-exhaust-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-exhaust.jpg",
            "assets/img/ducting/ducting-exhaust-2.jpg",
            "assets/img/ducting/ducting-exhaust-3.jpg",
            "assets/img/ducting/ducting-fresh-air.jpg",
            "assets/img/ducting/ducting-bjls.jpg",
            "assets/img/ducting/ducting-ac.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Hood & Ducting Exhaust Komersial"),
            ("Material Utama", "Stainless Steel 304 / BJLS G120"),
            ("Kapasitas Airflow", "2.500 – 25.000 CFM"),
            ("Tipe Filter", "Removable Stainless Steel Baffle Filter"),
            ("Standar Keselamatan", "NFPA 96 & SMACNA Kitchen Duct"),
            ("Tipe Blower", "Centrifugal High Static Backward Curved"),
            ("Garansi Resmi", "Garansi Kebocoran & Motor 1 Tahun")
        ]
    },
    {
        "id": "produk-ducting-ac-sentral",
        "file": "produk-ducting-ac-sentral.html",
        "title": "Ducting AC Sentral Gedung Perkantoran",
        "category": "Ducting AC & PU",
        "filter": "filter-ac",
        "tag": "Ducting AC Sentral AHU/VRV",
        "summary": "Saluran pipa dan cerobong distribusi udara pendingin merata dari unit AHU/FCU untuk menara perkantoran bertingkat.",
        "p1": "Ducting AC Sentral Gedung Perkantoran merupakan solusi utama dalam mendistribusikan udara dingin dari mesin pendingin sentral (Air Handling Unit / Fan Coil Unit) ke seluruh lantai dan ruangan kerja. Menggunakan lembaran baja lapis seng (BJLS) pilihan dengan sambungan Flange TDC/TDF bersealant anti-bocor, serta dilapisi insulasi Glasswool berdensitas tinggi berperekat aluminium foil tebal.",
        "p2": "Sistem ini menjamin efisiensi pendinginan maksimal dengan kehilangan temperatur dingin kurang dari 1°C di sepanjang jalur saluran. Aliran udara dirancang aerodinamis untuk mencegah desis bising pada diffuser (Noise Criteria di bawah NC-30) sehingga menciptakan suasana ruang kantor yang sejuk, hening, dan produktif bagi seluruh karyawan.",
        "tab2_title": "Insulasi Termal & Efisiensi Energi",
        "tab2_text": "Insulasi Glasswool 24-32 kg/m³ atau busa sel tertutup (closed-cell nitrile rubber) dipasang dengan lem khusus bebas bau untuk mencegah terjadinya titik embun kondensasi (sweating) yang dapat merusak plafon gypsum. Sambungan antar segmen diperkuat dengan corner lock dan klem g-clamp untuk meminimalkan tingkat kebocoran udara hingga di bawah 1%.",
        "tab3_title": "Aplikasi Gedung & Komisioning TAB",
        "tab3_text": "Dirancang khusus untuk menara perkantoran, gedung perbankan, instansi pemerintah, dan coworking space modern. Setiap instalasi disertai penyetelan volume control damper (VCD) dan pengetesan Test Adjust Balance (TAB) menggunakan anemometer digital agar setiap kubikel ruangan memperoleh hembusan udara yang proporsional.",
        "slider_imgs": ["assets/img/ducting/ducting-ac.jpg", "assets/img/ducting/ducting-ac-2.jpg", "assets/img/ducting/ducting-ac-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-ac.jpg",
            "assets/img/ducting/ducting-ac-2.jpg",
            "assets/img/ducting/ducting-ac-3.jpg",
            "assets/img/ducting/ducting-pu.jpg",
            "assets/img/ducting/ducting-bjls-2.jpg",
            "assets/img/ducting/ducting-fresh-air-2.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Saluran Distribusi AC Sentral"),
            ("Material Utama", "BJLS Galvalum G80 – G100"),
            ("Insulasi Termal", "Glasswool 24-32 kg/m³ + Foil / NBR"),
            ("Kapasitas Airflow", "5.000 – 60.000 CFM"),
            ("Tingkat Kebocoran", "Leakage Class 3 SMACNA"),
            ("Kriteria Bising", "NC-25 hingga NC-30 (Senyap)"),
            ("Garansi Resmi", "Garansi Termal & Kebocoran 2 Tahun")
        ]
    },
    {
        "id": "produk-ducting-bjls-smoke-spill",
        "file": "produk-ducting-bjls-smoke-spill.html",
        "title": "Ducting BJLS Smoke Spill Basement",
        "category": "Ducting BJLS & Industri",
        "filter": "filter-bjls",
        "tag": "Smoke Spill & Evakuasi Asap",
        "summary": "Saluran baja galvanis berkekuatan mekanis tinggi tahan panas untuk evakuasi asap darurat kebakaran di basement.",
        "p1": "Ducting BJLS Smoke Spill Basement adalah sistem saluran evakuasi darurat yang wajib dimiliki oleh gedung bertingkat untuk menyedot asap tebal bersuhu tinggi dan gas beracun (CO) saat terjadi kebakaran di area bawah tanah (basement) maupun lorong evakuasi. Dibuat dari plat BJLS tebal (gauge 18 - 20) dengan tulangan pengaku siku besi berstandar SMACNA High Pressure.",
        "p2": "Konstruksi cerobong ini mampu menahan temperatur udara hingga 250°C - 300°C selama minimal 2 jam operasi terus menerus tanpa mengalami deformasi atau keruntuhan struktur saluran. Sistem ini terintegrasi dengan Fire Damper bersertifikat UL dan motor blower exhaust berdaya dorong statis masif.",
        "tab2_title": "Daya Tahan Tekanan Vakum & Ketahanan Api",
        "tab2_text": "Karena motor smoke spill bekerja pada tekanan hisap negatif yang sangat tinggi, saluran ducting diperkuat dengan tie rod internal dan profil pengaku flange besi siku (angle iron). Seluruh sambungan menggunakan sealant tahan panas tinggi (fire-rated silicone sealant) yang lolos sertifikasi ketahanan api dinas pemadam kebakaran.",
        "tab3_title": "Aplikasi Basement & Terowongan Bawah Tanah",
        "tab3_text": "Digunakan pada basement mall, area parkir gedung apartemen, terowongan kereta bawah tanah, ruang genset, dan fasilitas utilitas vital. Dalam kondisi normal, saluran ini juga berfungsi sebagai ventilasi pembuangan gas buang emisi kendaraan bermotor.",
        "slider_imgs": ["assets/img/ducting/ducting-bjls.jpg", "assets/img/ducting/ducting-bjls-2.jpg", "assets/img/ducting/ducting-bjls-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-bjls.jpg",
            "assets/img/ducting/ducting-bjls-2.jpg",
            "assets/img/ducting/ducting-bjls-3.jpg",
            "assets/img/ducting/ducting-ac-3.jpg",
            "assets/img/ducting/ducting-exhaust-2.jpg",
            "assets/img/ducting/ducting-fresh-air.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Smoke Spill & Toxic Gas Extraction"),
            ("Material Utama", "BJLS Heavy Gauge (0.8mm – 1.2mm)"),
            ("Ketahanan Suhu", "250°C - 300°C (Selama 2 Jam)"),
            ("Kelas Tekanan", "High Pressure Class (hingga 2000 Pa)"),
            ("Standar Fabrikasi", "SMACNA High Pressure / NFPA 92"),
            ("Tipe Flange", "Angle Iron Flange / TDC 35"),
            ("Garansi Resmi", "Garansi Integritas Struktural 2 Tahun")
        ]
    },
    {
        "id": "produk-cleanroom-ducting-pu",
        "file": "produk-cleanroom-ducting-pu.html",
        "title": "Cleanroom Ducting PU Farmasi & RS",
        "category": "Ducting AC & PU",
        "filter": "filter-ac",
        "tag": "Ducting PU Pre-Insulated",
        "summary": "Panel busa Polyurethane higienis bebas serat partikel, anti-jamur, ideal untuk ruang operasi RS dan industri obat cGMP.",
        "p1": "Cleanroom Ducting PU (Polyurethane) adalah inovasi saluran udara modern berbahan panel sandwich pre-insulated dengan inti busa kaku Polyurethane (PIR/PUR) berdensitas tinggi 48-52 kg/m³, yang dilapisi aluminium foil timbul (embossed) di kedua sisinya. Sangat direkomendasikan untuk area dengan persyaratan higienitas tertinggi seperti ruang steril dan laboratorium.",
        "p2": "Keunggulan mutlak Ducting PU adalah permukaannya yang 100% bebas serat partikel (fiber-free) sehingga tidak melepaskan debu wol ke udara steril ruang operasi. Busa sel tertutupnya memiliki konduktivitas termal sangat rendah (0.020 W/m.K), mencegah kondensasi air embun, serta bersifat anti-jamur dan anti-bakteri.",
        "tab2_title": "Bobot Ringan & Kedap Udara Superior",
        "tab2_text": "Bobot panel PU mencapai 85% lebih ringan dibandingkan ducting seng konvensional yang diisolasi terpisah, sehingga sangat aman bagi struktur beban atap dan mempercepat pemasangan hingga 3x lipat. Sambungan sistem profil bayonet polimer dengan lem kedap udara menghasilkan tingkat kebocoran sangat rendah (Class C Standar Eropa).",
        "tab3_title": "Standar Medis & Regulasi Farmasi",
        "tab3_text": "Memenuhi standar ISO 14644 untuk Cleanroom Kelas 100 sampai Kelas 10.000, ruang operasi (OK) rumah sakit tipe A dan B, ruang ICU, laboratorium biosafety level (BSL), fasilitas formulasi farmasi BPOM/cGMP, dan perakitan mikroelektronika presisi.",
        "slider_imgs": ["assets/img/ducting/ducting-pu.jpg", "assets/img/ducting/ducting-pu-2.jpg", "assets/img/ducting/ducting-pu-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-pu.jpg",
            "assets/img/ducting/ducting-pu-2.jpg",
            "assets/img/ducting/ducting-pu-3.jpg",
            "assets/img/ducting/ducting-ac.jpg",
            "assets/img/ducting/ducting-fresh-air.jpg",
            "assets/img/ducting/ducting-fresh-air-2.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Cleanroom Pre-Insulated PU Duct"),
            ("Material Inti", "Rigid Polyurethane Foam (Densitas 50 kg/m³)"),
            ("Pelapis Permukaan", "Double Embossed Aluminium Foil 80 mikron"),
            ("Konduktivitas Termal", "0.020 W/m.K (Isolasi Prima)"),
            ("Sertifikasi Kebersihan", "ISO 14644 Cleanroom Class 100-10.000"),
            ("Ketahanan Api", "Class 0 / Class 1 Fire Retardant"),
            ("Garansi Resmi", "Garansi Anti-Kondensasi 3 Tahun")
        ]
    },
    {
        "id": "produk-fresh-air-tekanan-positif",
        "file": "produk-fresh-air-tekanan-positif.html",
        "title": "Sistem Fresh Air & Tekanan Positif RS",
        "category": "Exhaust & Fresh Air",
        "filter": "filter-exhaust",
        "tag": "Fresh Air & Filtrasi HEPA",
        "summary": "Saluran suplai udara segar luar berfiltrasi bertingkat untuk menjaga sirkulasi oksigen dan tekanan positif steril.",
        "p1": "Sistem Fresh Air & Tekanan Positif Rumah Sakit adalah infrastruktur vital yang menyuplai udara luar segar beroksigen tinggi setelah melalui tiga tahap filtrasi ketat (Pre-Filter G4, Medium Filter F8, dan HEPA Filter H14). Sistem ini secara aktif menciptakan tekanan udara positif di dalam ruangan steril.",
        "p2": "Dengan tekanan positif, saat pintu ruangan dibuka, udara di dalam akan berhembus keluar dan mencegah masuknya mikroorganisme, debu, atau virus dari koridor umum ke dalam ruangan sensitif. Dilengkapi dengan pengatur kecepatan motor VAV (Variable Air Volume) dan sensor perbedaan tekanan digital.",
        "tab2_title": "Efisiensi Filtrasi Partikel 99.97%",
        "tab2_text": "Kotak filter (filter housing) dibuat dari stainless steel kedap udara dengan mekanisme clamping seal anti-bypass. Menjamin seluruh udara yang ditiupkan ke dalam ruangan telah tersaring dari bakteri, droplet aerosol, spora jamur, dan partikel debu mikro hingga ukuran 0.3 mikron.",
        "tab3_title": "Aplikasi Rumah Sakit & Fasilitas Medis",
        "tab3_text": "Diaplikasikan pada Ruang Bedah Sentral (OK), Ruang Bayi Tabung / NICU, Ruang Rawat Pasien Luka Bakar, Ruang Kemoterapi, serta ruang pemulihan pasca operasi. Memenuhi petunjuk teknis sarana tata udara rumah sakit Kementerian Kesehatan RI.",
        "slider_imgs": ["assets/img/ducting/ducting-fresh-air.jpg", "assets/img/ducting/ducting-fresh-air-2.jpg", "assets/img/ducting/ducting-fresh-air-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-fresh-air.jpg",
            "assets/img/ducting/ducting-fresh-air-2.jpg",
            "assets/img/ducting/ducting-fresh-air-3.jpg",
            "assets/img/ducting/ducting-pu.jpg",
            "assets/img/ducting/ducting-ac-2.jpg",
            "assets/img/ducting/ducting-exhaust.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Fresh Air Supply & Positive Pressure"),
            ("Tahap Filtrasi", "Pre-Filter G4 + Medium F8 + HEPA H14"),
            ("Efisiensi Penyaringan", "99.97% pada partikel 0.3 mikron"),
            ("Diferensial Tekanan", "+15 Pa hingga +25 Pa (Positif)"),
            ("Material Saluran", "BJLS Food-Grade / PU Cleanroom"),
            ("Standar Regulasi", "Permenkes RI & ASHRAE 170"),
            ("Garansi Resmi", "Garansi Integritas Tekanan 2 Tahun")
        ]
    },
    {
        "id": "produk-ventilasi-pabrik",
        "file": "produk-ventilasi-pabrik.html",
        "title": "Ventilasi Pabrik Manufaktur Otomotif",
        "category": "Ducting BJLS & Industri",
        "filter": "filter-bjls",
        "tag": "Ventilasi Industri Masif",
        "summary": "Saluran udara volume masif bertekanan tinggi untuk pembuangan polutan panas dan pendinginan lini produksi pabrik.",
        "p1": "Ventilasi Pabrik Manufaktur Otomotif dirancang untuk mengatasi beban kalor mesin yang luar biasa tinggi pada lini perakitan, area stamping, welding, dan oven pengecatan bodi kendaraan. Menghadirkan sirkulasi udara berkecepatan tinggi dengan saluran ducting baja galvanis berpenampang besar.",
        "p2": "Menggunakan diffuser jet nozzle berjangkauan tembak panjang yang dapat diarahkan langsung ke zona kerja operator, saluran ini mampu menurunkan temperatur operasional lingkungan kerja pabrik hingga 5°C-8°C. Konstruksi ducting dirancang sangat kokoh dengan pengaku rusuk silang (cross-broken) agar tahan terhadap getaran mesin manufaktur.",
        "tab2_title": "Kekuatan Mekanis & Daya Tahan Getaran",
        "tab2_text": "Dilengkapi dengan konektor fleksibel berbahan kanvas silikon anti-robek dan gantungan peredam getaran (vibration isolator hanger) yang memisahkan getaran motor blower sentrifugal dari rangka atap pabrik. Seluruh sambungan flange diperkuat baut baja tahan karat grade tinggi.",
        "tab3_title": "Aplikasi Kawasan Industri",
        "tab3_text": "Telah diimplementasikan pada kawasan industri otomotif, pabrik komponen logam, pabrik manufaktur plastik injeksi, dan fasilitas peleburan aluminium di Cikarang, Karawang, dan Surabaya.",
        "slider_imgs": ["assets/img/ducting/ducting-bjls-2.jpg", "assets/img/ducting/ducting-bjls-3.jpg", "assets/img/ducting/ducting-bjls.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-bjls-2.jpg",
            "assets/img/ducting/ducting-bjls-3.jpg",
            "assets/img/ducting/ducting-bjls.jpg",
            "assets/img/ducting/ducting-exhaust.jpg",
            "assets/img/ducting/ducting-ac-3.jpg",
            "assets/img/ducting/ducting-fresh-air.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Sistem Sirkulasi & Ventilasi Pabrik"),
            ("Material Utama", "Galvalum / BJLS Tebal G120"),
            ("Kapasitas Airflow", "15.000 – 120.000 CFM"),
            ("Tipe Diffuser", "Jet Nozzle Adjustable Long-Throw"),
            ("Fitur Khusus", "Heavy-Duty Anti-Vibration Connector"),
            ("Standar Industri", "SMACNA Industrial Duct Construction"),
            ("Garansi Resmi", "Garansi Konstruksi Pabrik 2 Tahun")
        ]
    },
    {
        "id": "produk-exhaust-shaft-restoran",
        "file": "produk-exhaust-shaft-restoran.html",
        "title": "Exhaust Shaft Restoran Hotel Bintang 5",
        "category": "Exhaust & Fresh Air",
        "filter": "filter-exhaust",
        "tag": "Riser Shaft Gedung Bertingkat",
        "summary": "Sistem cerobong pembuangan minyak dan asap vertikal menjulang puluhan lantai bebas kebocoran aroma ke kamar tamu.",
        "p1": "Exhaust Shaft Restoran Hotel Bintang 5 adalah saluran pembuangan asap dan minyak vertikal yang membentang dari dapur lantai podium melintasi puluhan lantai gedung hingga cerobong rooftop hotel. Dibangun dengan standar kekedapan absolut untuk menjamin tidak ada kebocoran bau masakan ke koridor atau kamar tamu hotel.",
        "p2": "Menggunakan plat baja lapis seng tebal atau baja hitam (black steel) yang dilapisi selimut pelindung api (firewrap blanket), saluran ini tahan terhadap nyala api langsung saat terjadi kebakaran minyak dapur. Di setiap lantai dilengkapi pintu inspeksi pembersih minyak (grease cleanout door).",
        "tab2_title": "Insulasi Fire-Rated & Proteksi Bau",
        "tab2_text": "Insulasi thermal ceramic blanket fire-rated 2 jam menjaga suhu eksterior shaft tetap aman dan tidak meradiasikan panas ke dinding shaft shaft utilitas. Dilengkapi dengan electrostatic precipitator (ESP) pada rooftop untuk menyaring asap dan partikel minyak sebelum dilepaskan ke udara bebas.",
        "tab3_title": "Aplikasi Perhotelan & Gedung Mixed-Use",
        "tab3_text": "Solusi wajib bagi hotel bintang 5, restoran fine dining di gedung pencakar langit, apartemen terpadu mall, dan fasilitas klub eksklusif yang memprioritaskan standar kenyamanan tamu bebas gangguan bau.",
        "slider_imgs": ["assets/img/ducting/ducting-exhaust-2.jpg", "assets/img/ducting/ducting-exhaust.jpg", "assets/img/ducting/ducting-exhaust-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-exhaust-2.jpg",
            "assets/img/ducting/ducting-exhaust.jpg",
            "assets/img/ducting/ducting-exhaust-3.jpg",
            "assets/img/ducting/ducting-fresh-air-2.jpg",
            "assets/img/ducting/ducting-bjls.jpg",
            "assets/img/ducting/ducting-ac-2.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Vertical Kitchen Exhaust Shaft"),
            ("Material Utama", "BJLS G120 / Carbon Steel Welded"),
            ("Fire Protection", "Firewrap Ceramic Blanket 2-Hour Rated"),
            ("Kapasitas Airflow", "4.000 – 35.000 CFM"),
            ("Tipe Sambungan", "Fully Sealed Grease-Tight Connection"),
            ("Aksesoris", "Integrated Cleanout Access Doors"),
            ("Garansi Resmi", "Garansi Bebas Bocor & Bau 2 Tahun")
        ]
    },
    {
        "id": "produk-ducting-vrv",
        "file": "produk-ducting-vrv.html",
        "title": "Instalasi Ducting VRV Hunian Mewah",
        "category": "Ducting AC & PU",
        "filter": "filter-ac",
        "tag": "Ducting AC Residensial Mewah",
        "summary": "Sistem saluran pendingin tersembunyi ceiling konsil dengan difuser linier minimalis dan operasional super senyap.",
        "p1": "Instalasi Ducting VRV Hunian Mewah dirancang bagi pemilik rumah mewah, penthouse, dan villa eksklusif yang menginginkan estetika interior bersih tanpa unit AC indoor yang tampak mengganggu dinding. Saluran udara tersembunyi rapi di balik celah drop ceiling dengan hembusan difuser linier tipis yang elegan.",
        "p2": "Menggunakan panel ducting berprofil slim dengan peredam akustik acoustic liner internal berstandar studio, menghasilkan suara hembusan udara yang nyaris tanpa suara (Noise Criteria di bawah NC-25). Sirkulasi pendinginan menyebar halus merata tanpa hembusan angin keras yang menusuk tubuh.",
        "tab2_title": "Estetika Arsitektural & Difuser Linier",
        "tab2_text": "Difuser linier slot aluminium dapat di-powder coating warna kustom (putih doff, hitam matte, atau warna kayu) sesuai konsep desainer interior. Jalur ducting dirancang fleksibel menyesuaikan ketinggian plafon ruang tamu, kamar tidur utama, dan ruang keluarga.",
        "tab3_title": "Aplikasi Hunian Eksklusif & Villa",
        "tab3_text": "Sangat cocok untuk hunian mewah di kawasan Menteng, Kebayoran Baru, Bukit Darmo Surabaya, dan villa resort di Bali yang mengutamakan privasi, kenyamanan suhu presisi, dan kemewahan visual tak tertandingi.",
        "slider_imgs": ["assets/img/ducting/ducting-ac-2.jpg", "assets/img/ducting/ducting-ac.jpg", "assets/img/ducting/ducting-ac-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-ac-2.jpg",
            "assets/img/ducting/ducting-ac.jpg",
            "assets/img/ducting/ducting-ac-3.jpg",
            "assets/img/ducting/ducting-pu-2.jpg",
            "assets/img/ducting/ducting-fresh-air-3.jpg",
            "assets/img/ducting/ducting-exhaust.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Residential Concealed VRV/VRF Duct"),
            ("Material Utama", "Slim Profile PU Panel / BJLS Acoustic"),
            ("Level Kebisingan", "NC-20 hingga NC-25 (Super Quiet)"),
            ("Tipe Diffuser", "Architectural Linear Slot Diffuser"),
            ("Kapasitas Airflow", "800 – 8.000 CFM"),
            ("Insulasi Termal", "Non-Allergenic Foam Anti-Condensation"),
            ("Garansi Resmi", "Garansi Kenyamanan Akustik 2 Tahun")
        ]
    },
    {
        "id": "produk-ducting-galvanis-gudang",
        "file": "produk-ducting-galvanis-gudang.html",
        "title": "Ducting Galvanis Gudang Logistik",
        "category": "Ducting BJLS & Industri",
        "filter": "filter-bjls",
        "tag": "Spiral Ducting Pergudangan",
        "summary": "Jaringan saluran udara bentang panjang tahan korosi untuk menjaga kestabilan temperatur dan kelembapan ruang kargo.",
        "p1": "Ducting Galvanis Gudang Logistik menggunakan saluran berbentuk spiral bulat (spiral round duct) atau persegi berbentang panjang yang dirancang melintasi lorong-lorong rak penyimpanan logistik modern. Saluran bulat spiral memiliki kekakuan struktural tinggi dan hambatan gesek udara yang sangat rendah.",
        "p2": "Berfungsi menjaga sirkulasi udara konstan guna mencegah penumpukan kelembapan tinggi yang dapat merusak barang kargo, kemasan karton, dan produk farmasi/elektronik di dalam gudang. Digantung dengan sistem wire rope sling modern yang kokoh, rapi, dan cepat dipasang.",
        "tab2_title": "Keunggulan Bentuk Spiral Bulat",
        "tab2_text": "Saluran spiral memiliki kekuatan tekan mekanis 4x lebih kuat dibanding ducting persegi biasa, sehingga menghemat jumlah gantungan atap. Penampang aerodinamis bulat meminimalkan penurunan tekanan (pressure drop), menghemat konsumsi listrik fan blower hingga 15%.",
        "tab3_title": "Aplikasi Pergudangan & Pusat Distribusi",
        "tab3_text": "Diterapkan pada distribution center e-commerce skala besar, gudang logistik berpendingin (cold chain storage), gudang farmasi berstandar CDOB, dan hanggar kargo bandara.",
        "slider_imgs": ["assets/img/ducting/ducting-bjls-3.jpg", "assets/img/ducting/ducting-bjls.jpg", "assets/img/ducting/ducting-bjls-2.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-bjls-3.jpg",
            "assets/img/ducting/ducting-bjls.jpg",
            "assets/img/ducting/ducting-bjls-2.jpg",
            "assets/img/ducting/ducting-ac-3.jpg",
            "assets/img/ducting/ducting-fresh-air.jpg",
            "assets/img/ducting/ducting-exhaust-2.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Spiral Galvanized Logistics Duct"),
            ("Material Utama", "Baja Lapis Seng Galvanis Lock Seam"),
            ("Bentuk Saluran", "Spiral Round / High Aspect Ratio Rectangular"),
            ("Kapasitas Airflow", "12.000 – 75.000 CFM"),
            ("Sistem Gantungan", "High-Tensile Wire Rope Suspension"),
            ("Ketahanan Korosi", "Lapisan Seng Z275 (Tahan Karat Tinggi)"),
            ("Garansi Resmi", "Garansi Struktural & Korosi 3 Tahun")
        ]
    },
    {
        "id": "produk-ducting-pu-bank",
        "file": "produk-ducting-pu-bank.html",
        "title": "Ducting PU Pre-Insulated Gedung Bank",
        "category": "Ducting AC & PU",
        "filter": "filter-ac",
        "tag": "Pre-Insulated PU Korporat",
        "summary": "Instalasi saluran pendingin berbobot ringan, hemat daya operasional chiller, dan bebas risiko kebocoran tetesan air plafon.",
        "p1": "Ducting PU Pre-Insulated Gedung Bank mengutamakan efisiensi operasional dan keamanan aset perkantoran perbankan. Dalam gedung perbankan, kebocoran tetesan air kondensasi AC dapat berakibat fatal merusak server IT, dokumen arsip finansial, dan perangkat elektronik penting.",
        "p2": "Dengan teknologi Polyurethane PIR Pre-Insulated, insulasi termal menyatu secara molekuler dengan lapisan aluminium pelindung, menjamin tidak akan ada titik embun (sweating) sepanjang umur gedung. Pemasangannya yang bebas debu dan sangat cepat sangat menguntungkan untuk proyek renovasi cabang bank tanpa mengganggu jam kerja.",
        "tab2_title": "Efisiensi Energi Chiller & Ringan Beban",
        "tab2_text": "Koefisien hambatan panas (R-value) yang unggul membuat suhu udara AC tetap terjaga dingin dari chiller room hingga ujung diffuser lantai eksekutif. Mengurangi beban kompresor AC dan memangkas tagihan listrik gedung hingga 20%.",
        "tab3_title": "Aplikasi Sektor Perbankan & Korporat",
        "tab3_text": "Dipilih oleh gedung kantor pusat perbankan BUMN dan swasta, lantai dealing room trading, pusat data server finansial, dan kantor asuransi di kawasan finansial Sudirman dan Thamrin.",
        "slider_imgs": ["assets/img/ducting/ducting-pu-2.jpg", "assets/img/ducting/ducting-pu.jpg", "assets/img/ducting/ducting-pu-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-pu-2.jpg",
            "assets/img/ducting/ducting-pu.jpg",
            "assets/img/ducting/ducting-pu-3.jpg",
            "assets/img/ducting/ducting-ac.jpg",
            "assets/img/ducting/ducting-fresh-air-2.jpg",
            "assets/img/ducting/ducting-bjls-2.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Corporate Pre-Insulated PU Duct"),
            ("Material Utama", "PIR Polyisocyanurate Rigid Foam 20mm"),
            ("Efisiensi Energi", "Hemat Daya Termal hingga 20%"),
            ("Kapasitas Airflow", "3.000 – 40.000 CFM"),
            ("Berat Saluran", "1.4 kg/m² (Sangat Ringan)"),
            ("Tingkat Kedap", "Class C Standard (Zero Air Leakage)"),
            ("Garansi Resmi", "Garansi Anti-Kondensasi 3 Tahun")
        ]
    },
    {
        "id": "produk-fresh-air-bioskop",
        "file": "produk-fresh-air-bioskop.html",
        "title": "Sirkulasi Fresh Air Gedung Bioskop",
        "category": "Exhaust & Fresh Air",
        "filter": "filter-exhaust",
        "tag": "Ventilasi Teater & Akustik",
        "summary": "Pengaturan suplai oksigen konstan di ruang auditorium teater kedap suara tanpa menimbulkan desis kebisingan.",
        "p1": "Sirkulasi Fresh Air Gedung Bioskop memecahkan tantangan besar dalam tata udara bioskop: memasok oksigen segar bagi ratusan penonton di dalam ruangan tertutup kedap suara tanpa menimbulkan desis atau getaran suara yang mengganggu audio film.",
        "p2": "Sistem ini menggunakan cerobong udara berkecepatan rendah (low-velocity ductwork) yang dilengkapi dengan sound attenuator (silencer duct) bertingkat. Sirkulasi oksigen dijaga konstan sehingga penonton merasa segar, nyaman, dan tidak mengantuk meski berada di dalam studio bioskop selama berjam-jam.",
        "tab2_title": "Peredam Akustik Khusus & Sensor CO2",
        "tab2_text": "Saluran udara dilengkapi silencer baffle berbahan glass fabric khusus yang menyerap gelombang suara frekuensi rendah dan menengah dari mesin blower. Terintegrasi dengan sensor CO2 otomatis yang menambah debit udara segar secara otomatis ketika auditorium bioskop penuh terisi penonton.",
        "tab3_title": "Aplikasi Teater, Bioskop & Auditorium",
        "tab3_text": "Telah diaplikasikan pada jaringan bioskop XXI, CGV, Cinepolis, gedung pertunjukan konser musik, auditorium universitas, dan studio rekaman broadcast berstandar Dolby Atmos.",
        "slider_imgs": ["assets/img/ducting/ducting-fresh-air-2.jpg", "assets/img/ducting/ducting-fresh-air.jpg", "assets/img/ducting/ducting-fresh-air-3.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-fresh-air-2.jpg",
            "assets/img/ducting/ducting-fresh-air.jpg",
            "assets/img/ducting/ducting-fresh-air-3.jpg",
            "assets/img/ducting/ducting-ac-2.jpg",
            "assets/img/ducting/ducting-pu-2.jpg",
            "assets/img/ducting/ducting-exhaust.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Acoustic Cinema Fresh Air Ventilation"),
            ("Level Kebisingan", "NC-20 / NR-20 (Dolby Atmos Certified)"),
            ("Fitur Akustik", "Multi-Stage Duct Silencer / Sound Attenuator"),
            ("Kapasitas Airflow", "3.000 – 25.000 CFM"),
            ("Kontrol Otomatis", "CO2 Demand Controlled Ventilation (DCV)"),
            ("Material Saluran", "BJLS G100 dengan Acoustic Internal Lining"),
            ("Garansi Resmi", "Garansi Akustik & Aliran Udara 2 Tahun")
        ]
    },
    {
        "id": "produk-ducting-ahu-bandara",
        "file": "produk-ducting-ahu-bandara.html",
        "title": "Ducting AHU Utama Concourse Bandara",
        "category": "Ducting BJLS & Industri",
        "filter": "filter-bjls",
        "tag": "Ducting Concourse Skala Masif",
        "summary": "Sistem distribusi saluran udara masif di area concourse terminal bandara dengan jangkauan hembusan jarak jauh.",
        "p1": "Ducting AHU Utama Concourse Bandara menangani volume sirkulasi udara luar biasa besar di ruang tunggu bandara yang memiliki plafon tinggi (high ceiling) dan fasad kaca luas dengan beban radiasi matahari tinggi. Dibuat dengan penampang ducting raksasa hingga ukuran 3.000 mm x 1.500 mm menggunakan mesin otomatis CNC.",
        "p2": "Mendistribusikan ratusan ribu CFM udara pendingin menggunakan kombinasi drum louver dan jet diffuser bertekanan tinggi yang mampu melemparkan udara dingin sejauh 30 meter secara merata. Saluran diperkuat dengan sistem sambungan flange TDC heavy-duty dan pengaku internal berbahan baja galvanis tebal.",
        "tab2_title": "Kapasitas Raksasa & Pengendalian VAV Cerdas",
        "tab2_text": "Terhubung dengan sistem Building Automation System (BAS) cerdas yang mengatur bukaan damper VAV sesuai kepadatan penumpang di masing-masing boarding gate, memastikan efisiensi daya pendingin tetap maksimal tanpa pemborosan energi saat gate sedang sepi penerbangan.",
        "tab3_title": "Aplikasi Bandara & Terminal Transit Masif",
        "tab3_text": "Diaplikasikan pada terminal bandara internasional, stasiun transit kereta cepat LRT/MRT/KRL, gedung pameran konvensi (ICE/JCC), dan atrium pusat perbelanjaan bertingkat tinggi.",
        "slider_imgs": ["assets/img/ducting/ducting-ac-3.jpg", "assets/img/ducting/ducting-bjls-3.jpg", "assets/img/ducting/ducting-bjls-2.jpg"],
        "gallery_imgs": [
            "assets/img/ducting/ducting-ac-3.jpg",
            "assets/img/ducting/ducting-bjls-3.jpg",
            "assets/img/ducting/ducting-bjls-2.jpg",
            "assets/img/ducting/ducting-fresh-air.jpg",
            "assets/img/ducting/ducting-pu.jpg",
            "assets/img/ducting/ducting-exhaust-2.jpg"
        ],
        "specs": [
            ("Kategori Produk", "Mega Terminal AHU Distribution Duct"),
            ("Dimensi Saluran", "Hingga 3.000 mm x 1.500 mm (Penampang Besar)"),
            ("Material Utama", "BJLS Heavy Gauge 1.0mm - 1.2mm"),
            ("Kapasitas Airflow", "20.000 – 150.000 CFM"),
            ("Tipe Diffuser", "High-Induction Drum Louver & Jet Nozzle"),
            ("Integrasi Kontrol", "VAV Damper + Building Automation System"),
            ("Garansi Resmi", "Garansi Konstruksi Masif 3 Tahun")
        ]
    }
]

# Template for Product Detail Page
def generate_product_html(p):
    specs_html = "".join([f"<li><strong>{s[0]}:</strong> <span>{s[1]}</span></li>\n" for s in p["specs"]])
    slider_slides = "".join([f'''<div class="swiper-slide">
                    <img src="{img}" alt="{p['title']}" class="img-fluid" loading="lazy">
                  </div>\n''' for img in p["slider_imgs"]])
    gallery_cols = "".join([f'''<div class="col-4">
                  <a href="{img}" class="glightbox" data-gallery="detail-gallery">
                    <img src="{img}" alt="{p['title']} Showcase" class="img-fluid" loading="lazy">
                  </a>
                </div>\n''' for img in p["gallery_imgs"]])

    html = f'''<!DOCTYPE html>
<html lang="id">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{p['title']} - Ducting HVAC</title>
  <meta name="description" content="{p['summary']}">
  <meta name="keywords" content="{p['title'].lower()}, ducting hvac, spesifikasi ducting, fabrikasi ducting, harga ducting">

  <!-- Favicons -->
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Nunito:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Main CSS File -->
  <link href="assets/css/main.css" rel="stylesheet">
</head>

<body class="project-details-page">

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
          <li><a href="products.html" class="active">Produk</a></li>
          <li><a href="blog.html">Blog</a></li>
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
        <a class="btn-quote d-none d-sm-inline-flex" href="contact.html">Minta Estimasi</a>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </div>

    </div>
  </header>

  <main class="main">

    <!-- Page Title -->
    <div class="page-title light-background">
      <div class="container d-lg-flex justify-content-between align-items-center">
        <h1 class="mb-2 mb-lg-0">Detail Produk</h1>
        <nav class="breadcrumbs">
          <ol>
            <li><a href="index.html">Beranda</a></li>
            <li><a href="products.html">Produk</a></li>
            <li class="current">{p['title']}</li>
          </ol>
        </nav>
      </div>
    </div><!-- End Page Title -->

    <!-- Product Details Section -->
    <section id="project-details" class="project-details section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-5">

          <div class="col-lg-8">

            <div class="hero-banner" data-aos="zoom-in">
              <div class="banner-slider swiper init-swiper">
                <script type="application/json" class="swiper-config">
                  {{
                    "loop": true,
                    "speed": 700,
                    "autoplay": {{
                      "delay": 4500
                    }},
                    "effect": "slide",
                    "slidesPerView": 1,
                    "pagination": {{
                      "el": ".swiper-pagination",
                      "type": "fraction"
                    }},
                    "navigation": {{
                      "nextEl": ".swiper-button-next",
                      "prevEl": ".swiper-button-prev"
                    }}
                  }}
                </script>
                <div class="swiper-wrapper">
                  {slider_slides}
                </div>
                <div class="slider-controls">
                  <div class="swiper-button-prev"></div>
                  <div class="swiper-pagination"></div>
                  <div class="swiper-button-next"></div>
                </div>
              </div><!-- End Banner Slider -->

              <div class="banner-overlay">
                <span class="tag">{p['tag']}</span>
                <h2>{p['title']}</h2>
              </div>
            </div><!-- End Hero Banner -->

            <div class="detail-tabs mt-4" data-aos="fade-up" data-aos-delay="200">
              <ul class="nav nav-tabs" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#project-details-tab-1" type="button" role="tab" aria-selected="true">
                    <i class="bi bi-info-circle"></i> Deskripsi &amp; Spesifikasi
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" data-bs-toggle="tab" data-bs-target="#project-details-tab-2" type="button" role="tab" aria-selected="false">
                    <i class="bi bi-shield-check"></i> Keunggulan Teknis
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" data-bs-toggle="tab" data-bs-target="#project-details-tab-3" type="button" role="tab" aria-selected="false">
                    <i class="bi bi-gear"></i> Aplikasi &amp; Pemasangan
                  </button>
                </li>
              </ul>

              <div class="tab-content">
                <div class="tab-pane fade show active" id="project-details-tab-1" role="tabpanel">
                  <p class="summary">
                    {p['summary']}
                  </p>
                  <p>
                    {p['p1']}
                  </p>
                  <p>
                    {p['p2']}
                  </p>
                </div><!-- End Tab 1 -->

                <div class="tab-pane fade" id="project-details-tab-2" role="tabpanel">
                  <h4>{p['tab2_title']}</h4>
                  <p>
                    {p['tab2_text']}
                  </p>
                </div><!-- End Tab 2 -->

                <div class="tab-pane fade" id="project-details-tab-3" role="tabpanel">
                  <h4>{p['tab3_title']}</h4>
                  <p>
                    {p['tab3_text']}
                  </p>
                </div><!-- End Tab 3 -->
              </div>
            </div><!-- End Detail Tabs -->

            <div class="photo-grid mt-4" data-aos="fade-up" data-aos-delay="300">
              <h4>Galeri Dokumentasi Produk</h4>
              <div class="row g-3">
                {gallery_cols}
              </div>
            </div><!-- End Photo Grid -->

          </div>

          <div class="col-lg-4">
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
          </div>

        </div>

      </div>

    </section><!-- /Product Details Section -->

  </main>

  <footer id="footer" class="footer">

    <div class="container footer-top">
      <div class="row gy-4">
        <div class="col-lg-5 col-md-12 footer-about">
          <a href="index.html" class="logo d-flex align-items-center">
            <span class="sitename">Ducting HVAC</span>
          </a>
          <p>Menghadirkan solusi fabrikasi dan instalasi Ducting HVAC terpadu (Exhaust, Fresh Air, AC Sentral, PU, dan BJLS) dengan pengalaman lebih dari 25 tahun, mengedepankan kualitas prima, efisiensi energi, dan standar SMACNA.</p>
          <div class="social-links d-flex mt-4">
            <a href="#"><i class="bi bi-twitter-x"></i></a>
            <a href="#"><i class="bi bi-facebook"></i></a>
            <a href="#"><i class="bi bi-instagram"></i></a>
            <a href="#"><i class="bi bi-linkedin"></i></a>
          </div>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h4>Tautan Cepat</h4>
          <ul>
            <li><a href="index.html">Beranda</a></li>
            <li><a href="about.html">Tentang Kami</a></li>
            <li><a href="services.html">Layanan</a></li>
            <li><a href="products.html">Katalog Produk</a></li>
            <li><a href="blog.html">Blog &amp; Berita</a></li>
            <li><a href="contact.html">Hubungi Kami</a></li>
          </ul>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h4>Produk Ducting</h4>
          <ul>
            <li><a href="ducting-exhaust.html">Ducting Exhaust</a></li>
            <li><a href="ducting-fresh-air.html">Ducting Fresh Air</a></li>
            <li><a href="ducting-ac.html">Ducting AC Sentral</a></li>
            <li><a href="ducting-pu.html">Ducting PU</a></li>
            <li><a href="ducting-bjls.html">Ducting BJLS</a></li>
            <li><a href="service-details.html">Maintenance &amp; Cleaning</a></li>
          </ul>
        </div>

        <div class="col-lg-3 col-md-12 footer-contact text-center text-md-start">
          <h4>Kontak Kami</h4>
          <p>Workshop Fabrikasi Ducting HVAC</p>
          <p>Jakarta &amp; Sekitarnya</p>
          <p>Indonesia</p>
          <p class="mt-4"><strong>Telepon:</strong> <span>0852-1062-0252</span></p>
          <p><strong>Email:</strong> <span>info@ductinghvac.co.id</span></p>
        </div>

      </div>
    </div>

    <div class="container copyright text-center mt-4">
      <p>© <span>Hak Cipta</span> <strong class="px-1 sitename">Ducting HVAC</strong> <span>Seluruh Hak Dilindungi</span></p>
    </div>

  </footer>

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Preloader -->
  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/purecounter/purecounter_vanilla.js"></script>
  <script src="assets/vendor/imagesloaded/imagesloaded.pkgd.min.js"></script>
  <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>

  <!-- Main JS File -->
  <script src="assets/js/main.js"></script>

</body>

</html>
'''
    return html

# 1. Generate all 12 product detail pages
for p in products:
    filepath = f"d:/Constructify-pro/{p['file']}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(generate_product_html(p))
    print(f"Created {p['file']}")

# 2. Generate products.html (Catalog of all 12 products)
product_cards_html = ""
for idx, p in enumerate(products, 1):
    product_cards_html += f'''            <!-- Product {idx} -->
            <div class="col-lg-4 col-md-6 portfolio-item isotope-item {p['filter']}">
              <div class="project-card">
                <img src="{p['slider_imgs'][0]}" alt="{p['title']}" class="img-fluid" loading="lazy">
                <div class="card-overlay">
                  <div class="card-content">
                    <span class="tag">{p['category']}</span>
                    <h3>{p['title']}</h3>
                    <p>{p['summary']}</p>
                  </div>
                  <div class="card-actions">
                    <a href="{p['slider_imgs'][0]}" class="card-action glightbox" data-gallery="projects" title="{p['title']}"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="{p['file']}" class="card-action" title="Lihat Detail Produk"><i class="bi bi-arrow-right"></i></a>
                  </div>
                </div>
              </div>
            </div><!-- End Product -->\n\n'''

products_page_html = f'''<!DOCTYPE html>
<html lang="id">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>Katalog Produk Ducting HVAC - Saluran Udara Profesional</title>
  <meta name="description" content="Jelajahi 12 produk ducting HVAC unggulan: sistem exhaust hood dapur, ducting AC sentral perkantoran, ducting PU cleanroom, ducting BJLS smoke spill, hingga ventilasi pabrik.">
  <meta name="keywords" content="katalog produk ducting, produk ducting hvac, exhaust hood dapur, ducting ac sentral, ducting pu, ducting bjls galvalum, fresh air">

  <!-- Favicons -->
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Nunito:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Main CSS File -->
  <link href="assets/css/main.css" rel="stylesheet">
</head>

<body class="projects-page">

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
          <li><a href="products.html" class="active">Produk</a></li>
          <li><a href="blog.html">Blog</a></li>
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
        <a class="btn-quote d-none d-sm-inline-flex" href="contact.html">Minta Estimasi</a>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </div>

    </div>
  </header>

  <main class="main">

    <!-- Page Title -->
    <div class="page-title light-background">
      <div class="container d-lg-flex justify-content-between align-items-center">
        <h1 class="mb-2 mb-lg-0">Katalog Produk</h1>
        <nav class="breadcrumbs">
          <ol>
            <li><a href="index.html">Beranda</a></li>
            <li class="current">Produk</li>
          </ol>
        </nav>
      </div>
    </div><!-- End Page Title -->

    <!-- Products Section -->
    <section id="projects" class="projects section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Katalog Produk Ducting HVAC Unggulan</h2>
        <p>Solusi lengkap cerobong dan saluran udara terstandardisasi SMACNA untuk kebutuhan komersial, perhotelan, rumah sakit, dan industri</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="isotope-layout" data-default-filter="*" data-layout="fitRows" data-sort="original-order">

          <ul class="portfolio-filters isotope-filters" data-aos="fade-up" data-aos-delay="100">
            <li data-filter="*" class="filter-active">Semua Produk</li>
            <li data-filter=".filter-exhaust">Exhaust &amp; Fresh Air</li>
            <li data-filter=".filter-ac">Ducting AC &amp; PU</li>
            <li data-filter=".filter-bjls">Ducting BJLS &amp; Industri</li>
          </ul><!-- End Portfolio Filters -->

          <div class="row g-4 isotope-container" data-aos="fade-up" data-aos-delay="200">

{product_cards_html}

          </div><!-- End Portfolio Items Container -->

        </div>

      </div>

    </section><!-- /Products Section -->

    <!-- Call To Action Section -->
    <section id="call-to-action" class="call-to-action section dark-background">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row align-items-center gy-5">

          <div class="col-lg-6" data-aos="fade-right" data-aos-delay="150">
            <div class="info-block">
              <span class="tagline">Bermitra dengan Tim Profesional</span>
              <h2>Pesan Produk Ducting HVAC Sesuai Spesifikasi Gedung Anda</h2>
              <p>Dapatkan penawaran harga terbaik, konsultasi pemilihan material (BJLS / PU / Stainless), serta survei kebutuhan CFM gratis dari teknisi spesialis kami.</p>

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

    </section><!-- /Call To Action Section -->

  </main>

  <footer id="footer" class="footer">

    <div class="container footer-top">
      <div class="row gy-4">
        <div class="col-lg-5 col-md-12 footer-about">
          <a href="index.html" class="logo d-flex align-items-center">
            <span class="sitename">Ducting HVAC</span>
          </a>
          <p>Menghadirkan solusi fabrikasi dan instalasi Ducting HVAC terpadu (Exhaust, Fresh Air, AC Sentral, PU, dan BJLS) dengan pengalaman lebih dari 25 tahun, mengedepankan kualitas prima, efisiensi energi, dan standar SMACNA.</p>
          <div class="social-links d-flex mt-4">
            <a href="#"><i class="bi bi-twitter-x"></i></a>
            <a href="#"><i class="bi bi-facebook"></i></a>
            <a href="#"><i class="bi bi-instagram"></i></a>
            <a href="#"><i class="bi bi-linkedin"></i></a>
          </div>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h4>Tautan Cepat</h4>
          <ul>
            <li><a href="index.html">Beranda</a></li>
            <li><a href="about.html">Tentang Kami</a></li>
            <li><a href="services.html">Layanan</a></li>
            <li><a href="products.html">Katalog Produk</a></li>
            <li><a href="blog.html">Blog &amp; Berita</a></li>
            <li><a href="contact.html">Hubungi Kami</a></li>
          </ul>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h4>Produk Ducting</h4>
          <ul>
            <li><a href="ducting-exhaust.html">Ducting Exhaust</a></li>
            <li><a href="ducting-fresh-air.html">Ducting Fresh Air</a></li>
            <li><a href="ducting-ac.html">Ducting AC Sentral</a></li>
            <li><a href="ducting-pu.html">Ducting PU</a></li>
            <li><a href="ducting-bjls.html">Ducting BJLS</a></li>
            <li><a href="service-details.html">Maintenance &amp; Cleaning</a></li>
          </ul>
        </div>

        <div class="col-lg-3 col-md-12 footer-contact text-center text-md-start">
          <h4>Kontak Kami</h4>
          <p>Workshop Fabrikasi Ducting HVAC</p>
          <p>Jakarta &amp; Sekitarnya</p>
          <p>Indonesia</p>
          <p class="mt-4"><strong>Telepon:</strong> <span>0852-1062-0252</span></p>
          <p><strong>Email:</strong> <span>info@ductinghvac.co.id</span></p>
        </div>

      </div>
    </div>

    <div class="container copyright text-center mt-4">
      <p>© <span>Hak Cipta</span> <strong class="px-1 sitename">Ducting HVAC</strong> <span>Seluruh Hak Dilindungi</span></p>
    </div>

  </footer>

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Preloader -->
  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/purecounter/purecounter_vanilla.js"></script>
  <script src="assets/vendor/imagesloaded/imagesloaded.pkgd.min.js"></script>
  <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>

  <!-- Main JS File -->
  <script src="assets/js/main.js"></script>

</body>

</html>
'''

with open("d:/Constructify-pro/products.html", "w", encoding="utf-8") as f:
    f.write(products_page_html)
print("products.html created successfully!")

# Also update projects.html to match products.html so anyone navigating to projects.html sees the updated products
with open("d:/Constructify-pro/projects.html", "w", encoding="utf-8") as f:
    f.write(products_page_html)
print("projects.html updated to sync with products.html!")

# 3. Update index.html:
# - Navbar: Proyek -> Produk (href="products.html")
# - Hero action: href="projects.html" -> href="products.html", "Jelajahi Produk Kami"
# - Section #projects: replace project-details.html links with the specific product files
with open("d:/Constructify-pro/index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Replace Navbar
idx_content = idx_content.replace('<li><a href="projects.html">Proyek</a></li>', '<li><a href="products.html">Produk</a></li>')
idx_content = idx_content.replace('<li><a href="projects.html" class="active">Proyek</a></li>', '<li><a href="products.html" class="active">Produk</a></li>')
idx_content = idx_content.replace('href="projects.html" class="btn-main">Jelajahi Proyek Kami</a>', 'href="products.html" class="btn-main">Jelajahi Produk Kami</a>')
idx_content = idx_content.replace('href="projects.html" class="stats-link">Lihat Portofolio Proyek', 'href="products.html" class="stats-link">Lihat Katalog Produk')
idx_content = idx_content.replace('<h2>Portofolio Proyek Ducting HVAC</h2>', '<h2>Katalog Produk Ducting HVAC Unggulan</h2>')
idx_content = idx_content.replace('<li data-filter="*" class="filter-active">Semua Proyek</li>', '<li data-filter="*" class="filter-active">Semua Produk</li>')

# Replace project-details.html with the actual 6 product files in index.html
# Product 1
idx_content = idx_content.replace(
    '''<h3>Sistem Exhaust Hood Dapur Komersial</h3>
                    <p>Instalasi cerobong exhaust uap dan asap bertekanan tinggi di food court pusat perbelanjaan</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-exhaust.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Exhaust Hood Dapur Komersial"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>''',
    '''<h3>Sistem Exhaust Hood Dapur Komersial</h3>
                    <p>Instalasi cerobong exhaust uap dan asap bertekanan tinggi di food court pusat perbelanjaan</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-exhaust.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Exhaust Hood Dapur Komersial"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="produk-exhaust-hood.html" class="card-action" title="Lihat Detail Produk"><i class="bi bi-arrow-right"></i></a>'''
)

# Product 2
idx_content = idx_content.replace(
    '''<h3>Ducting AC Sentral Gedung Perkantoran</h3>
                    <p>Sistem distribusi pendingin AHU bertingkat dengan insulasi termal prima dan difusi merata</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-ac.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting AC Sentral Gedung Perkantoran"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>''',
    '''<h3>Ducting AC Sentral Gedung Perkantoran</h3>
                    <p>Sistem distribusi pendingin AHU bertingkat dengan insulasi termal prima dan difusi merata</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-ac.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting AC Sentral Gedung Perkantoran"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="produk-ducting-ac-sentral.html" class="card-action" title="Lihat Detail Produk"><i class="bi bi-arrow-right"></i></a>'''
)

# Product 3
idx_content = idx_content.replace(
    '''<h3>Ducting BJLS Smoke Spill Basement</h3>
                    <p>Fabrikasi saluran baja lapis seng tebal tahan api untuk evakuasi asap darurat basement</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting BJLS Smoke Spill Basement"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>''',
    '''<h3>Ducting BJLS Smoke Spill Basement</h3>
                    <p>Fabrikasi saluran baja lapis seng tebal tahan api untuk evakuasi asap darurat basement</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls.jpg" class="card-action glightbox" data-gallery="projects" title="Ducting BJLS Smoke Spill Basement"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="produk-ducting-bjls-smoke-spill.html" class="card-action" title="Lihat Detail Produk"><i class="bi bi-arrow-right"></i></a>'''
)

# Product 4
idx_content = idx_content.replace(
    '''<h3>Cleanroom Ducting PU Farmasi &amp; RS</h3>
                    <p>Pemasangan panel Polyurethane higienis bebas serat partikel untuk ruang operasi dan laboratorium</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-pu.jpg" class="card-action glightbox" data-gallery="projects" title="Cleanroom Ducting PU Farmasi &amp; RS"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>''',
    '''<h3>Cleanroom Ducting PU Farmasi &amp; RS</h3>
                    <p>Pemasangan panel Polyurethane higienis bebas serat partikel untuk ruang operasi dan laboratorium</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-pu.jpg" class="card-action glightbox" data-gallery="projects" title="Cleanroom Ducting PU Farmasi &amp; RS"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="produk-cleanroom-ducting-pu.html" class="card-action" title="Lihat Detail Produk"><i class="bi bi-arrow-right"></i></a>'''
)

# Product 5
idx_content = idx_content.replace(
    '''<h3>Sistem Fresh Air &amp; Tekanan Positif</h3>
                    <p>Saluran suplai udara segar berfiltrasi HEPA menjaga kemurnian sirkulasi oksigen gedung bertingkat</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-fresh-air.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Fresh Air &amp; Tekanan Positif"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>''',
    '''<h3>Sistem Fresh Air &amp; Tekanan Positif</h3>
                    <p>Saluran suplai udara segar berfiltrasi HEPA menjaga kemurnian sirkulasi oksigen gedung bertingkat</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-fresh-air.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Fresh Air &amp; Tekanan Positif"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="produk-fresh-air-tekanan-positif.html" class="card-action" title="Lihat Detail Produk"><i class="bi bi-arrow-right"></i></a>'''
)

# Product 6
idx_content = idx_content.replace(
    '''<h3>Sistem Ventilasi Pabrik Industri Manufaktur</h3>
                    <p>Saluran udara volume besar bertekanan tinggi untuk pembuangan polutan dan pendinginan lini produksi</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls-2.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Ventilasi Pabrik Industri Manufaktur"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="project-details.html" class="card-action" title="Lihat Detail Proyek"><i class="bi bi-arrow-right"></i></a>''',
    '''<h3>Sistem Ventilasi Pabrik Industri Manufaktur</h3>
                    <p>Saluran udara volume besar bertekanan tinggi untuk pembuangan polutan dan pendinginan lini produksi</p>
                  </div>
                  <div class="card-actions">
                    <a href="assets/img/ducting/ducting-bjls-2.jpg" class="card-action glightbox" data-gallery="projects" title="Sistem Ventilasi Pabrik Industri Manufaktur"><i class="bi bi-arrows-fullscreen"></i></a>
                    <a href="produk-ventilasi-pabrik.html" class="card-action" title="Lihat Detail Produk"><i class="bi bi-arrow-right"></i></a>'''
)

idx_content = idx_content.replace('<li><a href="projects.html">Portofolio Proyek</a></li>', '<li><a href="products.html">Katalog Produk</a></li>')

with open("d:/Constructify-pro/index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)
print("index.html updated with Produk menu and product links!")

# 4. Update Navbars in ALL HTML files
all_html = glob.glob("d:/Constructify-pro/*.html")
for fpath in all_html:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # Navbar update
    c = c.replace('<li><a href="projects.html">Proyek</a></li>', '<li><a href="products.html">Produk</a></li>')
    c = c.replace('<li><a href="projects.html" class="active">Proyek</a></li>', '<li><a href="products.html" class="active">Produk</a></li>')
    c = c.replace('<li><a href="projects.html">Portofolio Proyek</a></li>', '<li><a href="products.html">Katalog Produk</a></li>')
    c = c.replace('<li><a href="projects.html">Proyek</a>', '<li><a href="products.html">Produk</a>')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)

print("All navigation bars updated with Produk menu!")
