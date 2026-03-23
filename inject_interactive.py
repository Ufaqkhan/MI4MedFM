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
           Hover over the network to reveal layers
        </div>
      </div>
    </section>
"""

with open('index.html', 'r') as f:
    text = f.read()

# insert css link
if 'interactive.css' not in text:
    text = text.replace('<link rel="stylesheet" href="teaser.css" />', '<link rel="stylesheet" href="teaser.css" />\n  <link rel="stylesheet" href="interactive.css" />')

# insert section before topics
if 'Interactive 3D Layer Analysis' not in text:
    text = text.replace('    <section class="section muted-section" id="topics">', html_to_inject + '\n    <section class="section muted-section" id="topics">')

with open('index.html', 'w') as f:
    f.write(text)
