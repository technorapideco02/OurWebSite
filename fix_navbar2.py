import os
import glob
import re

with open("index.html", "r") as f:
    home_content = f.read()

# 1. Get the EXACT <nav> block from index.html
nav_match = re.search(r'<nav class="fixed w-full top-0 z-50 nav-glass border-b border-slate-200 dark:border-slate-800">.*?</nav>', home_content, re.DOTALL)
if not nav_match:
    print("Could not find <nav> in index.html")
    exit(1)

home_nav = nav_match.group(0)

def fix_inner_nav(nav_html):
    # Adjust paths for inner pages
    html = nav_html
    # Links like href="portfolio/" -> href="../portfolio/"
    # Links like href="about/" -> href="../about/"
    # Links like href="web-development/" -> href="../web-development/"
    # Links like href="tech-stack/" -> href="../tech-stack/"
    # Links like href="insights/" -> href="../insights/"
    
    # We replace href="xyz/" with href="../xyz/"
    html = re.sub(r'href="(?!https?://|mailto:|tel:|#|\.\.)([^/]+)/"', r'href="../\1/"', html)
    
    # Add Back to Home Link in the header
    # In index.html: <div class="hidden md:flex items-center gap-10">
    html = html.replace('<div class="hidden md:flex items-center gap-10">', '<div class="hidden md:flex items-center gap-10">\n                <a class="text-sm font-semibold hover:text-primary transition-colors" href="../">Back to Home</a>')
    
    return html

inner_nav = fix_inner_nav(home_nav)

font_link = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Great+Vibes&display=swap" rel="stylesheet">'
font_face_css = """
        @font-face {
            font-family: 'Runiga';
            src: local('Runiga');
        }

        @font-face {
            font-family: 'Gafiya';
            src: local('Gafiya');
        }

        @font-face {
            font-family: 'Vartensie';
            src: local('Vartensie');
        }
"""

def process_file(filepath):
    if filepath.endswith("index.html") and filepath != "./index.html":
        with open(filepath, 'r') as f:
            content = f.read()
            
        original_content = content
        
        # Replace entire <nav> block
        content = re.sub(r'<nav class="fixed w-full top-0 z-50 nav-glass border-b border-slate-200 dark:border-slate-800">.*?</nav>', inner_nav, content, flags=re.DOTALL)
        
        # Inject Google fonts link
        if "family=Playfair+Display" not in content:
            content = content.replace('<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>', 
                                      '<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>\n    ' + font_link)
        
        # Inject @font-face blocks
        if "font-family: 'Gafiya';" not in content and "font-family: 'Runiga';" not in content:
            if '<style type="text/tailwindcss">' in content:
                content = content.replace('<style type="text/tailwindcss">', '<style type="text/tailwindcss">' + font_face_css)
            else:
                style_block = f'<style type="text/tailwindcss">{font_face_css}</style>\n'
                content = content.replace('</head>', style_block + '</head>')
                
        if content != original_content:
            with open(filepath, 'w') as f:
                f.write(content)
            print("Updated", filepath)

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            process_file(os.path.join(root, f))
