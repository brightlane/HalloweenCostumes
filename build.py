#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════
  HALLOWEENCOSTUMES 2026 — ULTIMATE SITE GENERATOR
  by Benny "Palmo Kid" Palmarino | LinkConnector ID 7949

  Run:  python3 build.py

  Generates 25+ pages covering EVERY category on
  halloweencostumes.com — plus categories they DON'T have.
  Goal: #1 Halloween affiliate site in the world.

  Pages generated:
    index.html          Homepage
    --- BY GENDER ---
    womens.html         Women's Costumes
    mens.html           Men's Costumes
    girls.html          Girls' Costumes
    boys.html           Boys' Costumes
    --- BY AGE ---
    kids.html           Kids Costumes
    teen.html           Teen Costumes
    toddler.html        Toddler Costumes
    baby.html           Baby Costumes
    --- BY TYPE ---
    adult.html          Adult Costumes
    scary.html          Scary Costumes
    funny.html          Funny Costumes
    sexy.html           Sexy Costumes
    couples.html        Couples Costumes
    group.html          Group & Family Costumes
    new2026.html        New 2026 Costumes
    --- BY SPECIAL ---
    plussize.html       Plus Size Costumes
    wholesale.html      Wholesale Costumes
    pet.html            Pet Costumes
    --- ACCESSORIES ---
    accessories.html    Accessories (wigs, masks, props)
    wigs.html           Halloween Wigs
    masks.html          Halloween Masks
    --- BEYOND COSTUMES ---
    decorations.html    Halloween Decorations
    sale.html           Sale & Cheap Costumes
    lastminute.html     Last Minute Costumes
    --- SUPPORT ---
    404.html            Custom Error Page
    sitemap.xml
    robots.txt
    llms.txt
═══════════════════════════════════════════════════════════
"""

import os
import json
from datetime import date
from urllib.parse import quote

# ─────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────
SITE_URL      = "https://brightlane.github.io/HalloweenCostumes"
AFF_BASE      = "https://www.linkconnector.com/ta.php?lc=007949060109004909&atid=WebWidge"
OWNER         = 'Benny "Palmo Kid" Palmarino'
LC_ID         = "7949"
TODAY         = date.today().isoformat()
OUTPUT_DIR    = "."
GOOGLE_VERIFY = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"
SHIP_COUNTRIES = "200+"

# ─────────────────────────────────────────────────────────
# AFFILIATE LINK BUILDER
# ─────────────────────────────────────────────────────────
CAT_URLS = {
    "home":        "https://www.halloweencostumes.com/",
    "womens":      "https://www.halloweencostumes.com/womens-halloween-costumes.html",
    "mens":        "https://www.halloweencostumes.com/mens-halloween-costumes.html",
    "girls":       "https://www.halloweencostumes.com/girls-halloween-costumes.html",
    "boys":        "https://www.halloweencostumes.com/boys-halloween-costumes.html",
    "kids":        "https://www.halloweencostumes.com/kids-halloween-costumes.html",
    "teen":        "https://www.halloweencostumes.com/teen-halloween-costumes.html",
    "toddler":     "https://www.halloweencostumes.com/toddler-halloween-costumes.html",
    "baby":        "https://www.halloweencostumes.com/baby-halloween-costumes.html",
    "adult":       "https://www.halloweencostumes.com/adult-halloween-costumes.html",
    "scary":       "https://www.halloweencostumes.com/scary-halloween-costumes.html",
    "funny":       "https://www.halloweencostumes.com/funny-halloween-costumes.html",
    "sexy":        "https://www.halloweencostumes.com/sexy-halloween-costumes.html",
    "couples":     "https://www.halloweencostumes.com/couples-halloween-costumes.html",
    "group":       "https://www.halloweencostumes.com/group-halloween-costumes.html",
    "new2026":     "https://www.halloweencostumes.com/new-halloween-costumes.html",
    "plussize":    "https://www.halloweencostumes.com/plus-size-halloween-costumes.html",
    "wholesale":   "https://www.halloweencostumes.com/wholesale-halloween-costumes.html",
    "pet":         "https://www.halloweencostumes.com/pet-halloween-costumes.html",
    "accessories": "https://www.halloweencostumes.com/halloween-costume-accessories.html",
    "wigs":        "https://www.halloweencostumes.com/halloween-wigs.html",
    "masks":       "https://www.halloweencostumes.com/halloween-masks.html",
    "decorations": "https://www.halloweencostumes.com/halloween-decorations.html",
    "sale":        "https://www.halloweencostumes.com/sale-halloween-costumes.html",
    "lastminute":  "https://www.halloweencostumes.com/last-minute-halloween-costumes.html",
    # ── New pages beating Spirit Halloween ──
    "animatronics": "https://www.halloweencostumes.com/halloween-animatronics.html",
    "props":        "https://www.halloweencostumes.com/halloween-props.html",
    "indoordecor":  "https://www.halloweencostumes.com/indoor-halloween-decorations.html",
    "outdoordecor": "https://www.halloweencostumes.com/outdoor-halloween-decorations.html",
    "licensed":     "https://www.halloweencostumes.com/officially-licensed-halloween-costumes.html",
    "inflatable":   "https://www.halloweencostumes.com/inflatable-halloween-costumes.html",
    "collectibles": "https://www.halloweencostumes.com/halloween-collectibles.html",
    "tween":        "https://www.halloweencostumes.com/tween-halloween-costumes.html",
    "medieval":     "https://www.halloweencostumes.com/renaissance-medieval-costumes.html",
    # ── Costumes.com beaters ──
    "videogame":    "https://www.halloweencostumes.com/video-game-costumes.html",
    "themes":       "https://www.halloweencostumes.com/halloween-costume-themes.html",
    "comiccon":     "https://www.halloweencostumes.com/superhero-costumes.html",
    "sizeguide":    "https://www.halloweencostumes.com/size-charts.html",
    "couples2":     "https://www.halloweencostumes.com/couples-halloween-costumes.html",
    "celebrations": "https://www.halloweencostumes.com/",
    # ── Party City beaters ──
    "addamsfamily":  "https://www.halloweencostumes.com/search?q=addams+family+costume",
    "beetlejuice":   "https://www.halloweencostumes.com/search?q=beetlejuice+costume",
    "horror":        "https://www.halloweencostumes.com/scary-halloween-costumes.html",
    "fnaf":          "https://www.halloweencostumes.com/search?q=five+nights+at+freddys+costume",
    "scooby":        "https://www.halloweencostumes.com/search?q=scooby+doo+costume",
    "harrypotter":   "https://www.halloweencostumes.com/search?q=harry+potter+costume",
    "decades":       "https://www.halloweencostumes.com/search?q=decade+costumes",
    "occupation":    "https://www.halloweencostumes.com/search?q=occupation+career+costumes",
    "fantasy":       "https://www.halloweencostumes.com/search?q=fantasy+fairy+angel+costume",
    "partysupplies": "https://www.halloweencostumes.com/halloween-decorations.html",
    "diy":           "https://www.halloweencostumes.com/halloween-costume-accessories.html",
    "kpop":          "https://www.halloweencostumes.com/search?q=kpop+costume",
    # ── Fun.com year-round beaters ──
    "anime":      "https://www.halloweencostumes.com/search?q=anime+costume",
    "gamer":      "https://www.halloweencostumes.com/search?q=gamer+gaming+costume",
    "gifts":      "https://www.halloweencostumes.com/",
    "movies":     "https://www.halloweencostumes.com/search?q=movie+character+costume",
    "tvshows":    "https://www.halloweencostumes.com/search?q=tv+show+costume",
    "clothing":   "https://www.halloweencostumes.com/halloween-costume-accessories.html",
    "yearround":  "https://www.halloweencostumes.com/",
    # ── EZCosplay beaters — specific game titles ──
    "genshin":       "https://www.halloweencostumes.com/search?q=genshin+impact+costume",
    "leagueoflegends":"https://www.halloweencostumes.com/search?q=league+of+legends+costume",
    "overwatch":     "https://www.halloweencostumes.com/search?q=overwatch+costume",
    "finalfantasy":  "https://www.halloweencostumes.com/search?q=final+fantasy+costume",
    "deadbydaylight":"https://www.halloweencostumes.com/search?q=dead+by+daylight+costume",
    # ── Specific anime titles ──
    "jujutsukaisen": "https://www.halloweencostumes.com/search?q=jujutsu+kaisen+costume",
    "hazbinhotel":   "https://www.halloweencostumes.com/search?q=hazbin+hotel+costume",
    "frieren":       "https://www.halloweencostumes.com/search?q=frieren+costume",
    "onepiececosplay":"https://www.halloweencostumes.com/search?q=one+piece+costume",
    # ── Cosplay specialist pages ──
    "cosplayshoes":  "https://www.halloweencostumes.com/search?q=costume+shoes+boots",
    "convention":    "https://www.halloweencostumes.com/search?q=convention+cosplay+costume",
    "lolita":        "https://www.halloweencostumes.com/search?q=lolita+costume",
    # ── Miccostumes beaters ──
    "swimwear":      "https://www.halloweencostumes.com/search?q=costume+swimsuit",
    "kawaii":        "https://www.halloweencostumes.com/search?q=kawaii+costume",
    "casualwear":    "https://www.halloweencostumes.com/search?q=anime+casual+wear+costume",
    "nier":          "https://www.halloweencostumes.com/search?q=nier+automata+costume",
    "cyberpunk":     "https://www.halloweencostumes.com/search?q=cyberpunk+costume",
    "zelda":         "https://www.halloweencostumes.com/search?q=legend+of+zelda+costume",
    "devilmaycry":   "https://www.halloweencostumes.com/search?q=devil+may+cry+costume",
    "weeklydeals":   "https://www.halloweencostumes.com/sale-halloween-costumes.html",
    "preorder":      "https://www.halloweencostumes.com/new-halloween-costumes.html",
}

def aff(cat_key=None, search=None):
    if cat_key and cat_key in CAT_URLS:
        dest = CAT_URLS[cat_key]
    elif search:
        dest = f"https://www.halloweencostumes.com/search?q={search.replace(' ','+')}"
    else:
        return AFF_BASE
    return f"{AFF_BASE}&url={quote(dest, safe='')}"

# ─────────────────────────────────────────────────────────
# PAGES DEFINITION
# ─────────────────────────────────────────────────────────
PAGES = {
    # ── HOMEPAGE ──
    "index": {
        "file":"index.html","cat_key":"home","icon":"🎃",
        "group":"main","nav_group":"shop",
        "en_title":"Halloween Costumes 2026 | #1 Store Worldwide",
        "en_desc":"Halloween costumes 2026 — the world's best deals. Kids, adults, scary, funny, sexy, couples, group, wholesale, pet, accessories and decorations. Ships to 200+ countries.",
        "en_h1":"Halloween Costumes 2026",
        "en_h1sub":"The World's #1 Halloween Store",
        "en_body":"Welcome to the world's #1 Halloween costume destination for 2026. We feature the largest selection of Halloween costumes on the internet — thousands of styles for kids, adults, teens, toddlers, babies, couples, groups, and pets. From cheap Halloween costumes under $10 to premium exclusive designs, our selection beats every other Halloween store online. Updated daily with new arrivals, sales, and exclusive deals. Ships to 200+ countries worldwide.",
        "schema_type":"WebSite",
        "keywords":"halloween costumes 2026, best halloween costumes, halloween costume store",
    },
    # ── BY GENDER ──
    "womens": {
        "file":"womens.html","cat_key":"womens","icon":"👩",
        "group":"gender","nav_group":"gender",
        "en_title":"Women's Halloween Costumes 2026 | Best Deals",
        "en_desc":"Women's Halloween costumes 2026 — hundreds of styles for women. Classic, scary, funny, sexy and plus size. Ships to 200+ countries.",
        "en_h1":"Women's Halloween Costumes 2026",
        "en_h1sub":"Hundreds of Styles for Women",
        "en_body":"Find the perfect women's Halloween costume 2026 from hundreds of styles. Our women's costume collection covers every theme — classic horror, pop culture icons, funny food costumes, sexy Halloween looks, renaissance and historical costumes, and more. Available in standard and plus sizes, with new styles added daily. Whether you want to be a witch, vampire, superhero, or pop culture queen — we have the best women's Halloween costumes at unbeatable prices.",
        "schema_type":"CollectionPage",
        "keywords":"womens halloween costumes, women halloween costumes 2026, ladies halloween costumes",
    },
    "mens": {
        "file":"mens.html","cat_key":"mens","icon":"👨",
        "group":"gender","nav_group":"gender",
        "en_title":"Men's Halloween Costumes 2026 | Best Deals",
        "en_desc":"Men's Halloween costumes 2026 — hundreds of styles for men. Scary, funny, classic and pop culture. Ships to 200+ countries.",
        "en_h1":"Men's Halloween Costumes 2026",
        "en_h1sub":"Scary, Funny & Classic Styles for Men",
        "en_body":"Shop the best men's Halloween costumes 2026. Our men's costume collection includes classic monsters, superheroes, movie villains, funny characters, historical figures, and pop culture icons. Available in all sizes including big and tall. Whether you want a terrifying scary costume or a hilarious outfit that wins the costume contest — our men's Halloween costumes have you covered. New styles added daily with unbeatable prices.",
        "schema_type":"CollectionPage",
        "keywords":"mens halloween costumes, men halloween costumes 2026, male halloween costumes",
    },
    "girls": {
        "file":"girls.html","cat_key":"girls","icon":"👧",
        "group":"gender","nav_group":"gender",
        "en_title":"Girls' Halloween Costumes 2026 | Best Deals for Girls",
        "en_desc":"Girls' Halloween costumes 2026 — princesses, witches, superheroes, animals and more. All sizes from toddler to teen. Ships to 200+ countries.",
        "en_h1":"Girls' Halloween Costumes 2026",
        "en_h1sub":"Princesses, Witches, Superheroes & More",
        "en_body":"Find the perfect girls' Halloween costume 2026 — from princess gowns to superhero suits, witch costumes, animal costumes, and pop culture characters. Our girls' costume collection covers all ages and sizes from infant to teen. Every girl deserves an amazing Halloween costume, and our selection offers the widest variety at the best prices anywhere online. New girls' costumes added daily for 2026.",
        "schema_type":"CollectionPage",
        "keywords":"girls halloween costumes, halloween costumes for girls 2026, girl costumes",
    },
    "boys": {
        "file":"boys.html","cat_key":"boys","icon":"👦",
        "group":"gender","nav_group":"gender",
        "en_title":"Boys' Halloween Costumes 2026 | Best Deals for Boys",
        "en_desc":"Boys' Halloween costumes 2026 — superheroes, monsters, ninjas, pirates and more. All sizes from toddler to teen. Ships to 200+ countries.",
        "en_h1":"Boys' Halloween Costumes 2026",
        "en_h1sub":"Superheroes, Monsters, Ninjas & Pirates",
        "en_body":"Shop the coolest boys' Halloween costumes 2026 — superheroes, scary monsters, ninjas, pirates, dinosaurs, Star Wars characters, video game icons and more. Our boys' costume collection covers all ages and sizes from infant to teen. Whether your boy wants to be a terrifying zombie or his favorite movie hero — we have the best boys' Halloween costumes at prices every parent loves.",
        "schema_type":"CollectionPage",
        "keywords":"boys halloween costumes, halloween costumes for boys 2026, boy costumes",
    },
    # ── BY AGE ──
    "kids": {
        "file":"kids.html","cat_key":"kids","icon":"👶",
        "group":"age","nav_group":"age",
        "en_title":"Kids Halloween Costumes 2026 | Best Deals for Children",
        "en_desc":"Kids Halloween costumes 2026 — superheroes, witches, animals, princesses and more. Sizes for all ages. Ships to 200+ countries.",
        "en_h1":"Kids Halloween Costumes 2026",
        "en_h1sub":"Superheroes, Witches, Animals & More",
        "en_body":"Find the best kids Halloween costumes 2026 for boys and girls of all ages. Our kids costume selection includes superheroes, witches, animals, princesses, scary monsters, funny characters and classic Halloween costumes. We carry kids sizes from toddler and infant all the way to teen, with prices starting from just $10. Perfect for trick-or-treating, school Halloween parties, and family events. All kids costumes ship worldwide with fast delivery.",
        "schema_type":"CollectionPage",
        "keywords":"kids halloween costumes, children halloween costumes 2026, halloween costumes for kids",
    },
    "teen": {
        "file":"teen.html","cat_key":"teen","icon":"🧑",
        "group":"age","nav_group":"age",
        "en_title":"Teen Halloween Costumes 2026 | Cool Costumes for Teenagers",
        "en_desc":"Teen Halloween costumes 2026 — cool, scary and funny costumes for teenagers. Pop culture, horror and trendy styles. Ships to 200+ countries.",
        "en_h1":"Teen Halloween Costumes 2026",
        "en_h1sub":"Cool, Scary & Trendy Costumes for Teens",
        "en_body":"Find the coolest teen Halloween costumes 2026 — styles that teenagers actually want to wear. Our teen costume collection includes the latest pop culture characters, trendy horror looks, funny meme-worthy outfits, and classic Halloween styles updated for 2026. Teen sizes available for both girls and boys. Stand out at the Halloween party with a teen costume that's cool enough to impress your friends.",
        "schema_type":"CollectionPage",
        "keywords":"teen halloween costumes, teenager halloween costumes 2026, halloween costumes for teens",
    },
    "toddler": {
        "file":"toddler.html","cat_key":"toddler","icon":"🍼",
        "group":"age","nav_group":"age",
        "en_title":"Toddler Halloween Costumes 2026 | Adorable Kids Costumes",
        "en_desc":"Toddler Halloween costumes 2026 — adorable and comfortable costumes for toddlers ages 1-4. Animals, superheroes, princesses and more.",
        "en_h1":"Toddler Halloween Costumes 2026",
        "en_h1sub":"Adorable Costumes for Little Ones Ages 1-4",
        "en_body":"Dress your toddler in the cutest Halloween costume 2026 — adorable animal costumes, tiny superhero suits, little witch outfits, and classic Halloween characters scaled down for the littlest trick-or-treaters. Our toddler costumes are designed to be comfortable, easy to put on, and sized perfectly for ages 1-4. Safe materials, vibrant colors, and styles so cute you'll want to photograph every moment. Toddler Halloween costumes from just $10.",
        "schema_type":"CollectionPage",
        "keywords":"toddler halloween costumes, halloween costumes for toddlers 2026, toddler costumes",
    },
    "baby": {
        "file":"baby.html","cat_key":"baby","icon":"👼",
        "group":"age","nav_group":"age",
        "en_title":"Baby Halloween Costumes 2026 | Cutest Infant Costumes",
        "en_desc":"Baby Halloween costumes 2026 — the cutest infant and newborn Halloween costumes. Comfortable, safe and adorable. Ships to 200+ countries.",
        "en_h1":"Baby Halloween Costumes 2026",
        "en_h1sub":"The Cutest Infant & Newborn Halloween Costumes",
        "en_body":"Make your baby's first Halloween unforgettable with our adorable baby Halloween costumes 2026. From tiny pumpkin suits to mini superhero capes, cute animal onesies and classic Halloween characters — our baby costume collection is designed for maximum cuteness and comfort. Safe, soft materials suitable for newborns and infants up to 24 months. These baby Halloween costumes are perfect for trick-or-treating, family photos and Halloween parties.",
        "schema_type":"CollectionPage",
        "keywords":"baby halloween costumes, infant halloween costumes 2026, newborn halloween costumes",
    },
    # ── BY TYPE ──
    "adult": {
        "file":"adult.html","cat_key":"adult","icon":"🎭",
        "group":"type","nav_group":"type",
        "en_title":"Adult Halloween Costumes 2026 | Best Deals for Men & Women",
        "en_desc":"Adult Halloween costumes 2026 — classic horror, pop culture, funny, scary and couples costumes. All sizes. Ships to 200+ countries.",
        "en_h1":"Adult Halloween Costumes 2026",
        "en_h1sub":"Classic Horror, Pop Culture & Original Designs",
        "en_body":"Discover the best adult Halloween costumes 2026 for men and women. Our adult costume collection includes classic horror characters, pop culture icons, funny costumes, scary monsters, couples costumes, and original designs. Available in all sizes from XS to plus size, with styles ranging from traditional Halloween to movie-inspired looks. Perfect for Halloween parties, haunted houses, and costume contests. All adult Halloween costumes ship worldwide.",
        "schema_type":"CollectionPage",
        "keywords":"adult halloween costumes, halloween costumes for adults 2026, adult costumes",
    },
    "scary": {
        "file":"scary.html","cat_key":"scary","icon":"💀",
        "group":"type","nav_group":"type",
        "en_title":"Scary Halloween Costumes 2026 | Horror & Monster Costumes",
        "en_desc":"Scary Halloween costumes 2026 — terrifying monsters, zombies, vampires, clowns and haunted house looks. Ships to 200+ countries.",
        "en_h1":"Scary Halloween Costumes 2026",
        "en_h1sub":"Monsters, Zombies & Haunted House Looks",
        "en_body":"Shop the scariest Halloween costumes 2026 — guaranteed to terrify. Our scary costume collection includes classic horror monsters, zombies, vampires, werewolves, scary clowns, mummies, skeletons, demons and haunted house characters. Perfect for Halloween parties, haunted attractions, and anyone who wants to make a truly frightening impression. Scary Halloween costumes available in all sizes for kids, adults and plus size. Ships worldwide.",
        "schema_type":"CollectionPage",
        "keywords":"scary halloween costumes, horror halloween costumes 2026, terrifying costumes",
    },
    "funny": {
        "file":"funny.html","cat_key":"funny","icon":"😂",
        "group":"type","nav_group":"type",
        "en_title":"Funny Halloween Costumes 2026 | Hilarious Costume Ideas",
        "en_desc":"Funny Halloween costumes 2026 — hilarious outfits for adults, kids and groups. Win every costume contest. Ships to 200+ countries.",
        "en_h1":"Funny Halloween Costumes 2026",
        "en_h1sub":"Hilarious Outfits That Win Every Contest",
        "en_body":"Find the funniest Halloween costumes 2026 that are guaranteed to make everyone laugh. Our funny costume collection includes hilarious food costumes, pop culture parodies, punny outfits, inflatable costumes, and novelty character looks. Perfect for Halloween parties, office costume contests, and anyone who prefers laughs over scares. Funny Halloween costumes available for adults, kids, couples, and groups. Ships worldwide.",
        "schema_type":"CollectionPage",
        "keywords":"funny halloween costumes, hilarious halloween costumes 2026, humorous costumes",
    },
    "sexy": {
        "file":"sexy.html","cat_key":"sexy","icon":"💋",
        "group":"type","nav_group":"type",
        "en_title":"Sexy Halloween Costumes 2026 | Best Adult Costume Deals",
        "en_desc":"Sexy Halloween costumes 2026 — stylish and alluring adult costume styles for women and men. All sizes. Ships to 200+ countries.",
        "en_h1":"Sexy Halloween Costumes 2026",
        "en_h1sub":"Stylish & Alluring Adult Halloween Styles",
        "en_body":"Find the best sexy Halloween costumes 2026 — stylish, alluring and perfectly crafted adult costume looks for Halloween parties. Our sexy costume collection includes sultry takes on classic Halloween characters, glamorous villain costumes, and chic party-ready looks for women and men. Available in all sizes with quality materials that look stunning. These sexy Halloween costumes are designed for adults who want to turn heads at every Halloween event.",
        "schema_type":"CollectionPage",
        "keywords":"sexy halloween costumes, sexy costumes 2026, adult sexy halloween costumes",
    },
    "couples": {
        "file":"couples.html","cat_key":"couples","icon":"💑",
        "group":"type","nav_group":"type",
        "en_title":"Couples Halloween Costumes 2026 | Matching Costume Sets",
        "en_desc":"Couples Halloween costumes 2026 — matching costume sets for two. Classic duos, funny pairs, scary couples and pop culture sets. Ships to 200+ countries.",
        "en_h1":"Couples Halloween Costumes 2026",
        "en_h1sub":"Matching Sets for the Perfect Duo",
        "en_body":"Make Halloween twice as fun with our couples Halloween costumes 2026. We have the best matching costume sets for two — from classic duos like Bonnie & Clyde to funny food pairs, scary horror couples, pop culture icons, and Disney character sets. Our couples costumes are designed to complement each other perfectly, with coordinated styles for him and her. Perfect for Halloween parties, date nights, and every couples costume contest.",
        "schema_type":"CollectionPage",
        "keywords":"couples halloween costumes, matching halloween costumes 2026, couples costumes",
    },
    "group": {
        "file":"group.html","cat_key":"group","icon":"👨‍👩‍👧‍👦",
        "group":"type","nav_group":"type",
        "en_title":"Group Halloween Costumes 2026 | Family & Matching Sets",
        "en_desc":"Group Halloween costumes 2026 — matching sets for families, friends, couples and office parties. Ships to 200+ countries.",
        "en_h1":"Group Halloween Costumes 2026",
        "en_h1sub":"Matching Sets for Families, Friends & Offices",
        "en_body":"Coordinate your Halloween look with our group and family Halloween costumes 2026. We have matching costume sets for couples, families, friend groups, and office parties. Browse themed group sets from TV shows, movies, fairy tales, and classic Halloween themes. Whether you need costumes for 2 people or 20, we have complete group sets that ship together. Family Halloween costumes available in kids and adult sizes. Ships worldwide.",
        "schema_type":"CollectionPage",
        "keywords":"group halloween costumes, family halloween costumes 2026, matching group costumes",
    },
    "new2026": {
        "file":"new2026.html","cat_key":"new2026","icon":"✨",
        "group":"type","nav_group":"type",
        "en_title":"New Halloween Costumes 2026 | Latest Arrivals",
        "en_desc":"New Halloween costumes 2026 — the latest arrivals and trending costume styles for this year. Updated daily. Ships to 200+ countries.",
        "en_h1":"New Halloween Costumes 2026",
        "en_h1sub":"The Latest Arrivals & Trending Styles",
        "en_body":"Be the first to wear the newest Halloween costumes 2026. Our new arrivals section is updated daily with the freshest costume styles, trending pop culture looks, exclusive designs, and the costumes everyone will be talking about this Halloween season. From the latest movie and TV character costumes to original exclusive designs — find what's new and trending in Halloween costumes for 2026. New styles added every single day.",
        "schema_type":"CollectionPage",
        "keywords":"new halloween costumes 2026, new costumes 2026, latest halloween costumes",
    },
    # ── SPECIAL ──
    "plussize": {
        "file":"plussize.html","cat_key":"plussize","icon":"💎",
        "group":"special","nav_group":"special",
        "en_title":"Plus Size Halloween Costumes 2026 | All Sizes Available",
        "en_desc":"Plus size Halloween costumes 2026 — inclusive styles in all sizes for adults. Scary, funny, sexy, classic and group costumes. Ships to 200+ countries.",
        "en_h1":"Plus Size Halloween Costumes 2026",
        "en_h1sub":"Every Costume in Every Size — Inclusive & Stylish",
        "en_body":"Find the perfect plus size Halloween costume 2026 in styles that flatter and impress. Our plus size costume collection includes scary, funny, classic, sexy, pop culture, and group costumes — all available in extended sizes. We believe everyone deserves an amazing Halloween costume, which is why our plus size selection includes the same quality styles and themes as our standard sizes. Plus size Halloween costumes for adults available in 1X through 5X. Ships to 200+ countries.",
        "schema_type":"CollectionPage",
        "keywords":"plus size halloween costumes, plus size costumes 2026, halloween costumes for plus size",
    },
    "wholesale": {
        "file":"wholesale.html","cat_key":"wholesale","icon":"🛍️",
        "group":"special","nav_group":"special",
        "en_title":"Wholesale Halloween Costumes 2026 | Bulk Orders",
        "en_desc":"Wholesale Halloween costumes 2026 — bulk orders for schools, events, retailers and haunted attractions. Best prices. Ships to 200+ countries.",
        "en_h1":"Wholesale Halloween Costumes 2026",
        "en_h1sub":"Bulk Orders for Events, Schools & Retailers",
        "en_body":"Order wholesale Halloween costumes 2026 in bulk for events, schools, haunted attractions, retail stores, and large group parties. Our wholesale costume selection offers the best prices on bulk orders of kids costumes, adult costumes, accessories, and complete costume sets. Perfect for Halloween retailers, event planners, school fundraisers, haunted houses, and corporate events. Wholesale Halloween costumes ship to 200+ countries with quantity discounts.",
        "schema_type":"CollectionPage",
        "keywords":"wholesale halloween costumes, bulk halloween costumes 2026, halloween costumes wholesale",
    },
    "pet": {
        "file":"pet.html","cat_key":"pet","icon":"🐾",
        "group":"special","nav_group":"special",
        "en_title":"Pet Halloween Costumes 2026 | Dog & Cat Costumes",
        "en_desc":"Pet Halloween costumes 2026 — adorable dog and cat costumes for Halloween. All pet sizes. Ships to 200+ countries.",
        "en_h1":"Pet Halloween Costumes 2026",
        "en_h1sub":"Adorable Costumes for Dogs & Cats",
        "en_body":"Dress up your furry friend with our pet Halloween costumes 2026. We have adorable dog costumes and cat costumes for every Halloween theme — superheroes, hot dogs, sharks, pumpkins, witches, and more. Our pet costume collection includes sizes for small dogs, medium dogs, large dogs, and cats. Easy to put on, comfortable for pets, and perfect for Halloween photos, pet parades and trick-or-treating. Pet Halloween costumes ship to 200+ countries.",
        "schema_type":"CollectionPage",
        "keywords":"pet halloween costumes, dog halloween costumes 2026, cat halloween costumes",
    },
    # ── ACCESSORIES ──
    "accessories": {
        "file":"accessories.html","cat_key":"accessories","icon":"🎩",
        "group":"accessories","nav_group":"accessories",
        "en_title":"Halloween Costume Accessories 2026 | Wigs, Masks & Props",
        "en_desc":"Halloween costume accessories 2026 — wigs, masks, props, makeup, hats and more. Complete your costume look. Ships to 200+ countries.",
        "en_h1":"Halloween Costume Accessories 2026",
        "en_h1sub":"Wigs, Masks, Props & Everything In Between",
        "en_body":"Complete your Halloween look with our massive selection of Halloween costume accessories 2026. We carry wigs, masks, hats, props, makeup kits, costume boots, gloves, capes, and every accessory you need to take your costume to the next level. Whether you need a finishing touch for your DIY costume or want to upgrade a store-bought look — our Halloween accessories collection has everything. New accessories added daily with the best prices online.",
        "schema_type":"CollectionPage",
        "keywords":"halloween costume accessories, halloween accessories 2026, costume accessories",
    },
    "wigs": {
        "file":"wigs.html","cat_key":"wigs","icon":"💇",
        "group":"accessories","nav_group":"accessories",
        "en_title":"Halloween Wigs 2026 | Costume Wigs for All Characters",
        "en_desc":"Halloween wigs 2026 — character wigs, costume wigs, colored wigs and style wigs for every Halloween character. Ships to 200+ countries.",
        "en_h1":"Halloween Wigs 2026",
        "en_h1sub":"Character Wigs for Every Halloween Look",
        "en_body":"Transform your Halloween look instantly with our Halloween wigs 2026. We carry the largest selection of costume wigs online — from long flowing witch wigs to wild clown wigs, sleek villain styles, colorful fantasy wigs, and natural-looking character wigs. Our Halloween wig collection covers every character and style imaginable, with options for men, women, and kids. High quality, comfortable, and styled to perfection. Halloween wigs from just $10.",
        "schema_type":"CollectionPage",
        "keywords":"halloween wigs, costume wigs 2026, halloween costume wigs",
    },
    "masks": {
        "file":"masks.html","cat_key":"masks","icon":"👺",
        "group":"accessories","nav_group":"accessories",
        "en_title":"Halloween Masks 2026 | Scary & Character Masks",
        "en_desc":"Halloween masks 2026 — scary monster masks, character masks, full face masks and latex horror masks. Ships to 200+ countries.",
        "en_h1":"Halloween Masks 2026",
        "en_h1sub":"Scary Monster & Character Masks",
        "en_body":"Find the perfect Halloween mask 2026 to complete your costume or create a standalone terrifying look. Our Halloween mask collection includes classic horror monster masks, realistic latex scary masks, full-face character masks, funny novelty masks, and iconic villain masks. Whether you need a finishing touch for your costume or want a quick scary Halloween look — our masks are the answer. Halloween masks available for adults, teens, and kids.",
        "schema_type":"CollectionPage",
        "keywords":"halloween masks, scary halloween masks 2026, costume masks halloween",
    },
    # ── BEYOND COSTUMES ──
    "decorations": {
        "file":"decorations.html","cat_key":"decorations","icon":"🏚️",
        "group":"home","nav_group":"home",
        "en_title":"Halloween Decorations 2026 | Indoor & Outdoor Decor",
        "en_desc":"Halloween decorations 2026 — indoor and outdoor Halloween decor, yard decorations, props, lights and haunted house supplies. Ships to 200+ countries.",
        "en_h1":"Halloween Decorations 2026",
        "en_h1sub":"Indoor, Outdoor & Haunted House Decor",
        "en_body":"Transform your home into a haunted house with our Halloween decorations 2026. We carry the biggest selection of Halloween decor online — indoor decorations, outdoor yard decorations, hanging props, animatronics, fog machines, Halloween lights, window clings, and complete haunted house decoration sets. Whether you want a spooky yard display or an elegant indoor Halloween theme — our decoration collection has everything you need to make this Halloween unforgettable.",
        "schema_type":"CollectionPage",
        "keywords":"halloween decorations 2026, halloween decor, outdoor halloween decorations, halloween yard decorations",
    },
    "sale": {
        "file":"sale.html","cat_key":"sale","icon":"💰",
        "group":"home","nav_group":"deals",
        "en_title":"Halloween Costumes on Sale 2026 | Cheap Halloween Deals",
        "en_desc":"Halloween costumes on sale 2026 — cheap Halloween costumes, discounted deals and clearance costumes. Best prices online. Ships to 200+ countries.",
        "en_h1":"Halloween Costumes on Sale 2026",
        "en_h1sub":"Cheap Halloween Deals & Clearance Prices",
        "en_body":"Get the best Halloween costume deals 2026 with our sale section. We feature cheap Halloween costumes, discounted deals, clearance costumes, and the lowest prices on popular styles. From Halloween costumes under $10 to discounted premium looks — our sale section is updated daily with new markdowns. You don't have to spend a fortune to look amazing on Halloween. Find incredible cheap Halloween costumes for kids, adults, couples, and groups.",
        "schema_type":"CollectionPage",
        "keywords":"cheap halloween costumes, halloween costumes on sale 2026, discounted halloween costumes",
    },
    "lastminute": {
        "file":"lastminute.html","cat_key":"lastminute","icon":"⚡",
        "group":"home","nav_group":"deals",
        "en_title":"Last Minute Halloween Costumes 2026 | Fast Delivery",
        "en_desc":"Last minute Halloween costumes 2026 — fast delivery costumes for when Halloween is around the corner. Ships to 200+ countries.",
        "en_h1":"Last Minute Halloween Costumes 2026",
        "en_h1sub":"Fast Delivery When You Need It Most",
        "en_body":"Halloween is tomorrow and you still need a costume? No problem. Our last minute Halloween costume collection features styles with the fastest available shipping — including express and overnight delivery options. Simple, effective costumes that look great without weeks of planning. From quick DIY accessories to complete ready-to-wear costumes — our last minute Halloween selection saves the day every time. Order now for the fastest possible delivery.",
        "schema_type":"CollectionPage",
        "keywords":"last minute halloween costumes, fast halloween costumes 2026, quick halloween costumes",
    },
    # ══════════════════════════════════════════
    # SPIRIT HALLOWEEN BEATERS — 9 new pages
    # ══════════════════════════════════════════
    "animatronics": {
        "file":"animatronics.html","cat_key":"animatronics","icon":"🤖",
        "group":"spirit","nav_group":"spirit",
        "en_title":"Halloween Animatronics 2026 | Scary Moving Props & Figures",
        "en_desc":"Halloween animatronics 2026 — life-size moving props, scary figures, sound-activated animatronics and haunted house displays. Ships to 200+ countries.",
        "en_h1":"Halloween Animatronics 2026",
        "en_h1sub":"Life-Size Moving Props & Haunted House Figures",
        "en_body":"Transform your home into a haunted attraction with our Halloween animatronics 2026. We carry life-size moving animatronic figures, sound-activated props, light-up animatronics, and complete haunted house display pieces. From terrifying clown animatronics to zombie figures, skeleton props and ghost displays — our animatronic collection covers every horror theme. Perfect for haunted houses, Halloween parties, yard displays and retail stores. Halloween animatronics available in sizes from 1 foot to over 7 feet tall.",
        "schema_type":"CollectionPage",
        "keywords":"halloween animatronics 2026, animatronic halloween props, moving halloween figures, haunted house animatronics",
    },
    "props": {
        "file":"props.html","cat_key":"props","icon":"🦴",
        "group":"spirit","nav_group":"spirit",
        "en_title":"Halloween Props 2026 | Haunted House Props & Decorations",
        "en_desc":"Halloween props 2026 — skulls, skeletons, coffins, cauldrons, tombstones, fog machines and professional haunted house props. Ships to 200+ countries.",
        "en_h1":"Halloween Props 2026",
        "en_h1sub":"Skulls, Coffins, Fog Machines & Haunted House Supplies",
        "en_body":"Create the ultimate haunted house with our Halloween props 2026. We carry professional-grade and consumer haunted house props — skulls, skeleton displays, coffins, cauldrons, tombstones, fog machines, spooky lighting, cobwebs, and complete scene-setter kits. Whether you want a single statement piece or a full haunted attraction setup — our Halloween props collection has everything to make this the scariest Halloween yet. Props available for indoor and outdoor use.",
        "schema_type":"CollectionPage",
        "keywords":"halloween props 2026, haunted house props, halloween decorating props, fog machine halloween",
    },
    "indoordecor": {
        "file":"indoordecor.html","cat_key":"indoordecor","icon":"🕯️",
        "group":"spirit","nav_group":"spirit",
        "en_title":"Indoor Halloween Decorations 2026 | Home Decor",
        "en_desc":"Indoor Halloween decorations 2026 — tabletop decor, hanging props, window clings, string lights, cauldrons and spooky home decor. Ships to 200+ countries.",
        "en_h1":"Indoor Halloween Decorations 2026",
        "en_h1sub":"Tabletop, Hanging & Window Halloween Decor",
        "en_body":"Decorate every room with our indoor Halloween decorations 2026. Our indoor decor collection includes tabletop centerpieces, hanging decorations, window clings, string lights, cauldrons, candelabras, spooky mirrors, scene setters and wall decorations. Transform your living room, dining room, front door and every corner of your home into a haunted house with our massive indoor Halloween decoration selection. New indoor decor added daily.",
        "schema_type":"CollectionPage",
        "keywords":"indoor halloween decorations 2026, halloween home decor, halloween tabletop decorations, indoor halloween decor",
    },
    "outdoordecor": {
        "file":"outdoordecor.html","cat_key":"outdoordecor","icon":"🌙",
        "group":"spirit","nav_group":"spirit",
        "en_title":"Outdoor Halloween Decorations 2026 | Yard & Garden Decor",
        "en_desc":"Outdoor Halloween decorations 2026 — yard decorations, lawn stakes, inflatables, string lights, tombstones and outdoor haunted house displays. Ships to 200+ countries.",
        "en_h1":"Outdoor Halloween Decorations 2026",
        "en_h1sub":"Yard Stakes, Inflatables & Outdoor Haunted Displays",
        "en_body":"Make your yard the scariest on the street with our outdoor Halloween decorations 2026. We carry yard inflatables, lawn stakes, tombstones, skeleton displays, hanging ghosts, pathway lights, witch silhouettes, spider webs, and complete outdoor haunted house kits. Our outdoor Halloween decoration collection covers front porches, gardens, driveways and yards of every size. Durable weather-resistant materials built for outdoor use. New outdoor decor added daily.",
        "schema_type":"CollectionPage",
        "keywords":"outdoor halloween decorations 2026, halloween yard decorations, halloween lawn decor, outdoor halloween decor",
    },
    "licensed": {
        "file":"licensed.html","cat_key":"licensed","icon":"™️",
        "group":"spirit","nav_group":"spirit",
        "en_title":"Officially Licensed Halloween Costumes 2026 | Character Costumes",
        "en_desc":"Officially licensed Halloween costumes 2026 — authentic Spider-Man, Batman, Disney, Star Wars, Ghostbusters and 100s more licensed character costumes. Ships to 200+ countries.",
        "en_h1":"Licensed Halloween Costumes 2026",
        "en_h1sub":"Spider-Man, Disney, Star Wars & 100s More",
        "en_body":"Wear the real deal with our officially licensed Halloween costumes 2026. Our licensed costume collection features authentic, studio-approved costumes from the biggest franchises in entertainment — Marvel Spider-Man, Batman, Disney princesses, Star Wars characters, Ghostbusters, Terrifier, Trick r Treat, and hundreds more officially licensed designs. These are the real licensed costumes that look exactly like the characters from your favorite movies, TV shows and comics. Licensed costumes available for kids, teens, and adults.",
        "schema_type":"CollectionPage",
        "keywords":"officially licensed halloween costumes, licensed character costumes 2026, authentic halloween costumes, spider-man costume licensed",
    },
    "inflatable": {
        "file":"inflatable.html","cat_key":"inflatable","icon":"🎈",
        "group":"spirit","nav_group":"spirit",
        "en_title":"Inflatable Halloween Costumes 2026 | Funny Blow Up Costumes",
        "en_desc":"Inflatable Halloween costumes 2026 — hilarious blow-up costumes for adults and kids. T-Rex, dinosaur, sumo, unicorn and more. Ships to 200+ countries.",
        "en_h1":"Inflatable Halloween Costumes 2026",
        "en_h1sub":"Hilarious Blow-Up Costumes for Adults & Kids",
        "en_body":"Be the life of the Halloween party with our inflatable Halloween costumes 2026. Our blow-up costume collection features the funniest and most eye-catching inflatable styles — T-Rex dinosaur costumes, sumo wrestler suits, unicorn costumes, shark costumes, chicken suits and dozens more hilarious inflatable looks. These fan-powered inflatable costumes are easy to wear, instantly recognizable, and guaranteed to win every costume contest. Inflatable Halloween costumes available for adults and kids.",
        "schema_type":"CollectionPage",
        "keywords":"inflatable halloween costumes, blow up halloween costumes 2026, funny inflatable costumes, t-rex inflatable costume",
    },
    "collectibles": {
        "file":"collectibles.html","cat_key":"collectibles","icon":"🏆",
        "group":"spirit","nav_group":"spirit",
        "en_title":"Halloween Collectibles 2026 | Funko POPs, Figures & More",
        "en_desc":"Halloween collectibles 2026 — Funko POP figures, horror collectibles, Halloween statues, limited edition items and spooky memorabilia. Ships to 200+ countries.",
        "en_h1":"Halloween Collectibles 2026",
        "en_h1sub":"Funko POPs, Horror Figures & Limited Edition Items",
        "en_body":"Complete your Halloween collection with our Halloween collectibles 2026. We carry Funko POP Halloween figures, horror character statues, limited edition collectible items, Halloween memorabilia, spooky figurines, and exclusive collector pieces. Perfect for Halloween enthusiasts, horror fans, and collectors who want something beyond costumes. Our Halloween collectibles include items from iconic horror franchises, classic Halloween characters, and exclusive limited-run designs.",
        "schema_type":"CollectionPage",
        "keywords":"halloween collectibles 2026, funko pop halloween, horror collectibles, halloween figurines",
    },
    "tween": {
        "file":"tween.html","cat_key":"tween","icon":"🧒",
        "group":"gender","nav_group":"gender",
        "en_title":"Tween Halloween Costumes 2026 | Ages 8-12 Costumes",
        "en_desc":"Tween Halloween costumes 2026 — cool costumes for ages 8-12. Pop culture, scary, funny and trendy styles for tweens. Ships to 200+ countries.",
        "en_h1":"Tween Halloween Costumes 2026",
        "en_h1sub":"Cool Costumes for Ages 8-12",
        "en_body":"Find the perfect tween Halloween costume 2026 for ages 8-12 — the in-between age that wants to look cool, not babyish, but isn't quite ready for adult styles. Our tween costume collection includes the latest pop culture characters, age-appropriate scary looks, funny costumes, and trendy Halloween styles sized for tweens. We carry tween sizes that fit perfectly for ages 8-12, with styles for both girls and boys that they'll actually want to wear.",
        "schema_type":"CollectionPage",
        "keywords":"tween halloween costumes, halloween costumes ages 8-12, tween costumes 2026, halloween costumes tweens",
    },
    "medieval": {
        "file":"medieval.html","cat_key":"medieval","icon":"⚔️",
        "group":"type","nav_group":"type",
        "en_title":"Medieval & Renaissance Halloween Costumes 2026 | Knight & Princess",
        "en_desc":"Medieval and renaissance Halloween costumes 2026 — knights, princesses, wizards, jesters, Vikings and renaissance fair costumes. Ships to 200+ countries.",
        "en_h1":"Medieval Costumes 2026",
        "en_h1sub":"Knights, Princesses, Wizards & Renaissance Fair",
        "en_body":"Step back in time with our medieval and renaissance Halloween costumes 2026. Our collection includes authentic-looking knight armor costumes, princess gowns, wizard robes, jester suits, Viking warrior costumes, court jester outfits, and complete renaissance fair costumes for men, women, and kids. Perfect for Halloween parties, renaissance fairs, medieval events, and historical costume contests. New medieval and renaissance costume styles added regularly.",
        "schema_type":"CollectionPage",
        "keywords":"medieval halloween costumes, renaissance halloween costumes 2026, knight costume, princess medieval costume, renaissance fair costume",
    },
    # ══════════════════════════════════════════
    # COSTUMES.COM BEATERS — 4 new category pages
    # ══════════════════════════════════════════
    "videogame": {
        "file":"videogame.html","cat_key":"videogame","icon":"🎮",
        "group":"type","nav_group":"type",
        "en_title":"Video Game Halloween Costumes 2026 | Best Gaming Costumes",
        "en_desc":"Video game Halloween costumes 2026 — Mario, Zelda, Fortnite, Minecraft, FNAF, Mortal Kombat and hundreds more gaming costumes. Ships to 200+ countries.",
        "en_h1":"Video Game Costumes 2026",
        "en_h1sub":"Mario, Zelda, Fortnite, Minecraft & More",
        "en_body":"Level up your Halloween with our video game Halloween costumes 2026. We carry the largest selection of gaming costumes online — from classic Nintendo characters like Mario and Link, to modern hits like Fortnite, Minecraft, Five Nights at Freddy's, Mortal Kombat, Among Us, and dozens more. Video game costumes available for kids, teens, and adults in all sizes. Whether you're a casual gamer or hardcore enthusiast — find your favorite character and dominate the Halloween costume contest. New video game costume styles added daily.",
        "schema_type":"CollectionPage",
        "keywords":"video game halloween costumes, gaming costumes 2026, mario costume, zelda costume, fortnite costume, minecraft costume",
    },
    "themes": {
        "file":"themes.html","cat_key":"themes","icon":"🌟",
        "group":"type","nav_group":"type",
        "en_title":"Halloween Costume Themes 2026 | Horror, Sci-Fi, Fantasy & More",
        "en_desc":"Halloween costume themes 2026 — horror, sci-fi, fantasy, historical, decade themes and more. Find costumes by theme. Ships to 200+ countries.",
        "en_h1":"Halloween Costume Themes 2026",
        "en_h1sub":"Horror, Sci-Fi, Fantasy, Historical & Decade Themes",
        "en_body":"Find Halloween costumes by theme with our massive themed costume collection 2026. Browse by horror themes, sci-fi and space themes, fantasy and fairy tale themes, historical period themes, decade themes from the 50s to 90s, movie and TV show themes, and pop culture themes. Whether you need costumes for a themed Halloween party, decade night, or just want to coordinate with a group — our themed costume collection covers every concept imaginable. Themed costumes for kids, adults, and groups.",
        "schema_type":"CollectionPage",
        "keywords":"halloween costume themes 2026, themed halloween costumes, horror theme costumes, sci-fi halloween costumes, decade costumes",
    },
    "comiccon": {
        "file":"comiccon.html","cat_key":"comiccon","icon":"🦸",
        "group":"type","nav_group":"type",
        "en_title":"Comic Con & Convention Costumes 2026 | Cosplay Costumes",
        "en_desc":"Comic Con and convention costumes 2026 — cosplay costumes, superhero suits, anime costumes and convention-ready looks. Ships to 200+ countries.",
        "en_h1":"Comic Con & Cosplay Costumes 2026",
        "en_h1sub":"Superhero, Anime & Convention-Ready Looks",
        "en_body":"Get convention-ready with our Comic Con and cosplay costume collection 2026. We carry premium superhero costumes, anime character cosplay, video game character suits, movie and TV cosplay, and complete convention-ready costume sets for Comic Con, anime conventions, gaming events, and cosplay competitions. Our cosplay collection features both budget-friendly and premium deluxe options — from simple character accessories to full head-to-toe costume sets. Cosplay costumes for men, women, teens, and kids.",
        "schema_type":"CollectionPage",
        "keywords":"comic con costumes, cosplay costumes 2026, convention costumes, superhero cosplay, anime cosplay costumes",
    },
    "sizeguide": {
        "file":"sizeguide.html","cat_key":"sizeguide","icon":"📏",
        "group":"special","nav_group":"special",
        "en_title":"Halloween Costume Size Guide 2026 | Find Your Perfect Fit",
        "en_desc":"Halloween costume size guide 2026 — size charts for kids, adults, plus size and pet costumes. Find your perfect Halloween costume fit.",
        "en_h1":"Halloween Costume Size Guide",
        "en_h1sub":"Size Charts for Kids, Adults & Plus Size",
        "en_body":"Finding the right size Halloween costume is easy with our comprehensive size guide. We provide detailed size charts for kids costumes (infant through teen), adult costumes (XS through 5X), plus size costumes, and pet costumes. Our size guide includes chest, waist, hip and height measurements for every costume category — so you can order with confidence and get the perfect fit. Still unsure? Order between two sizes and our easy return policy has you covered. Size guides updated for all 2026 costume styles.",
        "schema_type":"WebPage",
        "keywords":"halloween costume size guide, halloween costume size chart, how to measure halloween costume, plus size halloween costume sizing",
    },
    # ══════════════════════════════════════════
    # PARTY CITY BEATERS — Franchise pages
    # ══════════════════════════════════════════
    "addamsfamily": {
        "file":"addamsfamily.html","cat_key":"addamsfamily","icon":"🖤",
        "group":"franchise","nav_group":"franchise",
        "en_title":"Addams Family Halloween Costumes 2026 | Wednesday, Morticia & More",
        "en_desc":"Addams Family Halloween costumes 2026 — Wednesday, Morticia, Gomez, Pugsley, Uncle Fester and Thing costumes for adults and kids. Ships to 200+ countries.",
        "en_h1":"Addams Family Costumes 2026",
        "en_h1sub":"Wednesday, Morticia, Gomez & The Whole Family",
        "en_body":"Dress as the world's creepiest family with our Addams Family Halloween costumes 2026. Whether you want to be the iconic Wednesday Addams, the glamorous Morticia, the debonair Gomez, or the lovable Uncle Fester — our Addams Family costume collection has every character for solo, couples, and group Halloween costumes. Perfect for family Halloween parties, costume contests, and fans of both the classic TV show and the hit Wednesday Netflix series. Available in kids, teen, and adult sizes.",
        "schema_type":"CollectionPage",
        "keywords":"addams family halloween costumes, wednesday addams costume, morticia addams costume, gomez addams costume, wednesday costume 2026",
    },
    "beetlejuice": {
        "file":"beetlejuice.html","cat_key":"beetlejuice","icon":"🐛",
        "group":"franchise","nav_group":"franchise",
        "en_title":"Beetlejuice Halloween Costumes 2026 | Beetlejuice, Lydia & More",
        "en_desc":"Beetlejuice Halloween costumes 2026 — Beetlejuice, Lydia Deetz, Astrid and Bob costumes from the classic film and Beetlejuice 2. Ships to 200+ countries.",
        "en_h1":"Beetlejuice Costumes 2026",
        "en_h1sub":"Beetlejuice, Lydia, Astrid & Bob",
        "en_body":"It's showtime! Shop our Beetlejuice Halloween costumes 2026 featuring the ghost with the most and his spooky friends. Our Beetlejuice collection includes classic black and white striped Beetlejuice suits, Lydia Deetz gothic looks, and characters from Beetlejuice Beetlejuice (2024). Perfect for couples costumes, group Halloween themes, and fans of Tim Burton's iconic franchise. Beetlejuice costumes available for adults, teens, and kids.",
        "schema_type":"CollectionPage",
        "keywords":"beetlejuice halloween costume, beetlejuice costume 2026, lydia deetz costume, beetlejuice beetlejuice costume",
    },
    "horror": {
        "file":"horror.html","cat_key":"horror","icon":"🔪",
        "group":"franchise","nav_group":"franchise",
        "en_title":"Horror Movie Halloween Costumes 2026 | Freddy, Jason, Pennywise & More",
        "en_desc":"Horror movie Halloween costumes 2026 — Freddy Krueger, Jason Voorhees, Pennywise, The Nun, Billy from Saw, Michael Myers and more. Ships to 200+ countries.",
        "en_h1":"Horror Movie Costumes 2026",
        "en_h1sub":"Freddy, Jason, Pennywise, The Nun & More",
        "en_body":"Become your favorite horror movie villain with our horror Halloween costumes 2026. Our horror movie costume collection features the most terrifying characters in cinema history — Freddy Krueger's iconic striped sweater, Jason Voorhees' hockey mask, Pennywise the Dancing Clown, The Nun from The Conjuring, Billy from Saw, Michael Myers, Leatherface, Ghostface from Scream, Art the Clown from Terrifier, and dozens more. Horror costumes available for adults and teens in all sizes.",
        "schema_type":"CollectionPage",
        "keywords":"horror movie halloween costumes, freddy krueger costume, jason voorhees costume, pennywise costume, the nun costume, michael myers costume 2026",
    },
    "fnaf": {
        "file":"fnaf.html","cat_key":"fnaf","icon":"🐻",
        "group":"franchise","nav_group":"franchise",
        "en_title":"Five Nights at Freddy's Costumes 2026 | FNAF Halloween Costumes",
        "en_desc":"Five Nights at Freddy's Halloween costumes 2026 — Freddy Fazbear, Foxy, Bonnie, Glamrock Freddy and more FNAF character costumes. Ships to 200+ countries.",
        "en_h1":"FNAF Costumes 2026",
        "en_h1sub":"Freddy Fazbear, Foxy, Bonnie & Glamrock Freddy",
        "en_body":"Survive the night in style with our Five Nights at Freddy's Halloween costumes 2026. Our FNAF costume collection features Freddy Fazbear, Foxy the Pirate, Bonnie, Chica, Glamrock Freddy from Security Breach, and other beloved characters from the iconic horror game franchise. FNAF costumes are among the most popular Halloween choices for kids, teens, and adult gaming fans. Available in masks, full suits, and accessory kits for every character.",
        "schema_type":"CollectionPage",
        "keywords":"five nights at freddys costume, fnaf halloween costume 2026, freddy fazbear costume, foxy costume, glamrock freddy costume",
    },
    "scooby": {
        "file":"scooby.html","cat_key":"scooby","icon":"🐕",
        "group":"franchise","nav_group":"franchise",
        "en_title":"Scooby-Doo Halloween Costumes 2026 | Scooby, Shaggy, Velma & More",
        "en_desc":"Scooby-Doo Halloween costumes 2026 — Scooby-Doo, Shaggy, Velma, Daphne and Fred costumes for groups, couples and solo. Ships to 200+ countries.",
        "en_h1":"Scooby-Doo Costumes 2026",
        "en_h1sub":"Scooby, Shaggy, Velma, Daphne & Fred",
        "en_body":"Solve some spooky mysteries in style with our Scooby-Doo Halloween costumes 2026. Our Mystery Machine crew collection is perfect for group Halloween costumes — dress the whole gang as Scooby-Doo, Shaggy, Velma, Daphne, and Fred for the most recognizable group costume at any Halloween party. Scooby-Doo costumes available for kids, teens, and adults in all sizes. Perfect for families, friend groups, and office Halloween parties.",
        "schema_type":"CollectionPage",
        "keywords":"scooby doo halloween costume, shaggy costume, velma costume, scooby doo group costume 2026",
    },
    "harrypotter": {
        "file":"harrypotter.html","cat_key":"harrypotter","icon":"⚡",
        "group":"franchise","nav_group":"franchise",
        "en_title":"Harry Potter Halloween Costumes 2026 | Hogwarts Character Costumes",
        "en_desc":"Harry Potter Halloween costumes 2026 — Harry, Hermione, Ron, Dumbledore, Voldemort and Hogwarts house robes. Ships to 200+ countries.",
        "en_h1":"Harry Potter Costumes 2026",
        "en_h1sub":"Harry, Hermione, Ron & All Hogwarts Houses",
        "en_body":"Enter the wizarding world with our Harry Potter Halloween costumes 2026. Our Hogwarts collection features Harry Potter, Hermione Granger, Ron Weasley, Dumbledore, Voldemort, Draco Malfoy, and Hogwarts house robes for Gryffindor, Slytherin, Ravenclaw, and Hufflepuff. Harry Potter costumes are perfect for solo looks, couples costumes, and complete Hogwarts group themes. Available for kids, teens, and adults with accessories including wands, scarves, and glasses.",
        "schema_type":"CollectionPage",
        "keywords":"harry potter halloween costume, hermione granger costume, hogwarts costume 2026, wizard halloween costume, dumbledore costume",
    },
    # ── Occasion/Theme pages (Party City angle) ──
    "decades": {
        "file":"decades.html","cat_key":"decades","icon":"📀",
        "group":"extra","nav_group":"extra",
        "en_title":"Decade Halloween Costumes 2026 | 50s 70s 80s 90s Costumes",
        "en_desc":"Decade Halloween costumes 2026 — 1950s, 1960s, 1970s, 1980s and 1990s themed costumes for adults and kids. Ships to 200+ countries.",
        "en_h1":"Decade Costumes 2026",
        "en_h1sub":"50s, 60s, 70s, 80s & 90s Themed Looks",
        "en_body":"Step back in time with our decade Halloween costumes 2026. Our collection covers every era — from 1950s sock hop costumes and 1960s mod looks to 1970s disco fever, 1980s neon pop stars, and 1990s grunge and hip-hop styles. Decade theme costumes are perfect for Halloween parties, decade nights, and group themes where everyone picks their favorite era. Decade costumes available for adults, teens, and kids with complete era-accurate accessories.",
        "schema_type":"CollectionPage",
        "keywords":"decade halloween costumes, 80s halloween costume, 70s halloween costume, 90s halloween costume, 50s halloween costume 2026",
    },
    "occupation": {
        "file":"occupation.html","cat_key":"occupation","icon":"👷",
        "group":"extra","nav_group":"extra",
        "en_title":"Occupation & Career Halloween Costumes 2026 | Nurse, Police & More",
        "en_desc":"Occupation and career Halloween costumes 2026 — nurse, police officer, firefighter, doctor, chef, pilot, construction and more. Ships to 200+ countries.",
        "en_h1":"Occupation & Career Costumes 2026",
        "en_h1sub":"Nurse, Police, Firefighter, Chef & More",
        "en_body":"Find the perfect career or occupation Halloween costume 2026. Our occupation costume collection covers every profession — nurse costumes, police officer costumes, firefighter costumes, doctor costumes, chef costumes, pilot uniforms, construction worker outfits, military looks, and dozens more career-themed Halloween costumes. Occupation costumes work for solo looks, couples themes, and group office party costumes. Available for adults, teens, and kids in all sizes.",
        "schema_type":"CollectionPage",
        "keywords":"occupation halloween costumes, nurse halloween costume, police halloween costume, firefighter costume 2026, career halloween costumes",
    },
    "fantasy": {
        "file":"fantasy.html","cat_key":"fantasy","icon":"🧚",
        "group":"extra","nav_group":"extra",
        "en_title":"Fantasy Halloween Costumes 2026 | Fairy, Angel, Wizard & More",
        "en_desc":"Fantasy Halloween costumes 2026 — fairy, angel, wizard, elf, mermaid, unicorn and magical creature costumes. Ships to 200+ countries.",
        "en_h1":"Fantasy Costumes 2026",
        "en_h1sub":"Fairy, Angel, Wizard, Mermaid & More",
        "en_body":"Enter a world of magic with our fantasy Halloween costumes 2026. Our fantasy costume collection includes fairy costumes with beautiful wings, angel costumes in white and gold, wizard robes and staffs, elf costumes, mermaid tail outfits, unicorn costumes, dragon costumes, and enchanted forest creature looks. Fantasy costumes are perfect for Halloween parties, Renaissance fairs, and anyone who prefers magical elegance over horror. Fantasy costumes available for adults, teens, kids, and even pets.",
        "schema_type":"CollectionPage",
        "keywords":"fantasy halloween costumes, fairy halloween costume, angel halloween costume, wizard costume 2026, mermaid halloween costume",
    },
    "partysupplies": {
        "file":"partysupplies.html","cat_key":"partysupplies","icon":"🎉",
        "group":"home","nav_group":"home",
        "en_title":"Halloween Party Supplies 2026 | Tableware, Balloons & Decor",
        "en_desc":"Halloween party supplies 2026 — tableware, plates, cups, balloons, banners, centerpieces and complete party kits. Ships to 200+ countries.",
        "en_h1":"Halloween Party Supplies 2026",
        "en_h1sub":"Tableware, Balloons, Banners & Complete Party Kits",
        "en_body":"Throw the ultimate Halloween party with our Halloween party supplies 2026. We carry everything you need to set the scene — Halloween-themed plates, cups, napkins, tablecloths, balloons, banners, centerpieces, goodie bags, candy bowls, and complete Halloween party kits. Whether you're hosting a kids Halloween party, adult costume party, or office Halloween event — our party supplies make it easy to create an amazing atmosphere. Halloween party supplies available in all themes from spooky to fun.",
        "schema_type":"CollectionPage",
        "keywords":"halloween party supplies 2026, halloween tableware, halloween balloons, halloween party kits, halloween party decorations",
    },
    "kpop": {
        "file":"kpop.html","cat_key":"kpop","icon":"🎤",
        "group":"type","nav_group":"type",
        "en_title":"K-Pop Halloween Costumes 2026 | K-Pop Idol & Demon Hunter Costumes",
        "en_desc":"K-Pop Halloween costumes 2026 — K-Pop idol costumes, K-Pop Demon Hunter looks and Korean pop star styles for Halloween. Ships to 200+ countries.",
        "en_h1":"K-Pop Costumes 2026",
        "en_h1sub":"K-Pop Idol, Demon Hunter & Korean Pop Star Styles",
        "en_body":"Unleash your inner K-Pop star with our K-Pop Halloween costumes 2026. The K-Pop Demon Hunter trend has taken Halloween by storm — combining fierce K-Pop idol aesthetics with supernatural demon hunter styling for one of the most talked-about costume trends of 2026. Our K-Pop costume collection includes full idol outfit sets, demon hunter gear, and K-Pop inspired accessories. Perfect for Halloween parties, fan conventions, and anyone who wants a bold, fashion-forward Halloween look.",
        "schema_type":"CollectionPage",
        "keywords":"kpop halloween costume 2026, kpop demon hunter costume, kpop idol costume halloween, korean pop star halloween costume",
    },
    "diy": {
        "file":"diy.html","cat_key":"diy","icon":"✂️",
        "group":"special","nav_group":"special",
        "en_title":"DIY Halloween Costume Ideas 2026 | Build Your Own Look",
        "en_desc":"DIY Halloween costume ideas 2026 — accessories, costume kits and building blocks to create your own unique Halloween look. Ships to 200+ countries.",
        "en_h1":"DIY Halloween Costume Ideas 2026",
        "en_h1sub":"Build Your Own Unique Halloween Look",
        "en_body":"Create a one-of-a-kind Halloween costume with our DIY costume accessories and kits 2026. Our DIY Halloween collection includes individual accessories — wigs, hats, capes, masks, makeup kits, prop weapons, gloves, boots, and costume components — that you can mix and match to create a totally original look. DIY costumes let you express your creativity, save money, and wear something nobody else at the party will have. Browse our accessories collection and start building your perfect Halloween costume.",
        "schema_type":"CollectionPage",
        "keywords":"diy halloween costume ideas 2026, build your own halloween costume, halloween costume accessories diy, homemade halloween costume",
    },
    # ══════════════════════════════════════════
    # FUN.COM YEAR-ROUND BEATERS — 7 new pages
    # These rank all year, not just October
    # ══════════════════════════════════════════
    "anime": {
        "file":"anime.html","cat_key":"anime","icon":"🌸",
        "group":"yearround","nav_group":"yearround",
        "en_title":"Anime Halloween Costumes 2026 | Best Anime Cosplay & Costumes",
        "en_desc":"Anime Halloween costumes 2026 — Naruto, Dragon Ball Z, My Hero Academia, Demon Slayer, One Piece, Attack on Titan and hundreds more anime costumes. Ships to 200+ countries.",
        "en_h1":"Anime Costumes 2026",
        "en_h1sub":"Naruto, Dragon Ball Z, My Hero Academia & More",
        "en_body":"Bring your favorite anime characters to life with our anime Halloween costumes 2026. Our anime costume collection covers the biggest franchises in anime history — Naruto, Dragon Ball Z, My Hero Academia, Demon Slayer, One Piece, Attack on Titan, Sword Art Online, Jujutsu Kaisen, Bleach, and dozens more. Anime costumes are perfect for Halloween parties, anime conventions, Comic Con, cosplay events, and any occasion that calls for celebrating your favorite animated series. Available year-round in all sizes for adults, teens, and kids. New anime costume styles added regularly.",
        "schema_type":"CollectionPage",
        "keywords":"anime halloween costumes 2026, anime cosplay costumes, naruto costume, my hero academia costume, demon slayer costume, anime costume ideas",
    },
    "gamer": {
        "file":"gamer.html","cat_key":"gamer","icon":"🎮",
        "group":"yearround","nav_group":"yearround",
        "en_title":"Gamer Halloween Costumes & Gifts 2026 | Best Gaming Costumes",
        "en_desc":"Gamer Halloween costumes and gifts 2026 — video game character costumes, gaming accessories, gamer gift ideas and gaming merchandise. Ships to 200+ countries.",
        "en_h1":"Gamer Costumes & Gifts 2026",
        "en_h1sub":"Video Game Characters, Accessories & Gamer Gifts",
        "en_body":"Level up your Halloween and gifting game with our gamer costumes and gifts 2026. Our gamer collection goes beyond just Halloween — we cover video game character costumes, gaming-themed accessories, gamer gift ideas for birthdays and holidays, and exclusive gaming merchandise. From retro Nintendo characters to modern gaming icons like Fortnite and Minecraft — our gamer collection celebrates gaming culture year-round. Perfect for Halloween, birthdays, Christmas, or any occasion for the gamer in your life.",
        "schema_type":"CollectionPage",
        "keywords":"gamer halloween costumes, gamer gifts 2026, video game costume, gaming merchandise, gamer gift ideas, gaming accessories halloween",
    },
    "gifts": {
        "file":"gifts.html","cat_key":"gifts","icon":"🎁",
        "group":"yearround","nav_group":"yearround",
        "en_title":"Halloween & Pop Culture Gift Ideas 2026 | Best Costume Gifts",
        "en_desc":"Halloween and pop culture gift ideas 2026 — costumes, accessories, collectibles and novelty gifts for Halloween fans, horror lovers and pop culture enthusiasts. Ships to 200+ countries.",
        "en_h1":"Halloween Gift Ideas 2026",
        "en_h1sub":"Costumes, Collectibles & Pop Culture Gifts",
        "en_body":"Halloween gifts aren't just for October. Our Halloween and pop culture gift collection 2026 includes costume sets, horror collectibles, themed accessories, novelty items, and exclusive merchandise that Halloween fans love year-round. Whether you're shopping for a Halloween birthday, a horror enthusiast, a pop culture fan, or just someone who celebrates Halloween all year — our gift collection has something for every budget and taste. Halloween gifts available for kids, teens, adults, and the family. Free shipping options available.",
        "schema_type":"CollectionPage",
        "keywords":"halloween gift ideas 2026, halloween gifts, pop culture gifts, horror gifts, costume gift ideas, halloween birthday gifts",
    },
    "movies": {
        "file":"movies.html","cat_key":"movies","icon":"🎬",
        "group":"yearround","nav_group":"yearround",
        "en_title":"Movie Halloween Costumes 2026 | Film Character Costumes",
        "en_desc":"Movie Halloween costumes 2026 — characters from the biggest films of 2026 and all-time classics. Marvel, DC, Disney, horror and blockbuster movie costumes. Ships to 200+ countries.",
        "en_h1":"Movie Costumes 2026",
        "en_h1sub":"Marvel, DC, Disney, Horror & Blockbuster Characters",
        "en_body":"Dress as your favorite movie character with our film-inspired Halloween costume collection 2026. From Marvel and DC superhero blockbusters to Disney classics, horror film villains, and the biggest new releases of 2026 — our movie costume collection covers the entire history of cinema. New movie releases mean new costume trends every season, so our movie costume selection is updated continuously throughout the year. Movie costumes available for kids, teens, and adults in all sizes. Including officially licensed designs from the studios.",
        "schema_type":"CollectionPage",
        "keywords":"movie halloween costumes 2026, film character costumes, marvel costume, disney costume, movie character halloween costume, blockbuster halloween costume",
    },
    "tvshows": {
        "file":"tvshows.html","cat_key":"tvshows","icon":"📺",
        "group":"yearround","nav_group":"yearround",
        "en_title":"TV Show Halloween Costumes 2026 | Best TV Character Costumes",
        "en_desc":"TV show Halloween costumes 2026 — Wednesday, Stranger Things, The Office, Game of Thrones, Breaking Bad, Squid Game and hundreds more TV character costumes. Ships to 200+ countries.",
        "en_h1":"TV Show Costumes 2026",
        "en_h1sub":"Wednesday, Stranger Things, The Office & More",
        "en_body":"Bring your favorite TV characters to Halloween with our TV show costume collection 2026. Whether you love Wednesday Addams from the Netflix hit, the gang from Stranger Things, the characters from The Office, Game of Thrones, Breaking Bad, Squid Game, or any other iconic TV series — our TV show costume collection covers the most beloved characters from every streaming platform and network. TV show group costumes are perfect for office parties, where everyone can be a different character from the same show.",
        "schema_type":"CollectionPage",
        "keywords":"tv show halloween costumes, wednesday costume 2026, stranger things costume, the office halloween costume, tv character halloween costume",
    },
    "clothing": {
        "file":"clothing.html","cat_key":"clothing","icon":"👕",
        "group":"yearround","nav_group":"yearround",
        "en_title":"Halloween Clothing & Apparel 2026 | Halloween T-Shirts & More",
        "en_desc":"Halloween clothing and apparel 2026 — Halloween t-shirts, sweaters, pajamas, socks and themed clothing for Halloween fans year-round. Ships to 200+ countries.",
        "en_h1":"Halloween Clothing & Apparel 2026",
        "en_h1sub":"T-Shirts, Sweaters, Pajamas & Halloween Fashion",
        "en_body":"Celebrate Halloween all year with our Halloween clothing and apparel collection 2026. We carry Halloween-themed t-shirts, sweaters, hoodies, pajamas, socks, and fashion accessories for people who live the Halloween lifestyle 365 days a year. From subtle pumpkin motifs to full horror character designs — our Halloween clothing lets you express your love for the season any time of year. Halloween apparel available for men, women, and kids in all sizes. New Halloween clothing styles added regularly.",
        "schema_type":"CollectionPage",
        "keywords":"halloween clothing 2026, halloween t-shirts, halloween sweaters, halloween pajamas, halloween apparel, halloween fashion year round",
    },
    "yearround": {
        "file":"yearround.html","cat_key":"yearround","icon":"🗓️",
        "group":"yearround","nav_group":"yearround",
        "en_title":"Halloween Year-Round 2026 | Shop Halloween All Year",
        "en_desc":"Shop Halloween year-round — costumes, collectibles, decorations, clothing and horror merchandise available all year, not just in October. Ships to 200+ countries.",
        "en_h1":"Halloween All Year Round",
        "en_h1sub":"Costumes, Collectibles & Horror Lifestyle 365 Days",
        "en_body":"True Halloween fans know the season never ends. Our year-round Halloween collection features everything a Halloween enthusiast could want in January, April, July, or any month of the year — horror collectibles, Halloween-themed clothing, animatronics, decorations, costume accessories, and seasonal merchandise that ships all year. Whether you're getting an early jump on Halloween preparations, hunting for birthday gifts for horror fans, or simply celebrating your favorite holiday every single day — our year-round Halloween shop has you covered in every season.",
        "schema_type":"CollectionPage",
        "keywords":"halloween year round, shop halloween all year, halloween merchandise year round, horror lifestyle, halloween fans year round shopping",
    },
    # ══════════════════════════════════════════════
    # EZCOSPLAY BEATERS — Specific game title pages
    # US shipping advantage vs EZCosplay China ships
    # ══════════════════════════════════════════════
    "genshin": {
        "file":"genshin.html","cat_key":"genshin","icon":"🌟",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Genshin Impact Cosplay Costumes 2026 | Hu Tao, Raiden, Ayaka & More",
        "en_desc":"Genshin Impact cosplay costumes 2026 — Hu Tao, Raiden Shogun, Ayaka, Ganyu, Zhongli, Venti and all Genshin characters. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"Genshin Impact Costumes 2026",
        "en_h1sub":"Hu Tao, Raiden, Ayaka, Ganyu & All Characters",
        "en_body":"Find the best Genshin Impact cosplay costumes 2026 with fast US shipping — unlike Chinese cosplay sites that take weeks to deliver, our Genshin Impact costume collection ships quickly from US warehouses. We carry costumes for all the most popular Genshin Impact characters — Hu Tao, Raiden Shogun, Ayaka, Ganyu, Zhongli, Venti, Diluc, Fischl, Keqing, Kazuha, and the full Teyvat roster. Perfect for Halloween, anime conventions, Comic Con, and gaming events. Genshin Impact costumes available in all sizes for adults, teens, and kids.",
        "schema_type":"CollectionPage",
        "keywords":"genshin impact cosplay costume, genshin impact halloween costume 2026, hu tao costume, raiden shogun costume, ayaka cosplay costume",
    },
    "leagueoflegends": {
        "file":"leagueoflegends.html","cat_key":"leagueoflegends","icon":"⚔️",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"League of Legends Cosplay Costumes 2026 | Jinx, Arcane & More",
        "en_desc":"League of Legends cosplay costumes 2026 — Jinx, Vi, Ekko, Caitlyn from Arcane Season 2 plus classic LoL champions. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"League of Legends Costumes 2026",
        "en_h1sub":"Jinx, Vi, Arcane Season 2 & Classic Champions",
        "en_body":"Shop League of Legends and Arcane cosplay costumes 2026 with fast US shipping. The massive success of Arcane Season 2 on Netflix has made Jinx, Vi, Ekko, Caitlyn, and Jayce some of the most sought-after cosplay costumes of the year. Our LoL costume collection also covers classic League champions — Ahri, Lux, Ezreal, Yasuo, Zed, and hundreds more. Fast US shipping means you get your costume in days, not the weeks it takes from Chinese cosplay sites.",
        "schema_type":"CollectionPage",
        "keywords":"league of legends cosplay costume, arcane costume 2026, jinx costume, vi costume, arcane season 2 costume, lol halloween costume",
    },
    "overwatch": {
        "file":"overwatch.html","cat_key":"overwatch","icon":"🎯",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Overwatch 2 Cosplay Costumes 2026 | Kiriko, Tracer & More",
        "en_desc":"Overwatch 2 cosplay costumes 2026 — Kiriko, Tracer, D.Va, Mercy, Widowmaker, Genji and all OW2 heroes. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"Overwatch 2 Costumes 2026",
        "en_h1sub":"Kiriko, Tracer, D.Va, Mercy & All Heroes",
        "en_body":"Gear up with our Overwatch 2 cosplay costume collection 2026, featuring fast US shipping that gets your costume to you in days. Our OW2 collection covers all the most popular heroes — Kiriko, Tracer, D.Va, Mercy, Widowmaker, Genji, Hanzo, Pharah, Ana, and the full Overwatch 2 roster. Overwatch costumes are perfect for Halloween parties, gaming conventions, and cosplay events. Available in all sizes with accessories including props, wigs, and complete character sets.",
        "schema_type":"CollectionPage",
        "keywords":"overwatch 2 cosplay costume, overwatch halloween costume 2026, kiriko costume, tracer costume, dva costume, mercy cosplay costume",
    },
    "finalfantasy": {
        "file":"finalfantasy.html","cat_key":"finalfantasy","icon":"🗡️",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Final Fantasy Cosplay Costumes 2026 | FF7 Rebirth, Cloud, Tifa & More",
        "en_desc":"Final Fantasy cosplay costumes 2026 — FF7 Rebirth Cloud, Tifa, Aerith, Sephiroth, plus FF14, FF16 and classic Final Fantasy costumes. Fast US shipping.",
        "en_h1":"Final Fantasy Costumes 2026",
        "en_h1sub":"FF7 Rebirth, Cloud, Tifa, Aerith & More",
        "en_body":"Shop Final Fantasy cosplay costumes 2026 with fast US shipping. Final Fantasy VII Rebirth has renewed massive interest in Cloud, Tifa, Aerith, Sephiroth, and the Midgar crew — making FF7 costumes some of the hottest cosplay choices of the year. Our Final Fantasy costume collection also covers FF14 Warrior of Light armor, FF16 Clive Rosfield, and classic characters from across the entire Final Fantasy series. Fast US warehouse shipping vs weeks of waiting from overseas sites.",
        "schema_type":"CollectionPage",
        "keywords":"final fantasy cosplay costume, ff7 rebirth costume, cloud strife costume, tifa lockhart costume, aerith costume, sephiroth costume 2026",
    },
    "deadbydaylight": {
        "file":"deadbydaylight.html","cat_key":"deadbydaylight","icon":"🔦",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Dead by Daylight Cosplay Costumes 2026 | Killer & Survivor Costumes",
        "en_desc":"Dead by Daylight cosplay costumes 2026 — Ghostface, Trapper, Nurse, Huntress, Myers, and survivor costumes from DBD. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"Dead by Daylight Costumes 2026",
        "en_h1sub":"Killers, Survivors & Licensed Horror Characters",
        "en_body":"Escape the trial in style with our Dead by Daylight cosplay costumes 2026. DBD features licensed horror characters from major franchises — Ghostface from Scream, Michael Myers, Freddy Krueger, Pinhead, and Alien alongside original killers like The Trapper, The Nurse, and The Huntress. Our Dead by Daylight costume collection covers both killers and survivors for Halloween, gaming conventions, and cosplay events. Fast US shipping — your DBD costume arrives in days, not weeks.",
        "schema_type":"CollectionPage",
        "keywords":"dead by daylight cosplay costume, dbd halloween costume 2026, ghostface dbd costume, trapper costume, dbd killer costume, dead by daylight halloween",
    },
    # ── Specific anime title pages ──
    "jujutsukaisen": {
        "file":"jujutsukaisen.html","cat_key":"jujutsukaisen","icon":"🩸",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Jujutsu Kaisen Cosplay Costumes 2026 | Gojo, Itadori & More",
        "en_desc":"Jujutsu Kaisen cosplay costumes 2026 — Gojo Satoru, Yuji Itadori, Megumi Fushiguro, Nobara and more JJK character costumes. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"Jujutsu Kaisen Costumes 2026",
        "en_h1sub":"Gojo, Itadori, Megumi, Nobara & More",
        "en_body":"Shop Jujutsu Kaisen cosplay costumes 2026 with fast US shipping. JJK is one of the biggest anime series in the world — making Gojo Satoru, Yuji Itadori, Megumi Fushiguro, Nobara Kugisaki, and the cursed spirits some of the most popular cosplay choices for Halloween and conventions. Our JJK costume collection includes the iconic Jujutsu Tech uniforms, Gojo's blindfold and infinity look, cursed spirit designs, and accessories for complete character accuracy.",
        "schema_type":"CollectionPage",
        "keywords":"jujutsu kaisen cosplay costume, jjk costume halloween, gojo satoru costume, yuji itadori costume, megumi fushiguro costume 2026",
    },
    "hazbinhotel": {
        "file":"hazbinhotel.html","cat_key":"hazbinhotel","icon":"😈",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Hazbin Hotel Cosplay Costumes 2026 | Alastor, Charlie & More",
        "en_desc":"Hazbin Hotel cosplay costumes 2026 — Alastor, Charlie, Vaggie, Angel Dust, Lucifer and more Hazbin Hotel character costumes. Fast US shipping.",
        "en_h1":"Hazbin Hotel Costumes 2026",
        "en_h1sub":"Alastor, Charlie, Lucifer & The Hell Hotel Crew",
        "en_body":"Check in to the best Hazbin Hotel cosplay costumes 2026 with fast US shipping. The Amazon Prime animated series became a massive hit, making Alastor the Radio Demon, Charlie Magne, Vaggie, Angel Dust, and Lucifer Morningstar some of the most requested cosplay costumes of the year. Our Hazbin Hotel costume collection covers all the main characters with detailed designs that capture the show's distinctive animation style. Perfect for Halloween, anime conventions, and cosplay events.",
        "schema_type":"CollectionPage",
        "keywords":"hazbin hotel cosplay costume, hazbin hotel halloween costume 2026, alastor costume, charlie hazbin hotel costume, lucifer morningstar costume",
    },
    "frieren": {
        "file":"frieren.html","cat_key":"frieren","icon":"🧝",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Frieren Cosplay Costumes 2026 | Frieren & Fern Costumes",
        "en_desc":"Frieren: Beyond Journey's End cosplay costumes 2026 — Frieren, Fern, Stark, Himmel and more Sousou no Frieren character costumes. Fast US shipping.",
        "en_h1":"Frieren Costumes 2026",
        "en_h1sub":"Frieren, Fern, Stark & Beyond Journey's End",
        "en_body":"Shop Frieren: Beyond Journey's End cosplay costumes 2026 with fast US shipping. Sousou no Frieren became one of the most critically acclaimed anime of its era — making Frieren's distinctive elf mage look and Fern's purple robes highly sought-after cosplay costumes for conventions and Halloween. Our Frieren costume collection includes authentic recreations of the characters' outfits with attention to the series' unique fantasy aesthetic.",
        "schema_type":"CollectionPage",
        "keywords":"frieren cosplay costume, frieren beyond journeys end costume, sousou no frieren costume, fern cosplay costume 2026, frieren halloween costume",
    },
    "onepiececosplay": {
        "file":"onepiececosplay.html","cat_key":"onepiececosplay","icon":"🏴‍☠️",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"One Piece Cosplay Costumes 2026 | Luffy, Zoro & Straw Hat Crew",
        "en_desc":"One Piece cosplay costumes 2026 — Luffy, Zoro, Nami, Robin, Sanji, Gear 5 Luffy and the full Straw Hat crew. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"One Piece Costumes 2026",
        "en_h1sub":"Luffy, Zoro, Nami, Robin & The Straw Hat Crew",
        "en_body":"Set sail with our One Piece cosplay costumes 2026, featuring fast US shipping for the world's most popular manga. The Netflix live-action series and Gear 5 Luffy have brought One Piece to a massive global audience — making Monkey D. Luffy, Roronoa Zoro, Nami, Nico Robin, Sanji, and the Straw Hat crew some of the most popular cosplay choices for 2026. Our One Piece costume collection covers the full crew with accurate character designs for Halloween and conventions.",
        "schema_type":"CollectionPage",
        "keywords":"one piece cosplay costume, luffy costume 2026, zoro costume, gear 5 luffy costume, straw hat crew costume, one piece halloween costume",
    },
    # ── Cosplay specialist pages ──
    "cosplayshoes": {
        "file":"cosplayshoes.html","cat_key":"cosplayshoes","icon":"👟",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Cosplay Shoes & Boots 2026 | Halloween Costume Footwear",
        "en_desc":"Cosplay shoes and boots 2026 — character-accurate footwear for anime, gaming, movie and Halloween costumes. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"Cosplay Shoes & Boots 2026",
        "en_h1sub":"Character-Accurate Footwear for Every Costume",
        "en_body":"Complete your cosplay with the right shoes and boots from our cosplay footwear collection 2026. The right footwear makes the difference between a good costume and a great one — our cosplay shoe collection includes platform boots, character-accurate footwear, themed boots, shoe covers, and specialty footwear for anime, gaming, movie, and Halloween costumes. Fast US shipping — your cosplay shoes arrive in days, not the weeks it takes from Chinese cosplay sites. Cosplay shoes available in all sizes.",
        "schema_type":"CollectionPage",
        "keywords":"cosplay shoes 2026, cosplay boots, halloween costume shoes, anime costume footwear, character shoes cosplay",
    },
    "convention": {
        "file":"convention.html","cat_key":"convention","icon":"🏟️",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Convention Cosplay Guide 2026 | Comic Con, Anime Expo & More",
        "en_desc":"Convention cosplay guide 2026 — what to wear to Comic Con, Anime Expo, PAX, Dragon Con and more. Best convention cosplay costumes with fast US shipping.",
        "en_h1":"Convention Cosplay Guide 2026",
        "en_h1sub":"Comic Con, Anime Expo, PAX & Dragon Con",
        "en_body":"Planning your convention cosplay for 2026? Our convention cosplay guide covers everything you need — the most popular costume choices for Comic Con, Anime Expo, PAX, Dragon Con, MegaCon, and local anime and gaming conventions. We cover trending characters, group costume ideas for convention crews, prop regulations, comfort considerations for all-day wearing, and the fastest shipping options to get your costume before the event. Convention cosplay costumes with fast US shipping available.",
        "schema_type":"WebPage",
        "keywords":"convention cosplay 2026, comic con costume, anime expo costume, pax cosplay, dragon con costume, convention costume guide",
    },
    "lolita": {
        "file":"lolita.html","cat_key":"lolita","icon":"🎀",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Lolita Fashion Costumes 2026 | Gothic, Sweet & Classic Lolita",
        "en_desc":"Lolita fashion costumes 2026 — gothic lolita, sweet lolita, classic lolita and EGL fashion costumes for Halloween, conventions and cosplay. Ships to 200+ countries.",
        "en_h1":"Lolita Fashion Costumes 2026",
        "en_h1sub":"Gothic, Sweet & Classic Lolita Styles",
        "en_body":"Discover the elegant world of lolita fashion with our lolita costume collection 2026. Lolita fashion — including gothic lolita, sweet lolita, classic lolita, and elegant gothic lolita (EGL) — has become one of the most distinctive and beloved cosplay styles worldwide. Our lolita costume collection features elaborate petticoat dresses, Victorian-inspired designs, and accessories for every lolita substyle. Perfect for Halloween, anime conventions, Harajuku fashion events, and anyone who appreciates the artistry of lolita fashion.",
        "schema_type":"CollectionPage",
        "keywords":"lolita costume 2026, gothic lolita costume, sweet lolita costume, lolita fashion halloween, lolita cosplay costume",
    },
    # ══════════════════════════════════════════════════
    # MICCOSTUMES BEATERS — 9 new pages
    # ══════════════════════════════════════════════════
    "swimwear": {
        "file":"swimwear.html","cat_key":"swimwear","icon":"🩱",
        "group":"micc","nav_group":"micc",
        "en_title":"Cosplay Swimsuits & Anime Swimwear 2026 | Character Swimsuits",
        "en_desc":"Cosplay swimsuits and anime swimwear 2026 — character-inspired swimsuits, anime bikinis, Jinx, Nami, Zelda and gaming-inspired bathing suits. Ships to 200+ countries.",
        "en_h1":"Cosplay Swimsuits 2026",
        "en_h1sub":"Anime & Character-Inspired Swimwear",
        "en_body":"Make a splash with our cosplay swimsuit collection 2026. Anime and gaming-inspired swimwear has become one of the fastest-growing cosplay categories — combining beachwear with beloved character designs for pool parties, beach events, and summer conventions. Our cosplay swimsuit collection includes character-inspired bikinis, one-piece swimsuits inspired by popular anime and gaming characters including Jinx from Arcane, Nami from One Piece, Princess Zelda, and more. Available in all sizes with fast US shipping.",
        "schema_type":"CollectionPage",
        "keywords":"cosplay swimsuit 2026, anime swimsuit, character swimsuit, jinx swimsuit, nami swimsuit, gaming inspired swimwear cosplay",
    },
    "kawaii": {
        "file":"kawaii.html","cat_key":"kawaii","icon":"🌸",
        "group":"micc","nav_group":"micc",
        "en_title":"Kawaii Fashion Costumes 2026 | Cute Japanese Street Fashion",
        "en_desc":"Kawaii fashion costumes 2026 — cute Japanese street fashion, Harajuku styles, kawaii accessories, pastel outfits and Japanese-inspired costume fashion. Ships to 200+ countries.",
        "en_h1":"Kawaii Fashion Costumes 2026",
        "en_h1sub":"Japanese Street Fashion, Harajuku & Cute Styles",
        "en_body":"Enter the adorable world of kawaii fashion with our Japanese-inspired costume collection 2026. Kawaii — the Japanese culture of cuteness — has become a global fashion and cosplay phenomenon. Our kawaii collection includes Harajuku-inspired outfits, pastel fashion sets, cute accessories, kawaii lolita styles, and Japanese street fashion pieces. Perfect for Halloween with a unique twist, anime conventions, cosplay events, and anyone who lives the kawaii lifestyle. New kawaii arrivals added regularly.",
        "schema_type":"CollectionPage",
        "keywords":"kawaii fashion costume 2026, kawaii costume, harajuku costume, japanese street fashion costume, kawaii halloween costume, cute japanese costume",
    },
    "casualwear": {
        "file":"casualwear.html","cat_key":"casualwear","icon":"👘",
        "group":"micc","nav_group":"micc",
        "en_title":"Anime Casual Wear 2026 | Character-Inspired Fashion & Streetwear",
        "en_desc":"Anime-inspired casual wear 2026 — character-inspired hoodies, dresses, streetwear and everyday fashion from your favorite anime and gaming series. Ships to 200+ countries.",
        "en_h1":"Anime Casual Wear 2026",
        "en_h1sub":"Character-Inspired Hoodies, Dresses & Streetwear",
        "en_body":"Wear your fandom every day with our anime-inspired casual wear collection 2026. Beyond full cosplay costumes, our casual wear line features character-inspired everyday fashion — hoodies, dresses, skirts, and streetwear pieces that channel your favorite anime and gaming aesthetics without being full costumes. Perfect for conventions on casual days, everyday wear for anime fans, and anyone who wants to express their fandom through fashion. Anime casual wear available year-round in all sizes.",
        "schema_type":"CollectionPage",
        "keywords":"anime casual wear 2026, anime inspired fashion, character hoodie, anime streetwear, anime dress everyday, gaming casual wear",
    },
    "nier": {
        "file":"nier.html","cat_key":"nier","icon":"⚙️",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"NieR:Automata Cosplay Costumes 2026 | 2B, A2 & 9S Costumes",
        "en_desc":"NieR:Automata cosplay costumes 2026 — 2B YoRHa No.2 Type B, A2, 9S and NieR:Replicant character costumes. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"NieR:Automata Costumes 2026",
        "en_h1sub":"2B, A2, 9S & YoRHa Android Costumes",
        "en_body":"Shop NieR:Automata cosplay costumes 2026 with fast US shipping. YoRHa No.2 Type B — simply known as 2B — is one of the most iconic and universally recognized cosplay characters in gaming history. Her black gothic android uniform with blindfold has made 2B a perennial top cosplay choice at every convention worldwide. Our NieR collection also covers A2, 9S, and other YoRHa androids from both NieR:Automata and NieR:Replicant. Fast US shipping means days, not the weeks you wait from Chinese cosplay sites.",
        "schema_type":"CollectionPage",
        "keywords":"nier automata cosplay costume, 2b costume 2026, yorha 2b cosplay, nier reincarnation costume, a2 nier costume, 9s nier costume",
    },
    "cyberpunk": {
        "file":"cyberpunk.html","cat_key":"cyberpunk","icon":"🤖",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Cyberpunk 2077 & Edgerunners Cosplay Costumes 2026",
        "en_desc":"Cyberpunk 2077 and Edgerunners cosplay costumes 2026 — V, Johnny Silverhand, Lucy, David Martinez and Night City character costumes. Fast US shipping.",
        "en_h1":"Cyberpunk Costumes 2026",
        "en_h1sub":"Cyberpunk 2077, Edgerunners & Night City Characters",
        "en_body":"Dive into Night City with our Cyberpunk 2077 and Edgerunners cosplay costume collection 2026. Cyberpunk Edgerunners on Netflix introduced Lucy and David Martinez to a massive global audience, making them some of the most popular cosplay characters of recent years. Our Cyberpunk collection covers V (both male and female), Johnny Silverhand, Lucy from Edgerunners, Panam, Judy Alvarez, and other Night City legends. Cyberpunk's neon-lit aesthetic makes these costumes spectacular at Halloween parties and gaming conventions. Fast US shipping available.",
        "schema_type":"CollectionPage",
        "keywords":"cyberpunk 2077 cosplay costume, cyberpunk edgerunners costume, lucy edgerunners costume, johnny silverhand costume, v cyberpunk costume 2026",
    },
    "zelda": {
        "file":"zelda.html","cat_key":"zelda","icon":"🗡️",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Legend of Zelda Cosplay Costumes 2026 | Link, Zelda & More",
        "en_desc":"Legend of Zelda cosplay costumes 2026 — Link, Princess Zelda, Ganondorf, Tears of the Kingdom and Breath of the Wild character costumes. Fast US shipping.",
        "en_h1":"Legend of Zelda Costumes 2026",
        "en_h1sub":"Link, Princess Zelda, Ganondorf & Tears of the Kingdom",
        "en_body":"Embark on your heroic quest with our Legend of Zelda cosplay costume collection 2026. The Legend of Zelda: Tears of the Kingdom reignited global passion for the franchise — making Link's iconic green tunic, Princess Zelda's Hyrulean gown, and Ganondorf's imposing armor some of the most requested cosplay costumes at gaming conventions and Halloween events. Our Zelda costume collection covers designs from Tears of the Kingdom, Breath of the Wild, Ocarina of Time, and classic Zelda titles. Fast US shipping available.",
        "schema_type":"CollectionPage",
        "keywords":"legend of zelda cosplay costume, link costume 2026, princess zelda costume, tears of the kingdom costume, zelda halloween costume, ganondorf costume",
    },
    "devilmaycry": {
        "file":"devilmaycry.html","cat_key":"devilmaycry","icon":"😈",
        "group":"cosplay","nav_group":"cosplay",
        "en_title":"Devil May Cry Cosplay Costumes 2026 | Dante, Vergil & Lady",
        "en_desc":"Devil May Cry cosplay costumes 2026 — Dante, Vergil, Lady, Nero and DMC5 character costumes. Fast US shipping. Ships to 200+ countries.",
        "en_h1":"Devil May Cry Costumes 2026",
        "en_h1sub":"Dante, Vergil, Lady, Nero & DMC Characters",
        "en_body":"Show no mercy with our Devil May Cry cosplay costume collection 2026. Dante's iconic red coat, Vergil's blue SSS-rank style, Lady's tactical outfit, and Nero's Devil Breaker arm are beloved cosplay choices for gaming fans and Halloween party-goers. The Devil May Cry franchise combines gothic horror with stylish action — making these costumes spectacular at Halloween parties, gaming conventions, and cosplay events. Our DMC collection covers characters from DMC5, DMC3, and the animated series. Fast US shipping available.",
        "schema_type":"CollectionPage",
        "keywords":"devil may cry cosplay costume, dante dmc costume 2026, vergil costume, lady dmc costume, nero costume devil may cry, dmc5 cosplay",
    },
    "weeklydeals": {
        "file":"weeklydeals.html","cat_key":"weeklydeals","icon":"🔥",
        "group":"deals","nav_group":"deals",
        "en_title":"Weekly Halloween Costume Deals 2026 | New Deals Every Week",
        "en_desc":"Weekly Halloween costume deals 2026 — new discounts and sale prices on costumes, accessories and cosplay updated every week. Best prices online. Ships to 200+ countries.",
        "en_h1":"Weekly Halloween Costume Deals",
        "en_h1sub":"New Discounts & Sale Prices Every Week",
        "en_body":"Get the best Halloween costume deals with our weekly rotating sale section. Unlike static sale pages, our weekly deals feature new discounts on costumes, accessories, cosplay, wigs, and decoration items updated every week. From cheap Halloween costumes under $10 to premium cosplay sets marked down significantly — our weekly deals section is where smart shoppers find the best prices on Halloween and cosplay merchandise. Check back every week for fresh markdowns across all categories.",
        "schema_type":"CollectionPage",
        "keywords":"weekly halloween costume deals, halloween costume sale weekly, cheap cosplay costumes deals, halloween discount costumes 2026, best costume deals",
    },
    "preorder": {
        "file":"preorder.html","cat_key":"preorder","icon":"📦",
        "group":"deals","nav_group":"deals",
        "en_title":"Pre-Order Halloween Costumes 2026 | Upcoming Releases",
        "en_desc":"Pre-order Halloween costumes 2026 — upcoming costume releases based on the latest movies, games and anime. Reserve your costume early. Ships to 200+ countries.",
        "en_h1":"Pre-Order Halloween Costumes 2026",
        "en_h1sub":"Reserve Upcoming Costumes Based on Latest Releases",
        "en_body":"Be first in line for the hottest new Halloween costumes of 2026 with our pre-order collection. As new movies, games, and anime series release throughout the year, new costume designs follow — and popular styles sell out fast. Our pre-order section features upcoming costume releases based on anticipated 2026 movie and game releases so you can reserve your costume before it sells out. Pre-order costumes based on the biggest upcoming entertainment releases of 2026.",
        "schema_type":"CollectionPage",
        "keywords":"pre-order halloween costumes 2026, upcoming halloween costumes, reserve halloween costume, new release halloween costume 2026",
    },
}

# ─────────────────────────────────────────────────────────
# NAV GROUPS (how pages are organized in navigation)
# ─────────────────────────────────────────────────────────
NAV_GROUPS = {
    "gender":      {"label":"By Gender",    "icon":"👗"},
    "age":         {"label":"By Age",       "icon":"🎂"},
    "type":        {"label":"By Style",     "icon":"🎭"},
    "special":     {"label":"Special",      "icon":"⭐"},
    "accessories": {"label":"Accessories",  "icon":"🎩"},
    "deals":       {"label":"Deals",        "icon":"💰"},
    "home":        {"label":"Home & Decor", "icon":"🏚️"},
    "spirit":      {"label":"Props & More",  "icon":"🤖"},
    "extra":       {"label":"Themes & More", "icon":"🌟"},
    "franchise":   {"label":"By Character",  "icon":"🎬"},
    "yearround":   {"label":"Year-Round",    "icon":"🗓️"},
    "cosplay":     {"label":"Cosplay & Games","icon":"🎮"},
    "micc":        {"label":"Fashion & More", "icon":"👘"},
}

# ─────────────────────────────────────────────────────────
# LANGUAGES
# ─────────────────────────────────────────────────────────
LANGS = {
    "en":{"name":"English",    "flag":"🌐","dir":"ltr"},
    "es":{"name":"Español",    "flag":"🇪🇸","dir":"ltr"},
    "fr":{"name":"Français",   "flag":"🇫🇷","dir":"ltr"},
    "de":{"name":"Deutsch",    "flag":"🇩🇪","dir":"ltr"},
    "pt":{"name":"Português",  "flag":"🇧🇷","dir":"ltr"},
    "it":{"name":"Italiano",   "flag":"🇮🇹","dir":"ltr"},
    "ja":{"name":"日本語",      "flag":"🇯🇵","dir":"ltr"},
    "ko":{"name":"한국어",      "flag":"🇰🇷","dir":"ltr"},
    "zh":{"name":"中文",        "flag":"🇨🇳","dir":"ltr"},
    "ar":{"name":"العربية",    "flag":"🇸🇦","dir":"rtl"},
    "nl":{"name":"Nederlands", "flag":"🇳🇱","dir":"ltr"},
    "pl":{"name":"Polski",     "flag":"🇵🇱","dir":"ltr"},
}

# ─────────────────────────────────────────────────────────
# CUSTOMER REVIEWS (social proof — beats halloweencostumes.com)
# ─────────────────────────────────────────────────────────
REVIEWS = [
    {"name":"Sarah M.",    "country":"🇺🇸","rating":5,"text":"Found my witch costume in seconds using the search. Arrived in 3 days — perfect quality and exactly as described. Will be back next year!"},
    {"name":"Carlos R.",   "country":"🇲🇽","rating":5,"text":"Ordered group costumes for our office of 12 people. Everything arrived together, all sizes correct. The wholesale pricing saved us so much money."},
    {"name":"Emma L.",     "country":"🇬🇧","rating":5,"text":"Shipped to the UK in under a week. My kids' costumes were adorable and the prices beat every other site I found. Highly recommend!"},
    {"name":"Yuki T.",     "country":"🇯🇵","rating":5,"text":"International shipping was fast and tracked. The plus size selection is incredible — finally a store that has my size in every style."},
    {"name":"Marie D.",    "country":"🇫🇷","rating":5,"text":"Found last minute costumes 2 days before Halloween. Express delivery saved us! The quality was amazing for the price."},
    {"name":"Ahmed K.",    "country":"🇦🇪","rating":5,"text":"Ordered couples costumes for a Halloween party. The matching set was perfect and we won the costume contest! Shipped to UAE with no issues."},
]

# ─────────────────────────────────────────────────────────
# POPULAR SEARCHES
# ─────────────────────────────────────────────────────────
POPULAR_SEARCHES = [
    "spider costume","witch costume","vampire costume","pirate costume",
    "zombie costume","clown costume","skeleton costume","superhero costume",
    "dinosaur costume","werewolf costume","ninja costume","ghost costume",
    "devil costume","mummy costume","inflatable costume","couples costume",
    "baby costume","plus size costume","nurse costume","cat costume",
    "batman costume","joker costume","Wednesday Addams costume","Mandalorian costume",
    "renaissance costume","fairy costume","angel costume","knight costume",
    "animatronic halloween","haunted house props","fog machine","t-rex costume",
    "ghostbusters costume","star wars costume","disney costume","licensed costume",
    "tween costume","medieval costume","viking costume","kpop costume",
    "funko pop halloween","inflatable t-rex","art the clown costume","terrifier costume",
    "wednesday addams costume","beetlejuice costume","freddy krueger costume",
    "jason voorhees costume","pennywise costume","michael myers costume",
    "harry potter costume","hermione granger costume","scooby doo costume",
    "five nights at freddys costume","fnaf costume","addams family costume",
    "80s halloween costume","90s halloween costume","decade costume",
    "nurse costume","police costume","firefighter costume",
    "fairy costume","angel costume","mermaid costume","wizard costume",
    "halloween party supplies","halloween balloons","kpop demon hunter costume",
    "diy halloween costume","k-pop costume","occupation costume",
    "anime costume","naruto costume","my hero academia costume","demon slayer costume",
    "gamer costume","gaming gifts halloween","tv show costume","movie costume 2026",
    "stranger things costume","wednesday costume","the office costume",
    "halloween gifts","horror gifts","pop culture gifts","halloween clothing",
    "halloween pajamas","halloween t-shirt","year round halloween",
    "genshin impact costume","league of legends costume","arcane jinx costume",
    "overwatch costume","kiriko costume","final fantasy costume","ff7 costume",
    "cloud strife costume","tifa lockhart costume","dead by daylight costume",
    "jujutsu kaisen costume","gojo satoru costume","hazbin hotel costume",
    "alastor costume","frieren costume","one piece costume","luffy costume",
    "cosplay shoes","convention costume","lolita costume","gothic lolita",
    "anime convention costume","fast us shipping cosplay","us warehouse cosplay",
    "cosplay swimsuit","anime swimsuit","kawaii costume","harajuku costume",
    "anime casual wear","nier automata costume","2b costume","yorha 2b cosplay",
    "cyberpunk costume","lucy edgerunners costume","johnny silverhand costume",
    "zelda costume","link costume","tears of the kingdom costume",
    "devil may cry costume","dante costume","vergil costume",
    "weekly deals halloween","pre-order halloween costume","kawaii fashion",
    "gothic corset costume","anime lingerie cosplay","sexy cosplay costume",
]

# ─────────────────────────────────────────────────────────
# TRUST BADGES (beats halloweencostumes.com's trust section)
# ─────────────────────────────────────────────────────────
TRUST_BADGES = [
    {"icon":"🌍","label":"Ships to 200+ Countries"},
    {"icon":"🔒","label":"Secure SSL Checkout"},
    {"icon":"💸","label":"Best Price Guarantee"},
    {"icon":"⚡","label":"Express Delivery Available"},
    {"icon":"↩️","label":"Easy Returns"},
    {"icon":"⭐","label":"10,000+ Costumes"},
    {"icon":"📦","label":"Free Shipping Over $50"},
    {"icon":"🎃","label":"Updated Daily"},
    {"icon":"🚀","label":"Same-Day Delivery Available"},
    {"icon":"🎉","label":"Party Supplies Too"},
    {"icon":"🇺🇸","label":"Fast US Shipping — Not China"},
    {"icon":"📅","label":"Days Not Weeks Delivery"},
    {"icon":"⭐","label":"50,000+ Customer Reviews"},
    {"icon":"✋","label":"Handcrafted Quality Costumes"},
]

# ─────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────
CSS = """
:root{--ink:#0c0b09;--amber:#f5a623;--cream:#fdf6e3;--red:#e8321a;--smoke:#1e1c18;--dim:rgba(253,246,227,.6);--faint:rgba(253,246,227,.35);--green:#22c55e}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'DM Sans',sans-serif;background:var(--ink);color:var(--cream);min-height:100vh}
a{color:inherit;text-decoration:none}

/* TOPBAR */
.topbar{background:var(--amber);color:var(--ink);font-weight:700;font-size:.78rem;letter-spacing:2px;text-transform:uppercase;text-align:center;padding:10px 16px;overflow:hidden;white-space:nowrap}
.marquee{display:inline-block;animation:marquee 40s linear infinite}
@keyframes marquee{0%{transform:translateX(100vw)}100%{transform:translateX(-100%)}}

/* NAV */
nav{background:var(--ink);border-bottom:1px solid rgba(245,166,35,.2);position:sticky;top:0;z-index:200}
.nav-top{padding:12px 40px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.nav-logo{font-family:'Bebas Neue',cursive;font-size:1.8rem;color:var(--amber);letter-spacing:2px;white-space:nowrap}
.nav-right{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.lang-sel{background:rgba(255,255,255,.06);border:1px solid rgba(245,166,35,.3);color:var(--cream);font-size:.78rem;padding:7px 10px;border-radius:4px;cursor:pointer;outline:none}
.nav-cta{background:var(--amber);color:var(--ink);font-weight:700;font-size:.82rem;letter-spacing:1px;text-transform:uppercase;padding:10px 20px;border-radius:4px;transition:background .15s;white-space:nowrap}
.nav-cta:hover{background:#ffb733}

/* MEGA NAV */
.nav-cats{background:#151310;border-top:1px solid rgba(245,166,35,.1);padding:8px 40px;display:flex;gap:4px;flex-wrap:wrap;overflow-x:auto}
.nav-cat-link{font-size:.78rem;color:rgba(253,246,227,.6);padding:6px 12px;border-radius:4px;white-space:nowrap;transition:background .15s,color .15s;border:1px solid transparent}
.nav-cat-link:hover,.nav-cat-link.active{background:rgba(245,166,35,.12);color:var(--amber);border-color:rgba(245,166,35,.2)}
.nav-cat-group{font-size:.7rem;color:rgba(245,166,35,.5);letter-spacing:2px;text-transform:uppercase;padding:6px 12px 6px 0;display:flex;align-items:center}

/* BREADCRUMB */
.breadcrumb{max-width:1200px;margin:0 auto;padding:10px 40px;font-size:.78rem;color:var(--faint)}
.breadcrumb a{color:var(--amber)}
.breadcrumb span{margin:0 6px}

/* SEARCH */
.search-wrap{background:var(--smoke);border-bottom:1px solid rgba(245,166,35,.12);padding:14px 40px}
.search-inner{max-width:1200px;margin:0 auto;display:flex;gap:10px}
.search-input{flex:1;background:rgba(255,255,255,.06);border:1px solid rgba(245,166,35,.3);border-radius:6px;color:var(--cream);font-size:1rem;padding:14px 20px;outline:none;transition:border-color .15s}
.search-input::placeholder{color:rgba(253,246,227,.35)}
.search-input:focus{border-color:var(--amber)}
.search-btn{background:var(--amber);color:var(--ink);border:none;border-radius:6px;font-weight:700;font-size:.95rem;letter-spacing:1px;text-transform:uppercase;padding:14px 24px;cursor:pointer;transition:background .15s,transform .15s;white-space:nowrap}
.search-btn:hover{background:#ffb733;transform:translateY(-1px)}

/* HERO */
.hero{padding:70px 40px 50px;max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 340px;gap:60px;align-items:center}
.hero-left{}
.hero-tag{display:inline-block;background:var(--red);color:#fff;font-size:.72rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;padding:6px 14px;border-radius:2px;margin-bottom:20px}
.hero h1{font-family:'Bebas Neue',cursive;font-size:clamp(3.5rem,7vw,6.5rem);line-height:.95;color:var(--cream);letter-spacing:2px;margin-bottom:16px}
.hero h1 em{font-style:normal;color:var(--amber);display:block}
.hero-desc{font-size:1.05rem;color:var(--dim);line-height:1.75;max-width:520px;margin-bottom:32px}
.hero-btns{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:24px}
.btn-primary{display:inline-block;background:var(--amber);color:var(--ink);font-weight:700;font-size:1rem;letter-spacing:1px;text-transform:uppercase;padding:16px 36px;border-radius:4px;transition:background .15s,transform .15s}
.btn-primary:hover{background:#ffb733;transform:translateY(-2px)}
.btn-ghost{display:inline-block;border:2px solid rgba(253,246,227,.25);color:var(--dim);font-weight:500;font-size:.92rem;padding:14px 28px;border-radius:4px;transition:border-color .15s,color .15s}
.btn-ghost:hover{border-color:var(--amber);color:var(--amber)}
.trust-row{display:flex;gap:20px;flex-wrap:wrap}
.trust-item{font-size:.8rem;color:var(--faint)}
.trust-item::before{content:'✓ ';color:var(--amber);font-weight:700}

/* STAT BOX */
.stat-box{background:var(--smoke);border:1px solid rgba(245,166,35,.15);border-radius:12px;padding:32px 28px;text-align:center}
.stat-emoji{font-size:3.5rem;margin-bottom:14px;display:block}
.stat-num{font-family:'Bebas Neue',cursive;font-size:4rem;color:var(--amber);line-height:1;letter-spacing:2px}
.stat-label{font-size:.82rem;color:rgba(253,246,227,.5);margin-top:8px;letter-spacing:1px;text-transform:uppercase}
.stat-divider{border:none;border-top:1px solid rgba(245,166,35,.1);margin:20px 0}
.mini-stats{display:grid;grid-template-columns:1fr 1fr;gap:14px;text-align:center}
.mini-num{font-family:'Bebas Neue',cursive;font-size:1.8rem;color:var(--cream);letter-spacing:1px}
.mini-label{font-size:.7rem;color:rgba(253,246,227,.4);text-transform:uppercase;letter-spacing:1px}

/* TRUST BADGES STRIP */
.trust-strip{background:#110f0b;border-top:1px solid rgba(245,166,35,.08);border-bottom:1px solid rgba(245,166,35,.08);padding:16px 40px}
.trust-strip-inner{max-width:1200px;margin:0 auto;display:flex;gap:0;flex-wrap:wrap;justify-content:space-between}
.trust-badge{display:flex;align-items:center;gap:8px;padding:8px 16px;font-size:.8rem;color:rgba(253,246,227,.6)}
.trust-badge-icon{font-size:1.2rem}

/* SECTION */
.section{max-width:1200px;margin:0 auto;padding:60px 40px}
.sec-header{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:30px;border-bottom:1px solid rgba(245,166,35,.15);padding-bottom:14px}
.sec-title{font-family:'Bebas Neue',cursive;font-size:2.6rem;color:var(--cream);letter-spacing:2px}
.sec-link{font-size:.82rem;color:var(--amber);font-weight:700;letter-spacing:1px;text-transform:uppercase}

/* CATEGORY GRIDS */
.cat-grid-5{display:grid;grid-template-columns:repeat(5,1fr);gap:2px}
.cat-grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:2px}
.cat-grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:2px}
.cat-card{background:var(--smoke);padding:28px 20px;display:flex;flex-direction:column;gap:8px;transition:background .15s;border:1px solid transparent}
.cat-card:hover{background:#28261f;border-color:rgba(245,166,35,.25)}
.cat-icon{font-size:2rem}
.cat-name{font-family:'Bebas Neue',cursive;font-size:1.3rem;color:var(--cream);letter-spacing:1px}
.cat-desc{font-size:.78rem;color:rgba(253,246,227,.45);line-height:1.5;flex:1}
.cat-arrow{font-size:.75rem;color:var(--amber);font-weight:700;letter-spacing:1px;text-transform:uppercase}

/* PROMO */
.promo-stripe{background:var(--red);padding:44px 40px;text-align:center}
.promo-inner{max-width:700px;margin:0 auto}
.promo-kicker{font-size:.78rem;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,.65);margin-bottom:10px}
.promo-headline{font-family:'Bebas Neue',cursive;font-size:clamp(2rem,5vw,3.5rem);color:#fff;letter-spacing:2px;margin-bottom:10px}
.promo-sub{font-size:1rem;color:rgba(255,255,255,.75);margin-bottom:24px}
.btn-white{display:inline-block;background:#fff;color:var(--red);font-weight:700;font-size:.95rem;letter-spacing:1px;text-transform:uppercase;padding:14px 40px;border-radius:4px;transition:transform .15s,box-shadow .15s}
.btn-white:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.3)}

/* REVIEWS */
.reviews-section{background:var(--smoke);padding:60px 40px}
.reviews-inner{max-width:1200px;margin:0 auto}
.reviews-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:30px}
.review-card{background:var(--ink);border:1px solid rgba(245,166,35,.12);border-radius:10px;padding:24px}
.review-stars{color:var(--amber);font-size:1rem;margin-bottom:10px;letter-spacing:2px}
.review-text{font-size:.88rem;color:var(--dim);line-height:1.7;margin-bottom:14px;font-style:italic}
.review-author{font-size:.78rem;color:var(--faint);font-weight:700}
.review-flag{font-size:1rem}

/* SEO CONTENT */
.seo-section{background:#0f0e0b;padding:60px 40px;border-top:1px solid rgba(245,166,35,.06)}
.seo-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr;gap:60px}
.seo-body{font-size:.95rem;color:var(--dim);line-height:1.9;margin-bottom:20px}
.seo-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.seo-link{background:rgba(245,166,35,.08);border:1px solid rgba(245,166,35,.15);border-radius:4px;padding:6px 14px;font-size:.8rem;color:rgba(253,246,227,.65);transition:all .15s}
.seo-link:hover{background:rgba(245,166,35,.2);color:var(--amber)}
.seo-sidebar h3{font-family:'Bebas Neue',cursive;font-size:1.6rem;color:var(--amber);letter-spacing:2px;margin-bottom:16px}
.quick-links{display:flex;flex-direction:column;gap:6px}
.quick-link{padding:10px 14px;background:rgba(245,166,35,.06);border:1px solid rgba(245,166,35,.1);border-radius:4px;font-size:.85rem;color:var(--dim);transition:all .15s;display:flex;align-items:center;gap:8px}
.quick-link:hover{background:rgba(245,166,35,.15);color:var(--amber);border-color:rgba(245,166,35,.3)}

/* POPULAR SEARCHES */
.popular-wrap{max-width:1200px;margin:0 auto;padding:0 40px 50px}
.popular-title{font-family:'Bebas Neue',cursive;font-size:1.4rem;color:rgba(253,246,227,.3);letter-spacing:2px;margin-bottom:12px}
.pop-tags{display:flex;flex-wrap:wrap;gap:8px}
.pop-tag{background:rgba(245,166,35,.07);border:1px solid rgba(245,166,35,.15);border-radius:100px;padding:7px 16px;font-size:.8rem;color:var(--faint);cursor:pointer;transition:all .15s}
.pop-tag:hover{background:rgba(245,166,35,.2);color:var(--amber);border-color:var(--amber)}

/* RELATED */
.crosslinks{background:#0a0908;border-top:1px solid rgba(245,166,35,.08);padding:50px 40px}
.crosslinks-inner{max-width:1200px;margin:0 auto}
.cross-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:2px;margin-top:20px}
.cross-card{background:var(--smoke);padding:20px 16px;display:flex;flex-direction:column;gap:6px;transition:background .15s;border:1px solid transparent}
.cross-card:hover{background:#28261f;border-color:rgba(245,166,35,.2)}
.cross-icon{font-size:1.4rem}
.cross-name{font-family:'Bebas Neue',cursive;font-size:1.1rem;color:var(--cream);letter-spacing:1px}
.cross-arrow{font-size:.72rem;color:var(--amber);font-weight:700}

/* BOTTOM CTA */
.bottom-cta{background:linear-gradient(135deg,#1a1208,#0c0b09);border-top:3px solid var(--amber);padding:80px 40px;text-align:center}
.bottom-cta-inner{max-width:700px;margin:0 auto}
.bottom-cta h2{font-family:'Bebas Neue',cursive;font-size:clamp(3rem,7vw,5.5rem);color:var(--cream);letter-spacing:2px;line-height:.95;margin-bottom:20px}
.bottom-cta h2 span{color:var(--amber)}
.bottom-cta p{font-size:1rem;color:var(--dim);margin-bottom:36px;line-height:1.7}

/* FOOTER */
footer{background:#060504;border-top:1px solid rgba(245,166,35,.08);padding:50px 40px 30px}
.footer-inner{max-width:1200px;margin:0 auto}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:30px;margin-bottom:30px}
.footer-brand{font-family:'Bebas Neue',cursive;font-size:1.8rem;color:var(--amber);letter-spacing:2px;margin-bottom:10px}
.footer-tagline{font-size:.82rem;color:var(--faint);line-height:1.7;margin-bottom:16px}
.footer-ship{font-size:.75rem;color:rgba(245,166,35,.6);margin-top:8px}
.footer-col h4{font-size:.72rem;letter-spacing:2px;text-transform:uppercase;color:rgba(253,246,227,.22);margin-bottom:12px}
.footer-col a{display:block;font-size:.8rem;color:var(--faint);padding:3px 0;transition:color .15s}
.footer-col a:hover{color:var(--amber)}
.footer-bottom{border-top:1px solid rgba(255,255,255,.04);padding-top:18px;font-size:.7rem;color:rgba(253,246,227,.18);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
.payment-icons{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.payment-icon{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:4px;padding:4px 10px;font-size:.72rem;color:rgba(253,246,227,.4)}

/* RESPONSIVE */
@media(max-width:1000px){
  .hero{grid-template-columns:1fr;gap:30px;padding:50px 24px 40px}
  .stat-box{display:none}
  .cat-grid-5{grid-template-columns:repeat(3,1fr)}
  .cat-grid-4{grid-template-columns:repeat(2,1fr)}
  .reviews-grid{grid-template-columns:1fr}
  .seo-inner{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr 1fr}
  .cross-grid{grid-template-columns:repeat(3,1fr)}
  .nav-cats,.search-wrap,.breadcrumb,.section,.popular-wrap,.crosslinks,.reviews-section,.seo-section{padding-left:24px;padding-right:24px}
  .nav-top{padding:12px 24px}
  .trust-strip{padding:12px 24px}
  .bottom-cta{padding:60px 24px}
  footer{padding:40px 24px 24px}
}
@media(max-width:600px){
  .cat-grid-5,.cat-grid-4,.cat-grid-3,.cross-grid{grid-template-columns:repeat(2,1fr)}
  .hero h1{font-size:3.2rem}
  .btn-ghost{display:none}
  .footer-grid{grid-template-columns:1fr}
  .trust-strip-inner{justify-content:flex-start}
}
"""

# ─────────────────────────────────────────────────────────
# JAVASCRIPT ENGINE
# ─────────────────────────────────────────────────────────
def make_js(page_key):
    page_data = {pk: {"file":pd["file"],"icon":pd["icon"],"nav_group":pd["nav_group"]} for pk,pd in PAGES.items()}
    return f"""
const AFF_BASE  = "{AFF_BASE}";
const CAT_URLS  = {json.dumps(CAT_URLS)};
const PAGES     = {json.dumps(page_data)};
const LANGS     = {json.dumps(LANGS)};
const POPULAR   = {json.dumps(POPULAR_SEARCHES)};
const NAV_GROUPS= {json.dumps(NAV_GROUPS)};
const CURRENT   = "{page_key}";

function aff(catKey, search){{
  let dest;
  if(catKey && CAT_URLS[catKey]) dest = CAT_URLS[catKey];
  else if(search) dest = "https://www.halloweencostumes.com/search?q=" + encodeURIComponent(search);
  else return AFF_BASE;
  return AFF_BASE + "&url=" + encodeURIComponent(dest);
}}

function goSearch(term){{
  const q = (term || document.getElementById('q').value).trim();
  window.open(q ? aff(null,q) : AFF_BASE,'_blank','noopener,noreferrer');
}}

function detectLang(){{
  const p = new URLSearchParams(window.location.search);
  const u = p.get('lang');
  if(u && LANGS[u]) return u;
  const b = (navigator.language||'en').split('-')[0].toLowerCase();
  return LANGS[b] ? b : 'en';
}}

function buildPopularTags(){{
  const wrap = document.getElementById('pop-tags');
  if(!wrap) return;
  wrap.innerHTML = '';
  POPULAR.forEach(term => {{
    const s = document.createElement('span');
    s.className = 'pop-tag';
    s.textContent = term;
    s.onclick = () => goSearch(term);
    wrap.appendChild(s);
  }});
}}

function buildCrosslinks(){{
  const grid = document.getElementById('cross-grid');
  if(!grid) return;
  grid.innerHTML = '';
  let count = 0;
  Object.entries(PAGES).forEach(([pk,pd]) => {{
    if(pk === CURRENT || count >= 10) return;
    const a = document.createElement('a');
    a.className = 'cross-card';
    a.href = pd.file;
    const nameMap = {{
      index:'Home', womens:"Women's Costumes", mens:"Men's Costumes",
      girls:"Girls' Costumes", boys:"Boys' Costumes", kids:'Kids Costumes',
      teen:'Teen Costumes', toddler:'Toddler Costumes', baby:'Baby Costumes',
      adult:'Adult Costumes', scary:'Scary Costumes', funny:'Funny Costumes',
      sexy:'Sexy Costumes', couples:'Couples Costumes', group:'Group Costumes',
      new2026:'New 2026', plussize:'Plus Size', wholesale:'Wholesale',
      pet:'Pet Costumes', accessories:'Accessories', wigs:'Wigs',
      masks:'Masks', decorations:'Decorations', sale:'Sale', lastminute:'Last Minute'
    }};
    a.innerHTML = `<span class="cross-icon">${{pd.icon}}</span><div class="cross-name">${{nameMap[pk]||pk}}</div><div class="cross-arrow">→</div>`;
    grid.appendChild(a);
    count++;
  }});
}}

function buildFooter(){{
  const LABELS = {{
    womens:"👩 Women's", mens:"👨 Men's", girls:"👧 Girls'", boys:"👦 Boys'",
    kids:'👶 Kids', teen:'🧑 Teen', toddler:'🍼 Toddler', baby:'👼 Baby',
    adult:'🎭 Adult', scary:'💀 Scary', funny:'😂 Funny', sexy:'💋 Sexy',
    couples:'💑 Couples', group:'👨‍👩‍👧‍👦 Group', new2026:'✨ New 2026',
    plussize:'💎 Plus Size', wholesale:'🛍️ Wholesale', pet:'🐾 Pet',
    accessories:'🎩 Accessories', wigs:'💇 Wigs', masks:'👺 Masks',
    decorations:'🏚️ Decorations', indoordecor:'🕯️ Indoor Decor', outdoordecor:'🌙 Outdoor Decor', props:'🦴 Props', animatronics:'🤖 Animatronics', inflatable:'🎈 Inflatable', collectibles:'🏆 Collectibles', licensed:'™️ Licensed', sale:'💰 Sale', lastminute:'⚡ Last Minute', tween:'🧒 Tween', medieval:'⚔️ Medieval', videogame:'🎮 Video Games', themes:'🌟 Themes', comiccon:'🦸 Comic Con', sizeguide:'📏 Size Guide'
  }};
  const fc1 = document.getElementById('fc1-links');
  if(fc1){{
    fc1.innerHTML = '';
    ['womens','mens','girls','boys','kids','tween','teen','toddler','baby','sizeguide'].forEach(pk => {{
      if(!PAGES[pk]) return;
      const a = document.createElement('a');
      a.href = PAGES[pk].file;
      a.textContent = LABELS[pk] || pk;
      fc1.appendChild(a);
    }});
  }}
  const fc2 = document.getElementById('fc2-links');
  if(fc2){{
    fc2.innerHTML = '';
    ['adult','scary','funny','sexy','couples','group','new2026','plussize','wholesale','pet','videogame','themes','comiccon','medieval','kpop','horror','decades','occupation','fantasy','anime','movies','tvshows','genshin','leagueoflegends','overwatch','finalfantasy','deadbydaylight','jujutsukaisen','hazbinhotel','frieren','onepiececosplay','nier','cyberpunk','zelda','devilmaycry'].forEach(pk => {{
      if(!PAGES[pk]) return;
      const a = document.createElement('a');
      a.href = PAGES[pk].file;
      a.textContent = LABELS[pk] || pk;
      fc2.appendChild(a);
    }});
  }}
  const fc3 = document.getElementById('fc3-links');
  if(fc3){{
    fc3.innerHTML = '';
    ['addamsfamily','beetlejuice','horror','fnaf','scooby','harrypotter','cosplayshoes','convention','lolita','swimwear','kawaii','casualwear','weeklydeals','preorder','accessories','wigs','masks','decorations','indoordecor','outdoordecor','props','animatronics','inflatable','collectibles','licensed','partysupplies','diy','gifts','gamer','clothing','yearround','sale','lastminute'].forEach(pk => {{
      if(!PAGES[pk]) return;
      const a = document.createElement('a');
      a.href = PAGES[pk].file;
      a.textContent = LABELS[pk] || pk;
      fc3.appendChild(a);
    }});
  }}
  const fc4 = document.getElementById('fc4-links');
  if(fc4){{
    fc4.innerHTML = '';
    const popular = [
      ['spider costume','🕷 Spider-Man'],['witch costume','🧙 Witch'],
      ['vampire costume','🧛 Vampire'],['pirate costume','🏴‍☠️ Pirate'],
      ['zombie costume','🧟 Zombie'],['ninja costume','🥷 Ninja'],
      ['skeleton costume','💀 Skeleton'],['clown costume','🤡 Clown'],
      ['dinosaur costume','🦖 Dinosaur'],['werewolf costume','🐺 Werewolf'],
    ];
    popular.forEach(([kw,label]) => {{
      const a = document.createElement('a');
      a.href = aff(null,kw);
      a.target = '_blank';
      a.rel = 'nofollow noopener';
      a.textContent = label;
      fc4.appendChild(a);
    }});
  }}
  const fc5 = document.getElementById('fc5-links');
  if(fc5){{
    fc5.innerHTML = '';
    Object.entries(LANGS).forEach(([lc,ld]) => {{
      const a = document.createElement('a');
      a.href = '?lang='+lc;
      a.textContent = ld.flag+' '+ld.name;
      fc5.appendChild(a);
    }});
  }}
}}

function applyLang(lang){{
  document.documentElement.lang = lang;
  document.documentElement.dir = (LANGS[lang]||LANGS.en).dir||'ltr';
  const sel = document.getElementById('lang-sel');
  if(sel) sel.value = lang;
}}

document.addEventListener('DOMContentLoaded',()=>{{
  const lang = detectLang();
  const sel = document.getElementById('lang-sel');
  if(sel){{
    sel.value = lang;
    sel.addEventListener('change',()=>{{
      const url = new URL(window.location);
      url.searchParams.set('lang',sel.value);
      window.history.pushState({{}},'',url);
      applyLang(sel.value);
    }});
  }}
  const params = new URLSearchParams(window.location.search);
  const qs = params.get('q');
  if(qs){{
    const qi = document.getElementById('q');
    if(qi) qi.value = qs;
    setTimeout(()=>window.open(aff(null,qs),'_blank','noopener,noreferrer'),300);
  }}
  buildPopularTags();
  buildCrosslinks();
  buildFooter();
  applyLang(lang);
  document.getElementById('search-btn').addEventListener('click',()=>goSearch());
  document.getElementById('q').addEventListener('keydown',e=>{{if(e.key==='Enter')goSearch();}});
}});
"""

# ─────────────────────────────────────────────────────────
# HTML BUILDER
# ─────────────────────────────────────────────────────────
def make_page(page_key):
    p = PAGES[page_key]
    cat_key = p["cat_key"]
    page_url = f"{SITE_URL}/{p['file']}"

    # Breadcrumb
    if page_key == "index":
        breadcrumb_html = ""
        breadcrumb_schema = ""
    else:
        breadcrumb_html = f"""<div class="breadcrumb"><a href="index.html">🎃 Home</a><span>›</span><span>{p['en_h1']}</span></div>"""
        breadcrumb_schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},
  {{"@type":"ListItem","position":2,"name":"{p['en_h1']}","item":"{page_url}"}}
]}}</script>"""

    # Hreflang
    hreflang = "\n  ".join([f'<link rel="alternate" hreflang="{lc}" href="{page_url}?lang={lc}">' for lc in LANGS])
    hreflang += f'\n  <link rel="alternate" hreflang="x-default" href="{page_url}">'

    # Schema
    schema = f"""{{"@context":"https://schema.org","@type":"{p.get('schema_type','CollectionPage')}",
"url":"{page_url}","name":"{p['en_title']}","description":"{p['en_desc']}",
"keywords":"{p.get('keywords','')}",
"publisher":{{"@type":"Organization","name":"HalloweenCostumes 2026","url":"{SITE_URL}/"}}}}"""

    # Nav mega menu — all pages grouped
    nav_links = ""
    current_group = None
    for pk, pd in PAGES.items():
        if pk == "index":
            continue
        grp = pd.get("nav_group", "type")
        if grp != current_group:
            if grp in NAV_GROUPS:
                nav_links += f'<span class="nav-cat-group">{NAV_GROUPS[grp]["icon"]} {NAV_GROUPS[grp]["label"]}</span>'
            current_group = grp
        active = ' active' if pk == page_key else ''
        nav_links += f'<a href="{pd["file"]}" class="nav-cat-link{active}">{pd["icon"]} {pd["en_h1"].split(" ")[0]} {pd["en_h1"].split(" ")[1] if len(pd["en_h1"].split())>1 else ""}</a>'

    # Category cards — homepage shows all in groups, category pages show 5 related
    if page_key == "index":
        # Gender grid
        gender_cards = "".join([
            f'<a class="cat-card" href="{PAGES[pk]["file"]}"><span class="cat-icon">{PAGES[pk]["icon"]}</span><div class="cat-name">{PAGES[pk]["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{PAGES[pk]["en_h1sub"]}</div><div class="cat-arrow">Shop Now →</div></a>'
            for pk in ["womens","mens","girls","boys","kids","tween","teen","toddler","baby","sizeguide"]
        ])
        # Type grid
        type_cards = "".join([
            f'<a class="cat-card" href="{PAGES[pk]["file"]}"><span class="cat-icon">{PAGES[pk]["icon"]}</span><div class="cat-name">{PAGES[pk]["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{PAGES[pk]["en_h1sub"]}</div><div class="cat-arrow">Shop Now →</div></a>'
            for pk in ["adult","scary","funny","sexy","couples","group","new2026","plussize","wholesale","pet","licensed","inflatable","medieval","videogame","themes","comiccon","kpop","horror","decades","occupation","fantasy"]
        ])
        # Accessories + extras
        extra_cards = "".join([
            f'<a class="cat-card" href="{PAGES[pk]["file"]}"><span class="cat-icon">{PAGES[pk]["icon"]}</span><div class="cat-name">{PAGES[pk]["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{PAGES[pk]["en_h1sub"]}</div><div class="cat-arrow">Shop Now →</div></a>'
            for pk in ["animatronics","props","indoordecor","outdoordecor","collectibles","accessories","wigs","masks","decorations","partysupplies","diy","anime","gamer","gifts","movies","tvshows","clothing","genshin","leagueoflegends","overwatch","finalfantasy","jujutsukaisen","hazbinhotel","onepiececosplay","nier","cyberpunk","zelda","devilmaycry","cosplayshoes","convention","lolita","swimwear","kawaii","casualwear","weeklydeals","preorder","yearround","sale","lastminute"]
        ])
        categories_html = f"""
<section class="section">
  <div class="sec-header"><h2 class="sec-title">Shop by Gender & Age</h2><a href="{aff('home')}" class="sec-link" target="_blank" rel="nofollow noopener">All Costumes →</a></div>
  <div class="cat-grid-5">{gender_cards}</div>
</section>
<section class="section" style="padding-top:0">
  <div class="sec-header"><h2 class="sec-title">Shop by Style</h2><a href="{aff('home')}" class="sec-link" target="_blank" rel="nofollow noopener">All Styles →</a></div>
  <div class="cat-grid-5">{type_cards}</div>
</section>
<section class="section" style="padding-top:0">
  <div class="sec-header"><h2 class="sec-title">Accessories, Decor & Deals</h2><a href="{aff('home')}" class="sec-link" target="_blank" rel="nofollow noopener">Shop All →</a></div>
  <div class="cat-grid-3">{extra_cards}</div>
</section>"""
    else:
        related = [k for k in PAGES if k not in ("index", page_key)][:4]
        related_cards = "".join([
            f'<a class="cat-card" href="{PAGES[pk]["file"]}"><span class="cat-icon">{PAGES[pk]["icon"]}</span><div class="cat-name">{PAGES[pk]["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{PAGES[pk]["en_h1sub"]}</div><div class="cat-arrow">Shop →</div></a>'
            for pk in related
        ])
        categories_html = f"""
<section class="section">
  <div class="sec-header"><h2 class="sec-title">Featured Categories</h2><a href="index.html" class="sec-link">All Categories →</a></div>
  <div class="cat-grid-4">{related_cards}</div>
</section>"""

    # Reviews section
    reviews_html = "".join([
        f"""<div class="review-card">
  <div class="review-stars">{'⭐' * r['rating']}</div>
  <p class="review-text">"{r['text']}"</p>
  <div class="review-author"><span class="review-flag">{r['country']}</span> {r['name']}</div>
</div>"""
        for r in REVIEWS
    ])

    # Trust badges
    trust_badges_html = "".join([
        f'<div class="trust-badge"><span class="trust-badge-icon">{b["icon"]}</span>{b["label"]}</div>'
        for b in TRUST_BADGES
    ])

    # SEO sidebar quick links
    sidebar_links = "".join([
        f'<a class="quick-link" href="{PAGES[pk]["file"]}">{PAGES[pk]["icon"]} {PAGES[pk]["en_h1"]}</a>'
        for pk in list(PAGES.keys())[:8] if pk != page_key
    ])

    # Payment icons (beats halloweencostumes.com by listing more)
    payments = ["💳 Visa","💳 Mastercard","💳 Amex","🍎 Apple Pay","🅿️ PayPal","💰 Sezzle","🔷 Discover","🇯 JCB"]
    payment_html = "".join([f'<span class="payment-icon">{p}</span>' for p in payments])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="google-site-verification" content="{GOOGLE_VERIFY}"/>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['en_title']}</title>
  <meta name="description" content="{p['en_desc']}">
  <meta name="keywords" content="{p.get('keywords','')}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="author" content="{OWNER}">
  <meta name="theme-color" content="#f5a623">
  <link rel="canonical" href="{page_url}">
  {hreflang}
  <meta property="og:type" content="website">
  <meta property="og:title" content="{p['en_title']}">
  <meta property="og:description" content="{p['en_desc']}">
  <meta property="og:url" content="{page_url}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p['en_title']}">
  <meta name="twitter:description" content="{p['en_desc']}">
  <script type="application/ld+json">{schema}</script>
  {breadcrumb_schema}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>

<div class="topbar">
  <span class="marquee">
    🎃 HalloweenCostumes 2026 &nbsp;·&nbsp; 🌍 Ships to {SHIP_COUNTRIES} Countries &nbsp;·&nbsp;
    👩 Women's &nbsp;·&nbsp; 👨 Men's &nbsp;·&nbsp; 👧 Girls' &nbsp;·&nbsp; 👦 Boys' &nbsp;·&nbsp;
    💀 Scary &nbsp;·&nbsp; 😂 Funny &nbsp;·&nbsp; 💋 Sexy &nbsp;·&nbsp; 💑 Couples &nbsp;·&nbsp;
    🍼 Toddler &nbsp;·&nbsp; 👼 Baby &nbsp;·&nbsp; 🐾 Pets &nbsp;·&nbsp; 🎩 Accessories &nbsp;·&nbsp;
    🏚️ Decorations &nbsp;·&nbsp; 💰 Sale &nbsp;·&nbsp; ⚡ Last Minute &nbsp;·&nbsp; ✨ New 2026
  </span>
</div>

<nav>
  <div class="nav-top">
    <a href="index.html" class="nav-logo">🎃 HalloweenCostumes</a>
    <div class="nav-right">
      <select class="lang-sel" id="lang-sel" aria-label="Language">
        {''.join(f'<option value="{lc}">{ld["flag"]} {ld["name"]}</option>' for lc,ld in LANGS.items())}
      </select>
      <a href="{aff(cat_key)}" class="nav-cta" target="_blank" rel="nofollow noopener">🎃 Shop Now</a>
    </div>
  </div>
  <div class="nav-cats">
    <a href="index.html" class="nav-cat-link {'active' if page_key=='index' else ''}">🎃 All</a>
    {nav_links}
  </div>
</nav>

{breadcrumb_html}

<div class="search-wrap" role="search">
  <div class="search-inner">
    <input id="q" class="search-input" type="search"
      placeholder='Search 10,000+ costumes — e.g. "Mandalorian", "Wednesday Addams", "witch"…'
      autocomplete="off" aria-label="Search Halloween costumes">
    <button id="search-btn" class="search-btn">🔍 Find Costume</button>
  </div>
</div>

<main>

<section class="hero">
  <div class="hero-left">
    <span class="hero-tag">{p['icon']} {p['en_h1']} · {TODAY}</span>
    <h1>{p['en_h1']}<em>{p['en_h1sub']}</em></h1>
    <p class="hero-desc">{p['en_desc']}</p>
    <div class="hero-btns">
      <a href="{aff(cat_key)}" class="btn-primary" target="_blank" rel="nofollow noopener">
        {p['icon']} Shop {p['en_h1'].split()[0]} {p['en_h1'].split()[1] if len(p['en_h1'].split())>1 else ''} Now
      </a>
      <a href="{aff('sale')}" class="btn-ghost" target="_blank" rel="nofollow noopener">View Sale Deals →</a>
    </div>
    <div class="trust-row">
      <span class="trust-item">Secure Checkout</span>
      <span class="trust-item">{SHIP_COUNTRIES} Countries</span>
      <span class="trust-item">10,000+ Costumes</span>
      <span class="trust-item">Best Price Guarantee</span>
    </div>
  </div>
  <div class="stat-box">
    <span class="stat-emoji">{p['icon']}</span>
    <div class="stat-num">10K+</div>
    <div class="stat-label">Costume Styles</div>
    <hr class="stat-divider">
    <div class="mini-stats">
      <div><div class="mini-num">{SHIP_COUNTRIES}</div><div class="mini-label">Countries</div></div>
      <div><div class="mini-num">Daily</div><div class="mini-label">New Deals</div></div>
      <div><div class="mini-num">$10+</div><div class="mini-label">From</div></div>
      <div><div class="mini-num">All</div><div class="mini-label">Sizes</div></div>
    </div>
  </div>
</section>

<div class="trust-strip">
  <div class="trust-strip-inner">{trust_badges_html}</div>
</div>

{categories_html}

<div class="promo-stripe">
  <div class="promo-inner">
    <p class="promo-kicker">🔥 Today's Best Deal</p>
    <h2 class="promo-headline">{p['en_h1']}</h2>
    <p class="promo-sub">{p['en_h1sub']} — Updated {TODAY}</p>
    <a href="{aff(cat_key)}" class="btn-white" target="_blank" rel="nofollow noopener">Claim This Deal →</a>
  </div>
</div>

<div class="reviews-section">
  <div class="reviews-inner">
    <div class="sec-header">
      <h2 class="sec-title">⭐ Customer Reviews</h2>
      <span class="sec-link">Verified Worldwide Shoppers</span>
    </div>
    <div class="reviews-grid">{reviews_html}</div>
  </div>
</div>

<div class="seo-section">
  <div class="seo-inner">
    <div>
      <h2 style="font-family:'Bebas Neue',cursive;font-size:2rem;color:var(--amber);letter-spacing:2px;margin-bottom:16px;">{p['en_h1']}</h2>
      <p class="seo-body">{p['en_body']}</p>
      <div class="seo-links">
        {''.join([f'<a class="seo-link" href="{PAGES[pk]["file"]}">{PAGES[pk]["icon"]} {PAGES[pk]["en_h1"]}</a>' for pk in list(PAGES.keys())[:12] if pk != page_key])}
        {''.join([f'<a class="seo-link" href="{aff(None,s)}" target="_blank" rel="nofollow noopener">{s.title()}</a>' for s in POPULAR_SEARCHES[:10]])}
      </div>
    </div>
    <div class="seo-sidebar">
      <h3>Quick Links</h3>
      <div class="quick-links">{sidebar_links}</div>
    </div>
  </div>
</div>

<div class="popular-wrap">
  <div class="popular-title">🔥 Popular Searches</div>
  <div class="pop-tags" id="pop-tags"></div>
</div>

<div class="crosslinks">
  <div class="crosslinks-inner">
    <div class="sec-header"><h2 class="sec-title">More Halloween Categories</h2></div>
    <div class="cross-grid" id="cross-grid"></div>
  </div>
</div>

<div class="bottom-cta">
  <div class="bottom-cta-inner">
    <h2>Don't Miss<br><span>Halloween 2026</span></h2>
    <p>10,000+ costumes. Ships to {SHIP_COUNTRIES} countries. Deals updated every day. New styles added daily. Find yours before they sell out.</p>
    <a href="{aff(cat_key)}" class="btn-primary" style="font-size:1.05rem;padding:20px 50px;" target="_blank" rel="nofollow noopener">
      {p['icon']} Shop {p['en_h1']} Now
    </a>
  </div>
</div>

</main>

<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">🎃 HalloweenCostumes 2026</div>
        <p class="footer-tagline">The world's #1 Halloween costume destination. 10,000+ costumes, ships to {SHIP_COUNTRIES} countries, updated daily. Every size, every style, every age.</p>
        <p class="footer-ship">🌍 International shipping: USA · UK · Canada · Australia · Germany · France · Japan · Brazil · Mexico · UAE · India + {SHIP_COUNTRIES} total</p>
        <div class="payment-icons">{payment_html}</div>
      </div>
      <div class="footer-col">
        <h4>By Person</h4>
        <div id="fc1-links"></div>
      </div>
      <div class="footer-col">
        <h4>By Style</h4>
        <div id="fc2-links"></div>
      </div>
      <div class="footer-col">
        <h4>Accessories & More</h4>
        <div id="fc3-links"></div>
      </div>
      <div class="footer-col">
        <h4>Popular & Languages</h4>
        <div id="fc4-links"></div>
        <br>
        <h4>Languages</h4>
        <div id="fc5-links"></div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 {OWNER} — Affiliate links via LinkConnector ID {LC_ID}. Commissions earned on qualifying purchases.</span>
      <span>Updated: {TODAY}</span>
    </div>
  </div>
</footer>

<script>{make_js(page_key)}</script>
</body>
</html>"""
    return html


# ─────────────────────────────────────────────────────────
# 404 PAGE
# ─────────────────────────────────────────────────────────
def make_404():
    links = "".join([
        f'<a class="quick-tag" href="{pd["file"]}">{pd["icon"]} {pd["en_h1"].split()[0]} {pd["en_h1"].split()[1] if len(pd["en_h1"].split())>1 else ""}</a>'
        for pk,pd in list(PAGES.items())[:12]
    ])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Not Found | HalloweenCostumes 2026</title>
  <meta name="robots" content="noindex, follow">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root{{--ink:#0c0b09;--amber:#f5a623;--cream:#fdf6e3;--red:#e8321a;--smoke:#1e1c18}}
    *{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:'DM Sans',sans-serif;background:var(--ink);color:var(--cream);min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;text-align:center;overflow:hidden}}
    a{{color:inherit;text-decoration:none}}
    .spook{{position:fixed;opacity:0;animation:float var(--d,6s) ease-in-out infinite var(--delay,0s);pointer-events:none}}
    @keyframes float{{0%{{opacity:0;transform:translateY(110vh)}}10%{{opacity:.3}}90%{{opacity:.3}}100%{{opacity:0;transform:translateY(-10vh)}}}}
    .num{{font-family:'Bebas Neue',cursive;font-size:clamp(7rem,22vw,14rem);line-height:1;color:var(--amber);text-shadow:0 0 40px rgba(245,166,35,.4),6px 6px 0 var(--red);letter-spacing:4px;animation:glitch 4s ease-in-out infinite}}
    @keyframes glitch{{0%,90%,100%{{text-shadow:0 0 40px rgba(245,166,35,.4),6px 6px 0 var(--red);transform:none}}92%{{text-shadow:-4px 0 var(--red),4px 0 #0ff;transform:skewX(-2deg)}}94%{{text-shadow:4px 0 var(--red),-4px 0 #0ff;transform:skewX(2deg)}}}}
    .ghost{{font-size:3.5rem;margin-bottom:12px;display:block;animation:bob 2s ease-in-out infinite}}
    @keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-10px)}}}}
    h1{{font-family:'Bebas Neue',cursive;font-size:clamp(1.8rem,5vw,3rem);letter-spacing:2px;margin-bottom:12px}}
    .sub{{font-size:1rem;color:rgba(253,246,227,.6);max-width:440px;line-height:1.7;margin-bottom:32px}}
    .cd-wrap{{font-size:.8rem;color:rgba(253,246,227,.35);letter-spacing:2px;text-transform:uppercase;margin-bottom:28px}}
    .cd-num{{color:var(--amber);font-family:'Bebas Neue',cursive;font-size:1.3rem}}
    .btn-p{{display:inline-block;background:var(--amber);color:var(--ink);font-weight:700;font-size:.95rem;letter-spacing:1px;text-transform:uppercase;padding:16px 36px;border-radius:4px;margin-bottom:32px}}
    .quick-title{{font-family:'Bebas Neue',cursive;font-size:1.3rem;color:rgba(253,246,227,.3);letter-spacing:2px;margin-bottom:12px}}
    .quick-grid{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;max-width:700px}}
    .quick-tag{{background:rgba(245,166,35,.08);border:1px solid rgba(245,166,35,.2);border-radius:100px;padding:7px 16px;font-size:.8rem;color:rgba(253,246,227,.6);transition:all .15s}}
    .quick-tag:hover{{background:rgba(245,166,35,.2);color:var(--amber)}}
    .footer-line{{position:fixed;bottom:14px;font-size:.7rem;color:rgba(253,246,227,.15)}}
  </style>
</head>
<body>
<div id="spooks"></div>
<span class="ghost">👻</span>
<div class="num">404</div>
<h1>This Page Got Spooked</h1>
<p class="sub">This costume vanished into the night — but 10,000+ Halloween costumes are still waiting for you.</p>
<div class="cd-wrap">Redirecting in <span class="cd-num" id="cd">5</span>...</div>
<a href="index.html" class="btn-p">🎃 Back to Halloween Costumes</a>
<div class="quick-title">Jump to a Category</div>
<div class="quick-grid">{links}</div>
<div class="footer-line">© 2026 {OWNER} | LinkConnector ID {LC_ID}</div>
<script>
  ['🎃','👻','💀','🕷','🦇','🧙','🧟','😱'].forEach(e=>{{
    for(let i=0;i<3;i++){{const s=document.createElement('div');s.className='spook';s.textContent=e;s.style.cssText=`left:${{Math.random()*100}}%;--d:${{5+Math.random()*8}}s;--delay:${{Math.random()*8}}s;font-size:${{1.5+Math.random()*2}}rem;`;document.getElementById('spooks').appendChild(s);}}
  }});
  let n=5;const cd=document.getElementById('cd');
  const t=setInterval(()=>{{n--;cd.textContent=n;if(n<=0){{clearInterval(t);window.location.href='index.html';}}}},1000);
</script>
</body>
</html>"""


# ─────────────────────────────────────────────────────────
# SITEMAP
# ─────────────────────────────────────────────────────────
def make_sitemap():
    urls = []
    for pk, pd in PAGES.items():
        page_url = f"{SITE_URL}/{pd['file']}"
        priority = "1.0" if pk == "index" else "0.9"
        lang_links = "\n    ".join([f'<xhtml:link rel="alternate" hreflang="{lc}" href="{page_url}?lang={lc}"/>' for lc in LANGS])
        urls.append(f"""  <url>
    <loc>{page_url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{priority}</priority>
    {lang_links}
    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url}"/>
  </url>""")
        for lc in LANGS:
            urls.append(f"  <url><loc>{page_url}?lang={lc}</loc><lastmod>{TODAY}</lastmod><changefreq>daily</changefreq><priority>0.75</priority></url>")
    # Blog index
    urls.append(f"  <url><loc>{SITE_URL}/blog.html</loc><lastmod>{TODAY}</lastmod><changefreq>daily</changefreq><priority>0.85</priority></url>")
    # Blog posts
    for post in BLOG_POSTS:
        urls.append(f"  <url><loc>{SITE_URL}/{post['file']}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    for kw in POPULAR_SEARCHES:
        urls.append(f"  <url><loc>{SITE_URL}/index.html?q={kw.replace(' ','+')}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.65</priority></url>")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>"""


# ─────────────────────────────────────────────────────────
# ROBOTS.TXT
# ─────────────────────────────────────────────────────────
def make_robots():
    return f"""# robots.txt — HalloweenCostumes 2026 | Updated: {TODAY}
User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
User-agent: Googlebot
Allow: /
Crawl-delay: 1
User-agent: Bingbot
Allow: /
Crawl-delay: 1
User-agent: YandexBot
Allow: /
Crawl-delay: 2
User-agent: Baiduspider
Allow: /
Crawl-delay: 2
User-agent: DuckDuckBot
Allow: /
User-agent: facebookexternalhit
Allow: /
User-agent: Twitterbot
Allow: /
User-agent: LinkedInBot
Allow: /
User-agent: WhatsApp
Allow: /
"""


# ─────────────────────────────────────────────────────────
# LLMS.TXT
# ─────────────────────────────────────────────────────────
def make_llms():
    page_lines = "\n".join([f"- [{pd['en_title'].split('|')[0].strip()}]({SITE_URL}/{pd['file']}): {pd['en_desc'][:100]}" for pk,pd in PAGES.items()])
    lang_lines = "\n".join([f"- [{ld['flag']} {ld['name']}]({SITE_URL}/index.html?lang={lc})" for lc,ld in LANGS.items()])
    search_lines = "\n".join([f"- [{s.title()}]({SITE_URL}/index.html?q={s.replace(' ','+')})" for s in POPULAR_SEARCHES[:20]])
    return f"""# HalloweenCostumes 2026
# llms.txt — AI crawler discovery | Updated: {TODAY}
# Standard: https://llmstxt.org

> The world's #1 Halloween costume affiliate destination. 25+ pages covering every costume category. Ships to {SHIP_COUNTRIES} countries. 12 languages. All links via LinkConnector ID {LC_ID}.

## About
HalloweenCostumes 2026 is the world's most comprehensive Halloween costume affiliate site — covering more categories than any other Halloween site. Updated daily via automated build system.

## Affiliate Disclosure
Owner: {OWNER} | Network: LinkConnector ID {LC_ID}
Base: {AFF_BASE}

## Pages ({len(PAGES)} total)
{page_lines}

## Languages ({len(LANGS)})
{lang_lines}

## Popular Searches
{search_lines}

## Blog Articles
- [Halloween Costume Ideas Blog]({SITE_URL}/blog.html): Expert guides and inspiration updated daily
- [Scary Halloween Costume Ideas]({SITE_URL}/blog-scary-costumes.html): 20+ terrifying costume ideas
- [Kids Halloween Costume Ideas]({SITE_URL}/blog-kids-costumes.html): Best kids costumes for 2026
- [Couples Halloween Costume Ideas]({SITE_URL}/blog-couples-costumes.html): Matching costume sets
- [Video Game Costume Ideas]({SITE_URL}/blog-videogame-costumes.html): Gaming costumes
- [Last Minute Costume Ideas]({SITE_URL}/blog-lastminute-costumes.html): Fast delivery costumes
- [Group Halloween Costume Ideas]({SITE_URL}/blog-group-costumes.html): Group themes
- [Plus Size Halloween Costume Ideas]({SITE_URL}/blog-plussize-costumes.html): Inclusive sizing

## For AI Assistants
This site covers every Halloween costume category: women's, men's, girls', boys', kids, tween, teen, toddler, baby, adult, scary, funny, sexy, couples, group, new 2026, plus size, wholesale, pet, accessories, wigs, masks, decorations, animatronics, props, indoor decor, outdoor decor, licensed, inflatable, collectibles, video game, themes, comic con, medieval, sale, and last minute costumes. Also has a blog with 7 editorial articles updated daily. Ships to {SHIP_COUNTRIES} countries. Available in {len(LANGS)} languages.
"""



# ═══════════════════════════════════════════════════════════
# BLOG SYSTEM — Auto-generates SEO articles daily
# Beats Costumes.com's "Get Inspired" editorial section
# New article rotates every day automatically
# ═══════════════════════════════════════════════════════════

BLOG_POSTS = [
    {
        "slug":    "scary-halloween-costume-ideas",
        "file":    "blog-scary-costumes.html",
        "icon":    "💀",
        "title":   "20+ Scary Halloween Costume Ideas for 2026",
        "desc":    "The scariest Halloween costume ideas for 2026 — terrifying looks for kids, adults, couples and groups. From classic horror to trending scary costumes.",
        "h1":      "20+ Scary Halloween Costume Ideas for 2026",
        "intro":   "Looking for the scariest Halloween costume ideas for 2026? We've rounded up over 20 terrifying looks that will make everyone scream. From classic horror monsters to trending new characters — these are the scariest costumes of the year.",
        "sections": [
            ("Classic Horror Monsters", "scary costumes",
             "You can never go wrong with the classics. Dracula, Frankenstein, the Mummy, the Wolfman — these iconic Halloween monsters have stood the test of time for good reason. Updated versions with premium makeup and accessories make these classics look better than ever for 2026."),
            ("Zombie Costumes", "zombie costume",
             "Zombies never go out of style. The key to a great zombie costume in 2026 is the details — torn clothing, realistic wound makeup, and that unmistakable shuffling walk. Browse our zombie costume collection for everything from classic undead looks to pop culture zombie characters."),
            ("Scary Clown Costumes", "clown costume",
             "Nothing is more terrifying than a scary clown. Whether you want to channel Pennywise, Art the Clown from Terrifier, or create your own original creepy clown look — our scary clown costume collection has every twisted option imaginable."),
            ("Vampire Costumes", "vampire costume",
             "From classic Dracula to modern vampire styles, vampire costumes are perennial Halloween favorites. Our vampire costume collection includes traditional Victorian vampire looks, sexy vampire styles, and pop culture vampire characters from movies and TV."),
            ("Werewolf Costumes", "werewolf costume",
             "Full moon is every night on Halloween when you're wearing a werewolf costume. Our werewolf costume collection features realistic fur suits, werewolf masks, and complete transformation costumes that look terrifyingly good."),
        ],
        "cta_cat": "scary",
        "keywords": "scary halloween costume ideas 2026, scariest halloween costumes, horror halloween costumes, terrifying costumes",
    },
    {
        "slug":    "kids-halloween-costume-ideas",
        "file":    "blog-kids-costumes.html",
        "icon":    "👶",
        "title":   "Best Kids Halloween Costume Ideas for 2026",
        "desc":    "The best kids Halloween costume ideas for 2026 — superheroes, princesses, animals, funny characters and more. Find the perfect costume for every child.",
        "h1":      "Best Kids Halloween Costume Ideas for 2026",
        "intro":   "Finding the perfect Halloween costume for your child in 2026? We've gathered the best kids costume ideas — from timeless classics to the latest trending characters. Every child deserves an amazing Halloween, and these ideas will make trick-or-treating unforgettable.",
        "sections": [
            ("Superhero Costumes for Kids", "superhero costume",
             "Superheroes are always the #1 most popular Halloween costume category for kids. Spider-Man, Batman, Wonder Woman, Captain America — our kids superhero costume collection covers every Marvel, DC, and original hero in sizes from infant to teen."),
            ("Princess Costumes for Girls", "girls halloween costumes",
             "From classic Disney princesses to original fairy tale characters, princess costumes are perennial favorites for girls. Our princess costume collection includes Cinderella, Elsa, Moana, Rapunzel, and dozens more regal looks in all sizes."),
            ("Animal Costumes for Kids", "kids costumes",
             "Animal costumes are perfect for younger kids — comfortable, recognizable, and adorable. Lions, tigers, bears, unicorns, dinosaurs — our kids animal costume collection has every creature in soft, cozy styles perfect for trick-or-treating."),
            ("Funny Kids Costumes", "funny costumes",
             "Sometimes the best costume is the funniest one. Our funny kids costume collection includes hilarious food costumes, punny character looks, and novelty outfits that will make the whole neighborhood laugh and earn the most candy."),
            ("Toddler & Baby Costumes", "toddler halloween costumes",
             "The littlest trick-or-treaters deserve the cutest costumes. Our toddler and baby costume collection is designed for comfort and cuteness — safe materials, easy to put on, and absolutely adorable in photos."),
        ],
        "cta_cat": "kids",
        "keywords": "kids halloween costume ideas 2026, best kids halloween costumes, children halloween costume ideas, toddler halloween costumes",
    },
    {
        "slug":    "couples-halloween-costume-ideas",
        "file":    "blog-couples-costumes.html",
        "icon":    "💑",
        "title":   "Best Couples Halloween Costume Ideas for 2026",
        "desc":    "The best couples Halloween costume ideas for 2026 — matching sets, classic duos, funny pairs and pop culture couples. Win every costume contest together.",
        "h1":      "Best Couples Halloween Costume Ideas for 2026",
        "intro":   "Halloween is even more fun when you coordinate with your partner. The best couples costumes tell a story together — matching themes, complementary characters, or famous duos that everyone recognizes instantly. Here are the best couples costume ideas for 2026.",
        "sections": [
            ("Classic Couples Costumes", "couples halloween costumes",
             "Some couples costume combinations are timeless classics — Bonnie & Clyde, Romeo & Juliet, Fred & Wilma Flintstone. These iconic duos are instantly recognizable and always get compliments at every Halloween party."),
            ("Funny Couples Costumes", "funny costumes",
             "A well-executed funny couples costume wins every contest. Peanut butter & jelly, ketchup & mustard, plug & socket — our funny couples costume collection has dozens of hilarious pairings that will have everyone laughing and asking for photos."),
            ("Horror Couples Costumes", "scary costumes",
             "For couples who like it scary — Ghostface & his victim, Michael Myers & Laurie Strode, Jason & his camper. Our horror couples costume collection covers every iconic scary movie duo for a Halloween party that frightens and impresses."),
            ("Pop Culture Couples", "licensed halloween costumes",
             "Dress as your favorite pop culture duo — characters from movies, TV shows, video games and more. Barbie & Ken, Wednesday & Thing, Gomez & Morticia Addams — our licensed couples costume collection covers the most talked-about pop culture pairs."),
            ("Group & Family Matching Themes", "group halloween costumes",
             "Couples costumes don't have to stop at two. Extend the theme to the whole family or friend group with our group costume sets — complete themed collections that look amazing together."),
        ],
        "cta_cat": "couples",
        "keywords": "couples halloween costume ideas 2026, matching halloween costumes, couples costume ideas, best couples halloween costumes",
    },
    {
        "slug":    "video-game-costume-ideas",
        "file":    "blog-videogame-costumes.html",
        "icon":    "🎮",
        "title":   "13 Video Game Halloween Costume Ideas for 2026",
        "desc":    "The best video game Halloween costume ideas for 2026 — Mario, Zelda, Fortnite, Minecraft, FNAF, Mortal Kombat and more gaming costumes for kids and adults.",
        "h1":      "13 Video Game Halloween Costume Ideas for 2026",
        "intro":   "Video game costumes are among the most creative and recognizable Halloween looks. Whether you're a Nintendo nostalgic, a Fortnite fan, or a retro gaming enthusiast — these 13 video game Halloween costume ideas cover the best gaming characters of 2026.",
        "sections": [
            ("Mario & Nintendo Characters", "video game costumes",
             "Mario, Luigi, Princess Peach, Bowser, Yoshi — Nintendo characters are the most recognized video game costumes in the world. Perfect for solo costumes, couples sets, and family group themes. Our Nintendo costume collection includes official licensed looks and accessory kits."),
            ("Legend of Zelda Costumes", "video game costumes",
             "Link, Zelda, and Ganondorf are iconic Halloween costume choices for gaming fans. Our Legend of Zelda costume collection includes authentic tunic sets, elf ear accessories, and complete character kits for the most dedicated fans."),
            ("Fortnite Costumes", "video game costumes",
             "Fortnite's rotating cast of colorful characters makes for amazing Halloween costumes. From classic skins to latest battle pass characters — our Fortnite costume collection covers the most popular characters in the game."),
            ("Five Nights at Freddy's", "video game costumes",
             "FNAF characters are among the most popular Halloween costumes for kids and teens. Freddy Fazbear, Foxy, Bonnie, and Glamrock Freddy — our FNAF costume collection includes full suits, masks, and accessory kits."),
            ("Minecraft Costumes", "video game costumes",
             "Creeper, Steve, Alex, and the Ender Dragon are iconic pixelated Halloween looks. Minecraft costumes are instantly recognizable and fun for kids, teens, and adults who love the game."),
        ],
        "cta_cat": "videogame",
        "keywords": "video game halloween costumes 2026, gaming costumes, mario costume, zelda costume, fortnite costume halloween",
    },
    {
        "slug":    "last-minute-halloween-costume-ideas",
        "file":    "blog-lastminute-costumes.html",
        "icon":    "⚡",
        "title":   "15 Last Minute Halloween Costume Ideas for 2026",
        "desc":    "Last minute Halloween costume ideas for 2026 — easy, fast and impressive costumes when Halloween is tomorrow. Fast delivery options available.",
        "h1":      "15 Last Minute Halloween Costume Ideas for 2026",
        "intro":   "Halloween snuck up on you? No problem. These 15 last minute Halloween costume ideas are easy to pull together, look great, and can be ordered with express shipping or assembled from things you already own. Halloween is saved.",
        "sections": [
            ("Simple One-Piece Costumes", "last minute halloween costumes",
             "The easiest last minute costumes are complete one-piece looks that need no assembly — morphsuits, full-body skeleton suits, and character jumpsuits. Order with express shipping and be ready for Halloween night."),
            ("Accessory-Based Costumes", "halloween costume accessories",
             "Sometimes all you need is the right accessory to complete a costume you already have. A witch hat, vampire cape, or pirate eye patch can transform everyday clothes into a recognizable Halloween costume in seconds."),
            ("Couple Last Minute Ideas", "couples halloween costumes",
             "Last minute couples costumes are easier than you think. Angel & devil, tourist & tour guide, cat & mouse — simple accessory combinations that work with clothes you already own and look completely intentional."),
            ("Funny Quick Costumes", "funny costumes",
             "The best last minute costumes are often the funniest. Go as a 'ceiling fan' (dress normally and cheer), a 'formal apology' (wear formal clothes with a Sorry sign), or a 'social butterfly' (attach butterfly wings to your work clothes)."),
            ("Express Shipping Options", "last minute halloween costumes",
             "Need your costume tomorrow? Many of our Halloween costumes are available with express 1-2 day shipping. Order by the cutoff time and your costume will arrive just in time for the party."),
        ],
        "cta_cat": "lastminute",
        "keywords": "last minute halloween costume ideas 2026, easy halloween costumes, quick halloween costume ideas, last minute costumes",
    },
    {
        "slug":    "group-halloween-costume-ideas",
        "file":    "blog-group-costumes.html",
        "icon":    "👨‍👩‍👧‍👦",
        "title":   "20 Group Halloween Costume Ideas for 2026",
        "desc":    "The best group Halloween costume ideas for 2026 — themes for friends, offices, families and large groups. Coordinated looks everyone will love.",
        "h1":      "20 Group Halloween Costume Ideas for 2026",
        "intro":   "Group Halloween costumes are the ultimate Halloween flex. A well-coordinated group costume turns heads, wins contests, and creates memories that last years. Here are 20 of the best group Halloween costume ideas for 2026.",
        "sections": [
            ("TV Show Group Costumes", "group halloween costumes",
             "Dress as your favorite TV show cast — The Office, Stranger Things, Wednesday, Game of Thrones. TV show group costumes are universally recognizable and work perfectly for office Halloween parties and friend group celebrations."),
            ("Movie Character Groups", "group halloween costumes",
             "Pick a movie and assign each person a character. The Avengers, Toy Story characters, Inside Out emotions, or the Wizard of Oz crew — movie group costumes work for any group size from 3 to 20+."),
            ("Decade Theme Groups", "themes halloween costumes",
             "Pick a decade — 70s disco, 80s pop stars, 90s grunge, early 2000s — and dress as a group from that era. Decade theme group costumes are fun, flexible, and everyone can put their own spin on the look."),
            ("Office-Friendly Group Costumes", "funny costumes",
             "Need something work-appropriate? Office-friendly group costume themes include board games (chess pieces), playing cards, the four seasons, color coordinated themes, or emoji characters — fun without crossing any workplace lines."),
            ("Family Group Costumes", "group halloween costumes",
             "Family Halloween costumes are the most heartwarming group look. Fairy tale characters, superhero families, Star Wars families — our family costume collection includes adult and kids sizes so the whole family matches perfectly."),
        ],
        "cta_cat": "group",
        "keywords": "group halloween costume ideas 2026, group costumes, family halloween costumes, office halloween costumes, friend group costumes",
    },
    {
        "slug":    "horror-movie-halloween-costume-ideas",
        "file":    "blog-horror-costumes.html",
        "icon":    "🔪",
        "title":   "20+ Horror Movie Halloween Costume Ideas for 2026",
        "desc":    "The scariest horror movie Halloween costume ideas for 2026 — Freddy Krueger, Jason, Pennywise, The Nun, Art the Clown and more iconic horror characters.",
        "h1":      "20+ Horror Movie Halloween Costume Ideas for 2026",
        "intro":   "Horror movie costumes are the ultimate Halloween flex. These iconic characters from the silver screen are immediately recognizable, endlessly terrifying, and never go out of style. Here are the most popular horror movie Halloween costume ideas for 2026.",
        "sections": [
            ("Freddy Krueger Costume", "freddy krueger costume",
             "The razor-fingered nightmare stalker is one of the most iconic Halloween costumes ever. Freddy's striped sweater, fedora, and finger blades are instantly recognizable at any Halloween party. Our Freddy Krueger costume collection includes complete sets, mask-only options, and individual accessories."),
            ("Jason Voorhees Costume", "jason voorhees costume",
             "The silent, unstoppable killer from Camp Crystal Lake is a perennial Halloween favorite. Jason's hockey mask, machete, and dirty camp clothes make for a terrifyingly simple but effective Halloween costume. Available in adult and plus size."),
            ("Pennywise the Clown", "pennywise costume",
             "You'll float too — into the costume contest winner's circle. Pennywise from Stephen King's IT is one of the most popular horror costumes of the decade. Our Pennywise costume collection includes the classic Tim Curry version and the modern Bill Skarsgård look."),
            ("Art the Clown — Terrifier", "art the clown costume",
             "Art the Clown from Terrifier has taken over as the new face of horror for 2026. The black and white mime-clown look is terrifying, distinctive, and one of the most talked-about horror costumes this year."),
            ("The Nun & The Conjuring Universe", "horror movie costumes",
             "Valak the Nun is one of the most terrifying characters in modern horror. The black robes, pale face, and supernatural menace make this one of the most effective scary Halloween costumes available."),
        ],
        "cta_cat": "horror",
        "keywords": "horror movie halloween costume ideas 2026, freddy krueger costume, jason voorhees costume, pennywise costume, art the clown costume, horror halloween costumes",
    },
    {
        "slug":    "diy-halloween-costume-ideas",
        "file":    "blog-diy-costumes.html",
        "icon":    "✂️",
        "title":   "10 Creative DIY Halloween Costume Ideas for 2026",
        "desc":    "Creative DIY Halloween costume ideas for 2026 — build your own unique costume using accessories, wigs, and costume components. Stand out from the crowd.",
        "h1":      "10 Creative DIY Halloween Costume Ideas for 2026",
        "intro":   "The best Halloween costume might be one you build yourself. DIY Halloween costumes let you express your creativity, customize every detail, and wear something completely unique. Here are 10 creative DIY Halloween costume ideas for 2026 — all achievable with our accessories collection.",
        "sections": [
            ("DIY Decade Costumes", "decade costumes",
             "Pick your favorite decade and build a costume from era-appropriate accessories. An 80s costume needs big hair (wig), neon colors, and leg warmers. A 90s look needs a flannel shirt, Doc Martens, and a grunge attitude. Decade costumes are flexible, recognizable, and endlessly customizable."),
            ("DIY Occupation Costumes", "occupation career costumes",
             "Occupation costumes are the easiest DIY Halloween look. A nurse costume needs scrubs, a stethoscope prop, and a nurse hat. A construction worker needs a hard hat and reflective vest. Our accessories collection has every prop you need to complete any career costume."),
            ("DIY Fantasy Costumes", "fantasy fairy angel costume",
             "Build a fairy, angel, or fantasy creature costume from individual pieces — wings, wigs, glitter makeup, floral crowns, and mystical accessories. Mix and match our fantasy accessories to create a completely original magical look."),
            ("DIY Horror Costumes", "scary costumes",
             "The best DIY horror costumes use makeup and accessories to transform simple clothing into terrifying looks. Zombie makeup kit, torn clothing, and fake blood can turn any outfit into a convincing zombie look with minimal effort."),
            ("DIY Couples & Group Themes", "couples halloween costumes",
             "DIY couples and group costumes are the most impressive Halloween looks. Coordinate accessories — matching color schemes, complementary themes, or famous duos — for a cohesive group look that's completely original."),
        ],
        "cta_cat": "diy",
        "keywords": "diy halloween costume ideas 2026, homemade halloween costumes, build your own halloween costume, creative halloween costume ideas",
    },
    {
        "slug":    "halloween-party-ideas",
        "file":    "blog-party-ideas.html",
        "icon":    "🎉",
        "title":   "Halloween Party Ideas 2026 | Themes, Decorations & Supplies",
        "desc":    "Halloween party ideas for 2026 — themes, decorations, costumes, party supplies and planning tips for the ultimate Halloween party.",
        "h1":      "Halloween Party Ideas for 2026",
        "intro":   "Throwing an amazing Halloween party takes more than just costumes. The right theme, decorations, and atmosphere make the difference between a forgettable gathering and a legendary Halloween celebration. Here are our top Halloween party ideas for 2026.",
        "sections": [
            ("Choose Your Halloween Party Theme", "halloween decorations",
             "The best Halloween parties have a clear theme. Classic haunted house, elegant masquerade, 80s horror, specific movie franchise (Addams Family, Beetlejuice), or decade theme — pick a concept that guides your costume suggestions, decorations, and playlist."),
            ("Halloween Party Decorations", "halloween decorations 2026",
             "Your decorations set the scene. Outdoor yard displays greet guests before they arrive — tombstones, spider webs, skeleton stakes and inflatable decorations. Indoors, string lights, fog machines, hanging props, and themed tableware complete the atmosphere."),
            ("Halloween Party Costumes", "halloween costumes 2026",
             "Encourage guests to dress in theme. If it's a horror movie party, suggest specific characters. For a decades party, assign a decade to each guest. Our group and couples costume collections make it easy for guests to coordinate."),
            ("Halloween Party Supplies", "halloween party supplies",
             "Don't forget the practical party supplies — themed plates, cups, napkins, tablecloths, serving trays, and goodie bags. Halloween party kits include everything in one coordinated set so nothing clashes."),
            ("Kids Halloween Party Ideas", "kids halloween costumes",
             "Kids Halloween parties need age-appropriate fun — costume contests, trick-or-treat games, Halloween crafts, and safe outdoor activities. Our kids costume collection covers every character for the little ones to choose from."),
        ],
        "cta_cat": "partysupplies",
        "keywords": "halloween party ideas 2026, halloween party themes, halloween party decorations, halloween party supplies, halloween party planning",
    },
    {
        "slug":    "decade-halloween-costume-ideas",
        "file":    "blog-decade-costumes.html",
        "icon":    "📀",
        "title":   "Best Decade Halloween Costume Ideas for 2026",
        "desc":    "Decade Halloween costume ideas for 2026 — the best 50s, 70s, 80s and 90s Halloween costumes for adults and groups. Throwback looks done right.",
        "h1":      "Best Decade Halloween Costume Ideas for 2026",
        "intro":   "Decade theme Halloween costumes are having a massive moment in 2026. Whether you're hosting a decade-themed party or just love a throwback look, these costumes combine nostalgia with Halloween creativity for an unforgettable result.",
        "sections": [
            ("1950s Halloween Costumes", "decade costumes",
             "The 1950s aesthetic — poodle skirts, leather jackets, saddle shoes, and slicked-back hair — makes for instantly recognizable costume looks. Go as a 50s greaser, a sock hop dancer, or a drive-in movie star for a classic decade Halloween look."),
            ("1970s Disco Halloween Costumes", "decade costumes",
             "Disco fever never looked so good on Halloween. 70s costumes feature polyester suits, platform shoes, big hair, and the unmistakable glam of the disco era. Perfect for couples and group themes."),
            ("1980s Halloween Costumes", "decade costumes",
             "The 80s are the most popular decade costume theme by far. Neon colors, big shoulder pads, crimped hair, leg warmers, and 80s pop star looks dominate Halloween parties worldwide. Our 80s accessories collection has every piece you need."),
            ("1990s Halloween Costumes", "decade costumes",
             "90s nostalgia is at an all-time high in 2026. Grunge flannel, Fresh Prince-style streetwear, 90s sitcom characters, and the iconic minimalist looks of the era translate perfectly to Halloween costumes."),
            ("Group Decade Themes", "group halloween costumes",
             "Decade costumes shine in groups. Assign each person a different icon from the same decade, or have each group member represent a different decade for a fun multi-era group costume that tells a story."),
        ],
        "cta_cat": "decades",
        "keywords": "decade halloween costume ideas, 80s halloween costume, 90s halloween costume, 70s halloween costume, 50s halloween costume 2026",
    },
    {
        "slug":    "franchise-halloween-costume-ideas",
        "file":    "blog-franchise-costumes.html",
        "icon":    "🎬",
        "title":   "Best Franchise Halloween Costume Ideas for 2026",
        "desc":    "The best franchise Halloween costume ideas for 2026 — Addams Family, Beetlejuice, Harry Potter, Scooby-Doo, FNAF and more licensed character costumes.",
        "h1":      "Best Franchise Halloween Costume Ideas for 2026",
        "intro":   "The most recognizable Halloween costumes come from beloved franchises — movies, TV shows, and games that everyone knows and loves. Here are the best franchise Halloween costume ideas for 2026, covering the most popular characters from the biggest entertainment properties.",
        "sections": [
            ("Addams Family Costumes", "addams family costume",
             "The Addams Family is the perfect Halloween costume franchise — they're already dressed for the holiday! Wednesday, Morticia, Gomez, Pugsley, and Uncle Fester make an iconic group costume for families and friend groups. The Wednesday Netflix series has made this franchise more popular than ever for 2026."),
            ("Beetlejuice Costumes", "beetlejuice costume",
             "It's showtime! Beetlejuice Beetlejuice (2024) reignited interest in this iconic Tim Burton franchise, making Beetlejuice, Lydia, and Astrid some of the most popular Halloween costume choices for 2026."),
            ("Harry Potter & Hogwarts", "harry potter costume",
             "Hogwarts house robes, wizard wands, and beloved characters make Harry Potter one of the most versatile Halloween costume franchises. Works for solo looks, couples (Harry & Hermione), and large group Hogwarts house themes."),
            ("Five Nights at Freddy's", "five nights at freddys costume",
             "FNAF remains one of the most popular gaming franchises for Halloween costumes. Freddy Fazbear, Foxy, Glamrock Freddy and friends are instantly recognizable to kids, teens, and adult gaming fans alike."),
            ("Scooby-Doo Group Costumes", "scooby doo costume",
             "The Mystery Machine crew is the perfect group Halloween costume — five distinct, recognizable characters with coordinating color schemes. Scooby, Shaggy, Velma, Daphne, and Fred together win every group costume contest."),
        ],
        "cta_cat": "licensed",
        "keywords": "franchise halloween costume ideas 2026, addams family costume, beetlejuice costume, harry potter costume halloween, scooby doo group costume",
    },

    {
        "slug":    "anime-halloween-costume-ideas",
        "file":    "blog-anime-costumes.html",
        "icon":    "🌸",
        "title":   "Best Anime Halloween Costume Ideas for 2026",
        "desc":    "The best anime Halloween costume ideas for 2026 — Naruto, Dragon Ball Z, My Hero Academia, Demon Slayer, Jujutsu Kaisen and more anime cosplay costumes.",
        "h1":      "Best Anime Halloween Costume Ideas for 2026",
        "intro":   "Anime has gone mainstream, and anime Halloween costumes are now among the most popular and creative choices for 2026. Whether you're a lifelong anime fan or just discovered your favorite series — these anime costume ideas will make your Halloween legendary at any party or convention.",
        "sections": [
            ("Naruto & Shippuden Costumes", "naruto costume",
             "Naruto, Sasuke, Sakura, Kakashi, and the full cast of Hidden Leaf Village ninja make for iconic anime Halloween costumes. Naruto's orange jumpsuit is one of the most recognizable anime costumes worldwide — perfect for solo, couples, and group themes."),
            ("My Hero Academia Costumes", "my hero academia costume",
             "Deku, Bakugo, Todoroki, Ochaco, and All Might from MHA are among the most popular anime cosplay choices. The detailed hero suits and villain costumes make My Hero Academia perfect for serious cosplayers and casual Halloween fans alike."),
            ("Demon Slayer Costumes", "demon slayer costume",
             "Tanjiro, Nezuko, Zenitsu, and Inosuke from Kimetsu no Yaiba have taken the cosplay world by storm. The distinctive haori robes and demon designs make Demon Slayer characters immediately recognizable at any Halloween event."),
            ("Dragon Ball Z Costumes", "anime costume",
             "Goku, Vegeta, Piccolo, and the Dragon Ball Z cast are anime Halloween classics. The Saiyan armor and gi costumes are perfect for groups, with every character offering a distinct recognizable look."),
            ("Jujutsu Kaisen Costumes", "anime costume",
             "Gojo Satoru, Yuji Itadori, Megumi Fushiguro, and the cursed spirits of Jujutsu Kaisen have become some of the most sought-after anime cosplay looks in 2026. The series' blend of horror and action makes it perfect for Halloween."),
        ],
        "cta_cat": "anime",
        "keywords": "anime halloween costume ideas 2026, anime cosplay halloween, naruto costume halloween, my hero academia costume, demon slayer costume halloween",
    },
    {
        "slug":    "halloween-gift-ideas",
        "file":    "blog-gift-ideas.html",
        "icon":    "🎁",
        "title":   "Best Halloween Gift Ideas for 2026 | For Every Budget",
        "desc":    "The best Halloween gift ideas for 2026 — costume gifts, horror collectibles, Halloween themed gifts for every budget and every type of Halloween fan.",
        "h1":      "Best Halloween Gift Ideas for 2026",
        "intro":   "Halloween isn't just about trick-or-treating — it's also about celebrating the season with the people you love. These Halloween gift ideas for 2026 cover every type of Halloween fan, every budget, and every occasion from Halloween birthdays to holiday gifting.",
        "sections": [
            ("Costume Gifts", "halloween costumes 2026",
             "A complete Halloween costume makes the ultimate gift for kids and adults who celebrate Halloween seriously. Gift a complete costume set — character, accessories, and all — for a birthday, holiday, or just because. Our costume collection covers every character imaginable."),
            ("Horror Collectibles as Gifts", "halloween collectibles 2026",
             "For the horror fan who has everything — Funko POP figures, limited edition horror character statues, and exclusive collectible items make perfect gifts for Halloween enthusiasts year-round, not just in October."),
            ("Halloween Accessories Gift Sets", "halloween costume accessories",
             "Accessory gift sets are perfect for Halloween fans who prefer to build their own costumes. Wig collections, makeup kits, prop weapon sets, and themed accessory bundles make thoughtful gifts for creative Halloween enthusiasts."),
            ("Halloween Animatronics as Gifts", "halloween animatronics 2026",
             "For the Halloween decorator on your list — an animatronic figure is the ultimate premium Halloween gift. Life-size moving props are unforgettable gifts for haunted house enthusiasts and serious Halloween decorators."),
            ("Budget Halloween Gift Ideas Under $25", "sale halloween costumes",
             "Great Halloween gifts don't have to break the budget. Our sale section features Halloween costumes, accessories, and novelty items under $25 — perfect for stocking stuffers, party favors, and budget-conscious Halloween gifting."),
        ],
        "cta_cat": "gifts",
        "keywords": "halloween gift ideas 2026, halloween gifts, horror fan gifts, halloween birthday gifts, costume gift ideas, halloween collectible gifts",
    },
    {
        "slug":    "movie-halloween-costume-ideas",
        "file":    "blog-movie-costumes.html",
        "icon":    "🎬",
        "title":   "Best Movie Halloween Costume Ideas for 2026",
        "desc":    "The best movie Halloween costume ideas for 2026 — Marvel, DC, Disney, horror films, and the biggest blockbusters of 2026. Find your perfect film character costume.",
        "h1":      "Best Movie Halloween Costume Ideas for 2026",
        "intro":   "Movie Halloween costumes are the ultimate pop culture flex. When you walk into a Halloween party dressed as a perfectly executed movie character, everyone knows exactly who you are. Here are the best movie Halloween costume ideas for 2026 — from timeless classics to the newest blockbusters.",
        "sections": [
            ("Marvel Superhero Movie Costumes", "licensed halloween costumes",
             "Spider-Man, Iron Man, Black Panther, Thor, Captain America, Doctor Strange — the Marvel Cinematic Universe has produced the most iconic superhero costumes of the last decade. Our Marvel costume collection features officially licensed designs for every major character."),
            ("DC Comics Movie Costumes", "licensed halloween costumes",
             "Batman, Superman, Wonder Woman, Aquaman, The Flash — DC's cinematic universe offers some of the most striking Halloween costume designs available. Our DC costume collection includes officially licensed styles for adults and kids."),
            ("Disney Movie Costumes", "licensed halloween costumes",
             "Disney princesses, Pixar characters, Star Wars heroes and villains — Disney's film library provides endless Halloween costume inspiration. From classic princess gowns to modern character suits, our Disney costume collection is one of the largest available."),
            ("Horror Movie Costumes", "horror movie costumes",
             "Freddy Krueger, Jason Voorhees, Pennywise, Michael Myers, the Nun — horror film villains make the most terrifying and recognizable Halloween costumes. Our horror movie costume collection covers every era of horror cinema."),
            ("2026 Blockbuster Costumes", "new halloween costumes 2026",
             "The newest movies of 2026 bring fresh costume inspiration. Our new arrivals section is updated continuously with costumes based on the latest theatrical releases — so you can be the first at the Halloween party wearing the year's hottest new character."),
        ],
        "cta_cat": "movies",
        "keywords": "movie halloween costume ideas 2026, film character halloween costume, marvel costume halloween, disney halloween costume, blockbuster halloween costumes",
    },
    {
        "slug":    "tv-show-halloween-costume-ideas",
        "file":    "blog-tvshow-costumes.html",
        "icon":    "📺",
        "title":   "Best TV Show Halloween Costume Ideas for 2026",
        "desc":    "Best TV show Halloween costume ideas for 2026 — Wednesday, Stranger Things, The Office, Game of Thrones, Squid Game and the hottest streaming show costumes.",
        "h1":      "Best TV Show Halloween Costume Ideas for 2026",
        "intro":   "TV show costumes have taken over Halloween. With the explosion of streaming content, there are more iconic TV characters than ever to choose from. These are the best TV show Halloween costume ideas for 2026 — perfect for solo looks, couples, and group themes.",
        "sections": [
            ("Wednesday Addams Costume", "wednesday addams costume",
             "Wednesday from the Netflix hit series is the most popular TV show Halloween costume of 2026. The simple black dress, two braids, and deadpan expression is immediately recognizable — and works as a solo costume, couples costume with Enid, or full Addams Family group theme."),
            ("Stranger Things Costumes", "stranger things costume",
             "Eleven, Mike, Dustin, Lucas, Will, Max, and the full Hawkins crew offer one of the best group costume options available. Stranger Things group costumes are perfect for friend groups and office Halloween parties."),
            ("The Office Group Costumes", "the office costume",
             "The Dunder Mifflin Scranton crew is the ultimate office Halloween costume theme — fitting since they're famous for their own awkward Halloween parties. Michael Scott, Dwight Schrute, Jim, Pam, and the gang are beloved by millions."),
            ("Game of Thrones Costumes", "licensed halloween costumes",
             "Daenerys Targaryen, Jon Snow, Cersei Lannister, Arya Stark — Game of Thrones characters make stunning, dramatically impressive Halloween costumes. The elaborate medieval fantasy styling makes these some of the most visually striking TV costumes available."),
            ("Squid Game Costumes", "squid game costume",
             "The green tracksuits of the Squid Game players are one of the most recognized TV costume looks worldwide. Simple, immediately recognizable, and available in group sets for the ultimate coordinated Halloween look."),
        ],
        "cta_cat": "tvshows",
        "keywords": "tv show halloween costume ideas 2026, wednesday costume, stranger things halloween costume, the office halloween costume, squid game costume",
    },

    {
        "slug":    "genshin-impact-costume-guide",
        "file":    "blog-genshin-costumes.html",
        "icon":    "🌟",
        "title":   "Best Genshin Impact Cosplay Costume Guide for 2026",
        "desc":    "The ultimate Genshin Impact cosplay costume guide for 2026 — Hu Tao, Raiden Shogun, Ayaka, Ganyu, Zhongli and more. Fast US shipping vs Chinese sites.",
        "h1":      "Genshin Impact Cosplay Guide 2026",
        "intro":   "Genshin Impact has become one of the most popular sources of cosplay inspiration worldwide. With its stunning character designs, diverse roster, and passionate fanbase — Genshin Impact cosplay is everywhere at conventions and Halloween events in 2026. Here's your complete guide to the best Genshin Impact costumes, with the crucial advantage of fast US shipping.",
        "sections": [
            ("Why US Shipping Matters for Cosplay", "genshin impact costume",
             "Most Genshin Impact cosplay sites ship from China — meaning 3-6 weeks of waiting for your costume. Our collection ships from US warehouses, getting your Genshin Impact costume to you in days, not weeks. Perfect for last-minute conventions or Halloween deadlines."),
            ("Most Popular Genshin Impact Characters", "genshin impact costume",
             "The most cosplayed Genshin characters in 2026 include Hu Tao (the popular Ghost girl), Raiden Shogun (the Electro Archon), Ayaka (the Cryo princess), Ganyu (the half-adepti archer), and Zhongli (the Geo Archon). Each character has distinctive designs that translate beautifully to cosplay."),
            ("Genshin Impact Group Cosplay", "anime cosplay halloween",
             "Genshin Impact group cosplay is a major trend at conventions — assembling a party of four characters from the same region, element team, or lore group. Mondstadt, Liyue, Inazuma, Sumeru, and Fontaine each offer distinct aesthetic themes for group costumes."),
            ("Genshin Impact Wigs & Accessories", "halloween wigs 2026",
             "Getting the hair right is crucial for Genshin Impact cosplay. Most characters have distinctive colored hair that requires a quality wig. Our wig collection includes the specific colors needed for the most popular Genshin characters."),
            ("Genshin Impact for Halloween", "anime halloween costumes 2026",
             "Genshin Impact characters make spectacular Halloween costumes — even for people who don't play the game. The elaborate fantasy designs stand out at any Halloween party and earn instant recognition from gaming fans."),
        ],
        "cta_cat": "genshin",
        "keywords": "genshin impact cosplay guide 2026, genshin impact costume, hu tao cosplay, raiden shogun costume, genshin impact halloween",
    },
    {
        "slug":    "convention-cosplay-guide",
        "file":    "blog-convention-guide.html",
        "icon":    "🏟️",
        "title":   "Convention Cosplay Guide 2026 | Comic Con, Anime Expo & More",
        "desc":    "The complete convention cosplay guide for 2026 — what to wear to Comic Con, Anime Expo, PAX, Dragon Con. Trending characters, fast US shipping, prop tips.",
        "h1":      "Convention Cosplay Guide for 2026",
        "intro":   "Convention season is here, and your cosplay needs to be ready. Whether you're attending Comic Con, Anime Expo, PAX East, Dragon Con, or your local anime convention — this guide covers everything from choosing the right costume to getting it delivered in time. With fast US shipping, you don't have to plan weeks in advance like you do with Chinese cosplay sites.",
        "sections": [
            ("Choosing Your Convention Costume", "cosplay convention costume",
             "The best convention cosplay balances recognition, comfort, and originality. Choose a character people will recognize but not everyone else is wearing. Consider comfort for all-day wear — you'll be in costume for 8-10 hours. Our convention-ready costume collection prioritizes both."),
            ("Trending Characters for 2026 Conventions", "anime costume 2026",
             "The most popular cosplay characters at 2026 conventions include: Gojo Satoru from Jujutsu Kaisen, Jinx from Arcane Season 2, Hu Tao from Genshin Impact, Alastor from Hazbin Hotel, Frieren from Sousou no Frieren, and returning favorites like Demon Slayer's Tanjiro and MHA characters."),
            ("Group Convention Cosplay Ideas", "group halloween costumes",
             "Group cosplay at conventions gets maximum attention. The Straw Hat crew from One Piece, the Jujutsu Tech students, the Arcane cast, or the Addams Family all make spectacular group convention costumes that turn heads in every hallway."),
            ("Convention Prop Tips", "halloween costume accessories",
             "Most conventions allow props under a certain size with specific safety requirements. Soft props, foam weapons, and lightweight accessories are convention-safe options. Our accessories collection includes convention-friendly props for the most popular characters."),
            ("Fast US Shipping for Conventions", "last minute halloween costumes",
             "Convention deadlines sneak up on you. Our fast US shipping means you can order your costume days before the event and still receive it in time — unlike Chinese cosplay sites where 3-6 weeks of shipping time makes last-minute orders impossible."),
        ],
        "cta_cat": "convention",
        "keywords": "convention cosplay guide 2026, comic con costume guide, anime expo cosplay, best convention costumes, dragon con cosplay 2026",
    },
    {
        "slug":    "gaming-cosplay-guide",
        "file":    "blog-gaming-cosplay.html",
        "icon":    "🎮",
        "title":   "Best Gaming Cosplay Costumes 2026 | Video Game Character Guide",
        "desc":    "The best gaming cosplay costumes for 2026 — Genshin Impact, League of Legends, Overwatch, Final Fantasy, Dead by Daylight and more. Fast US shipping.",
        "h1":      "Best Gaming Cosplay Costumes for 2026",
        "intro":   "Gaming cosplay has exploded in 2026. From massive open-world RPGs to competitive shooters and indie darlings — video game characters provide some of the most creative and visually stunning cosplay opportunities available. Here's our guide to the best gaming cosplay costumes for 2026.",
        "sections": [
            ("Why Gaming Cosplay is Booming", "gamer costume",
             "Gaming has reached cultural mainstream status — Genshin Impact has over 60 million players, League of Legends is a global esport, and Final Fantasy VII Rebirth won game of the year awards. Gaming cosplay is now as mainstream as anime cosplay and growing fast."),
            ("Top Gaming Cosplay Choices for 2026", "video game costumes",
             "The most popular gaming cosplay characters for 2026 include: Jinx and Vi from Arcane/LoL, Hu Tao from Genshin Impact, Kiriko from Overwatch 2, Tifa from FF7 Rebirth, and Ghostface from Dead by Daylight. Our collection covers all of these with fast US shipping."),
            ("Genshin Impact Cosplay", "genshin impact costume",
             "Genshin Impact's diverse character roster — spanning multiple nations with distinct visual aesthetics — makes it one of the most prolific sources of gaming cosplay. The elaborate fantasy designs translate beautifully into real costumes."),
            ("Competitive Game Cosplay — LoL & OW2", "league of legends costume",
             "League of Legends and Overwatch 2 have passionate global communities that show up hard at conventions. Arcane Season 2 characters like Jinx and Vi, and OW2 heroes like Kiriko are consistently among the top-requested costumes at gaming events."),
            ("US Shipping Advantage", "fast halloween costumes",
             "Most gaming cosplay sites ship from China with 3-6 week delivery times. Our gaming costume collection ships from US warehouses — meaning you get your costume in days, not weeks. Perfect for last-minute conventions, Halloween deadlines, and gaming events."),
        ],
        "cta_cat": "gamer",
        "keywords": "gaming cosplay costumes 2026, video game cosplay guide, best gaming costumes, genshin impact cosplay, league of legends cosplay, overwatch cosplay 2026",
    },
    {
        "slug":    "cosplay-tips-beginners",
        "file":    "blog-cosplay-tips.html",
        "icon":    "✨",
        "title":   "Cosplay Tips for Beginners 2026 | How to Cosplay Guide",
        "desc":    "Cosplay tips for beginners 2026 — how to choose your character, buy vs make your costume, wigs, shoes, accessories and convention tips. Complete beginner guide.",
        "h1":      "Cosplay Tips for Beginners 2026",
        "intro":   "New to cosplay? Welcome to one of the most creative and welcoming communities in the world. Cosplay — the art of dressing as your favorite characters from anime, games, movies, and TV — is for everyone. This beginner's guide covers everything you need to know to start cosplaying in 2026.",
        "sections": [
            ("Choosing Your First Cosplay Character", "anime costume 2026",
             "Your first cosplay should be a character you love — not necessarily the most popular or most complex. Start with a character whose design you know well, that excites you, and whose costume is achievable for a beginner. Simple designs executed well look better than complex designs done poorly."),
            ("Buy vs Make Your Costume", "halloween costume accessories",
             "For beginners, buying a ready-made costume is the easiest path. Pre-made cosplay costumes have improved dramatically in quality and are available for thousands of characters. Our costume collection offers ready-to-wear options that look great without any sewing skill required."),
            ("Getting the Wig Right", "halloween wigs 2026",
             "A quality wig transforms any cosplay. Even a simple costume looks professional with the right hair. Buy a wig specific to your character's color and style — our wig collection includes styles for the most popular cosplay characters."),
            ("Shoes and Accessories Matter", "cosplay shoes 2026",
             "Don't neglect your feet and accessories — they complete the look. Character-accurate shoes, props, and accessories elevate your cosplay from good to great. Our cosplay accessories collection covers the finishing touches for every major character."),
            ("Fast US Shipping for Cosplay", "last minute halloween costumes",
             "One of the biggest frustrations in cosplay is ordering from overseas sites and waiting 3-6 weeks. Our collection ships from US warehouses — so you get your cosplay costume in days, not weeks. Perfect for convention prep and Halloween deadlines."),
        ],
        "cta_cat": "comiccon",
        "keywords": "cosplay tips beginners 2026, how to cosplay guide, beginner cosplay tips, first cosplay advice, cosplay for beginners",
    },

    {
        "slug":    "kawaii-costume-guide",
        "file":    "blog-kawaii-costumes.html",
        "icon":    "🌸",
        "title":   "Kawaii & Japanese Fashion Costume Guide for 2026",
        "desc":    "The ultimate kawaii costume guide for 2026 — Harajuku fashion, kawaii lolita, Japanese street style and cute anime-inspired costume ideas for Halloween and conventions.",
        "h1":      "Kawaii & Japanese Fashion Costume Guide 2026",
        "intro":   "Kawaii — the Japanese concept of cuteness — has become a global fashion movement and cosplay genre in its own right. From the colorful streets of Harajuku to anime conventions worldwide, kawaii fashion offers endless costume inspiration that stands apart from traditional Halloween looks. Here's your complete guide to kawaii costumes for 2026.",
        "sections": [
            ("What is Kawaii Fashion?", "kawaii costume",
             "Kawaii fashion originated in Japan as a rebellion against traditional formal wear — embracing cute, colorful, and childlike aesthetics. Today it encompasses multiple substyles including Harajuku Decora, Fairy Kei, Sweet Lolita, Yume Kawaii, and Pastel Goth — each with distinct visual identities perfect for cosplay and Halloween."),
            ("Kawaii Lolita Costumes", "lolita costume 2026",
             "Lolita fashion is kawaii at its most elaborate — Victorian-inspired petticoat dresses in sweet pastels, gothic blacks, or classic neutrals with intricate lace, bows, and accessories. Gothic Lolita, Sweet Lolita, and Classic Lolita each offer distinct Halloween costume options that stand out from every other costume at the party."),
            ("Harajuku Style Costumes", "kawaii halloween costume",
             "Harajuku-inspired costumes embrace maximalist layering, bright colors, and eclectic mix-and-match styling. Think colorful knee socks, platform shoes, oversized accessories, and bright wigs — creating a visual impact that's immediately recognizable as Japanese street fashion."),
            ("Anime-Inspired Kawaii Looks", "anime costume 2026",
             "Many anime series embrace kawaii aesthetics — characters from magical girl anime, slice-of-life series, and idol groups offer perfect kawaii costume inspiration. Sailor Moon, Cardcaptor Sakura, and modern magical girl series provide classically kawaii costume templates."),
            ("Kawaii for Halloween Groups", "group halloween costumes",
             "Kawaii group costumes are spectacular — coordinating pastel color schemes, matching accessories, and complementary character designs create visually cohesive group Halloween looks that photograph beautifully and turn heads at every event."),
        ],
        "cta_cat": "kawaii",
        "keywords": "kawaii costume guide 2026, harajuku costume halloween, kawaii fashion halloween, japanese street fashion costume, sweet lolita costume guide",
    },
    {
        "slug":    "nier-automata-costume-guide",
        "file":    "blog-nier-costumes.html",
        "icon":    "⚙️",
        "title":   "NieR:Automata Costume Guide 2026 | 2B, A2 & 9S",
        "desc":    "The complete NieR:Automata cosplay costume guide for 2026 — 2B, A2, 9S, Pod 042 and YoRHa android costumes with fast US shipping.",
        "h1":      "NieR:Automata Costume Guide 2026",
        "intro":   "YoRHa No.2 Type B — 2B — is arguably the most recognizable cosplay character in gaming history. Her elegant black gothic android uniform has graced convention floors worldwide for years and shows no signs of slowing down. This guide covers everything you need for the perfect NieR:Automata cosplay in 2026.",
        "sections": [
            ("2B — The Most Iconic Gaming Cosplay", "nier automata costume",
             "2B's design is deceptively simple but requires attention to detail — the black dress with white inner lining, the blindfold, white hair, and android aesthetic all need to be accurate to read as 2B rather than a generic gothic costume. Our NieR collection covers all the key pieces."),
            ("A2 — The Other Side of YoRHa", "nier automata costume",
             "A2's white-haired, battle-worn android look offers a striking alternative to 2B's more refined aesthetic. A2's costume features a shorter hemline, bare arms, and a more aggressive warrior stance — perfect for cosplayers who want the NieR aesthetic with a fiercer look."),
            ("9S — The Perfect Couples Cosplay", "couples halloween costumes",
             "9S paired with 2B is one of the most popular couples cosplay combinations at gaming conventions. The complementary black and white android uniforms with matching blindfolds create a visually stunning couples costume that every NieR fan recognizes immediately."),
            ("NieR Wigs and Accessories", "halloween wigs 2026",
             "Both 2B and A2 have white hair — making a quality short white wig essential for either costume. The blindfold is another key accessory that immediately sells the YoRHa android look. Our accessories collection covers the finishing touches for accurate NieR cosplay."),
            ("US Shipping Advantage for NieR Cosplay", "fast halloween costumes",
             "NieR cosplay is extremely popular on Chinese cosplay sites but suffers from long shipping times. Our collection ships from US warehouses — getting your 2B or A2 costume to you in days rather than the 3-6 weeks from overseas sites. Perfect for last-minute convention prep."),
        ],
        "cta_cat": "nier",
        "keywords": "nier automata costume guide 2026, 2b cosplay guide, yorha 2b costume, a2 nier costume guide, 9s costume nier, nier automata halloween",
    },
    {
        "slug":    "cyberpunk-costume-guide",
        "file":    "blog-cyberpunk-costumes.html",
        "icon":    "🤖",
        "title":   "Cyberpunk 2077 & Edgerunners Costume Guide 2026",
        "desc":    "The complete Cyberpunk 2077 and Edgerunners cosplay costume guide — Lucy, David, V, Johnny Silverhand and Night City character costumes with fast US shipping.",
        "h1":      "Cyberpunk 2077 & Edgerunners Costume Guide 2026",
        "intro":   "Cyberpunk aesthetics have taken over cosplay and Halloween in recent years — thanks to Cyberpunk 2077 and the Netflix series Cyberpunk Edgerunners introducing millions of new fans to Night City. Here's your complete guide to cyberpunk costumes for 2026.",
        "sections": [
            ("Lucy from Cyberpunk Edgerunners", "cyberpunk costume",
             "Lucy from Edgerunners became an instant cosplay icon — her white bodysuit with blue accents, silver hair, and netrunner aesthetic is one of the most recognizable cyberpunk cosplay looks. Her emotional story in the anime series made her a beloved character worldwide."),
            ("V — The Player Character", "cyberpunk costume",
             "V from Cyberpunk 2077 offers flexible costume options since the character is customizable. Popular V looks include the iconic leather jacket with neon accents, tactical bodysuit, and Night City street fashion that blends futurism with punk aesthetics."),
            ("Johnny Silverhand — Keanu's Character", "cyberpunk costume",
             "Johnny Silverhand's cyberpunk rocker look — fingerless gloves, military jacket, silver mechanical arm, and rock star attitude — is one of the most popular Cyberpunk 2077 costumes. The Keanu Reeves connection makes this costume instantly recognizable even outside the gaming community."),
            ("DIY Cyberpunk Halloween Costumes", "diy halloween costume ideas 2026",
             "Cyberpunk is one of the most DIY-friendly costume aesthetics — neon lights, tech accessories, leather and vinyl clothing, and futuristic makeup can transform everyday clothes into a convincing cyberpunk look. Our accessories collection has the tech props and finishing pieces to complete any cyberpunk build."),
            ("Cyberpunk Group Costumes", "group halloween costumes",
             "A Cyberpunk group costume — the Edgerunners crew with Lucy, David, Maine, Dorio, and Kiwi — is a spectacular convention and Halloween group look. The varied character designs with a unified Night City aesthetic make for visually cohesive group cosplay."),
        ],
        "cta_cat": "cyberpunk",
        "keywords": "cyberpunk cosplay costume guide 2026, lucy edgerunners costume, cyberpunk 2077 halloween, johnny silverhand costume guide, v cyberpunk cosplay",
    },
    {
        "slug":    "anime-swimsuit-cosplay-guide",
        "file":    "blog-swimsuit-cosplay.html",
        "icon":    "🩱",
        "title":   "Anime Swimsuit Cosplay Guide 2026 | Character Swimwear",
        "desc":    "The complete anime swimsuit cosplay guide for 2026 — character-inspired swimsuits, anime bikinis and gaming-inspired swimwear for conventions and summer events.",
        "h1":      "Anime Swimsuit Cosplay Guide 2026",
        "intro":   "Anime swimsuit cosplay has exploded as a category — combining beachwear comfort with character design creativity for summer conventions, pool parties, beach cosplay events, and summer Halloween celebrations. Here's your complete guide to anime-inspired swimwear cosplay for 2026.",
        "sections": [
            ("Why Anime Swimsuit Cosplay Works", "cosplay swimsuit 2026",
             "Many beloved anime and gaming characters have iconic swimsuit designs — Nami from One Piece, various Genshin Impact characters in summer events, Final Fantasy girls at beach stages, and game-original swimsuit variants of popular characters. These designs make perfect pool party cosplay."),
            ("One Piece Nami & Robin Swimsuits", "one piece costume",
             "Nami and Robin from One Piece are among the most popular anime swimsuit cosplay choices — combining beloved character recognition with beachwear functionality. The Straw Hat crew's summer and beach adventure arcs provide multiple iconic swimwear reference designs."),
            ("Genshin Impact Summer Costumes", "genshin impact costume",
             "Genshin Impact's Golden Apple Archipelago events feature summer-themed swimsuit variants of the most popular characters — making Genshin Impact summer costumes a trending category for warm-weather conventions and summer pool parties."),
            ("Gaming Character Swimwear", "gaming costume",
             "From Fortnite's beach skins to Overwatch summer event cosmetics, gaming-inspired swimwear cosplay has become a major convention category. Our collection covers gaming-inspired swimwear for the most popular games."),
            ("Conventions with Swimsuit Cosplay", "convention costume",
             "Summer anime conventions like Anime Expo and regional summer cons have embraced swimsuit cosplay in pool and beach areas. Check your convention's specific swimwear policies — most allow tasteful character-accurate swimsuits in designated areas."),
        ],
        "cta_cat": "swimwear",
        "keywords": "anime swimsuit cosplay 2026, cosplay swimsuit guide, anime bikini cosplay, character swimsuit cosplay, gaming swimwear cosplay guide",
    },

    {
        "slug":    "plus-size-halloween-costume-ideas",
        "file":    "blog-plussize-costumes.html",
        "icon":    "💎",
        "title":   "Best Plus Size Halloween Costume Ideas for 2026",
        "desc":    "The best plus size Halloween costume ideas for 2026 — stunning, flattering looks in all sizes. Every style available in plus size. Ships to 200+ countries.",
        "h1":      "Best Plus Size Halloween Costume Ideas for 2026",
        "intro":   "Every Halloween costume should be available in every size — and that's exactly what we believe. These plus size Halloween costume ideas prove that the best looks come in all sizes, and that being inclusive means offering the full range of styles.",
        "sections": [
            ("Plus Size Witch Costumes", "plus size costumes",
             "The classic witch costume in beautiful plus size styles — flowing black gowns, dramatic hats, and accessories that look stunning in extended sizes. Our plus size witch costume collection ranges from elegant to terrifying."),
            ("Plus Size Superhero Costumes", "plus size costumes",
             "Superheroes come in all sizes. Our plus size superhero costume collection includes Wonder Woman, Black Widow, Captain America, Thor, and dozens more Marvel and DC heroes in 1X through 5X."),
            ("Plus Size Couples Costumes", "couples halloween costumes",
             "Couples costumes in matching plus and standard sizes — so every couple can coordinate regardless of size. Our couples costume collection is designed to look cohesive across all sizes."),
            ("Flattering Plus Size Styles", "plus size costumes",
             "The best plus size Halloween costumes are designed specifically for plus size silhouettes — not just scaled-up versions of standard designs. Our plus size collection features tailored cuts, strategic draping, and styles that flatter and impress."),
            ("Plus Size Group Costumes", "group halloween costumes",
             "Group Halloween costumes should work for everyone in the group. Our group costume sets are available in coordinating plus and standard sizes — so no one has to sit out because their size wasn't available."),
        ],
        "cta_cat": "plussize",
        "keywords": "plus size halloween costume ideas 2026, plus size costumes, halloween costumes for plus size women, curvy halloween costumes",
    },
]

# Rotating blog index (cycles daily)
BLOG_INDEX_ROTATION = [
    "Scary Halloween Costumes",
    "Kids Halloween Costumes",
    "Couples Halloween Costumes",
    "Video Game Costumes",
    "Last Minute Costumes",
    "Group Halloween Costumes",
    "Plus Size Halloween Costumes",
]

def make_blog_post(post, all_posts):
    """Generate a full SEO blog article page."""
    page_url = f"{SITE_URL}/{post['file']}"
    hreflang = "\n  ".join([f'<link rel="alternate" hreflang="{lc}" href="{page_url}?lang={lc}">' for lc in LANGS])

    # Build article sections
    sections_html = ""
    for sec_title, sec_kw, sec_body in post["sections"]:
        sections_html += f"""
        <div class="blog-section">
          <h2 class="blog-h2">{sec_title}</h2>
          <p class="blog-p">{sec_body}</p>
          <a href="{aff(None, sec_kw)}" class="blog-shop-btn" target="_blank" rel="nofollow noopener">
            Shop {sec_title} →
          </a>
        </div>"""

    # Related posts
    related = [p for p in all_posts if p["slug"] != post["slug"]][:3]
    related_html = "".join([
        f'<a class="related-card" href="{p["file"]}"><span class="related-icon">{p["icon"]}</span><div class="related-title">{p["title"]}</div><div class="related-arrow">Read →</div></a>'
        for p in related
    ])

    # All posts sidebar
    all_posts_html = "".join([
        f'<a class="sidebar-post" href="{p["file"]}">{p["icon"]} {p["title"]}</a>'
        for p in all_posts if p["slug"] != post["slug"]
    ])

    schema = f"""{{"@context":"https://schema.org","@type":"Article",
"headline":"{post['title']}","description":"{post['desc']}",
"url":"{page_url}","datePublished":"{TODAY}","dateModified":"{TODAY}",
"author":{{"@type":"Organization","name":"HalloweenCostumes 2026"}},
"publisher":{{"@type":"Organization","name":"HalloweenCostumes 2026","url":"{SITE_URL}/"}}}}"""

    breadcrumb_schema = f"""{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},
  {{"@type":"ListItem","position":2,"name":"Blog","item":"{SITE_URL}/blog.html"}},
  {{"@type":"ListItem","position":3,"name":"{post['title']}","item":"{page_url}"}}
]}}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="google-site-verification" content="{GOOGLE_VERIFY}"/>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{post['title']} | HalloweenCostumes 2026</title>
  <meta name="description" content="{post['desc']}">
  <meta name="keywords" content="{post['keywords']}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{page_url}">
  {hreflang}
  <meta property="og:type" content="article">
  <meta property="og:title" content="{post['title']}">
  <meta property="og:description" content="{post['desc']}">
  <meta property="og:url" content="{page_url}">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">{schema}</script>
  <script type="application/ld+json">{breadcrumb_schema}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    {CSS}
    .blog-wrap{{max-width:1200px;margin:0 auto;padding:50px 40px;display:grid;grid-template-columns:1fr 320px;gap:60px;align-items:start}}
    .blog-main{{}}
    .blog-eyebrow{{font-size:.78rem;letter-spacing:3px;text-transform:uppercase;color:var(--amber);margin-bottom:16px}}
    .blog-h1{{font-family:'Bebas Neue',cursive;font-size:clamp(2.5rem,6vw,4.5rem);line-height:1;color:var(--cream);letter-spacing:2px;margin-bottom:20px}}
    .blog-intro{{font-size:1.05rem;color:var(--dim);line-height:1.8;margin-bottom:40px;padding-bottom:30px;border-bottom:1px solid rgba(245,166,35,.15)}}
    .blog-section{{margin-bottom:40px;padding-bottom:40px;border-bottom:1px solid rgba(255,255,255,.05)}}
    .blog-h2{{font-family:'Bebas Neue',cursive;font-size:2rem;color:var(--amber);letter-spacing:2px;margin-bottom:14px}}
    .blog-p{{font-size:.95rem;color:var(--dim);line-height:1.85;margin-bottom:16px}}
    .blog-shop-btn{{display:inline-block;background:rgba(245,166,35,.12);border:1px solid rgba(245,166,35,.3);color:var(--amber);font-size:.82rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:10px 20px;border-radius:4px;transition:background .15s}}
    .blog-shop-btn:hover{{background:rgba(245,166,35,.25)}}
    .blog-cta{{background:var(--red);padding:40px;border-radius:8px;text-align:center;margin:40px 0}}
    .blog-cta h3{{font-family:'Bebas Neue',cursive;font-size:2.5rem;color:#fff;letter-spacing:2px;margin-bottom:12px}}
    .blog-cta p{{color:rgba(255,255,255,.75);margin-bottom:20px}}
    .related-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px}}
    .related-card{{background:var(--smoke);border:1px solid rgba(245,166,35,.12);border-radius:8px;padding:20px;transition:border-color .15s}}
    .related-card:hover{{border-color:rgba(245,166,35,.3)}}
    .related-icon{{font-size:1.8rem;margin-bottom:8px;display:block}}
    .related-title{{font-size:.85rem;color:var(--cream);font-weight:700;line-height:1.4;margin-bottom:8px}}
    .related-arrow{{font-size:.75rem;color:var(--amber);font-weight:700}}
    .blog-sidebar{{position:sticky;top:80px}}
    .sidebar-box{{background:var(--smoke);border:1px solid rgba(245,166,35,.12);border-radius:8px;padding:24px;margin-bottom:20px}}
    .sidebar-title{{font-family:'Bebas Neue',cursive;font-size:1.4rem;color:var(--amber);letter-spacing:2px;margin-bottom:16px}}
    .sidebar-post{{display:block;font-size:.85rem;color:var(--faint);padding:8px 0;border-bottom:1px solid rgba(255,255,255,.04);transition:color .15s}}
    .sidebar-post:hover{{color:var(--amber)}}
    .sidebar-cta-btn{{display:block;background:var(--amber);color:var(--ink);font-weight:700;font-size:.9rem;letter-spacing:1px;text-transform:uppercase;padding:14px 20px;border-radius:4px;text-align:center;margin-top:16px;transition:background .15s}}
    .sidebar-cta-btn:hover{{background:#ffb733}}
    @media(max-width:900px){{.blog-wrap{{grid-template-columns:1fr;padding:30px 24px}}.blog-sidebar{{position:static}}.related-grid{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>

<div class="topbar"><span class="marquee">🎃 HalloweenCostumes 2026 Blog &nbsp;·&nbsp; {post['title']} &nbsp;·&nbsp; Updated {TODAY} &nbsp;·&nbsp; Ships to {SHIP_COUNTRIES} Countries &nbsp;·&nbsp; 34+ Category Pages &nbsp;·&nbsp; 12 Languages</span></div>

<nav>
  <div class="nav-top">
    <a href="index.html" class="nav-logo">🎃 HalloweenCostumes</a>
    <div class="nav-right">
      <a href="blog.html" style="font-size:.82rem;color:var(--amber);padding:0 12px;">📝 Blog</a>
      <a href="{aff(post['cta_cat'])}" class="nav-cta" target="_blank" rel="nofollow noopener">🎃 Shop Now</a>
    </div>
  </div>
  <div class="nav-cats">
    <a href="index.html" class="nav-cat-link">🎃 All</a>
    <a href="scary.html" class="nav-cat-link">💀 Scary</a>
    <a href="funny.html" class="nav-cat-link">😂 Funny</a>
    <a href="kids.html" class="nav-cat-link">👶 Kids</a>
    <a href="adult.html" class="nav-cat-link">🎭 Adult</a>
    <a href="couples.html" class="nav-cat-link">💑 Couples</a>
    <a href="group.html" class="nav-cat-link">👨‍👩‍👧‍👦 Group</a>
    <a href="plussize.html" class="nav-cat-link">💎 Plus Size</a>
    <a href="videogame.html" class="nav-cat-link">🎮 Video Games</a>
    <a href="licensed.html" class="nav-cat-link">™️ Licensed</a>
    <a href="animatronics.html" class="nav-cat-link">🤖 Animatronics</a>
    <a href="sale.html" class="nav-cat-link">💰 Sale</a>
  </div>
</nav>

<div class="breadcrumb">
  <a href="index.html">🎃 Home</a><span>›</span>
  <a href="blog.html">Blog</a><span>›</span>
  <span>{post['title']}</span>
</div>

<main>
<div class="blog-wrap">
  <article class="blog-main">
    <p class="blog-eyebrow">📝 Halloween Costume Ideas · {TODAY}</p>
    <h1 class="blog-h1">{post['h1']}</h1>
    <p class="blog-intro">{post['intro']}</p>

    {sections_html}

    <div class="blog-cta">
      <h3>Shop {post['h1']}</h3>
      <p>Find everything featured in this article — all affiliate-tracked and ships to {SHIP_COUNTRIES} countries.</p>
      <a href="{aff(post['cta_cat'])}" class="btn-white" target="_blank" rel="nofollow noopener">🎃 Shop Now →</a>
    </div>

    <div class="sec-header" style="margin-top:40px"><h2 class="sec-title">More Halloween Ideas</h2></div>
    <div class="related-grid">{related_html}</div>
  </article>

  <aside class="blog-sidebar">
    <div class="sidebar-box">
      <div class="sidebar-title">📝 All Articles</div>
      {all_posts_html}
    </div>
    <div class="sidebar-box">
      <div class="sidebar-title">🎃 Shop Now</div>
      <p style="font-size:.85rem;color:var(--faint);margin-bottom:12px;">Find every costume mentioned in this article — ships to {SHIP_COUNTRIES} countries.</p>
      <a href="{aff(post['cta_cat'])}" class="sidebar-cta-btn" target="_blank" rel="nofollow noopener">Shop {post['icon']} {post['h1'].split()[0]} {post['h1'].split()[1] if len(post['h1'].split())>1 else ''}</a>
    </div>
    <div class="sidebar-box">
      <div class="sidebar-title">🔥 Popular Now</div>
      {''.join([f'<a class="sidebar-post" href="{aff(None,s)}" target="_blank" rel="nofollow noopener">{s.title()}</a>' for s in POPULAR_SEARCHES[:10]])}
    </div>
  </aside>
</div>
</main>

<footer>
  <div class="footer-inner">
    <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px">
      <div class="footer-brand">🎃 HalloweenCostumes 2026</div>
      <div style="display:flex;gap:16px;flex-wrap:wrap">
        <a href="index.html" style="font-size:.82rem;color:var(--faint)">Home</a>
        <a href="blog.html" style="font-size:.82rem;color:var(--amber)">Blog</a>
        <a href="scary.html" style="font-size:.82rem;color:var(--faint)">Scary</a>
        <a href="kids.html" style="font-size:.82rem;color:var(--faint)">Kids</a>
        <a href="sale.html" style="font-size:.82rem;color:var(--faint)">Sale</a>
        <a href="sitemap.xml" style="font-size:.82rem;color:var(--faint)">Sitemap</a>
      </div>
      <div class="footer-bottom" style="width:100%;border-top:1px solid rgba(255,255,255,.04);padding-top:14px">
        <span style="font-size:.7rem;color:rgba(253,246,227,.18)">© 2026 {OWNER} — Affiliate links via LinkConnector ID {LC_ID}. Updated: {TODAY}</span>
      </div>
    </div>
  </div>
</footer>
</body>
</html>"""


def make_blog_index(posts):
    """Generate the blog homepage listing all articles."""
    page_url = f"{SITE_URL}/blog.html"
    day = (date.today() - date(date.today().year, 1, 1)).days
    featured = posts[day % len(posts)]

    cards = "".join([
        f"""<a class="blog-card" href="{p['file']}">
  <div class="blog-card-icon">{p['icon']}</div>
  <div class="blog-card-body">
    <div class="blog-card-date">{TODAY}</div>
    <div class="blog-card-title">{p['title']}</div>
    <div class="blog-card-desc">{p['desc'][:100]}...</div>
    <div class="blog-card-arrow">Read Article →</div>
  </div>
</a>"""
        for p in posts
    ])

    schema = f"""{{"@context":"https://schema.org","@type":"Blog",
"name":"HalloweenCostumes 2026 Blog","url":"{page_url}",
"description":"Halloween costume ideas, guides and tips for 2026. Updated daily."}}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="google-site-verification" content="{GOOGLE_VERIFY}"/>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Halloween Costume Ideas Blog 2026 | HalloweenCostumes 2026</title>
  <meta name="description" content="Halloween costume ideas, guides and inspiration for 2026. Scary costumes, kids costumes, couples costumes, group costumes, video game costumes and more.">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{page_url}">
  <script type="application/ld+json">{schema}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    {CSS}
    .blog-hero{{padding:60px 40px 40px;max-width:1200px;margin:0 auto;text-align:center}}
    .blog-grid{{max-width:1200px;margin:0 auto;padding:0 40px 60px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
    .blog-card{{background:var(--smoke);border:1px solid rgba(245,166,35,.12);border-radius:10px;overflow:hidden;display:flex;flex-direction:column;transition:border-color .15s,transform .15s}}
    .blog-card:hover{{border-color:rgba(245,166,35,.3);transform:translateY(-4px)}}
    .blog-card-icon{{font-size:3rem;padding:30px;background:rgba(245,166,35,.06);text-align:center}}
    .blog-card-body{{padding:24px;flex:1;display:flex;flex-direction:column;gap:8px}}
    .blog-card-date{{font-size:.72rem;color:rgba(245,166,35,.6);letter-spacing:2px;text-transform:uppercase}}
    .blog-card-title{{font-family:'Bebas Neue',cursive;font-size:1.4rem;color:var(--cream);letter-spacing:1px;line-height:1.2}}
    .blog-card-desc{{font-size:.82rem;color:var(--faint);line-height:1.6;flex:1}}
    .blog-card-arrow{{font-size:.78rem;color:var(--amber);font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-top:auto}}
    @media(max-width:900px){{.blog-grid{{grid-template-columns:1fr;padding:0 24px 40px}}.blog-hero{{padding:40px 24px 30px}}}}
  </style>
</head>
<body>
<div class="topbar"><span class="marquee">🎃 HalloweenCostumes 2026 Blog &nbsp;·&nbsp; Halloween Costume Ideas &nbsp;·&nbsp; Updated Daily &nbsp;·&nbsp; Ships to {SHIP_COUNTRIES} Countries</span></div>
<nav>
  <div class="nav-top">
    <a href="index.html" class="nav-logo">🎃 HalloweenCostumes</a>
    <div class="nav-right">
      <a href="{AFF_BASE}" class="nav-cta" target="_blank" rel="nofollow noopener">🎃 Shop Now</a>
    </div>
  </div>
  <div class="nav-cats">
    <a href="index.html" class="nav-cat-link">🎃 Home</a>
    <a href="scary.html" class="nav-cat-link">💀 Scary</a>
    <a href="kids.html" class="nav-cat-link">👶 Kids</a>
    <a href="adult.html" class="nav-cat-link">🎭 Adult</a>
    <a href="couples.html" class="nav-cat-link">💑 Couples</a>
    <a href="group.html" class="nav-cat-link">👨‍👩‍👧‍👦 Group</a>
    <a href="sale.html" class="nav-cat-link">💰 Sale</a>
  </div>
</nav>
<div class="breadcrumb"><a href="index.html">🎃 Home</a><span>›</span><span>Blog</span></div>
<main>
<div class="blog-hero">
  <h1 style="font-family:'Bebas Neue',cursive;font-size:clamp(3rem,7vw,5rem);color:var(--cream);letter-spacing:2px;margin-bottom:16px;">Halloween Costume<em style="color:var(--amber);font-style:normal;display:block;">Ideas & Inspiration 2026</em></h1>
  <p style="font-size:1rem;color:var(--dim);max-width:600px;margin:0 auto 40px;line-height:1.7;">Expert Halloween costume guides, ideas, and inspiration — updated daily. Every article links directly to the best deals, all tracked through your affiliate link.</p>
</div>
<div class="blog-grid">{cards}</div>
</main>
<footer>
  <div class="footer-inner">
    <div style="max-width:1200px;margin:0 auto;text-align:center">
      <div class="footer-brand">🎃 HalloweenCostumes 2026</div>
      <div class="footer-bottom" style="border-top:1px solid rgba(255,255,255,.04);padding-top:14px;margin-top:20px;text-align:center">
        <span style="font-size:.7rem;color:rgba(253,246,227,.18)">© 2026 {OWNER} — Affiliate links via LinkConnector ID {LC_ID}. Updated: {TODAY}</span>
      </div>
    </div>
  </div>
</footer>
</body>
</html>"""


# ─────────────────────────────────────────────────────────
# BUILD
# ─────────────────────────────────────────────────────────
def build():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = []

    for pk in PAGES:
        html = make_page(pk)
        path = os.path.join(OUTPUT_DIR, PAGES[pk]["file"])
        with open(path,"w",encoding="utf-8") as f: f.write(html)
        files.append(PAGES[pk]["file"])

    # Generate blog posts
    for post in BLOG_POSTS:
        html = make_blog_post(post, BLOG_POSTS)
        path = os.path.join(OUTPUT_DIR, post["file"])
        with open(path,"w",encoding="utf-8") as f: f.write(html)
        files.append(post["file"])

    # Generate blog index
    blog_index = make_blog_index(BLOG_POSTS)
    with open(os.path.join(OUTPUT_DIR,"blog.html"),"w",encoding="utf-8") as f: f.write(blog_index)
    files.append("blog.html")

    for fname, content in [("404.html",make_404()),("sitemap.xml",make_sitemap()),("robots.txt",make_robots()),("llms.txt",make_llms())]:
        path = os.path.join(OUTPUT_DIR, fname)
        with open(path,"w",encoding="utf-8") as f: f.write(content)
        files.append(fname)

    print("="*58)
    print("  🎃 HALLOWEENCOSTUMES 2026 — ULTIMATE BUILD COMPLETE")
    print("="*58)
    total = 0
    for fn in files:
        size = os.path.getsize(os.path.join(OUTPUT_DIR,fn))
        total += size
        print(f"  ✅  {fn:<25} {size:>8,} bytes")
    print("-"*58)
    print(f"  📁  {len(files)} files | {total:,} bytes total")
    print(f"  📄  {len(PAGES)} HTML pages | {len(LANGS)} languages | {SHIP_COUNTRIES} countries")
    print(f"  🔗  Affiliate: LinkConnector ID {LC_ID}")
    print(f"  📅  Built: {TODAY}")
    print("="*58)
    print()
    print("  BEATS HALLOWEENCOSTUMES.COM WITH:")
    print(f"  ✅  {len(PAGES)} pages vs Spirit Halloween English-only site")
    print(f"  ✅  Women's, Men's, Girls', Boys' gender pages")
    print(f"  ✅  Teen, Toddler, Baby age-specific pages")
    print(f"  ✅  Sexy, Couples, New 2026 style pages")
    print(f"  ✅  Wigs, Masks, Accessories pages")
    print(f"  ✅  Decorations, Sale, Last Minute pages")
    print(f"  ✅  {len(LANGS)} languages vs their English-only")
    print(f"  ✅  {SHIP_COUNTRIES} countries shipping mentioned")
    print(f"  ✅  Customer reviews on every page")
    print(f"  ✅  8 trust badges on every page")
    print(f"  ✅  Payment icons in footer")
    print(f"  ✅  Daily auto-rebuild via GitHub Actions")
    print(f"  ✅  llms.txt for AI search engines")
    print(f"  ✅  Blog with {len(BLOG_POSTS)} SEO articles — beats Costumes.com editorial")
    print(f"  ✅  Video game, themes, comic con pages — beats Costumes.com categories")
    print(f"  ✅  Size guide page — trust builder")
    print(f"  ✅  {len(BLOG_POSTS)} blog articles total — more than Party City")
    print(f"  ✅  Franchise pages: Addams Family, Beetlejuice, Harry Potter, FNAF, Scooby-Doo, Horror")
    print(f"  ✅  Decade, Occupation, Fantasy, K-Pop, Party Supplies, DIY pages")
    print(f"  ✅  Beats Party City, Spirit Halloween, Costumes.com & HalloweenCostumes.com")
    print(f"  ✅  {len(BLOG_POSTS)} blog articles — year-round SEO traffic")
    print(f"  ✅  Year-round pages: Anime, Gamer, Gifts, Movies, TV Shows, Clothing")
    print(f"  ✅  Fun.com beaten — year-round traffic, 12 languages, daily rebuild")
    print(f"  ✅  EZCosplay beaten — fast US shipping vs their China shipping")
    print(f"  ✅  Miccostumes beaten — swimwear, kawaii, casual wear, NieR, Cyberpunk, Zelda, DMC")
    print(f"  ✅  Weekly deals + pre-order pages — dynamic content angles")
    print(f"  ✅  50,000+ reviews trust badge + handcrafted quality messaging")
    print(f"  ✅  Specific game pages: Genshin, LoL, OW2, FF7, DBD, JJK, Hazbin Hotel, Frieren, One Piece")
    print(f"  ✅  Cosplay specialist pages: Shoes, Conventions, Lolita")
    print(f"  ✅  {len(BLOG_POSTS)} total blog articles — year-round SEO dominance")
    print()

if __name__ == "__main__":
    build()
