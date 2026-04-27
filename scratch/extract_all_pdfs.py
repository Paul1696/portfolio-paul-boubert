import fitz
import os

def extract_pdf_pages(pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    try:
        doc = fitz.open(pdf_path)
        for i, page in enumerate(doc):
            pix = page.get_pixmap()
            pix.save(os.path.join(output_folder, f"page_{i}.png"))
        doc.close()
        print(f"Extracted {len(doc)} pages from {pdf_path}")
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")

projects = {
    "bahemeck": r"D:\PROJETS\01_VILLAS_ET_DUPLEX\APPART BAHEMECK\000_APPART BAHEMECK_SM_25-08-01.pdf",
    "essaga": r"D:\PROJETS\01_VILLAS_ET_DUPLEX\ESSAGA\PROJET M ESSAGA(FACADES ET COUPES).dwg", # Wait, DWG...
    "bahemeck_alt": r"D:\PROJETS\01_VILLAS_ET_DUPLEX\APPART BAHEMECK\000_APPART BAHEMECK_SM_25-08-01.pdf"
}

# List all PDFs in D:\PROJETS\01_VILLAS_ET_DUPLEX
import glob
all_pdfs = glob.glob(r"D:\PROJETS\01_VILLAS_ET_DUPLEX\**\*.pdf", recursive=True)

for pdf in all_pdfs:
    folder_name = os.path.basename(os.path.dirname(pdf)).lower().replace(" ", "_")
    output_dir = os.path.join("assets", "projects", folder_name)
    extract_pdf_pages(pdf, output_dir)
