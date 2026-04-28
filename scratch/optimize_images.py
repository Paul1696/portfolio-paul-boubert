import os
from PIL import Image

def optimize_image(filepath):
    try:
        img = Image.open(filepath)
        original_size = os.path.getsize(filepath)
        
        # Resize if too large
        max_width = 1920
        if img.width > max_width:
            w_percent = (max_width / float(img.width))
            h_size = int((float(img.height) * float(w_percent)))
            img = img.resize((max_width, h_size), Image.Resampling.LANCZOS)
        
        # Convert RGBA to RGB if saving as JPEG
        if img.mode in ("RGBA", "P") and filepath.lower().endswith(('.jpg', '.jpeg')):
            img = img.convert("RGB")
            
        # Save with optimization
        if filepath.lower().endswith(('.jpg', '.jpeg')):
            img.save(filepath, "JPEG", quality=80, optimize=True)
        elif filepath.lower().endswith('.png'):
            img.save(filepath, "PNG", optimize=True)
            
        new_size = os.path.getsize(filepath)
        return original_size - new_size
    except Exception as e:
        print(f"Error optimizing {filepath}: {e}")
        return 0

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert\assets"
total_saved = 0
count = 0

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(dirpath, filename)
            saved = optimize_image(filepath)
            total_saved += saved
            count += 1
            if count % 10 == 0:
                print(f"Optimized {count} images...")

print(f"Finished! Optimized {count} images. Total space saved: {total_saved / 1024 / 1024:.2f} MB")
