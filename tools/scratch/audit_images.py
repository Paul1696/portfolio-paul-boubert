import os
import re

base_path = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
projects_dir = os.path.join(base_path, "projects")
assets_dir = os.path.join(base_path, "assets", "projects")

html_files = [os.path.join(base_path, "index.html")] + \
             [os.path.join(projects_dir, f) for f in os.listdir(projects_dir) if f.endswith(".html")]

missing_images = []

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trouver tous les src d'images
    # On cherche les src="assets/..." ou src="../assets/..."
    images = re.findall(r'src="([^"]+)"', content)
    
    for img_path in images:
        if "assets/projects" in img_path:
            # Normaliser le chemin
            # Si c'est dans index.html, le chemin est direct
            # Si c'est dans projects/*.html, le chemin commence par ../
            clean_path = img_path.replace("../", "")
            full_path = os.path.join(base_path, clean_path.replace("/", os.sep))
            
            if not os.path.exists(full_path):
                missing_images.append({
                    "file": os.path.basename(html_file),
                    "path": img_path,
                    "full_path": full_path
                })

for m in missing_images:
    print(f"MISSING in {m['file']}: {m['path']}")
