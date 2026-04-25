import os
import re

projects_dir = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert\projects"
files = [f for f in os.listdir(projects_dir) if f.endswith(".html")]

# On ne traite pas web_tower.html car il est déjà fait
files = [f for f in files if f != "web_tower.html"]

for filename in files:
    filepath = os.path.join(projects_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extraire le src de l'image hero pour l'utiliser en fond
    hero_img_match = re.search(r'<img src="([^"]+)" alt="[^"]+" class="hero-img">', content)
    if not hero_img_match:
        # Essayer un autre pattern si besoin
        hero_img_match = re.search(r'<header class="project-hero">.*?<img src="([^"]+)"', content, re.DOTALL)
    
    if hero_img_match:
        hero_img_src = hero_img_match.group(1)
        
        # 2. Remplacer tout le bloc <style>
        # On définit le nouveau style
        new_style = f"""    <style>
        :root {{
            --color-bg: #ffffff;
            --color-text: #111827;
            --color-primary: #0047AB; 
            --color-secondary: #f8fafc;
            --color-accent: #e2e8f0;
        }}

        html {{
            background-color: var(--color-bg);
        }}

        body {{
            background-color: transparent;
            color: var(--color-text);
            margin: 0;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
            position: relative;
        }}

        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('{hero_img_src}');
            background-size: cover;
            background-position: center;
            opacity: 0.15;
            pointer-events: none;
            z-index: -1;
        }}

        .project-hero {{
            height: 70vh;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #000;
        }}

        .hero-img {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.6);
            z-index: 0;
        }}

        .hero-content {{
            text-align: center;
            padding: 0 1rem;
            position: relative;
            z-index: 10;
            color: #ffffff;
        }}

        .hero-content h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(3rem, 8vw, 5rem);
            margin-bottom: 1rem;
            letter-spacing: -2px;
        }}

        .project-meta {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            font-size: 0.9rem;
            color: #ffffff;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        .container {{
            max-width: 1920px;
            margin: 0 auto;
            padding: 4rem 3vw;
        }}

        .project-description {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 4rem;
            margin-bottom: 6rem;
        }}

        @media (max-width: 768px) {{
            .project-description {{
                grid-template-columns: 1fr;
                gap: 2rem;
            }}
        }}

        .desc-text p {{
            line-height: 1.8;
            font-size: 1.1rem;
            color: #4B5563;
            margin-bottom: 1.5rem;
        }}

        .desc-text h2 {{
            font-family: 'Outfit', sans-serif;
            color: #111827;
            margin-bottom: 1.5rem;
        }}

        .project-specs {{
            background: var(--color-secondary);
            padding: 2rem;
            border-radius: 12px;
            height: fit-content;
        }}

        .spec-item {{
            margin-bottom: 1.5rem;
        }}

        .spec-label {{
            display: block;
            font-size: 0.7rem;
            color: var(--color-primary);
            text-transform: uppercase;
            margin-bottom: 0.3rem;
            letter-spacing: 1px;
        }}

        .spec-value {{
            font-weight: 500;
            font-size: 1.1rem;
        }}

        .gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));
            gap: 2rem;
        }}

        .gallery-item {{
            position: relative;
            border-radius: 8px;
            overflow: hidden;
            cursor: none;
            transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        }}

        .gallery-item:hover {{
            transform: scale(1.02);
        }}

        .gallery-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }}

        .back-nav {{
            position: fixed;
            top: 2rem;
            left: 2rem;
            z-index: 100;
        }}

        .btn-back {{
            background: rgba(0, 0, 0, 0.05);
            backdrop-filter: blur(10px);
            color: #111827;
            text-decoration: none;
            padding: 0.8rem 1.5rem;
            border-radius: 50px;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
            transition: all 0.3s;
            border: 1px solid rgba(0, 0, 0, 0.1);
            cursor: none;
        }}

        .btn-back:hover {{
            background: var(--color-primary);
            color: #ffffff;
        }}

        * {{
            cursor: none !important;
        }}
    </style>"""
        
        # On remplace l'ancien bloc style par le nouveau
        content = re.sub(r'    <style>.*?</style>', new_style, content, flags=re.DOTALL)
        
        # 3. S'assurer que hero-content a les bonnes classes et structure (normalement c'est déjà bon)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
