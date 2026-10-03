import re
import os
import glob

# 1. Update contact.html FAQ & CTA
with open("d:/Constructify-pro/contact.html", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    "Apakah Constructify dapat melakukan survei langsung ke lokasi untuk estimasi awal?",
    "Apakah tim teknis Ducting HVAC dapat melakukan survei langsung ke lokasi untuk estimasi awal?"
)
c = c.replace(
    "Untuk proyek residensial besar, komersial, maupun renovasi struktural, salah satu insinyur lapangan kami akan berkunjung ke lokasi Anda guna meninjau kondisi kontur tanah, akses jalan, dan regulasi zonasi daerah.",
    "Ya. Untuk proyek gedung komersial, rumah sakit, restoran, maupun pabrik, insinyur tata udara kami akan berkunjung ke lokasi Anda guna mengukur dimensi ruangan, jalur lintasan ducting, dan kalkulasi kebutuhan CFM."
)
c = c.replace(
    "sketsa konsep awal arsitektur, dan perkiraan alokasi anggaran agar proses perhitungan RAB dapat berjalan lebih cepat dan akurat.",
    "denah gedung / layout MEP, dan spesifikasi unit pendingin/blower agar proses perhitungan dimensi ducting dan RAB dapat berjalan lebih cepat dan akurat."
)
c = c.replace(
    "<h3>Apakah Constructify dapat membantu pengurusan perizinan konstruksi (PBG/IMB)?</h3>",
    "<h3>Apakah pengujian Air Balancing (TAB) dan jaminan kebocoran udara disertakan?</h3>"
)
c = c.replace(
    "<p>Tentu saja. Kami mengelola seluruh proses administrasi perizinan dinas tata kota, pengurusan PBG (Persetujuan Bangunan Gedung), izin lingkungan, serta sertifikat laik fungsi bangunan.</p>",
    "<p>Tentu saja. Setiap proyek instalasi saluran ducting kami dilengkapi dengan pengetesan Testing Adjusting Balancing (TAB) dan sertifikat garansi bebas kebocoran udara sesuai standar SMACNA.</p>"
)

# CTA in contact.html
old_cta_pattern = r'<!-- Call To Action Section -->.*?<!-- /Call To Action Section -->'
new_cta = '''<!-- Call To Action Section -->
    <section id="call-to-action" class="call-to-action section dark-background">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row align-items-center gy-5">

          <div class="col-lg-6" data-aos="fade-right" data-aos-delay="150">
            <div class="info-block">
              <span class="tagline">Bermitra dengan Tim Profesional</span>
              <h2>Optimalkan Sirkulasi Tata Udara &amp; Efisiensi Gedung Anda</h2>
              <p>Konsultasikan langsung rencana instalasi saluran ducting HVAC Anda bersama para insinyur senior kami dan temukan bagaimana Ducting HVAC menghadirkan nilai tambah, efisiensi energi, dan mutu presisi terbaik.</p>

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
c = re.sub(old_cta_pattern, new_cta, c, flags=re.DOTALL)
with open("d:/Constructify-pro/contact.html", "w", encoding="utf-8") as f:
    f.write(c)

# 2. General sweep across all HTML files for any remaining "Constructify" or "konstruksi"
for html_file in glob.glob("d:/Constructify-pro/*.html"):
    with open(html_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Case-insensitive replacements where appropriate or specific replacements
    text = text.replace("info@constructify.co.id", "info@ductinghvac.co.id")
    text = text.replace("privacy@constructify.com", "privacy@ductinghvac.co.id")
    text = text.replace("proyek@constructify.id", "proyek@ductinghvac.co.id")
    text = text.replace("legalitas constructify", "legalitas ducting hvac")
    text = text.replace("template constructify", "template ducting hvac")
    text = text.replace("perlindungan privasi constructify", "perlindungan privasi ducting hvac")
    text = text.replace("Mengapa Constructify", "Mengapa Ducting HVAC")
    text = text.replace("Di Constructify", "Di Ducting HVAC")
    text = text.replace("kepada Constructify", "kepada tim Ducting HVAC")
    text = text.replace("tim Constructify", "tim Ducting HVAC")
    text = text.replace("ahli Constructify", "ahli Ducting HVAC")
    text = text.replace("konstruksi hijau", "tata udara ramah lingkungan")
    text = text.replace("inovasi konstruksi", "inovasi tata udara")
    text = text.replace("rekayasa konstruksi", "rekayasa tata udara")
    text = text.replace("pengerjaan konstruksi", "pengerjaan ducting HVAC")
    text = text.replace("saat dekonstruksi", "saat peremajaan gedung")
    text = text.replace("Lokasi Konstruksi Constructify", "Instalasi Ducting HVAC")
    text = text.replace("Konstruksi Residensial", "Ducting Exhaust")

    # Clean any keyword mentioning constructify
    text = re.sub(r',\s*constructify\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\bconstructify\b', 'Ducting HVAC', text, flags=re.IGNORECASE)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(text)

print("Final cleanup completed across all HTML files!")
