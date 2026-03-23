with open('index.html', 'r') as f:
    html = f.read()

with open('teaser.html', 'r') as f:
    teaser_html = f.read()

# Insert the css link
if 'teaser.css' not in html:
    html = html.replace('<link rel="stylesheet" href="styles.css" />', '<link rel="stylesheet" href="styles.css" />\n  <link rel="stylesheet" href="teaser.css" />')

# Find the hero-visual and insert teaser_html BEFORE analysis-shell
# Or replace analysis-shell. Let's replace it to make it cleaner.
import re
# Replace the analysis-shell block
html = re.sub(r'<div class="analysis-shell">.*?(?=\s*</div>\s*</div>\s*</section>)', teaser_html, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
