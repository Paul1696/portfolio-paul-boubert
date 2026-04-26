import fitz
import os

def extract_project_images(project_name, pages):
    doc = fitz.open('PAUL BOUBERT _PORTFOLIO 2025.pdf')
    output_dir = f'assets/projects/{project_name}'
    os.makedirs(output_dir, exist_ok=True)
    
    count = 1
    for p in pages:
        image_list = doc[p].get_images()
        for i, img in enumerate(image_list):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            
            # Convert to RGB if necessary
            if pix.n - pix.alpha > 3:
                pix = fitz.Pixmap(fitz.csRGB, pix)
                
            if pix.width > 200 and pix.height > 200:
                out_path = os.path.join(output_dir, f"{project_name}_{count}.png")
                pix.save(out_path)
                print(f"Saved {out_path} ({pix.width}x{pix.height})")
                count += 1
            pix = None # free memory

if __name__ == "__main__":
    extract_project_images('hunter', [3, 4])
    extract_project_images('workbox', [5, 6])
    extract_project_images('bicec', [7, 8])
    extract_project_images('residence_h', [9, 10])
    extract_project_images('oasis', [11, 12])
    extract_project_images('harmony', [13, 14])
    extract_project_images('tonye', [15, 16])
    extract_project_images('mbella', [17, 18])
    extract_project_images('boj', [19, 20])
    extract_project_images('enem', [21, 22])
