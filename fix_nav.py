content = open('build.py').read()

# Hide the nav-cats mega menu completely - move it below the fold
old = '''.nav-cats{background:#151310;border-top:1px solid rgba(245,166,35,.1);padding:8px 40px;display:flex;gap:4px;flex-wrap:wrap;overflow-x:auto}'''
new = '''.nav-cats{display:none}'''
content = content.replace(old, new)

# Hide topbar marquee
old2 = '''.topbar{background:var(--amber);color:var(--ink);font-weight:700;font-size:.78rem;letter-spacing:2px;text-transform:uppercase;text-align:center;padding:10px 16px;overflow:hidden;white-space:nowrap}'''
new2 = '''.topbar{display:none}'''
content = content.replace(old2, new2)

# Hide breadcrumb
old3 = '''.breadcrumb{max-width:1200px;margin:0 auto;padding:10px 40px;font-size:.78rem;color:var(--faint)}'''
new3 = '''.breadcrumb{display:none}'''
content = content.replace(old3, new3)

# Hide search bar
old4 = '''.search-wrap{background:var(--smoke);border-bottom:1px solid rgba(245,166,35,.12);padding:14px 40px}'''
new4 = '''.search-wrap{display:none}'''
content = content.replace(old4, new4)

# Tighten hero padding
old5 = '.hero{padding:70px 40px 50px;'
new5 = '.hero{padding:24px 40px 24px;'
content = content.replace(old5, new5)

open('build.py', 'w').write(content)
print('DONE - run python3 build.py and push')
