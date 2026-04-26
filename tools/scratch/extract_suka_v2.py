import fitz
import os

def extract_suka_images():
    pdf_path = r'C:\Users\JEREMY\Documents\SUKA CAFE TERRASSE_5_APS_1_Presentation_26-03-21 [Autosaved].pdf'
    output_dir = 'assets/projects/suka_cafe'
    os.makedirs(output_dir, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    count = 2
    
    # We want the best images (renders, plans)
    # Usually they are large
    for p in range(len(doc)):
        image_list = doc[p].get_images()
        for i, img in enumerate(image_list):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            
            # Convert to RGB if necessary
            if pix.n - pix.alpha > 3:
                pix = fitz.Pixmap(fitz.csRGB, pix)
            
            # Filter for high quality images
            if pix.width > 1000 and pix.height > 800:
                out_path = os.path.join(output_dir, f"suka_{count}.jpg")
                pix.save(out_path)
                print(f"Saved {out_path} ({pix.width}x{pix.height})")
                count += 1
                if count > 20:
                    return
            pix = None

if __name__ == "__main__":
    extract_suka_images()
