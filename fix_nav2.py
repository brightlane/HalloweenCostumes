content = open('build.py').read()

# Remove the entire nav-cats div from the HTML template
old = '''  <div class="nav-cats">
    <a href="index.html" class="nav-cat-link {\'active\' if page_key==\'index\' else \'\'}">🎃 All</a>
    {nav_links}
  </div>'''
new = ''
content = content.replace(old, new)

# Remove topbar
old2 = '''<div class="topbar">
  <span class="marquee">
    🎃 HalloweenCostumes 2026 &nbsp;·&nbsp; 🌍 Ships to {SHIP_COUNTRIES} Countries &nbsp;·&nbsp;
    👩 Women\'s &nbsp;·&nbsp; 👨 Men\'s &nbsp;·&nbsp; 👧 Girls\' &nbsp;·&nbsp; 👦 Boys\' &nbsp;·&nbsp;
    💀 Scary &nbsp;·&nbsp; 😂 Funny &nbsp;·&nbsp; 💋 Sexy &nbsp;·&nbsp; 💑 Couples &nbsp;·&nbsp;
    🍼 Toddler &nbsp;·&nbsp; 👼 Baby &nbsp;·&nbsp; 🐾 Pets &nbsp;·&nbsp; 🎩 Accessories &nbsp;·&nbsp;
    🏚️ Decorations &nbsp;·&nbsp; 💰 Sale &nbsp;·&nbsp; ⚡ Last Minute &nbsp;·&nbsp; ✨ New 2026
  </span>
</div>

<nav>'''
new2 = '<nav>'
content = content.replace(old2, new2)

# Remove breadcrumb
old3 = '\n{breadcrumb_html}\n'
new3 = '\n'
content = content.replace(old3, new3)

# Remove search bar
old4 = '''<div class="search-wrap" role="search">
  <div class="search-inner">
    <input id="q" class="search-input" type="search"
      placeholder=\'Search 10,000+ costumes — e.g. "Mandalorian", "Wednesday Addams", "witch"…\'
      autocomplete="off" aria-label="Search Halloween costumes">
    <button id="search-btn" class="search-btn">🔍 Find Costume</button>
  </div>
</div>

<main>'''
new4 = '<main>'
content = content.replace(old4, new4)

# Tighten hero
content = content.replace('.hero{padding:70px 40px 50px;', '.hero{padding:20px 40px 20px;')

open('build.py', 'w').write(content)
print('DONE - run python3 build.py and push')
