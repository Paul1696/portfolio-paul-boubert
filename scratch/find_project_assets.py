import os

base_path = r"D:\PROJETS\01_VILLAS_ET_DUPLEX"
projects = [
    "BOLY", "COUPLE CARON", "DUPLEX DOMEGNE", "ESSAGA", "M. NGOUNOU",
    "M.OWONA", "MANDENG", "MVOGT", "MVOLYE", "ONGUENE",
    "PROJET VILLA EDEME", "SA MAJESTE", "VILLA", "VILLA AKWA",
    "VILLA BARLA", "VILLA BOUMSONG", "VILLA DOUBLE M"
]

results = {}

for project in projects:
    project_path = os.path.join(base_path, project)
    if not os.path.exists(project_path):
        results[project] = "MISSING"
        continue
    
    found_images = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                found_images.append(os.path.join(root, file))
                if len(found_images) >= 3:
                    break
        if len(found_images) >= 3:
            break
    
    results[project] = found_images

for p, imgs in results.items():
    print(f"--- {p} ---")
    if imgs == "MISSING":
        print("Project folder not found.")
    elif not imgs:
        print("No images found.")
    else:
        for img in imgs:
            print(img)
