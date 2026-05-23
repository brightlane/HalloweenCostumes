content = open('build.py').read()

# Fix homepage inline cards
content = content.replace(
    '<div class="cat-arrow">Shop Now →</div></a>\'',
    '<div class="cat-arrow">Shop Now →</div></a>\''
)

# Fix all cat-card hrefs to open affiliate link in new tab
old1 = 'f\'<a class="cat-card" href="{PAGES[pk]["file"]}">'
new1 = 'f\'<a class="cat-card" href="{aff(PAGES[pk][\'cat_key\'])}" target="_blank" rel="nofollow noopener">'
content = content.replace(old1, new1)

# Fix subpage _card() function
old2 = '''        def _card(pk, arrow="Shop Now \u2192"):
            pd = PAGES[pk]
            return f\'<a class="cat-card" href="{pd["file"]}">'''
new2 = '''        def _card(pk, arrow="Shop Now \u2192"):
            pd = PAGES[pk]
            return f\'<a class="cat-card" href="{aff(pd[\'cat_key\'])}" target="_blank" rel="nofollow noopener">'''
content = content.replace(old2, new2)

open('build.py', 'w').write(content)
print('DONE - run python3 build.py and push')
