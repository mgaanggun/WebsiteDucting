import os
import re

root = "c:/Users/FERDY/Downloads/Ducting"
files = [f for f in os.listdir(root) if f.endswith(".html")]

wa_snippet = """

  <!-- Floating WhatsApp -->
  <a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20konsultasi%20mengenai%20instalasi%20ducting" class="floating-wa" target="_blank" rel="noopener noreferrer" aria-label="Hubungi Kami via WhatsApp" title="Chat WhatsApp">
    <i class="bi bi-whatsapp"></i>
  </a>"""

count = 0
for f in files:
    path = os.path.join(root, f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    if 'class="floating-wa"' in content:
        continue
    
    pattern = r'(<a href="#" id="scroll-top"[^>]*>.*?</a>)'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1' + wa_snippet, content)
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
        count += 1

print(f"Added floating WhatsApp button to {count} HTML files.")
