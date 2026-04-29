import os
import re

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
index_path = os.path.join(root, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to match project cards
project_pattern = re.compile(r'(<article class="project-card".*?</article>)', re.DOTALL)
projects = project_pattern.findall(content)

seen_names = set()
new_projects_list = []
removed_count = 0

for project_html in projects:
    # Extract project name to find duplicates
    name_match = re.search(r'<h3 class="project-name">(.*?)</h3>', project_html)
    name = name_match.group(1).strip() if name_match else "Unknown"
    
    # Extract folder name
    folder_match = re.search(r'assets/projects/([^/"\'\s]+)', project_html)
    folder_name = folder_match.group(1) if folder_match else "none"

    # CRITERIA FOR REMOVAL:
    # 1. Duplicates
    # 2. Projects with "placeholder" in them if any
    # 3. Specific projects the user might want removed (e.g. old ones)
    
    is_duplicate = name in seen_names
    
    if is_duplicate:
        print(f"Removing duplicate: {name}")
        removed_count += 1
        continue
    
    # Keep the project
    seen_names.add(name)
    new_projects_list.append(project_html)

# We want to keep the overall structure but replace the project cards
# This is tricky because projects are in different category-blocks.
# Instead of replacing everything, let's do a targeted replacement for known duplicates and the specific Meeting Room update.

# Update Meeting Room image
content = content.replace('assets/projects/meeting_room/hero.jpg', 'assets/projects/meeting_room/img_7.jpg')

# Manual removal of the confirmed duplicate Boutique Biyem-Assi
# I'll use a more precise replacement for the duplicate
duplicate_biyem = '''                        <article class="project-card" data-category="architecture" data-type="commercial">
                            <div class="project-image">
                                <img src="assets/projects/boutique_biyem_assi/hero.jpg" alt="Boutique Biyem-Assi">
                                <div class="project-info-overlay">
                                    <span class="project-category">Commerce de Proximit</span>
                                    <h3 class="project-name">Boutique Biyem-Assi</h3>
                                    <p class="project-desc">Conception d'un espace commercial sur trois niveaux au cur du quartier Biyem-Assi  Yaound.</p>
                                    <a href="projects/boutique_biyem_assi.html" class="project-link">Dcouvrir <i class="fas fa-long-arrow-alt-right"></i></a>
                                </div>
                            </div>
                        </article>'''

# Replace the second occurrence (which has a slightly different indentation or same)
# Actually, I'll just use a script to find and remove any exact repeated block
blocks = re.split(r'(<article class="project-card".*?</article>)', content, flags=re.DOTALL)
final_blocks = []
seen_blocks = set()

for block in blocks:
    clean_block = re.sub(r'\s+', ' ', block).strip()
    if clean_block.startswith('<article class="project-card"'):
        if clean_block in seen_blocks:
            print(f"Removing exact duplicate block")
            continue
        seen_blocks.add(clean_block)
    final_blocks.append(block)

new_content = "".join(final_blocks)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Cleanup done. Meeting Room updated.")
