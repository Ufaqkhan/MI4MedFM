import re

with open('index.html', 'r') as f:
    html = f.read()

replacements = [
    # Meta description
    ('MI4MedFM is a proposed MICCAI 2026 workshop', 'MI4MedFM is a MICCAI 2026 workshop'),
    # Header CTA
    ('<a class="btn btn-ghost header-cta" href="proposal.pdf" target="_blank" rel="noopener">Proposal PDF</a>', ''),
    # Hero Title
    ('<span class="pill pill-hero">MICCAI 2026 Workshop Proposal</span>', '<span class="pill pill-hero">MICCAI 2026 Workshop</span>'),
    # Hero subtitle
    ('MI4MedFM is a proposed half-day, in-person workshop', 'MI4MedFM is a half-day, in-person workshop'),
    # Hero action
    ('<a class="btn btn-secondary" href="#program">View proposed program</a>', '<a class="btn btn-secondary" href="#program">View program</a>'),
    # Open artifacts
    ('<p>Planned notebooks, baselines, and a curated list of open problems and datasets.</p>', '<p>Open-source notebooks, baselines, and a curated list of open problems and datasets.</p>'),
    # Proceedings plan
    ('<h4>Proceedings plan</h4>\n              <p>Optional LNCS proceedings track plus a non-archival extended-abstract track via OpenReview-based workflow.</p>', '<h4>Proceedings</h4>\n              <p>LNCS proceedings track plus a non-archival extended-abstract track via OpenReview-based workflow.</p>'),
    # Program kicker
    ('<h2>Proposed half-day experience</h2>', '<h2>Half-day experience</h2>'),
    # Keynotes
    ('<span class="section-kicker">Proposed keynote</span>', '<span class="section-kicker">Keynote</span>'),
    ('<h2>Planned invited speaker options</h2>\n          <p>The proposal aims to invite either Karim Lekadir or Vineeth N. Balasubramanian for the keynote session.</p>', '<h2>Invited Speakers</h2>\n          <p>We are honored to have the following distinguished keynote speakers for the session.</p>'),
    ('<span class="speaker-badge">Planned keynote candidate</span>', '<span class="speaker-badge">Keynote Speaker</span>'),
    # Submission & review
    ('<h2>Two-track submission plan with rigorous peer review</h2>\n          <p>The workshop proposes an OpenReview-based, double-blind review process with clearly differentiated tracks for original work and non-archival contributions.</p>', '<h2>Two-track submission with rigorous peer review</h2>\n          <p>The workshop uses an OpenReview-based, double-blind review process with clearly differentiated tracks for original work and non-archival contributions.</p>'),
    ('<h3>How submissions are planned to be evaluated</h3>', '<h3>How submissions are evaluated</h3>'),
    ('<p>All accepted works are planned to appear as posters, with a subset selected for oral presentation based on review quality and topic balance.</p>', '<p>All accepted works will appear as posters, with a subset selected for oral presentation based on review quality and topic balance.</p>'),
    # Footer
    ('<p>Mechanistic Interpretability for Medical Foundation Models - proposed workshop at MICCAI 2026.</p>', '<p>Mechanistic Interpretability for Medical Foundation Models - Workshop at MICCAI 2026.</p>'),
    ('<span>OpenReview-based workflow planned</span>', '<span>OpenReview-based workflow</span>'),
]

for target, replacement in replacements:
    html = html.replace(target, replacement)

# Removing entire blocks
# Stat strip
html = re.sub(r'<div class="stat-strip">.*?</div>\n\n          <div class="keyword-row"', r'<div class="keyword-row"', html, flags=re.DOTALL)

# Status band
html = re.sub(r'<section class="status-band reveal">.*?</section>\n\n    <section class="section" id="overview">', r'<section class="section" id="overview">', html, flags=re.DOTALL)

# On-site feasibility
html = re.sub(r'<article>\n              <h4>On-site feasibility</h4>.*?<p>Multiple organizers are based in Abu Dhabi/UAE, supporting local execution and regional outreach.</p>\n            </article>\n          </div>\n        </aside>', r'</div>\n        </aside>', html, flags=re.DOTALL)

# CTA section
html = re.sub(r'<section class="section cta-section">.*?</section>\n  </main>', r'</main>', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
