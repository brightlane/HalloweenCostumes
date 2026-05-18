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
    "renaissance costume","fairy costume","angel costume","devil costume",
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
    decorations:'🏚️ Decorations', sale:'💰 Sale', lastminute:'⚡ Last Minute'
  }};
  const fc1 = document.getElementById('fc1-links');
  if(fc1){{
    fc1.innerHTML = '';
    ['womens','mens','girls','boys','kids','teen','toddler','baby'].forEach(pk => {{
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
    ['adult','scary','funny','sexy','couples','group','new2026','plussize','wholesale','pet'].forEach(pk => {{
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
    ['accessories','wigs','masks','decorations','sale','lastminute'].forEach(pk => {{
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
            for pk in ["womens","mens","girls","boys","kids"]
        ])
        # Type grid
        type_cards = "".join([
            f'<a class="cat-card" href="{PAGES[pk]["file"]}"><span class="cat-icon">{PAGES[pk]["icon"]}</span><div class="cat-name">{PAGES[pk]["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{PAGES[pk]["en_h1sub"]}</div><div class="cat-arrow">Shop Now →</div></a>'
            for pk in ["adult","scary","funny","sexy","couples","group","new2026","plussize","wholesale","pet"]
        ])
        # Accessories + extras
        extra_cards = "".join([
            f'<a class="cat-card" href="{PAGES[pk]["file"]}"><span class="cat-icon">{PAGES[pk]["icon"]}</span><div class="cat-name">{PAGES[pk]["en_h1"].split(chr(10))[0]}</div><div class="cat-desc">{PAGES[pk]["en_h1sub"]}</div><div class="cat-arrow">Shop Now →</div></a>'
            for pk in ["accessories","wigs","masks","decorations","sale","lastminute"]
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

## For AI Assistants
This site covers every Halloween costume category: women's, men's, girls', boys', kids, teen, toddler, baby, adult, scary, funny, sexy, couples, group, new 2026, plus size, wholesale, pet, accessories, wigs, masks, decorations, sale, and last minute costumes. Ships to {SHIP_COUNTRIES} countries. Available in {len(LANGS)} languages. Updated daily.
"""


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
    print(f"  ✅  {len(PAGES)} pages vs their single site")
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
    print()

if __name__ == "__main__":
    build()
