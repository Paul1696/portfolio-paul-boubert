import os
import re
import subprocess

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
index_path = os.path.join(root, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all assets/projects/something
matches = re.findall(r'assets/projects/([^/"\'\s]+)', content)
used_folders = set(matches)

missing_folders = []
for folder in used_folders:
    folder_path = os.path.join(root, "assets", "projects", folder)
    if not os.path.exists(folder_path):
        missing_folders.append(folder)

print(f"Missing used folders: {missing_folders}")

for folder in missing_folders:
    print(f"Restoring {folder}...")
    # Try to restore from git
    subprocess.run(["git", "checkout", f"assets/projects/{folder}"], cwd=root)

# Check for missing project HTML files too
project_matches = re.findall(r'projects/([^/"\'\s]+\.html)', content)
used_projects = set(project_matches)

missing_projects = []
for project in used_projects:
    project_path = os.path.join(root, "projects", project)
    if not os.path.exists(project_path):
        missing_projects.append(project)

print(f"Missing used project files: {missing_projects}")
for project in missing_projects:
    print(f"Restoring {project}...")
    subprocess.run(["git", "checkout", f"projects/{project}"], cwd=root)
