import os

projects_dir = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert\projects"
files = [f for f in os.listdir(projects_dir) if f.endswith('.html')]

cursor_html = """    <!-- Custom Cursor -->
    <div class="cursor"></div>
    <div class="cursor-follower"></div>
"""

script_tag = '<script src="../script.js"></script>'

for filename in files:
    filepath = os.path.join(projects_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add cursor HTML if missing
    if '<div class="cursor">' not in content:
        if '<body class="loaded">' in content:
            content = content.replace('<body class="loaded">', '<body class="loaded">\n' + cursor_html)
        elif '<body>' in content:
            content = content.replace('<body>', '<body>\n' + cursor_html)
    
    # Add script tag if missing
    if 'script.js' not in content:
        content = content.replace('</body>', '    ' + script_tag + '\n</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(files)} files.")
