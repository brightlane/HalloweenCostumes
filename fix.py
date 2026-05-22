content = open('build.py').read()

old = '''    else:
        related = [k for k in PAGES if k not in ("index", page_key)][:4]
        related_cards = "".join([
            f\'<a class="cat-card" href="{PAGES[pk]["file"]}"><span class="cat-icon">{PAGES[pk]["icon"]}</span><div class="cat-name">{PAGES[pk]["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{PAGES[pk]["en_h1sub"]}</div><div class="cat-arrow">Shop →</div></a>\'
            for pk in related
        ])
        categories_html = f"""
<section class="section">
  <div class="sec-header"><h2 class="sec-title">Featured Categories</h2><a href="index.html" class="sec-link">All Categories →</a></div>
  <div class="cat-grid-4">{related_cards}</div>
</section>"""'''

new = '''    else:
        _g = ["womens","mens","girls","boys","kids","tween","teen","toddler","baby","sizeguide"]
        _t = ["adult","scary","funny","sexy","couples","group","new2026","plussize","wholesale","pet","licensed","inflatable","medieval","videogame","themes","comiccon","kpop","horror","decades","occupation","fantasy"]
        _e = ["sustainable","celebrity","officecostume","witchaesthetic","musicartist","adaptive","creepydoll","occult","gothic","larp","renfaire","carnival","racer","friendscostume","cosplaywigs","plusSizeCosplay","horrornight","skeletons","spiderwebs","tombstones","candy","trunkortreat","gnomes","nightmarebc","hocuspocus","budget","clearance","bestsellers","animals","dragon","glowinthedark","makeup","trickortreat","hauntedhouse","pumpkin","lighting","princess","mermaid","food","cheerleader","cowgirl","steampunk","masquerade","animatronics","props","indoordecor","outdoordecor","collectibles","accessories","wigs","masks","decorations","partysupplies","diy","anime","gamer","gifts","movies","tvshows","clothing","genshin","leagueoflegends","overwatch","finalfantasy","jujutsukaisen","hazbinhotel","onepiececosplay","nier","cyberpunk","zelda","devilmaycry","morphsuits","piggyback","digital","fullbody","cosplayshoes","convention","lolita","swimwear","kawaii","casualwear","halloweenfashion","halloweenpajamas","matchingfamily","halloweensweaters","halloweendresses","weeklydeals","preorder","yearround","sale","lastminute"]
        def _card(pk, arrow="Shop Now \u2192"):
            pd = PAGES[pk]
            return f\'<a class="cat-card" href="{pd["file"]}"><span class="cat-icon">{pd["icon"]}</span><div class="cat-name">{pd["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{pd["en_h1sub"]}</div><div class="cat-arrow">{arrow}</div></a>\'
        gender_cards  = "".join([_card(pk) for pk in _g if pk != page_key and pk in PAGES])
        type_cards    = "".join([_card(pk) for pk in _t if pk != page_key and pk in PAGES])
        extra_cards   = "".join([_card(pk) for pk in _e if pk != page_key and pk in PAGES])
        categories_html = f"""
<section class="section">
  <div class="sec-header"><h2 class="sec-title">Shop by Gender & Age</h2><a href="index.html" class="sec-link">\u2190 Back to Home</a></div>
  <div class="cat-grid-5">{gender_cards}</div>
</section>
<section class="section" style="padding-top:0">
  <div class="sec-header"><h2 class="sec-title">Shop by Style</h2><a href="{aff(\'home\')}" class="sec-link" target="_blank" rel="nofollow noopener">All Styles \u2192</a></div>
  <div class="cat-grid-5">{type_cards}</div>
</section>
<section class="section" style="padding-top:0">
  <div class="sec-header"><h2 class="sec-title">Accessories, Decor & Deals</h2><a href="{aff(\'home\')}" class="sec-link" target="_blank" rel="nofollow noopener">Shop All \u2192</a></div>
  <div class="cat-grid-3">{extra_cards}</div>
</section>"""'''

if old in content:
    open('build.py', 'w').write(content.replace(old, new))
    print('DONE - run python3 build.py and push to GitHub')
else:
    print('Pattern not found')
