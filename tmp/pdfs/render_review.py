from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageDraw


PDF = Path(r"C:\Users\hafiz\Desktop\pksp\Files\bukup-new.pdf")
OUT = Path(r"C:\Users\hafiz\Desktop\pksp\tmp\pdfs\review-contact-sheet.jpg")
pages = (0, 22, 45)
pdf = pdfium.PdfDocument(PDF)
thumbs = []
for page_index in pages:
    image = pdf[page_index].render(scale=0.7, rev_byteorder=True).to_pil().convert("RGB")
    image.thumbnail((500, 750))
    thumbs.append((page_index + 1, image.copy()))

canvas = Image.new("RGB", (1540, 820), "white")
draw = ImageDraw.Draw(canvas)
for column, (number, image) in enumerate(thumbs):
    x = 20 + column * 510
    draw.text((x, 10), f"Page {number}", fill="black")
    canvas.paste(image, (x, 40))
canvas.save(OUT, "JPEG", quality=90)
print(OUT)
