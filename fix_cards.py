content = open('build.py').read()

# Fix the _card() function on subpages to link to affiliate site
old = '''        def _card(pk, arrow="Shop Now \u2192"):
            pd = PAGES[pk]
            return f\'<a class="cat-card" href="{pd["file"]}">'''

new = '''        def _card(pk, arrow="Shop Now \u2192"):
            pd = PAGES[pk]
            return f\'<a class="cat-card" href="{aff(pd[\'cat_key\'])}" target="_blank" rel="nofollow noopener">'''

if old in content:
    open('build.py', 'w').write(content.replace(old, new))
    print('DONE - run python3 build.py and push')
else:
    print('Pattern not found')
