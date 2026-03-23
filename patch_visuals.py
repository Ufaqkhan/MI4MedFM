import re

## 1. Fix CSS naming and sizes in styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.node {', '.hero-node {')
css = css.replace('.node-icon', '.hero-node-icon')

# Reduce sizes slightly to avoid overflow
# .hero-node
css = re.sub(r'\.hero-node\s*\{.*?(?=\})\}',
""".hero-node {
  width: 120px;
  min-height: 120px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.96);
  border: 1px solid rgba(15, 23, 42, 0.08);
  box-shadow: 0 14px 30px rgba(15, 23, 42, 0.06);
  display: grid;
  place-items: center;
  padding: 1rem;
  text-align: center;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--muted-strong);
}""", css, flags=re.DOTALL)

# .hero-node-icon
css = re.sub(r'\.hero-node-icon\s*\{.*?(?=\})\}',
""".hero-node-icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  margin-bottom: 0.6rem;
  position: relative;
  overflow: hidden;
}""", css, flags=re.DOTALL)

# .model-shell
css = re.sub(r'\.model-shell\s*\{.*?(?=\})\}',
""".model-shell {
  width: 165px;
  min-height: 190px;
  padding: 1.4rem 1.1rem;
  border-radius: 26px;
  background: linear-gradient(160deg, #142341, #0f172a);
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.22);
}""", css, flags=re.DOTALL)

# .lens
css = re.sub(r'\.lens\s*\{.*?(?=\})\}',
""".lens {
  position: absolute;
  right: -1.2rem;
  top: -1.2rem;
  width: 85px;
  height: 85px;
}""", css, flags=re.DOTALL)

# .lens-ring
css = re.sub(r'\.lens-ring\s*\{.*?(?=\})\}',
""".lens-ring {
  width: 60px;
  height: 60px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.88);
  border: 4px solid var(--accent);
  box-shadow: 0 14px 28px rgba(15, 23, 42, 0.16);
}""", css, flags=re.DOTALL)

# teaser-scene grid gap
css = re.sub(r'\.teaser-scene\s*\{.*?(?=\})\}', 
""".teaser-scene {
  display: grid;
  grid-template-columns: auto minmax(60px, 1fr) auto minmax(60px, 1fr) auto;
  align-items: center;
  gap: 0.8rem;
  padding: 2rem 0.5rem 2.5rem;
}""", css, flags=re.DOTALL)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)


## 2. Fix HTML naming and replace icon with image
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# rename the top nodes
html = html.replace('class="node input-node"', 'class="hero-node input-node"')
html = html.replace('class="node output-node"', 'class="hero-node output-node"')
html = html.replace('node-icon', 'hero-node-icon')

# Replace the medical image square with an actual IMG tag
html = re.sub(r'<div class="hero-node-icon hero-node-icon-image"></div>', '<img src="assets/images/sample-scan.png" class="hero-node-icon" alt="Medical Scan" style="object-fit: cover;" />', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
