import re

# --- INDEX.HTML FIXES ---
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the CTA ready to publish section
text = re.sub(r'<section class="section cta-section">.*?</section>\n  </main>', '</main>', text, flags=re.DOTALL)

# Re-inject 3D interactive section if not present
html_to_inject = """
    <section class="section interactive-section">
      <div class="container interactive-container reveal">
        <div class="interactive-header">
          <h2>Interactive 3D Layer Analysis</h2>
          <p>Hover over the foundation model representation below to expand the hidden layers and inspect the mechanistic computations driving clinical predictions.</p>
        </div>
        <div class="model-showcase">
          <div class="layer layer-3">
            <div class="layer-label">Final Output & Concepts</div>
            <div class="layer-node-grid">
              <div class="node"></div><div class="node"></div><div class="node"></div>
              <div class="node"></div><div class="node"></div><div class="node"></div>
              <div class="node"></div><div class="node"></div><div class="node"></div>
            </div>
          </div>
          <div class="layer layer-2">
            <div class="layer-label">Sparse Autoencoder Features</div>
            <div class="layer-node-grid">
              <div class="node"></div><div class="node"></div><div class="node"></div>
              <div class="node"></div><div class="node"></div><div class="node"></div>
              <div class="node"></div><div class="node"></div><div class="node"></div>
            </div>
            <div class="connection-beam" style="bottom: 100%; left: 30%;"></div>
            <div class="connection-beam" style="bottom: 100%; right: 30%;"></div>
          </div>
          <div class="layer layer-1">
            <div class="layer-label">Early Attention Heads</div>
            <div class="layer-node-grid">
              <div class="node"></div><div class="node"></div><div class="node"></div>
              <div class="node"></div><div class="node"></div><div class="node"></div>
              <div class="node"></div><div class="node"></div><div class="node"></div>
            </div>
            <div class="connection-beam" style="bottom: 100%; left: 50%;"></div>
          </div>
        </div>
        <div class="interactive-tooltip">
           <i>🔍</i> Hover over the network to reveal layers
        </div>
      </div>
    </section>
"""

if 'Interactive 3D Layer Analysis' not in text:
    text = text.replace('    <section class="section muted-section" id="topics">', html_to_inject + '\n    <section class="section muted-section" id="topics">')

if 'interactive.css' not in text:
    text = text.replace('<link rel="stylesheet" href="styles.css" />', '<link rel="stylesheet" href="styles.css" />\n  <link rel="stylesheet" href="interactive.css" />')

# Fix meta templates again
text = re.sub(r'<section class="section miccai-section" id="miccai">.*?</section>\n\n    <section class="section" id="pillars">', 
              r'<section class="section" id="pillars">', text, flags=re.DOTALL)
text = text.replace('<h2>Four core pillars explain what attendees will actually get</h2>', '<h2>Four core pillars of MI4MedFM</h2>')
text = text.replace('<p>\n            The workshop is presented through a small number of concrete pillars so visitors quickly understand the scientific value without reading the full proposal.\n          </p>',
                    '<p>\n            Our scientific agenda is structured around four interlocking goals that translate mechanistic interpretability into robust clinical practice.\n          </p>')
text = text.replace('<h2>Representative directions in scope</h2>', '<h2>Topics of Interest</h2>')
text = text.replace('<p>\n            The content is trimmed to the main themes visitors need to understand quickly, while still reflecting the workshop’s technical depth.\n          </p>',
                    '<p>\n            We welcome submissions across a wide range of themes bridging foundation model interpretability with safety and deployment.\n          </p>')
text = text.replace('<h2>A compact half-day workshop with clear flow</h2>', '<h2>Workshop Program</h2>')
text = text.replace('<p>\n            The structure is designed to feel energetic and discussion-driven: keynote depth, paper exposure, poster interaction, and focused closing synthesis.\n          </p>',
                    '<p>\n            The half-day schedule features an invited keynote, oral presentations, dynamic poster sessions, and community discussions.\n          </p>')
text = text.replace('<h2>Invited speaker</h2>', '<h2>Keynote Speaker</h2>')
text = text.replace('<p>A centered single-speaker layout keeps the section balanced and visually clean.</p>',
                    '<p>We are honored to feature leading experts in trustworthy and transparent clinical AI.</p>')
text = text.replace('The speaker section is kept concise and visually weighted toward credibility, expertise, and fit with the workshop’s focus on robustness, fairness, uncertainty, and clinical reliability.',
                    'His pioneering research bridges deep learning robustness with ethical clinical translation, establishing critical benchmarks for fairness and certainty in medical deployments.')
text = text.replace('<h2>Faculty and researcher team with strong UAE presence</h2>', '<h2>Organizing Committee</h2>')
text = text.replace('<p>\n            The organizer presentation is simplified for the website: a strong faculty base plus early-career researchers, with local MICCAI relevance clearly visible.\n          </p>',
                    '<p>\n            Our international committee unites expertise in medical image analysis, foundation models, and trustworthy artificial intelligence.\n          </p>')
text = text.replace('<h2>Clear, concise submission and review overview</h2>', '<h2>Call for Papers</h2>')
text = text.replace('<p>\n            The website keeps only the details visitors need quickly: contribution types, review standards, and what accepted authors can expect.\n          </p>',
                    '<p>\n            We invite submissions across two tracks. All accepted papers will be presented, with top-tier submissions selected for oral presentation.\n          </p>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)


# --- STYLES.CSS FIXES ---
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The user has:
# .teaser-scene {
#   display: grid;
#   grid-template-columns: auto minmax(70px, 1fr) auto minmax(70px, 1fr) auto;
#   align-items: center;
#   gap: 0.9rem;
#   padding: 2rem 0.3rem 1.8rem;
# }
css = re.sub(r'\.teaser-scene\s*\{.*?(?=\})\}', 
""".teaser-scene {
  display: grid;
  grid-template-columns: auto minmax(80px, 1fr) auto minmax(80px, 1fr) auto;
  align-items: center;
  gap: 2.2rem;
  padding: 3rem 1rem 3.5rem;
}""", css, flags=re.DOTALL)

# .node { width: 112px; min-height: 112px; ... padding: 1rem; ... font-size: 0.84rem; ... }
css = re.sub(r'\.node\s*\{.*?(?=\})\}',
""".node {
  width: 148px;
  min-height: 148px;
  border-radius: 28px;
  background: rgba(255, 255, 255, 0.96);
  border: 1px solid rgba(15, 23, 42, 0.08);
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.06);
  display: grid;
  place-items: center;
  padding: 1.3rem;
  text-align: center;
  font-size: 1rem;
  font-weight: 700;
  color: var(--muted-strong);
}""", css, flags=re.DOTALL)

# .node-icon { width: 34px; height: 34px; ... }
css = re.sub(r'\.node-icon\s*\{.*?(?=\})\}',
""".node-icon {
  width: 50px;
  height: 50px;
  border-radius: 14px;
  margin-bottom: 0.8rem;
  position: relative;
}""", css, flags=re.DOTALL)

# .model-shell { width: 150px; min-height: 176px; padding: 1.2rem 1rem; ... }
css = re.sub(r'\.model-shell\s*\{.*?(?=\})\}',
""".model-shell {
  width: 210px;
  min-height: 250px;
  padding: 1.8rem 1.4rem;
  border-radius: 32px;
  background: linear-gradient(160deg, #142341, #0f172a);
  box-shadow: 0 24px 50px rgba(15, 23, 42, 0.25);
}""", css, flags=re.DOTALL)

# .model-head { ... }
css = re.sub(r'\.model-head\s*\{.*?(?=\})\}',
""".model-head {
  text-align: center;
  color: #fff;
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 1.6rem;
}""", css, flags=re.DOTALL)

# .model-layer { height: 10px; ... margin: 0.5rem 0; ... }
css = re.sub(r'\.model-layer\s*\{.*?(?=\})\}',
""".model-layer {
  height: 14px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.18);
  margin: 0.9rem 0;
}""", css, flags=re.DOTALL)

# .lens { right: -0.8rem; top: -0.6rem; width: 78px; height: 78px; ... }
css = re.sub(r'\.lens\s*\{.*?(?=\})\}',
""".lens {
  position: absolute;
  right: -1.5rem;
  top: -1.5rem;
  width: 100px;
  height: 100px;
}""", css, flags=re.DOTALL)

# .lens-ring { width: 52px; height: 52px; border: 3px solid ... }
css = re.sub(r'\.lens-ring\s*\{.*?(?=\})\}',
""".lens-ring {
  width: 68px;
  height: 68px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.88);
  border: 4px solid var(--accent);
  box-shadow: 0 16px 32px rgba(15, 23, 42, 0.16);
}""", css, flags=re.DOTALL)

# .lens-handle { width: 26px; height: 7px; right: 8px; bottom: 8px; ... }
css = re.sub(r'\.lens-handle\s*\{.*?(?=\})\}',
""".lens-handle {
  position: absolute;
  width: 38px;
  height: 9px;
  border-radius: 999px;
  background: var(--accent);
  right: 6px;
  bottom: 6px;
  transform: rotate(45deg);
  transform-origin: left center;
}""", css, flags=re.DOTALL)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

