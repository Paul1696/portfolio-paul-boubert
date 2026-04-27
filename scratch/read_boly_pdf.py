import PyPDF2

pdf_path = r"D:\PROJETS\01_VILLAS_ET_DUPLEX\BOLY\PDF\PROJET DE CONSTRUCTION D'UN IMMEUBLE R+2  A USAGE D'HABITATION POUR LE COMPTE DE Mme FOTSO FELICITE.pdf"

try:
    reader = PyPDF2.PdfReader(pdf_path)
    text = reader.pages[0].extract_text()
    print("--- PAGE 1 ---")
    print(text[:1000])
except Exception as e:
    print(f"Error: {e}")
