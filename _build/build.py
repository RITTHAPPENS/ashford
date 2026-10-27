#!/usr/bin/env python3
"""Baut die statischen Seiten des Prototyps aus gemeinsamen Bausteinen.
Aufruf: python3 _build/build.py   (aus dem Repo-Stamm)
Ordner mit Unterstrich werden von GitHub Pages nicht ausgeliefert."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS = json.load(open(os.path.join(ROOT, '_build', 'icons.json')))


import hashlib


def ver(rel):
    return hashlib.md5(open(os.path.join(ROOT, rel), 'rb').read()).hexdigest()[:8]


def ic(name, cls='icon'):
    return '<svg class="%s" viewBox="0 0 256 256" aria-hidden="true">%s</svg>' % (cls, ICONS[name])


PRODUCTS = [
    # slug, Name, Kategorie, Bild, Foto?, Kurztext
    ('ashford-formula', 'Ashford Formula', 'Verdichten', 'produkt-ashford.jpg', True,
     'Der Klassiker für Industrieböden, im Neubau und im Bestand. Er dringt 3 bis 5 mm tief ein und macht die Oberfläche dauerhaft hart, dicht und staubfrei.'),
    ('retroplate', 'RetroPlate', 'Verdichten und Polieren', 'packshot-retroplate.png', False,
     'Das System für geschliffene und polierte Betonböden. Für neuen Beton genauso wie für ältere Flächen, die wieder gut aussehen sollen.'),
    ('retroguard', 'RetroGuard', 'Schützen', 'packshot-retroguard.png', False,
     'Schützt verdichtete und polierte Böden vor Flecken durch Öl, Fett und viele andere Flüssigkeiten, ohne die Optik zu verändern.'),
    ('retropel', 'RetroPel', 'Schützen', 'packshot-retropel.png', False,
     'Macht Beton öl- und wasserabweisend. Verschüttetes perlt ab und lässt sich aufnehmen, bevor es einzieht.'),
    ('creteclean', 'CreteClean', 'Pflegen', 'packshot-creteclean.png', False,
     'Ein Reiniger, der auf Beton abgestimmt ist. Er hält verdichtete und polierte Böden sauber und greift die Oberfläche nicht an.'),
    ('cretefill', 'CreteFill', 'Reparieren', 'packshot-cretefill.png', False,
     'Repariert Ausbrüche, große Risse und beschädigte Fugenkanten. Mit Sand gemischt entsteht ein sehr fester Polymerbeton, der schnell wieder belastbar ist.'),
]


def head(p, title, desc):
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#16171A">
<link rel="preload" href="{p}assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/plex-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/css/style.css?v={ver('assets/css/style.css')}">
</head>
<body>
'''


def header(p, current=''):
    def cur(key):
        return ' aria-current="page"' if key == current else ''
    items = ''.join(
        f'<a href="{p}produkte/{s}/"><b>{n}</b><small>{c}</small></a>' for s, n, c, *_ in PRODUCTS)
    return f'''<div class="topbar">
  <div class="wrap">
    <span>Exklusiv in Deutschland über <strong>Beltex Commerce</strong></span>
    <nav aria-label="Service"><a href="mailto:info@beltex.org">info@beltex.org</a><a href="{p}downloads/">Datenblätter</a></nav>
  </div>
</div>
<header class="header" id="header">
  <div class="wrap">
    <a href="{p}./" class="logo" aria-label="Ashford Formula, zur Startseite"><img src="{p}assets/ashford-formula-logo.png" alt="Ashford Formula" width="1128" height="392"></a>
    <nav class="nav" id="nav" aria-label="Hauptmenü">
      <div class="dd">
        <a href="{p}produkte/" class="dd__toggle"{cur('produkte')}>Produkte {ic('caret-down')}</a>
        <div class="dd__menu">
          <a href="{p}produkte/" class="dd__all">Alle Produkte im Überblick</a>
          {items}
        </div>
      </div>
      <a href="{p}anwendung/"{cur('anwendung')}>Anwendung</a>
      <a href="{p}projekte/"{cur('projekte')}>Projekte</a>
      <a href="{p}downloads/"{cur('downloads')}>Downloads</a>
      <a href="{p}kontakt/" class="btn btn--red">Projekt anfragen</a>
    </nav>
    <button class="burger" id="burger" aria-label="Menü öffnen" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>
'''


def footer(p):
    plist = ''.join(f'<li><a href="{p}produkte/{s}/">{n}</a></li>' for s, n, *_ in PRODUCTS)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="{p}assets/ashford-formula-logo-weiss.png" alt="Ashford Formula" width="1128" height="392">
        <p>Der Original-Betonverdichter von Curecrete. Für Betonböden, die über Jahrzehnte hart, dicht und staubfrei bleiben.</p>
      </div>
      <div>
        <h2 class="fh">Produkte</h2>
        <ul>{plist}</ul>
      </div>
      <div>
        <h2 class="fh">Informationen</h2>
        <ul><li><a href="{p}produkte/">Produktübersicht</a></li><li><a href="{p}anwendung/">Anwendung</a></li><li><a href="{p}projekte/">Projekte</a></li><li><a href="{p}downloads/">Downloads</a></li><li><a href="{p}kontakt/">Kontakt</a></li></ul>
      </div>
      <div class="footer__partner">
        <small>Vertrieb in Deutschland</small>
        <img src="{p}assets/beltex-commerce-logo-weiss.png" alt="Beltex Commerce">
        <p>Berliner Straße 21<br>56470 Bad Marienberg<br><a href="mailto:info@beltex.org">info@beltex.org</a></p>
        <p class="sub">Zertifizierter Verarbeiter<br><a href="https://www.stratec-industrieboden.de/" target="_blank" rel="noopener">Stratec Industrieboden GmbH</a></p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 Ashford Formula Deutschland, Beltex Commerce</span>
      <nav aria-label="Rechtliches"><a href="{p}impressum/">Impressum</a><a href="{p}datenschutz/">Datenschutz</a></nav>
    </div>
  </div>
</footer>
<div class="lightbox" id="lightbox" role="dialog" aria-label="Bildansicht"><button aria-label="Schließen">{ic('x')}</button></div>
<div class="toast" id="toast" role="status"></div>
<script src="{p}assets/js/main.js?v={ver('assets/js/main.js')}"></script>
</body>
</html>
'''


def product_card(p, prod, i):
    s, n, c, img, photo, txt = prod
    d = ' reveal-d%d' % (i % 3) if i % 3 else ''
    cls = 'product__img product__img--photo' if photo else 'product__img'
    return f'''<article class="product reveal{d}">
        <div class="{cls}"><img src="{p}assets/{img}" alt="{n}" loading="lazy"></div>
        <div class="product__body">
          <span class="product__cat">{c}</span>
          <h3><a href="{p}produkte/{s}/">{n}</a></h3>
          <p>{txt}</p>
          <span class="product__more">Mehr erfahren {ic('arrow-right')}</span>
        </div>
      </article>'''


# ======================================================================
# Startseite
# ======================================================================
def home():
    p = ''
    h = head(p, 'Ashford Formula Deutschland | Betonverdichter für Industrieböden',
             'Ashford Formula macht Betonböden dauerhaft staubfrei, härter und abriebfester. Exklusiv in Deutschland über Beltex Commerce, ausgeführt von zertifizierten Fachbetrieben.')
    h += header(p)
    cards = '\n      '.join(product_card(p, pr, i) for i, pr in enumerate(PRODUCTS))
    h += f'''
<main id="top">

<section class="hero">
  <div class="hero__media"><img src="assets/hero-halle.jpg" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <h1><span>Betonböden, die hart bleiben.</span> <span>Und <em>staubfrei</em>.</span></h1>
    <p>Ashford Formula zieht in die Betonoberfläche ein und macht sie dauerhaft abriebfest und staubbindend. Eine Behandlung, die über Jahrzehnte wirkt.</p>
    <div class="hero__cta">
      <a href="#kontakt" class="btn btn--red">Projekt anfragen {ic('arrow-right')}</a>
      <a href="anwendung/" class="btn btn--light">So wirkt es</a>
    </div>
  </div>
</section>

<section class="proof" aria-label="Auf einen Blick">
  <div class="wrap">
    <ul>
      <li>{ic('seal-check')}<div><b>Original seit 1949</b><span>Weltweit auf Betonböden im Einsatz</span></div></li>
      <li>{ic('arrows-out-cardinal')}<div><b class="num">460.000 m²</b><span>In Deutschland behandelt</span></div></li>
      <li>{ic('shield-check')}<div><b>20 Jahre Garantie</b><span>Bei Ausführung durch Fachbetrieb</span></div></li>
      <li>{ic('clock-counter-clockwise')}<div><b>Einmal auftragen</b><span>Kein Nachstreichen, keine Beschichtung</span></div></li>
    </ul>
  </div>
</section>

<section class="sec" id="ueber">
  <div class="wrap intro">
    <div class="intro__img reveal"><img src="assets/intro-halle.jpg" alt="Große Halle mit verdichtetem, glänzendem Betonboden" loading="lazy"></div>
    <div class="reveal reveal-d1">
      <h2 class="h2">Kein Anstrich, sondern ein Teil des Betons</h2>
      <p>Beschichtungen liegen auf dem Beton und nutzen sich mit der Zeit ab. Ashford Formula funktioniert anders: Die Flüssigkeit dringt in die oberste Schicht ein und schließt Poren und Kapillaren von innen.</p>
      <p>Entwickelt und hergestellt wird Ashford Formula von Curecrete in Utah, USA. Seit 2019 ist Beltex Commerce exklusiver Vertriebspartner in Deutschland.</p>
      <a href="produkte/" class="textlink">Zu den Produkten {ic('arrow-right')}</a>
    </div>
  </div>
</section>

<section class="sec sec--concrete" id="vorteile">
  <div class="wrap">
    <div class="adv">
      <div class="adv__intro reveal">
        <h2 class="h2">Was ein behandelter Boden besser kann</h2>
        <p class="lead">Die Werte stammen aus Vergleichsprüfungen mit unbehandeltem Beton. Im Alltag heißt das: weniger Reinigung, weniger Verschleiß und kein Staub auf Ware und Maschinen.</p>
      </div>
      <ul class="figures">
        <li class="figure reveal"><div class="figure__n num"><span data-count="100">100</span><small>%</small></div><div><h3>staubfrei</h3><p>Der Boden gibt keinen Zementstaub mehr ab. Das schont Mitarbeiter, Technik und gelagerte Ware.</p></div></li>
        <li class="figure reveal"><div class="figure__n num"><span data-count="33">33</span><small>%</small></div><div><h3>abriebfester</h3><p>Stapler, Hubwagen und Palettenverkehr hinterlassen deutlich weniger Spuren.</p></div></li>
        <li class="figure reveal"><div class="figure__n num"><span data-count="38">38</span><small>%</small></div><div><h3>härter</h3><p>Die Oberfläche wird widerstandsfähiger, auch gegen Stöße und punktuelle Last.</p></div></li>
      </ul>
    </div>
    <div class="extras">
      <div class="extra reveal">{ic('clock-counter-clockwise')}<h3>Einmal behandeln</h3><p>Die Wirkung bleibt im Beton. Kein Nachstreichen, keine neue Beschichtung nach ein paar Jahren.</p></div>
      <div class="extra reveal reveal-d1">{ic('broom')}<h3>Leicht zu reinigen</h3><p>Auf der geschlossenen Oberfläche hält sich Schmutz schlecht. Eine Scheuersaugmaschine genügt.</p></div>
      <div class="extra reveal reveal-d2">{ic('shield-check')}<h3>20 Jahre Garantie</h3><p>Übernimmt ein zertifizierter Fachbetrieb die Ausführung, gibt es auf Wunsch eine Garantieerklärung.</p></div>
      <div class="extra reveal reveal-d3">{ic('leaf')}<h3>Wasserbasiert</h3><p>Frei von Lösemitteln und flüchtigen organischen Stoffen. Keine schädlichen Dämpfe bei der Verarbeitung.</p></div>
    </div>
  </div>
</section>

<section class="sec sec--concrete" id="bereiche">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2 class="h2">Überall dort, wo Beton viel aushalten muss</h2>
      <p class="lead">Vom Fitnessstudio bis zur Tiefgarage: Ashford Formula eignet sich für nahezu jeden Betonboden, auf dem täglich gefahren, gelaufen und gearbeitet wird.</p>
    </div>
    <div class="bento">
      <div class="tile reveal"><img src="assets/bereich-logistik.jpg" alt="Lagerhalle mit Regalen und glänzendem Betonboden" loading="lazy"><div class="tile__txt"><h3>Logistik und Lager</h3><p>Große Flächen, viel Verkehr, kein Staub auf der Ware.</p></div></div>
      <div class="tile reveal reveal-d1"><img src="assets/bereich-industrie.jpg" alt="Werkstatthalle mit Hebebühnen auf poliertem Betonboden" loading="lazy"><div class="tile__txt"><h3>Industrie und Werkstatt</h3><p>Robust unter Maschinen und schwerem Gerät.</p></div></div>
      <div class="tile reveal reveal-d2"><img src="assets/projekt-1.jpg" alt="Parkdeck während der Bodenbehandlung" loading="lazy"><div class="tile__txt"><h3>Tiefgaragen und Parkdecks</h3><p>Hält Reifenabrieb und täglichem Verkehr stand.</p></div></div>
      <div class="tile reveal reveal-d1"><img src="assets/bereich-oeffentlich.jpg" alt="Heller Eingangsbereich eines öffentlichen Gebäudes" loading="lazy"><div class="tile__txt"><h3>Handel und öffentliche Gebäude</h3><p>Pflegeleicht und ansprechend für stark begangene Flächen.</p></div></div>
    </div>
    <div class="also reveal">
      <div>
        <h3>Außerdem im Einsatz in</h3>
        <ul class="chips"><li>Kühlhäusern</li><li>Lebensmittelproduktion</li><li>Pharma und Laboren</li><li>Supermärkten</li><li>Autohäusern</li><li>Flugzeughangars</li><li>Rechenzentren</li><li>Fitnessstudios</li><li>Sporthallen</li><li>Schulen</li><li>Showrooms</li><li>Museen</li><li>Landwirtschaft</li><li>Wohnräumen</li></ul>
      </div>
      <div class="book">
        <p>Projektfotos und Fallbeispiele aus aller Welt finden Sie im Projektbuch von Curecrete (auf Englisch).</p>
        <a href="https://online.pubhtml5.com/zuil/pmja/" target="_blank" rel="noopener" class="textlink">Projektbuch ansehen {ic('arrow-up-right')}</a>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="produkte">
  <div class="wrap">
    <div class="sec-head sec-head--row reveal">
      <div>
        <h2 class="h2">Ein System für den ganzen Boden</h2>
        <p class="lead">Vom Verdichten über den Schutz bis zur Pflege. Alle Produkte stammen von Curecrete und sind aufeinander abgestimmt.</p>
      </div>
      <a href="produkte/" class="textlink">Alle Produkte im Überblick {ic('arrow-right')}</a>
    </div>
    <div class="products">
      {cards}
    </div>
  </div>
</section>

<section class="sec sec--concrete" id="anwendung">
  <div class="wrap teaser">
    <a class="teaser__media reveal" href="anwendung/">
      <img src="assets/schritt-2-verteilen.jpg" alt="Arbeiter verteilen Ashford Formula mit breiten Besen auf frischem Beton" loading="lazy">
    </a>
    <div class="reveal reveal-d1">
      <h2 class="h2">Aufgebracht im normalen Bauablauf</h2>
      <p class="lead">Im Neubau kommt Ashford Formula zwischen Glätten und Fugenschnitt auf den frischen Beton. Es entsteht kein zusätzlicher Bauabschnitt und keine Wartezeit.</p>
      <ul class="ticks">
        <li>{ic('check-circle')}Aufsprühen, verteilen, Fugen schneiden, reinigen</li>
        <li>{ic('check-circle')}Ca. 150 bis 250 g pro m², einmalig</li>
        <li>{ic('check-circle')}Ausgeführt von einem zertifizierten Fachbetrieb</li>
      </ul>
      <div class="teaser__partner">
        <img src="assets/stratec-logo.png" alt="Stratec Industrieboden GmbH">
        <span>Zertifizierter Verarbeiter in Deutschland</span>
      </div>
      <a href="anwendung/" class="btn btn--line">Zur Anwendung {ic('arrow-right')}</a>
    </div>
  </div>
</section>

<section class="sec" id="projekte">
  <div class="wrap">
    <div class="sec-head sec-head--row reveal">
      <div>
        <h2 class="h2">Böden, die für sich sprechen</h2>
        <p class="lead">Eine Auswahl von Flächen, die mit Produkten von Curecrete behandelt wurden.</p>
      </div>
      <a href="projekte/" class="textlink">Alle Projekte ansehen {ic('arrow-right')}</a>
    </div>
    <div class="gallery reveal">
      <a href="assets/projekt-1.jpg" class="g-wide"><img src="assets/projekt-1.jpg" alt="Parkdeck während der Bodenbehandlung" loading="lazy"></a>
      <a href="assets/projekt-2.jpg"><img src="assets/projekt-2.jpg" alt="Helle Halle mit großer Fensterfront" loading="lazy"></a>
      <a href="assets/projekt-3.jpg" class="g-tall"><img src="assets/projekt-3.jpg" alt="Drei Oldtimer auf poliertem Betonboden" loading="lazy"></a>
      <a href="assets/projekt-4.jpg"><img src="assets/projekt-4.jpg" alt="Glänzender Hallenboden vor einer Glasfassade" loading="lazy"></a>
      <a href="assets/projekt-5.jpg"><img src="assets/projekt-5.jpg" alt="Oldtimer-Garage mit spiegelndem Boden" loading="lazy"></a>
      <a href="assets/projekt-6.jpg"><img src="assets/projekt-6.jpg" alt="Halle mit Rolltoren und spiegelndem Betonboden" loading="lazy"></a>
      <a href="assets/projekt-7.jpg" class="g-wide"><img src="assets/projekt-7.jpg" alt="Geländewagen in einer Garage mit poliertem Boden" loading="lazy"></a>
      <a href="assets/projekt-8.jpg" class="g-wide"><img src="assets/projekt-8.jpg" alt="Sportwagen im Autolift vor glänzendem Betonboden" loading="lazy"></a>
    </div>
  </div>
</section>

<section class="sec sec--concrete" id="kontakt">
  <div class="wrap contact">
    <div class="reveal">
      <h2 class="h2">Sie planen einen neuen Betonboden?</h2>
      <p class="lead">Erzählen Sie uns von Ihrem Projekt. Wir melden uns schnellstmöglich und bringen Sie mit dem passenden Fachbetrieb zusammen.</p>
      <ul class="contact__info">
        <li>{ic('envelope-simple')}<div><small>E-Mail</small><a href="mailto:info@beltex.org">info@beltex.org</a></div></li>
        <li>{ic('map-pin')}<div><small>Vertrieb in Deutschland</small>Beltex Commerce, Berliner Straße 21, 56470 Bad Marienberg</div></li>
        <li>{ic('phone')}<div><small>Lieber telefonieren?</small>Fordern Sie im Formular einfach einen Rückruf an.</div></li>
      </ul>
    </div>
    {form()}
  </div>
</section>

</main>
'''
    h += footer(p)
    return h


def form():
    return f'''<form class="form reveal reveal-d1" id="form" novalidate>
      <h3>Projekt anfragen</h3>
      <p>Unverbindlich und kostenlos. Felder mit * sind Pflicht.</p>
      <div class="form__grid">
        <div class="field"><label for="f-name">Name *</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
        <div class="field"><label for="f-firma">Firma</label><input id="f-firma" name="firma" type="text" autocomplete="organization"></div>
        <div class="field"><label for="f-tel">Telefon</label><input id="f-tel" name="telefon" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="f-mail">E-Mail *</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-objekt">Art des Objekts</label>
          <select id="f-objekt" name="objekt"><option value="">Bitte wählen</option><option>Industrie, Produktion oder Werkstatt</option><option>Logistik oder Lager</option><option>Tiefgarage oder Parkdeck</option><option>Lebensmittel oder Pharma</option><option>Handel oder öffentliches Gebäude</option><option>Sonstiges</option></select></div>
        <div class="field"><label for="f-flaeche">Fläche in m²</label><input id="f-flaeche" name="flaeche" type="text" inputmode="numeric" placeholder="z. B. 5.000"></div>
        <div class="field field--full"><label for="f-zeit">Geplanter Zeitraum</label><input id="f-zeit" name="zeitraum" type="text" placeholder="z. B. Frühjahr 2027"></div>
        <div class="field field--full"><label for="f-msg">Nachricht</label><textarea id="f-msg" name="nachricht"></textarea></div>
        <label class="check"><input type="checkbox" name="rueckruf"><span>Bitte rufen Sie mich zurück.</span></label>
        <label class="check"><input type="checkbox" name="datenschutz" required><span>Ich habe die <a href="datenschutz/">Datenschutzerklärung</a> gelesen und bin mit der Verarbeitung meiner Angaben einverstanden. *</span></label>
      </div>
      <button type="submit" class="btn btn--red">Anfrage senden {ic('arrow-right')}</button>
    </form>'''


# ======================================================================
# Produktübersicht
# ======================================================================
DETAILS = {
    'ashford-formula': (['Für Neubau und Bestand, Eindringtiefe 3 bis 5 mm', 'Bis zu 32,5 % mehr Abriebfestigkeit (ASTM C779)', 'Wasserbasiert, lösemittelfrei, 0 g/L VOC', 'Farbe und Optik des Bodens bleiben erhalten'],
                        ['Neubau', 'Industrie', 'Logistik', 'Tiefgaragen']),
    'retroplate': (['Schleifen, verdichten und polieren in einem System', 'Für neue und bestehende Betonböden', 'Optik von seidenmatt bis hochglänzend'],
                   ['Showrooms', 'Handel', 'Büros', 'Wohnräume']),
    'retroguard': (['Schutz vor Flecken und Säureverätzungen', 'Gebrauchsfertig, mit hochglänzendem Finish', 'Für Beton und Terrazzo, ca. 37 bis 50 m² pro Liter'],
                   ['Gastronomie', 'Handel', 'Lebensmittel']),
    'retropel': (['Öl- und wasserabweisend für Beton und Terrazzo', 'Tiefenimprägnierung statt Oberflächenversiegelung', 'Schützt frisch verdichtete und polierte Böden', 'Verändert die Optik des Bodens nicht'],
                 ['Werkstätten', 'Eingangsbereiche', 'Lager']),
    'creteclean': (['Auf den pH-Wert von Beton abgestimmt', 'Ohne Nachspülen, für Wischmopp und Scheuersaugmaschine', 'Lässt feine Kratzer weniger sichtbar werden'],
                   ['Tägliche Reinigung', 'Polierte Böden', 'Große Flächen']),
    'cretefill': (['Zweikomponentiges Reparatursystem, Mischung 1:1', 'Mit Sand gemischt ein extrem fester Polymerbeton', 'Nach rund 45 Minuten wieder befahrbar'],
                  ['Hallen mit Staplerverkehr', 'Logistik', 'Sanierung']),
}

GROUPS = [
    ('verdichten', 'Verdichten', 'Die Grundlage. Macht die Oberfläche hart, dicht und staubfrei.', ['ashford-formula', 'retroplate']),
    ('schuetzen', 'Schützen', 'Ein zusätzlicher Schutz gegen Flecken und Flüssigkeiten.', ['retroguard', 'retropel']),
    ('pflegen', 'Reparieren und pflegen', 'Damit Fugen stabil bleiben und der Boden lange gut aussieht.', ['cretefill', 'creteclean']),
]

FINDER = [
    ('Betonboden in Halle, Lager oder Tiefgarage, neu oder bestehend', 'ashford-formula', 'Ashford Formula'),
    ('Polierte Optik, auch für einen bestehenden Boden', 'retroplate', 'RetroPlate'),
    ('Schutz vor Öl, Fett und Flecken', 'retroguard', 'RetroGuard'),
    ('Wasser und Schmutz sollen abperlen', 'retropel', 'RetroPel'),
    ('Fugen oder Kanten sind ausgebrochen', 'cretefill', 'CreteFill'),
    ('Der Boden soll täglich richtig gereinigt werden', 'creteclean', 'CreteClean'),
]


def products_page():
    p = '../'
    by = {pr[0]: pr for pr in PRODUCTS}
    h = head(p, 'Produkte | Ashford Formula Deutschland',
             'Ashford Formula, RetroPlate, RetroGuard, RetroPel, CreteClean und CreteFill: das abgestimmte System von Curecrete für Betonböden im Überblick.')
    h += header(p, 'produkte')

    finder = ''.join(
        f'<li><a href="#{s}"><span>{q}</span><b>{n} {ic("arrow-right")}</b></a></li>' for q, s, n in FINDER)

    groups = ''
    for gid, gname, gtxt, slugs in GROUPS:
        items = ''
        for i, s in enumerate(slugs):
            _, n, c, img, photo, txt = by[s]
            ticks, tags = DETAILS[s]
            tl = ''.join(f'<li>{ic("check-circle")}{t}</li>' for t in ticks)
            tg = ''.join(f'<li>{t}</li>' for t in tags)
            imgcls = 'pd__img pd__img--photo' if photo else 'pd__img'
            dl = (f'<a href="{p}downloads/datenblatt-{s}.pdf" target="_blank" rel="noopener" class="btn btn--line">Datenblatt {ic("file-pdf")}</a>'
                  if s in ('ashford-formula', 'retroplate', 'retropel', 'retroguard', 'cretefill') else '<span class="pd__soon">Datenblatt folgt</span>')
            items += f'''
        <article class="pd reveal{' reveal-d1' if i else ''}" id="{s}">
          <div class="{imgcls}"><img src="{p}assets/{img}" alt="{n}" loading="lazy"></div>
          <div class="pd__body">
            <span class="product__cat">{c}</span>
            <h3>{n}</h3>
            <p>{txt}</p>
            <ul class="ticks">{tl}</ul>
            <div class="pd__tags"><span>Typisch für</span><ul class="chips">{tg}</ul></div>
            <div class="pd__cta"><a href="{p}produkte/{s}/" class="btn btn--red">Zum Produkt {ic("arrow-right")}</a>{dl}</div>
          </div>
        </article>'''
        groups += f'''
    <section class="pgroup" id="{gid}" aria-labelledby="{gid}-h">
      <header class="pgroup__head reveal">
        <h2 id="{gid}-h">{gname}</h2>
        <p>{gtxt}</p>
      </header>
      <div class="pgroup__grid">{items}
      </div>
    </section>'''

    h += f'''
<main>
<section class="page-head">
  <div class="wrap">
    <h1>Produkte</h1>
    <p class="lead">Sechs Produkte von Curecrete, die aufeinander abgestimmt sind. Vom Verdichten über den Schutz bis zur täglichen Pflege.</p>
    <ol class="system" aria-label="Das System">
      <li><a href="#verdichten"><b>Verdichten</b><span>Ashford Formula, RetroPlate</span></a></li>
      <li><a href="#schuetzen"><b>Schützen</b><span>RetroGuard, RetroPel</span></a></li>
      <li><a href="#pflegen"><b>Reparieren und pflegen</b><span>CreteFill, CreteClean</span></a></li>
    </ol>
  </div>
</section>

<section class="sec finder-sec">
  <div class="wrap finder">
    <div class="reveal">
      <h2 class="h2">Welches Produkt passt?</h2>
      <p class="lead">Wählen Sie die Situation, die Ihrem Boden am nächsten kommt. Im Zweifel beraten wir Sie gern persönlich.</p>
    </div>
    <ul class="finder__list reveal reveal-d1">{finder}</ul>
  </div>
</section>

<div class="wrap pgroups">{groups}
</div>

<section class="sec">
  <div class="wrap">
    <div class="cta-band reveal">
      <div>
        <h2>Nicht sicher, was Ihr Boden braucht?</h2>
        <p>Schildern Sie uns kurz Ihr Objekt. Wir empfehlen die passende Kombination und stellen den Kontakt zum Fachbetrieb her.</p>
      </div>
      <a href="{p}kontakt/" class="btn btn--red">Projekt anfragen {ic("arrow-right")}</a>
    </div>
  </div>
</section>
</main>
'''
    h += footer(p)
    return h


# ======================================================================
# Anwendung
# ======================================================================
def anwendung_page():
    p = '../'
    h = head(p, 'Anwendung | Ashford Formula Deutschland',
             'So wird Ashford Formula aufgebracht: Wirkweise, Ablauf auf der Baustelle, Pflege nach der Übergabe und Ausführung durch den zertifizierten Fachbetrieb Stratec Industrieboden.')
    h += header(p, 'anwendung')
    h += f"""
<main>
<section class="page-head">
  <div class="wrap">
    <h1>Anwendung</h1>
    <p class="lead">Ashford Formula wird einmal aufgebracht und wirkt danach im Material selbst, im Neubau wie auf bestehenden Böden. So läuft es ab, vom ersten Sprühstoß bis zur Pflege im Alltag.</p>
    <ul class="facts">
      <li>{ic('calendar-check')}<div><b>Zeitpunkt</b><span>Zwischen Glätten und Fugenschnitt</span></div></li>
      <li>{ic('drop')}<div><b>Menge</b><span>Ca. 150 bis 250 g pro m², je nach Untergrund</span></div></li>
      <li>{ic('clock-counter-clockwise')}<div><b>Aufwand</b><span>Läuft im normalen Bauablauf mit</span></div></li>
    </ul>
  </div>
</section>

<section class="sec" id="wirkweise">
  <div class="wrap how how--stack">
    <div class="reveal">
      <h2 class="h2">Was im Beton passiert</h2>
      <p>Frischer Beton ist voller winziger Hohlräume. Dort sammeln sich Wasser und Schmutz, und an der Oberfläche löst sich nach und nach feiner Staub.</p>
      <p>Ashford Formula reagiert mit dem Calciumhydroxid im Beton und bildet feste Kristalle genau an diesen Stellen. Die oberste Schicht wird dicht und hart.</p>
      <ul class="ticks">
        <li>{ic('check-circle')}Der Beton bleibt diffusionsoffen.</li>
        <li>{ic('check-circle')}Keine Schicht, die sich ablösen oder abplatzen kann.</li>
        <li>{ic('check-circle')}Mit der Nutzung wird die Oberfläche dichter und bekommt Glanz.</li>
      </ul>
    </div>
    <figure class="how__fig reveal reveal-d1">
      <img src="{p}assets/wirkweise-grafik.jpg" alt="Vergleich: herkömmliche Imprägnierung bleibt als Film auf der Oberfläche, Ashford Formula dringt ein und bildet Kristalle" loading="lazy">
    </figure>
  </div>
</section>

<section class="sec sec--concrete" id="ablauf-baustelle">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2 class="h2">Der Ablauf auf der Baustelle</h2>
      <p class="lead">Im Neubau sind es vier Arbeitsschritte, die direkt an das Glätten des Betons anschließen. Entscheidend sind der richtige Zeitpunkt und eine gleichmäßige Menge.</p>
    </div>
    <ol class="bigsteps">
      <li class="bigstep reveal"><div class="bigstep__img"><img src="{p}assets/schritt-1-aufspruehen.jpg" alt="Ashford Formula wird mit der Sprühlanze auf die Hallenfläche aufgebracht" loading="lazy"></div>
        <div class="bigstep__txt"><h3>Aufsprühen</h3><p>Sobald der Beton geglättet ist, wird Ashford Formula gleichmäßig aufgesprüht, bis die Fläche gesättigt ist. Die Menge wird dabei genau gemessen, je nach Saugfähigkeit des Untergrunds rund 150 bis 250 g pro m².</p></div></li>
      <li class="bigstep reveal reveal-d1"><div class="bigstep__img"><img src="{p}assets/schritt-2-verteilen.jpg" alt="Arbeiter verteilen Ashford Formula mit breiten Besen" loading="lazy"></div>
        <div class="bigstep__txt"><h3>Verteilen</h3><p>Mit breiten, weichen Besen wird das Material über die ganze Fläche verteilt, damit jede Stelle genug aufnimmt. Jetzt beginnt die Reaktion im Beton.</p></div></li>
      <li class="bigstep reveal"><div class="bigstep__img"><img src="{p}assets/schritt-3-fugen.jpg" alt="Fugenschneider mit Absaugung auf einem Betonboden" loading="lazy"></div>
        <div class="bigstep__txt"><h3>Fugen schneiden</h3><p>Beim Fugenschnitt wird der entstehende Schlamm direkt abgesaugt. So bleiben die Fugen sauber und lassen sich später gut verfüllen, zum Beispiel mit CreteFill.</p></div></li>
      <li class="bigstep reveal reveal-d1"><div class="bigstep__img"><img src="{p}assets/schritt-4-reinigen.jpg" alt="Fertige Hallenfläche nach der maschinellen Reinigung" loading="lazy"></div>
        <div class="bigstep__txt"><h3>Reinigen und übergeben</h3><p>Zum Abschluss wird die gesamte Fläche maschinell gereinigt. Danach ist der Boden fertig und kann genutzt werden.</p></div></li>
    </ol>
    <div class="video reveal" id="video" role="button" tabindex="0" aria-label="Anwendungsvideo auf YouTube abspielen" data-yt="qfEuiGrz6tM">
      <img src="{p}assets/video-poster.jpg" alt="" loading="lazy">
      <span class="video__play">{ic('play')}</span>
      <div class="video__label"><b>Anwendung im Video</b><span>Mit dem Klick wird das Video von YouTube geladen. Dabei werden Daten an YouTube übertragen.</span></div>
    </div>
  </div>
</section>

<section class="sec" id="ausfuehrung">
  <div class="wrap coop">
    <div class="reveal">
      <h2 class="h2">So läuft die Zusammenarbeit</h2>
      <p class="lead">Ashford Formula gibt es nicht im freien Handel. Damit das Ergebnis stimmt, setzt ein geschulter und zertifizierter Fachbetrieb jedes Projekt um.</p>
      <ol class="flow">
        <li><div><h3>Anfrage stellen</h3><p>Sie schildern kurz Objekt, Fläche und den geplanten Zeitraum.</p></div></li>
        <li><div><h3>Beratung und Angebot</h3><p>Wir klären die Details und stimmen den Termin im Bauablauf ab.</p></div></li>
        <li><div><h3>Ausführung</h3><p>Unser zertifizierter Partner bringt Ashford Formula fachgerecht auf.</p></div></li>
        <li><div><h3>Garantie</h3><p>Auf Wunsch erhalten Sie eine Garantieerklärung über 20 Jahre.</p></div></li>
      </ol>
    </div>
    <div class="partner reveal reveal-d1" id="stratec">
      <img src="{p}assets/stratec-logo.png" alt="Stratec Industrieboden GmbH" class="partner__logo">
      <h3>Ausführung durch Stratec Industrieboden</h3>
      <p>In Deutschland übernimmt die Stratec Industrieboden GmbH die Anwendung von Ashford Formula. Das Team ist von Curecrete geschult und zertifiziert. Zeitpunkt, Menge und Verarbeitung stimmen, und nur so ist die Garantie über 20 Jahre möglich.</p>
      <a class="partner__cert" href="{p}downloads/stratec-zertifikat-ashford-formula-2025.pdf" target="_blank" rel="noopener">
        <img src="{p}assets/stratec-zertifikat.jpg" alt="Zertifikat von Curecrete für Stratec Industrieboden" loading="lazy">
        <div><b>Zertifizierter Verarbeiter</b><span>Ausgestellt von Curecrete, gültig bis Mai 2027</span><em>Zertifikat ansehen {ic('file-pdf')}</em></div>
      </a>
      <a href="https://www.stratec-industrieboden.de/" target="_blank" rel="noopener" class="textlink">Zu Stratec Industrieboden {ic('arrow-up-right')}</a>
    </div>
  </div>
</section>

<section class="sec sec--concrete" id="pflege">
  <div class="wrap care">
    <div class="reveal">
      <h2 class="h2">Nach der Übergabe</h2>
      <p class="lead">Ein behandelter Boden braucht wenig Pflege. Mit der richtigen Reinigung bleibt er dicht, sauber und bekommt mit der Zeit einen leichten Glanz.</p>
      <ul class="ticks">
        <li>{ic('check-circle')}Regelmäßig Staub und Schmutz entfernen, damit nichts auf der Oberfläche schleift.</li>
        <li>{ic('check-circle')}Mit einem auf Beton abgestimmten Reiniger wischen oder maschinell reinigen.</li>
        <li>{ic('check-circle')}Keine sauren Reiniger verwenden, sie greifen die Oberfläche an.</li>
      </ul>
    </div>
    <a class="care__product reveal reveal-d1" href="{p}produkte/creteclean/">
      <div class="care__img"><img src="{p}assets/packshot-creteclean.png" alt="CreteClean Gebinde" loading="lazy"></div>
      <div>
        <span class="product__cat">Empfohlen für die Pflege</span>
        <h3>CreteClean</h3>
        <p>Der Reiniger von Curecrete für verdichtete und polierte Betonböden. Ohne Nachspülen, für Wischmopp und Scheuersaugmaschine.</p>
        <span class="product__more">Zum Produkt {ic('arrow-right')}</span>
      </div>
    </a>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="note-row reveal">
      <div>
        <h2>Polierte Optik gewünscht?</h2>
        <p>Ashford Formula verdichtet die Oberfläche und erhält ihre Optik. Wer einen glänzenden, polierten Boden möchte, neu oder bestehend, greift zu RetroPlate.</p>
      </div>
      <a href="{p}produkte/retroplate/" class="textlink">Mehr zu RetroPlate {ic('arrow-right')}</a>
    </div>
    <div class="cta-band reveal">
      <div>
        <h2>Ihr Projekt steht an?</h2>
        <p>Schildern Sie uns Objekt, Fläche und Zeitraum. Wir stimmen den Termin mit dem Fachbetrieb ab.</p>
      </div>
      <a href="{p}kontakt/" class="btn btn--red">Projekt anfragen {ic('arrow-right')}</a>
    </div>
  </div>
</section>
</main>
"""
    h += footer(p)
    return h


if __name__ == '__main__':
    open(os.path.join(ROOT, 'index.html'), 'w').write(home())
    os.makedirs(os.path.join(ROOT, 'produkte'), exist_ok=True)
    open(os.path.join(ROOT, 'produkte', 'index.html'), 'w').write(products_page())
    os.makedirs(os.path.join(ROOT, 'anwendung'), exist_ok=True)
    open(os.path.join(ROOT, 'anwendung', 'index.html'), 'w').write(anwendung_page())
    print('gebaut')
