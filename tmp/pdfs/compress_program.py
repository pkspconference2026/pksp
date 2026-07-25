from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image
from reportlab.pdfgen import canvas


INPUT = Path(r"C:\Users\hafiz\Downloads\BUKU PROGRAM PRINT FINAL.pdf")
OUTPUT = Path(r"C:\Users\hafiz\Desktop\pksp\Files\bukup-new.pdf")
WORK = Path(r"C:\Users\hafiz\Desktop\pksp\tmp\pdfs\program-pages")
SCALE = 2.0  # 144 dpi: crisp on phone screens without print-resolution weight.
JPEG_QUALITY = 78

WORK.mkdir(parents=True, exist_ok=True)
pdf = pdfium.PdfDocument(INPUT)
document = canvas.Canvas(str(OUTPUT), pageCompression=1)

for index in range(len(pdf)):
    page = pdf[index]
    width, height = page.get_size()
    bitmap = page.render(scale=SCALE, rev_byteorder=True)
    image = bitmap.to_pil().convert("RGB")
    image_path = WORK / f"page-{index + 1:02d}.jpg"
    image.save(image_path, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    document.setPageSize((width, height))
    document.drawImage(str(image_path), 0, 0, width=width, height=height, mask="auto")
    document.showPage()
    print(f"Rendered {index + 1}/{len(pdf)}")

document.save()
print(f"Created: {OUTPUT}")
