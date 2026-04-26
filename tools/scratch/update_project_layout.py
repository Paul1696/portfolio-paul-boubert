import os
import re

projects_dir = r'c:\Users\JEREMY\APPS\Portfolio Paul Boubert\projects'

for filename in os.listdir(projects_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(projects_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update container max-width and padding
        new_content = re.sub(r'max-width:\s*1600px;', 'max-width: 1920px;', content)
        new_content = re.sub(r'padding:\s*4rem\s*5vw;', 'padding: 4rem 3vw;', new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")
