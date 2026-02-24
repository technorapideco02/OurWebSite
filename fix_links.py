import os
import re

base_dir = '/Users/sudeepmondal/Desktop/trwebnew'
whatsapp_href = 'https://wa.me/917001545612'

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Schedule a Call - replace #contact with /#contact and portfolio/ with /portfolio/
            # For Schedule a Call, make sure it points to /#contact
            content = re.sub(r'<a[^>]*href=["\'](?:#contact|/#contact)["\'][^>]*>\s*Schedule a Call', lambda m: m.group(0).replace('href="#contact"', 'href="/#contact"'), content)
            
            # Find any button that says Schedule a Call and change to an anchor linking to /#contact
            # It's an issue if it's already an <a>, we handle <button
            content = re.sub(r'<button([^>]*)>(\s*Schedule a Call\s*(?:<[^>]+>[^<]*</[^>]+>\s*)?)</button>', r'<button\1 onclick="window.location.href=\'/#contact\'">\2</button>', content)
            
            # 2. Case Studies - make sure href is /portfolio/ instead of portfolio/ or portfolio.html
            content = re.sub(r'href=["\'](portfolio/?|\./portfolio/?|\.\./portfolio/?)["\']([^>]*>\s*Case Studies)', r'href="/portfolio/"\2', content)
            
            # 3. Whatsapp - ensure any link with wa.me or text Whatsapp points to the unified whatsapp_href.
            # actually user said "if any page have : whatsapp : then it must folloow same function as : the navbar : whatsapp now button."
            # That might mean we need to make sure ALL buttons/links that say "Whatsapp Now" or contain Whatsapp use the right href AND target="_blank"
            content = re.sub(r'href=["\'](?:https://wa\.me/[^"\']+)["\']', f'href="{whatsapp_href}"', content)
            
            if content != original_content:
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated {filepath}")
