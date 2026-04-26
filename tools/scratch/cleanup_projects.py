import os
import re

projects_dir = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert\projects"
project_css_link = '<link rel="stylesheet" href="project.css">'

for filename in os.listdir(projects_dir):
    if filename.endswith(".html") and filename != "index.html":
        filepath = os.path.join(projects_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract background image
        bg_match = re.search(r"body::before\s*{[^}]*background-image:\s*url\(['\"]?([^'\")]*)['\"]?\)", content)
        if bg_match:
            bg_url = bg_match.group(1)
            
            # Create new style block
            new_style = f'    {project_css_link}\n    <style>\n        body::before {{\n            background-image: url("{bg_url}");\n        }}\n    </style>'
            
            # Replace old style block
            content = re.sub(r'\s*<style>.*?</style>', f'\n{new_style}', content, flags=re.DOTALL)
            
            # Clean up double head tags if any
            content = content.replace('</head>\n</head>', '</head>')
            
            # Standardize footer
            content = re.sub(r'<footer style=".*?">.*?</footer>', '<footer class="project-footer">\n        <p>&copy; 2026 Paul Boubert. Tous droits réservés.</p>\n    </footer>', content, flags=re.DOTALL)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
