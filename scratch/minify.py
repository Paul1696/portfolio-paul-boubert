import re
import os

def minify_css(css):
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Remove whitespace
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{:;,])\s*', r'\1', css)
    return css.strip()

def minify_js(js):
    # This is a very basic minifier, it might break complex code
    # but for simple JS it should be fine.
    # Remove single line comments
    js = re.sub(r'//.*', '', js)
    # Remove multiline comments
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    # Remove extra whitespace
    js = re.sub(r'\s+', ' ', js)
    return js.strip()

root = r"c:\Users\JEREMY\APPS\Portfolio Paul Boubert"

# Minify style.css -> style.min.css
with open(os.path.join(root, "style.css"), "r", encoding="utf-8") as f:
    css_content = f.read()
    min_css = minify_css(css_content)
    with open(os.path.join(root, "style.min.css"), "w", encoding="utf-8") as f_min:
        f_min.write(min_css)

# Minify script.js -> script.min.js
with open(os.path.join(root, "script.js"), "r", encoding="utf-8") as f:
    js_content = f.read()
    min_js = minify_js(js_content)
    with open(os.path.join(root, "script.min.js"), "w", encoding="utf-8") as f_min:
        f_min.write(min_js)

print("Minification complete.")
