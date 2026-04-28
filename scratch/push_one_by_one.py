import subprocess
import os

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"
folder_path = os.path.join(root, "assets", "projects", "bahemeck_final")
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for f in files:
    print(f"Pushing {f}...")
    subprocess.run(["git", "add", f"assets/projects/bahemeck_final/{f}"], cwd=root)
    subprocess.run(["git", "commit", "-m", f"Optimize image: {f}"], cwd=root)
    subprocess.run(["git", "push", "origin", "main"], cwd=root)

# Then continue with other folders
# I'll just run the previous script again but it will skip already pushed stuff
