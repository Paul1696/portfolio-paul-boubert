import os
import re

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
index_path = os.path.join(root, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to match project cards
project_pattern = re.compile(r'(<article class="project-card".*?</article>)', re.DOTALL)
projects = project_pattern.findall(content)

new_content = content
removed_count = 0

for project_html in projects:
    if "Villa Boumsong" in project_html or "Villa Double M" in project_html:
        print(f"Removing project card from index.html")
        new_content = new_content.replace(project_html, "")
        removed_count += 1

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Total projects removed from HTML: {removed_count}")
