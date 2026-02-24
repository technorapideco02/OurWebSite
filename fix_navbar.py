import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content

    # 1. Inject or replace Google font for Playfair Display + Great Vibes
    font_link = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Great+Vibes&display=swap" rel="stylesheet">'
    
    # Remove any existing playfair/great vibes links that might be incorrect
    content = re.sub(r'<link[^>]*family=Playfair\+Display[^>]*>\s*', '', content)
    
    # Insert the correct font link after the tailwindcss script or other fonts
    if font_link not in content:
        content = content.replace('<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>', 
                                  '<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>\n    ' + font_link)

    # 2. Inject @font-face blocks inside <style type="text/tailwindcss">
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
    # Check if @font-face for Gafiya exists
    if "@font-face" not in content and "font-family: 'Gafiya';" not in content:
        # We need to insert it
        if '<style type="text/tailwindcss">' in content:
            content = content.replace('<style type="text/tailwindcss">', '<style type="text/tailwindcss">' + font_face_css)
        else:
            style_block = f'<style type="text/tailwindcss">{font_face_css}</style>\n'
            content = content.replace('</head>', style_block + '</head>')


    # 3. Synchronize WhatsApp button classes
    whatsapp_cls_home = 'class="hidden sm:flex items-center gap-2 bg-primary text-white px-6 py-2.5 rounded-full font-bold text-sm hover:bg-primary/90 transition-all shadow-lg shadow-primary/20 hover:shadow-primary/40 hover:-translate-y-0.5"'
    content = re.sub(r'class="hidden sm:flex items-center gap-2 bg-primary text-white px-6 py-2\.5 rounded-(lg|full)[^>]*Whatsapp Now', whatsapp_cls_home + '>\n                    <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">\n                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.488-1.761-1.663-2.059-.175-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" /></svg>\n                    Whatsapp Now', content, flags=re.DOTALL)


    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

