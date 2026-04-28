import subprocess
import os

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
assets_projects_dir = os.path.join(root, "assets", "projects")

folders = [d for d in os.listdir(assets_projects_dir) if os.path.isdir(os.path.join(assets_projects_dir, d))]

for folder in folders:
    print(f"Pushing {folder}...")
    subprocess.run(["git", "add", f"assets/projects/{folder}"], cwd=root)
    subprocess.run(["git", "commit", "-m", f"Optimize project: {folder}"], cwd=root)
    res = subprocess.run(["git", "push", "origin", "main"], cwd=root)
    if res.returncode != 0:
        print(f"Failed to push {folder}. Retrying once...")
        subprocess.run(["git", "push", "origin", "main"], cwd=root)

print("Pushing remaining assets...")
subprocess.run(["git", "add", "."], cwd=root)
subprocess.run(["git", "commit", "-m", "Optimize remaining assets"], cwd=root)
subprocess.run(["git", "push", "origin", "main"], cwd=root)
