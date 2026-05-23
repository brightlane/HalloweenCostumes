content = open('build.py').read()

# Remove the topbar marquee (saves ~60px)
old1 = '''<div class="topbar">
  <span class="marquee">
    🎃 HalloweenCostumes 2026 &nbsp;·&nbsp; 🌍 Ships to {SHIP_COUNTRIES} Countries &nbsp;·&nbsp;
    👩 Women\'s &nbsp;·&nbsp; 👨 Men\'s &nbsp;·&nbsp; 👧 Girls\' &nbsp;·&nbsp; 👦 Boys\' &nbsp;·&nbsp;
    💀 Scary &nbsp;·&nbsp; 😂 Funny &nbsp;·&nbsp; 💋 Sexy &nbsp;·&nbsp; 💑 Couples &nbsp;·&nbsp;
    🍼 Toddler &nbsp;·&nbsp; 👼 Baby &nbsp;·&nbsp; 🐾 Pets &nbsp;·&nbsp; 🎩 Accessories &nbsp;·&nbsp;
    🏚️ Decorations &nbsp;·&nbsp; 💰 Sale &nbsp;·&nbsp; ⚡ Last Minute &nbsp;·&nbsp; ✨ New 2026
  </span>
</div>'''
new1 = ''
content = content.replace(old1, new1)

# Remove breadcrumb on subpages
old2 = '{breadcrumb_html}'
new2 = ''
content = content.replace(old2, new2)

# Remove search bar
old3 = '''<div class="search-wrap" role="search">
  <div class="search-inner">
    <input id="q" class="search-input" type="search"
      placeholder=\'Search 10,000+ costumes — e.g. "Mandalorian", "Wednesday Addams", "witch"…\'
      autocomplete="off" aria-label="Search Halloween costumes">
    <button id="search-btn" class="search-btn">🔍 Find Costume</button>
  </div>
</div>'''
new3 = ''
content = content.replace(old3, new3)

# Make hero padding much tighter
old4 = '.hero{padding:70px 40px 50px;'
new4 = '.hero{padding:20px 40px 20px;'
content = content.replace(old4, new4)

# Make nav-cats one line, smaller
old5 = '.nav-cats{background:#151310;border-top:1px solid rgba(245,166,35,.1);padding:8px 40px;display:flex;gap:4px;flex-wrap:wrap;overflow-x:auto}'
new5 = '.nav-cats{background:#151310;border-top:1px solid rgba(245,166,35,.1);padding:4px 40px;display:flex;gap:4px;flex-wrap:nowrap;overflow-x:auto;white-space:nowrap}'
content = content.replace(old5, new5)

# Shrink trust strip
old6 = '.trust-strip{background:#110f0b;border-top:1px solid rgba(245,166,35,.08);border-bottom:1px solid rgba(245,166,35,.08);padding:16px 40px}'
new6 = '.trust-strip{background:#110f0b;border-top:1px solid rgba(245,166,35,.08);border-bottom:1px solid rgba(245,166,35,.08);padding:6px 40px}'
content = content.replace(old6, new6)

# Make hero h1 smaller so it fits
old7 = '.hero h1{font-family:\'Bebas Neue\',cursive;font-size:clamp(3.5rem,7vw,6.5rem);'
new7 = '.hero h1{font-family:\'Bebas Neue\',cursive;font-size:clamp(2.2rem,5vw,4rem);'
content = content.replace(old7, new7)

# Shrink hero desc
old8 = '.hero-desc{font-size:1.05rem;color:var(--dim);line-height:1.75;max-width:520px;margin-bottom:32px}'
new8 = '.hero-desc{font-size:.9rem;color:var(--dim);line-height:1.5;max-width:520px;margin-bottom:16px}'
content = content.replace(old8, new8)

# Shrink hero buttons margin
old9 = '.hero-btns{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:24px}'
new9 = '.hero-btns{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:12px}'
content = content.replace(old9, new9)

open('build.py', 'w').write(content)
print('DONE - run python3 build.py and push')
