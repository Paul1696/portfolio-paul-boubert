import os

ga_tag = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-89V1WZL52D"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-89V1WZL52D');
    </script>
"""

def inject_tag(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'G-89V1WZL52D' in content:
        print(f"Tag already present in {file_path}")
        return

    # Inject before </head>
    if '</head>' in content:
        new_content = content.replace('</head>', ga_tag + '</head>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected tag into {file_path}")
    else:
        print(f"No </head> found in {file_path}")

# Root files
for f in ['index.html', 'about.html']:
    if os.path.exists(f):
        inject_tag(f)

# Projects
project_dir = 'projects'
if os.path.exists(project_dir):
    for f in os.listdir(project_dir):
        if f.endswith('.html'):
            inject_tag(os.path.join(project_dir, f))
