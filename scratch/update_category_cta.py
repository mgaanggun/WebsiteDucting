import re

replacements = {
    "ducting-exhaust.html": (
        r'<a\s+href="contact\.html"\s+class="btn\s+btn-quote\s+px-4\s+py-2">Minta Estimasi Biaya</a>',
        '<a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20estimasi%20biaya%20sistem%20Ducting%20Exhaust." target="_blank" rel="noopener noreferrer" class="btn btn-quote px-4 py-2"><i class="bi bi-whatsapp me-2"></i>Minta Estimasi Biaya</a>'
    ),
    "ducting-fresh-air.html": (
        r'<a\s+href="contact\.html"\s+class="btn\s+btn-quote\s+px-4\s+py-2">Minta Estimasi Biaya</a>',
        '<a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20estimasi%20biaya%20sistem%20Ducting%20Fresh%20Air." target="_blank" rel="noopener noreferrer" class="btn btn-quote px-4 py-2"><i class="bi bi-whatsapp me-2"></i>Minta Estimasi Biaya</a>'
    ),
    "ducting-ac.html": (
        r'<a\s+href="contact\.html"\s+class="btn\s+btn-quote\s+px-4\s+py-2">Minta Estimasi Biaya</a>',
        '<a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20estimasi%20biaya%20sistem%20Ducting%20AC." target="_blank" rel="noopener noreferrer" class="btn btn-quote px-4 py-2"><i class="bi bi-whatsapp me-2"></i>Minta Estimasi Biaya</a>'
    ),
    "ducting-pu.html": (
        r'<a\s+href="contact\.html"\s+class="btn\s+btn-quote\s+px-4\s+py-2">Minta Penawaran Panel PU</a>',
        '<a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20penawaran%20panel%20Ducting%20PU." target="_blank" rel="noopener noreferrer" class="btn btn-quote px-4 py-2"><i class="bi bi-whatsapp me-2"></i>Minta Penawaran Panel PU</a>'
    ),
    "ducting-bjls.html": (
        r'<a\s+href="contact\.html"\s+class="btn\s+btn-quote\s+px-4\s+py-2">Minta Penawaran Fabrikasi</a>',
        '<a href="https://wa.me/6285210620252?text=Halo%20Ducting%20HVAC%2C%20saya%20ingin%20minta%20penawaran%20fabrikasi%20Ducting%20BJLS." target="_blank" rel="noopener noreferrer" class="btn btn-quote px-4 py-2"><i class="bi bi-whatsapp me-2"></i>Minta Penawaran Fabrikasi</a>'
    )
}

for fname, (pattern, repl) in replacements.items():
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    if re.search(pattern, content):
        content = re.sub(pattern, repl, content)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname}")
    else:
        print(f"Pattern not found in {fname}")
