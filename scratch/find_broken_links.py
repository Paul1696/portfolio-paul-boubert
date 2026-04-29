import os
import re

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
index_path = os.path.join(root, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all src="assets/..."
matches = re.findall(r'src="(assets/[^"]+)"', content)

broken_links = []
for link in matches:
    # Remove any query params if present
    clean_link = link.split('?')[0]
    full_path = os.path.join(root, clean_link.replace('/', os.sep))
    if not os.path.exists(full_path):
        broken_links.append(link)

print(f"Found {len(broken_links)} broken links: {broken_links}")
