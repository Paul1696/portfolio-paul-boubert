import os
import re

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
index_path = os.path.join(root, "index.html")
assets_projects_dir = os.path.join(root, "assets", "projects")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to match a whole <article class="project-card" ... </article>
# Note: This is a bit risky with regex but I'll try to match balanced-ish blocks
project_pattern = re.compile(r'(<article class="project-card".*?</article>)', re.DOTALL)
projects = project_pattern.findall(content)

print(f"Found {len(projects)} projects in index.html")

new_content = content
removed_count = 0

for project_html in projects:
    # Find the folder name in src="assets/projects/folder_name/..."
    match = re.search(r'assets/projects/([^/"\'\s]+)', project_html)
    if match:
        folder_name = match.group(1)
        folder_path = os.path.join(assets_projects_dir, folder_name)
        
        # If the folder doesn't exist, remove the project from HTML
        if not os.path.exists(folder_path):
            print(f"Removing project referencing missing folder: {folder_name}")
            # Use escaped version to be safe with replacements
            new_content = new_content.replace(project_html, f"<!-- Removed unused project: {folder_name} -->")
            removed_count += 1

# Also update Meeting Room image while we are at it
new_content = new_content.replace('assets/projects/meeting_room/hero.jpg', 'assets/projects/meeting_room/img_7.jpg')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Total projects removed: {removed_count}")
