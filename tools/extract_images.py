import fitz
import os

pdf_path = r"C:\Users\JEREMY\APPS\NexusCore\PAUL BOUBERT _PORTFOLIO 2025.pdf"
doc = fitz.open(pdf_path)

projects = {
    "tonye": 28,
    "workbox": 8,
    "hunter": 3,
    "bicec": 12,
    "oasis": 20,
    "boj": 36,
    "enem": 40
}

output_dir = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"

for name, page_num in projects.items():
    try:
        page = doc[page_num]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        out_path = os.path.join(output_dir, f"{name}.png")
        pix.save(out_path)
        print(f"Saved {name}.png")
    except Exception as e:
        print(f"Error saving {name}.png: {e}")
