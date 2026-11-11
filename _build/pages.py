"""Unterseiten: Produktdetails, Projekte, Downloads, Kontakt, Impressum, Datenschutz.
Wird von build.py importiert und nutzt dessen Bausteine."""
import os
from __main__ import head, header, footer, ic, PRODUCTS, product_card, form

BY = {pr[0]: pr for pr in PRODUCTS}

# ----------------------------------------------------------------------
# Produktdaten (Quelle: Datenblätter Beltex, Stand Oktober 2026)
# ----------------------------------------------------------------------
PD = {
    'ashford-formula': dict(
        title='Ashford Formula',
        sub='Betonverdichter',
        lead='Ashford Formula ist ein wasserbasierter Betonverdichter auf Basis von Natriumsilikat. Er reagiert in den obersten 3 bis 5 mm mit dem Beton und macht die Oberfläche dauerhaft hart, dicht und staubfrei.',
        stats=[('32,5', '%', 'mehr Abriebfestigkeit', 'ASTM C779'),
               ('13,3', '%', 'mehr Schlagfestigkeit', 'ASTM C805'),
               ('22', '%', 'höhere Haftzugwerte', 'ASTM D3359')],
        benefits=['Für Neubau und bestehende Böden', 'Bindet den Zementstaub dauerhaft',
                  'Abriebfester und leichter zu reinigen', 'Wirkt öl- und wasserabweisend',
                  'Vergilbt nicht, Farbe und Optik bleiben erhalten', 'Lösemittelfrei, geruchsneutral und gebrauchsfertig'],
        how=['Die Fläche wird bis zur Sättigung mit Ashford Formula behandelt. Im Beton setzt das Material die Reaktion des Zements fort und bildet in den Poren festes Calciumsilikathydrat. Anschließend werden die gelösten Alkalien mit der Scheuersaugmaschine abgewaschen.',
             'Im Neubau passiert das direkt nach dem Glätten, auf bestehenden Böden nach einer gründlichen Reinigung. Die Wirkung ist nicht umkehrbar und nutzt sich nicht ab. Regelmäßige Nassreinigung verdichtet die Oberfläche mit der Zeit sogar weiter.'],
        how_link=('anwendung/', 'Ablauf auf der Baustelle ansehen'),
        note='Ashford Formula wird nur von geschulten und zertifizierten Fachbetrieben verarbeitet. Risse und Fehlstellen schließt das Material nicht, dafür gibt es CreteFill.',
        specs=[('Chemische Basis', 'Wässriges Natriumsilikat'), ('Form', 'Klare, transparente Flüssigkeit'),
               ('Verbrauch', 'Ca. 150 bis 250 g pro m², je nach Saugfähigkeit'), ('Eindringtiefe', '3 bis 5 mm'),
               ('VOC-Gehalt', '0 g/L'), ('Dichte', 'Ca. 1,20 g/cm³ bei 20 °C'), ('Verarbeitung', 'Bei 5 bis 35 °C'),
               ('Gebinde', '200 kg Fass'), ('Lagerung', 'Mindestens 24 Monate, trocken bei 5 bis 30 °C')],
        uses=['Logistikzentren', 'Produktion', 'Verkaufsflächen', 'Sporthallen', 'Messehallen', 'Tiefgaragen'],
        related=['retroguard', 'creteclean']),
    'retroplate': dict(
        title='RetroPlate',
        sub='Betonpoliersystem',
        lead='RetroPlate verbindet Verdichten und Polieren. Die Flüssigkeit RetroPlate 99 macht den Beton dichter und härter, danach wird er mit Diamantwerkzeugen geschliffen und poliert, bis er glänzt wie Naturstein.',
        stats=[('400', '%', 'mehr Abriebfestigkeit, je nach Betonqualität', 'bis zu'),
               ('21', '%', 'mehr Härte', 'Prüfwert'),
               ('30', '%', 'mehr Lichtreflexion', 'Prüfwert')],
        benefits=['Für neuen und bestehenden Beton', 'Glanzgrad von seidenmatt bis hochglänzend',
                  'Staubfrei und sehr abriebfest', 'Keine Beschichtung, die abblättern kann',
                  'Mehr Lichtreflexion, die Halle wirkt heller', 'Wasserbasiert, geruchlos und nicht brennbar'],
        how=['Der Boden wird in mehreren Stufen geschliffen. Zwischen den Schleifgängen kommt RetroPlate 99 auf die Fläche, reagiert mit dem Beton und verdichtet ihn. Danach wird bis zum gewünschten Glanz poliert.',
             'Ursprünglich wurde das System entwickelt, um alte Beschichtungen zu entfernen. Heute wird es auch für neue Böden geplant, weil die Oberfläche aus dem Beton selbst besteht und nicht auf ihm liegt.'],
        how_link=None,
        note='Für zusätzlichen Schutz vor Flecken passt RetroGuard, für die tägliche Reinigung CreteClean Plus.',
        specs=[('Form', 'Klare, farblose und geruchlose Flüssigkeit'), ('Ergiebigkeit', 'Ca. 5 m² pro Liter, je nach Porosität'),
               ('pH-Wert', '11,3 bis 11,6'), ('Verdünnung', 'Keine, wird so verwendet wie geliefert'),
               ('Wirkdauer', 'Dauerhaft'), ('Gebinde', '3,79 L Kanister, 19 L Eimer, 208 L Fass auf Anfrage'),
               ('Lagerung', 'Unbegrenzt, nach einem Jahr vor Gebrauch aufrühren')],
        uses=['Showrooms', 'Autohäuser', 'Handel', 'Büros', 'Wohnräume'],
        related=['retroguard', 'creteclean']),
    'retroguard': dict(
        title='RetroGuard',
        sub='Fleck- und Säureschutz',
        lead='RetroGuard ist ein gebrauchsfertiger Schutz für verdichtete und polierte Böden. Wenn etwas verschüttet wird, hält die Schutzschicht die Flüssigkeit zurück und verschafft Zeit, bevor ein Fleck bleibt.',
        stats=None,
        benefits=['Schützt vor Flecken und Säureverätzungen', 'Laut Hersteller fünfmal säurebeständiger als andere Schutzprodukte',
                  'Hochglänzendes Finish, Farben und Zuschlag kommen stärker zur Geltung', 'Gebrauchsfertig, kein Verdünnen oder Abmessen',
                  'Haftet fest, blättert nicht ab', 'Jederzeit nachbehandelbar ohne vorheriges Strippen', 'UV-stabil, innen und außen'],
        how=['Vor dem Auftragen wird der Boden gründlich gereinigt, am besten mit CreteClean Plus. Schmutz, Öl, Fett, Wachse und alte Versiegelungen müssen vollständig entfernt sein.',
             'Danach wird RetroGuard dünn aufgetragen. Eine kleine Probefläche vorab zeigt, ob Optik und Ergebnis zum Boden passen.'],
        how_link=None,
        note='RetroGuard eignet sich für alle mit Ashford Formula oder RetroPlate behandelten Böden, neu oder alt, grau oder farbig, sowie für Terrazzo.',
        specs=[('Form', 'Milchig weiße Flüssigkeit'), ('Ergiebigkeit', 'Ca. 37 bis 50 m² pro Liter, je nach Porosität und Polierstufe'),
               ('Gebinde', '3,79 L Kanister, 19 L Eimer, 208 L Fass auf Anfrage'), ('Lagerung', 'Ein Jahr im ungeöffneten Originalgebinde'),
               ('Frost', 'Vor Frost schützen')],
        uses=['Gastronomie', 'Handel', 'Lebensmittel', 'Showrooms', 'Terrazzo'],
        related=['retroplate', 'retropel']),
    'retropel': dict(
        title='RetroPel',
        sub='Öl- und wasserabweisend',
        lead='RetroPel macht Beton- und Terrazzoböden öl- und wasserabweisend. Es zieht als Tiefenimprägnierung in die Oberfläche ein und füllt feinste Lücken, ohne dass sich das Aussehen des Bodens verändert.',
        stats=None,
        benefits=['Öl und Wasser dringen nicht in den Boden ein', 'Verhindert weiße Verfärbungen durch Wasser',
                  'Schützt frisch verdichtete und polierte Böden', 'Keine Schicht auf der Oberfläche',
                  'Optik des Bodens bleibt unverändert', 'Wasserbasiert und geruchsarm'],
        how=['Ein frisch verdichteter Boden ist noch nicht ganz dicht. Die Kristalle im Beton wachsen bis zu zwölf Monate weiter, und in dieser Zeit können Öl und Wasser noch eindringen.',
             'RetroPel schließt diese Lücke. Es wird direkt nach dem Verdichten oder Polieren aufgebracht und schützt den Boden, bis er seine volle Dichte erreicht hat.'],
        how_link=None,
        note='Die wirksamen Bestandteile sind Fluorpolymere auf Wasserbasis. Ihre kleinen Moleküle dringen tief ein, statt einen Film zu bilden.',
        specs=[('Form', 'Klare Flüssigkeit'), ('Ergiebigkeit', 'Ca. 15 bis 30 m² pro Liter'), ('VOC-Gehalt', '90 g/L'),
               ('Geruch', 'Geruchsarm'), ('Gebinde', '3,79 L Kanister, 19 L Eimer, 208 L Fass auf Anfrage'),
               ('Lagerung', 'Ein Jahr im ungeöffneten Originalgebinde, vor Frost schützen')],
        uses=['Werkstätten', 'Eingangsbereiche', 'Lager', 'Parkdecks', 'Terrazzo'],
        related=['ashford-formula', 'retroguard']),
    'creteclean': dict(
        title='CreteClean Plus',
        sub='Reiniger mit Scar Guard',
        lead='CreteClean Plus mit Scar Guard ist ein konzentrierter Reiniger für verdichtete und polierte Betonböden. Er zieht Schmutz aus den Poren, hält ihn in der Schwebe und pflegt die Oberfläche bei jeder Reinigung mit.',
        stats=None,
        benefits=['Für verdichteten und polierten Beton und andere harte Böden, außer Naturholz', 'Erhält den Glanz der Oberfläche',
                  'Kleine Kratzer und Makel fallen weniger auf', 'Verringert mit der Zeit die Porosität des Bodens',
                  'Hoch konzentriert, dadurch weniger Verbrauch und Lagerplatz', 'NSF-zertifiziert'],
        how=['Zuerst groben Schmutz entfernen. Dann CreteClean Plus mit Wasser verdünnen, etwa 7,8 ml pro Liter, und mit Wischmopp oder Scheuersaugmaschine auftragen.',
             'Die überschüssige Lösung wieder aufnehmen und die Fläche an der Luft trocknen lassen. Empfohlen ist eine Reinigung etwa dreimal pro Woche.'],
        how_link=('downloads/reinigungsanleitung-creteclean.pdf', 'Reinigungsanleitung für Scheuersaugmaschinen'),
        note='Regelmäßig angewendet, hilft CreteClean Plus, Betonoberflächen zusätzlich zu festigen und zu härten.',
        specs=[('Form', 'Klare, grüne Flüssigkeit mit frischem Duft'), ('Dosierung', 'Ca. 7,8 ml pro Liter Wasser'),
               ('pH-Wert', '11,2 im Konzentrat'), ('Gewicht', '1,02 kg pro Liter'),
               ('Gebinde', '3,79 L Kanister, 19 L Eimer, 208 L Fass'), ('Einfrieren', 'Nach dem Auftauen aufrühren')],
        uses=['Tägliche Reinigung', 'Polierte Böden', 'Handel', 'Große Hallen'],
        related=['ashford-formula', 'retroplate']),
    'cretefill': dict(
        title='CreteFill Spall Repair',
        sub='Reparatursystem für Ausbrüche',
        lead='CreteFill Spall Repair repariert Ausbrüche, große Risse und beschädigte Scheinfugen in Beton. Mit Sand gemischt härtet es zu einem extrem festen Polymerbeton aus und ist nach kurzer Zeit wieder belastbar.',
        stats=[('45', 'Min.', 'bis die Fläche wieder in Betrieb gehen kann', 'Rund'),
               ('32,76', 'MPa', 'Druckfestigkeit mit Sand', 'ASTM C42'),
               ('70', 'Shore D', 'Härte', 'ASTM D2240')],
        benefits=['Zwei Komponenten, Mischung 1:1', 'Selbstnivellierend und selbstgrundierend',
                  'Schrumpft beim Aushärten nicht', 'Standardmäßig grau, Sonderfarben möglich',
                  'Für Stellen ohne zu erwartende Plattenbewegung'],
        how=['Die Schadstelle wird von Staub, Öl und losem Material befreit. Wird der Rand ausgeschnitten, braucht er eine senkrechte Kante von mindestens 12 mm.',
             'Dann beide Komponenten mischen, einfüllen und je nach Tiefe mit Sand anreichern. Bei Kälte das Material vorher langsam auf mindestens 21 °C bringen.'],
        how_link=None,
        note='Typische Einsätze sind Betonausbrüche, Hohllagen, Ausbesserungen vor dem Beschichten, Schwellen an Tiefkühlräumen, Höhenausgleich und Parkdecks.',
        specs=[('Mischung', '1:1 nach Volumen'), ('Verarbeitungszeit', '3 bis 4 Minuten bei 24 °C'),
               ('Viskosität', '90 ± 20 cps bei 24 °C, gemischt'), ('Härte', '70 ± 5 Shore D'),
               ('Zugfestigkeit', '13,79 ± 1,5 MPa'), ('Druckfestigkeit', '32,76 MPa mit Sand'),
               ('Gebinde', '650 ml Kartuschen, 4 L Gebinde'), ('Lagerung', 'Ein Jahr im ungeöffneten Originalgebinde')],
        uses=['Hallen mit Staplerverkehr', 'Logistik', 'Kühlhäuser', 'Parkdecks', 'Sanierung'],
        related=['ashford-formula', 'creteclean']),
}


def cta_band(p, h2='Ihr Projekt steht an?', txt='Schildern Sie uns Objekt, Fläche und Zeitraum. Wir stimmen alles Weitere mit dem Fachbetrieb ab.'):
    return f'''<div class="cta-band reveal">
      <div>
        <h2>{h2}</h2>
        <p>{txt}</p>
      </div>
      <a href="{p}kontakt/" class="btn btn--red">Projekt anfragen {ic("arrow-right")}</a>
    </div>'''


def product_page(slug):
    p = '../../'
    s, n, cat, img, photo, short = BY[slug]
    d = PD[slug]
    h = head(p, f'{d["title"]} | Ashford Formula Deutschland', d['lead'][:155].rsplit(' ', 1)[0] + '.')
    h += header(p, 'produkte')

    stats = ''
    if d['stats']:
        items = ''.join(
            f'<li><span class="pstat__pre">{pre}</span><b class="num">{v}<small>{u}</small></b><span>{lbl}</span></li>'
            for v, u, lbl, pre in d['stats'])
        stats = f'<ul class="pstats reveal">{items}</ul>'

    ben = ''.join(f'<li>{ic("check-circle")}{b}</li>' for b in d['benefits'])
    how = ''.join(f'<p>{t}</p>' for t in d['how'])
    if d['how_link']:
        href, label = d['how_link']
        icon = 'file-pdf' if href.endswith('.pdf') else 'arrow-right'
        extra = ' target="_blank" rel="noopener"' if href.endswith('.pdf') else ''
        how += f'<a href="{p}{href}" class="textlink"{extra}>{label} {ic(icon)}</a>'
    specs = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in d['specs'])
    uses = ''.join(f'<li>{u}</li>' for u in d['uses'])
    rel = '\n      '.join(product_card(p, BY[r], i) for i, r in enumerate(d['related']))
    imgcls = 'phero__img phero__img--photo' if photo else 'phero__img'

    h += f'''
<main>
<section class="phero">
  <div class="wrap phero__grid">
    <div class="phero__txt">
      <a href="{p}produkte/#{slug}" class="phero__back">{ic("arrow-left")} Alle Produkte</a>
      <h1>{d["title"]}</h1>
      <p class="phero__sub">{d["sub"]} <span>{cat}</span></p>
      <p class="lead">{d["lead"]}</p>
      <div class="phero__cta">
        <a href="{p}kontakt/" class="btn btn--red">Beratung anfragen {ic("arrow-right")}</a>
        <a href="{p}downloads/datenblatt-{slug}.pdf" target="_blank" rel="noopener" class="btn btn--line">Datenblatt {ic("file-pdf")}</a>
      </div>
    </div>
    <div class="{imgcls}"><img src="{p}assets/{img}" alt="{d["title"]}, Gebinde"></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {stats}
    <div class="pinfo">
      <div class="reveal">
        <h2 class="h2">Was {n} kann</h2>
        <ul class="ticks ticks--2">{ben}</ul>
      </div>
      <div class="pinfo__how reveal reveal-d1">
        <h2 class="h2">So wird es verwendet</h2>
        {how}
      </div>
    </div>
  </div>
</section>

<section class="sec sec--concrete">
  <div class="wrap pspec">
    <div class="reveal">
      <h2 class="h2">Technische Daten</h2>
      <p class="lead">Die wichtigsten Werte im Überblick. Alle Angaben, Sicherheitshinweise und Prüfnormen stehen im Datenblatt.</p>
      <p class="pspec__note">{d["note"]}</p>
      <div class="pspec__uses"><span>Typisch für</span><ul class="chips">{uses}</ul></div>
      <a href="{p}downloads/datenblatt-{slug}.pdf" target="_blank" rel="noopener" class="textlink">Datenblatt als PDF {ic("file-pdf")}</a>
    </div>
    <dl class="spec reveal reveal-d1">{specs}</dl>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head sec-head--row reveal">
      <div><h2 class="h2">Passt dazu</h2></div>
      <a href="{p}produkte/" class="textlink">Alle Produkte {ic("arrow-right")}</a>
    </div>
    <div class="products products--2">
      {rel}
    </div>
    <div class="spacer"></div>
    {cta_band(p, 'Fragen zu ' + n + '?', 'Wir beraten Sie gern zu Ihrem Boden und stellen den Kontakt zum zertifizierten Fachbetrieb her.')}
  </div>
</section>
</main>
'''
    return h + footer(p)


# ----------------------------------------------------------------------
# Projekte
# ----------------------------------------------------------------------
PROJECTS = [
    # Bild(er), Titel, Ort, Produkte, Fläche, Klasse
    (['classic-depot-wien-1', 'classic-depot-wien-2', 'classic-depot-wien-3', 'classic-depot-wien-4', 'classic-depot-wien-5'],
     'Classic Depot', 'Wien, Österreich', 'RetroPlate, RetroPel', '2.500 m²', 'feature'),
    (['sew-eurodrive-1', 'sew-eurodrive-2'], 'SEW-EURODRIVE', 'Produktionshalle', 'Ashford Formula', None, ''),
    (['supermarkt-flower-mound'], 'Supermarkt', 'Flower Mound, Texas, USA', 'RetroPlate, RetroGuard, CreteFill', 'ca. 3.970 m²', 'tall'),
    (['costco-bundamba'], 'Costco', 'Bundamba, Australien', 'RetroPlate', '9.000 m²', ''),
    (['bunnings-windale'], 'Bunnings Baumarkt', 'Windale, Australien', 'Ashford Formula', None, ''),
    (['cafe-brunei-1', 'cafe-brunei-2'], 'Café Hungry Hippo', 'Brunei', 'Ashford Formula, RetroPlate', None, ''),
    (['autohaus-salisbury'], 'VW-Autohaus', 'Salisbury, Maryland, USA', 'RetroPlate', None, ''),
    (['costco-madrid'], 'Costco', 'Madrid, Spanien', 'Produkte von Curecrete', None, ''),
    (['gaestehaus-china'], 'Gästehaus', 'China', 'Ashford Formula, RetroPlate', None, 'tall'),
    (['parkland-dallas'], 'Bürogebäude', 'Dallas, Texas, USA', 'RetroPlate, CreteFill', None, ''),
    (['parkdeck-monterrey'], 'Parkdeck', 'Monterrey, Mexiko', 'Produkte von Curecrete', None, ''),
    (['logistikhalle'], 'Logistikhalle', 'Neubau', 'Ashford Formula', None, ''),
    (['showroom'], 'Autoshowroom', 'Polierter Betonboden', 'Produkte von Curecrete', None, ''),
]


def projekte_page():
    p = '../'
    h = head(p, 'Projekte | Ashford Formula Deutschland',
             'Betonböden aus aller Welt, die mit Ashford Formula, RetroPlate und weiteren Produkten von Curecrete behandelt wurden.')
    h += header(p, 'projekte')
    cards = ''
    for i, (imgs, t, place, prods, area, cls) in enumerate(PROJECTS):
        first = imgs[0]
        more = ''.join(f'<a href="{p}assets/projekte/{x}.jpg" class="proj__more" aria-label="{t}, weiteres Foto"></a>' for x in imgs[1:])
        count = f'<span class="proj__count">{ic("images")} {len(imgs)} Fotos</span>' if len(imgs) > 1 else ''
        meta = f'<span>{place}</span>' + (f'<span>{area}</span>' if area else '')
        d = ' reveal-d%d' % (i % 3) if i % 3 else ''
        cards += f'''
      <figure class="proj{(' proj--' + cls) if cls else ''} reveal{d}">
        <a href="{p}assets/projekte/{first}.jpg" class="proj__img"><img src="{p}assets/projekte/{first}.jpg" alt="{t}, {place}" loading="lazy">{count}</a>{more}
        <figcaption><h2>{t}</h2><p class="proj__meta">{meta}</p><p class="proj__prod">{prods}</p></figcaption>
      </figure>'''

    h += f'''
<main>
<section class="page-head">
  <div class="wrap">
    <h1>Projekte</h1>
    <p class="lead">Lager, Autohaus, Supermarkt oder Café: Hier sehen Sie Böden aus aller Welt, die mit Produkten von Curecrete behandelt wurden. Ein Klick auf ein Foto öffnet die große Ansicht.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="projects">{cards}
    </div>
  </div>
</section>

<section class="sec sec--concrete">
  <div class="wrap">
    <div class="note-row reveal">
      <div>
        <h2>Noch mehr Referenzen</h2>
        <p>Im Projektbuch von Curecrete finden Sie Fallbeispiele aus vielen Branchen, von der Tiefgarage bis zum Rechenzentrum. Das Projektbuch ist auf Englisch.</p>
      </div>
      <a href="https://online.pubhtml5.com/zuil/pmja/" target="_blank" rel="noopener" class="textlink">Projektbuch ansehen {ic("arrow-up-right")}</a>
    </div>
    {cta_band(p, 'Ihr Boden als nächstes Projekt?', 'Erzählen Sie uns von Ihrem Objekt. Wir melden uns und bringen Sie mit dem passenden Fachbetrieb zusammen.')}
  </div>
</section>
</main>
'''
    return h + footer(p)


# ----------------------------------------------------------------------
# Downloads
# ----------------------------------------------------------------------
def size(root, f):
    b = os.path.getsize(os.path.join(root, 'downloads', f))
    return ('%.1f MB' % (b / 1048576)).replace('.', ',') if b > 1048576 else '%d KB' % round(b / 1024)


def downloads_page(root):
    p = '../'
    h = head(p, 'Downloads | Ashford Formula Deutschland',
             'Technische Datenblätter, Reinigungsanleitung, Zertifikat und Broschüre zu Ashford Formula und den Produkten von Curecrete als PDF.')
    h += header(p, 'downloads')

    groups = [
        ('Technische Datenblätter', 'Eigenschaften, Verbrauch, Verarbeitung und Sicherheitshinweise zu jedem Produkt.',
         [(f'datenblatt-{s}.pdf', ('CreteFill Spall Repair' if s == 'cretefill' else n), c) for s, n, c, *_ in PRODUCTS]),
        ('Anwendung und Pflege', 'Damit der Boden nach der Übergabe lange gut bleibt.',
         [('reinigungsanleitung-creteclean.pdf', 'Reinigungsanleitung CreteClean Plus', 'Für Scheuersaugmaschinen')]),
        ('Zertifikate und Informationen', 'Hintergründe zum Hersteller und zum zertifizierten Verarbeiter.',
         [('stratec-zertifikat-ashford-formula-2025.pdf', 'Zertifikat Stratec Industrieboden', 'Zertifizierter Verarbeiter, gültig bis Mai 2027'),
          ('broschuere-betonsanierung-curecrete.pdf', 'Broschüre Betonsanierung', 'Curecrete, die Wissenschaft hinter Betonböden')]),
    ]
    out = ''
    for title, txt, files in groups:
        rows = ''.join(f'''
          <li><a href="{p}downloads/{f}" target="_blank" rel="noopener" class="dl">
            {ic("file-pdf", "icon dl__icon")}
            <span class="dl__txt"><b>{t}</b><span>{sub}</span></span>
            <span class="dl__meta">PDF, {size(root, f)}</span>
            <span class="dl__go">{ic("download-simple")}</span>
          </a></li>''' for f, t, sub in files)
        out += f'''
    <section class="dlgroup reveal">
      <header><h2>{title}</h2><p>{txt}</p></header>
      <ul class="dllist">{rows}
      </ul>
    </section>'''

    h += f'''
<main>
<section class="page-head">
  <div class="wrap">
    <h1>Downloads</h1>
    <p class="lead">Alle Unterlagen als PDF. Die Dateien öffnen sich in einem neuen Fenster und lassen sich von dort speichern oder drucken.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap dlgroups">{out}
  </div>
</section>

<section class="sec sec--concrete">
  <div class="wrap">
    {cta_band(p, 'Etwas nicht gefunden?', 'Weitere Unterlagen zu den Produkten schicken wir Ihnen gern auf Anfrage.')}
  </div>
</section>
</main>
'''
    return h + footer(p)


# ----------------------------------------------------------------------
# Kontakt
# ----------------------------------------------------------------------
def kontakt_page():
    p = '../'
    h = head(p, 'Kontakt | Ashford Formula Deutschland',
             'Projekt anfragen bei Beltex Commerce, dem exklusiven Vertriebspartner von Ashford Formula in Deutschland. Per Formular, E-Mail oder Telefon.')
    h += header(p, 'kontakt')
    h += f'''
<main>
<section class="page-head">
  <div class="wrap">
    <h1>Kontakt</h1>
    <p class="lead">Sie planen einen neuen Boden oder wollen einen bestehenden aufwerten? Schreiben Sie uns, wir melden uns schnellstmöglich bei Ihnen.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap contact">
    <div class="reveal">
      <h2 class="h2">So erreichen Sie uns</h2>
      <ul class="contact__info">
        <li>{ic("envelope-simple")}<div><small>E-Mail</small><a href="mailto:info@beltex.org">info@beltex.org</a></div></li>
        <li>{ic("phone")}<div><small>Telefon</small><a href="tel:+4915170869002">+49 151 70869002</a></div></li>
        <li>{ic("map-pin")}<div><small>Vertrieb in Deutschland</small>Beltex Commerce<br>Berliner Straße 21<br>56470 Bad Marienberg</div></li>
      </ul>
      <div class="next">
        <h3>Nach Ihrer Anfrage</h3>
        <ol>
          <li><b>Wir melden uns</b><span>und klären Objekt, Fläche, Zustand des Bodens und Zeitplan.</span></li>
          <li><b>Sie erhalten eine Empfehlung</b><span>für das passende Produkt und ein Angebot.</span></li>
          <li><b>Der Fachbetrieb übernimmt</b><span>die Ausführung, auf Wunsch mit Garantie über 20 Jahre.</span></li>
        </ol>
      </div>
    </div>
    {form(p)}
  </div>
</section>
</main>
'''
    return h + footer(p)


# ----------------------------------------------------------------------
# Rechtliches
# ----------------------------------------------------------------------
def legal(p, key, title, desc, body):
    h = head(p, f'{title} | Ashford Formula Deutschland', desc)
    h += header(p, key)
    h += f'''
<main>
<section class="page-head page-head--slim">
  <div class="wrap"><h1>{title}</h1></div>
</section>
<section class="sec">
  <div class="wrap legal">
{body}
  </div>
</section>
</main>
'''
    return h + footer(p)


def impressum_page():
    body = '''
    <h2>Angaben gemäß § 5 DDG</h2>
    <p>BELTEX COMMERCE<br>Inh. Maria Wolf<br>Berliner Straße 21<br>56470 Bad Marienberg</p>

    <h2>Kontakt</h2>
    <p>Telefon: <a href="tel:+4915170869002">+49 151 70869002</a><br>E-Mail: <a href="mailto:info@beltex.org">info@beltex.org</a></p>

    <h2>Umsatzsteuer</h2>
    <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz:<br>DE 215 007 905</p>

    <h2>Verantwortlich für den Inhalt gemäß § 18 Abs. 2 MStV</h2>
    <p>Maria Wolf<br>Berliner Straße 21<br>56470 Bad Marienberg</p>

    <h2>Verbraucherstreitbeilegung</h2>
    <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

    <h2>Hersteller der Produkte</h2>
    <p>Curecrete<br>1203 Spring Creek Place<br>Springville, Utah 84663, USA</p>

    <h2>Haftung für Inhalte</h2>
    <p>Die Inhalte dieser Website wurden mit Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität können wir jedoch keine Gewähr übernehmen. Maßgeblich für die Eigenschaften und die Verarbeitung der Produkte sind die jeweils aktuellen technischen Datenblätter. Als Diensteanbieter sind wir für eigene Inhalte nach den allgemeinen Gesetzen verantwortlich. Wir sind jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen. Sobald uns eine Rechtsverletzung bekannt wird, entfernen wir den betreffenden Inhalt umgehend.</p>

    <h2>Haftung für Links</h2>
    <p>Diese Website enthält Links zu externen Seiten Dritter, auf deren Inhalte wir keinen Einfluss haben. Für diese Inhalte ist stets der jeweilige Anbieter oder Betreiber verantwortlich. Zum Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar. Werden uns Rechtsverletzungen bekannt, entfernen wir den Link umgehend.</p>

    <h2>Urheberrecht</h2>
    <p>Texte, Bilder und Grafiken auf dieser Website unterliegen dem Urheberrecht. Eine Vervielfältigung, Bearbeitung oder Verbreitung außerhalb der Grenzen des Urheberrechts ist nur mit schriftlicher Zustimmung erlaubt. Produktfotos, Projektfotos und Datenblätter stammen von Curecrete. Ashford Formula, RetroPlate, RetroGuard, RetroPel, CreteClean und CreteFill sind Marken von Curecrete.</p>

    <h2>Webdesign</h2>
    <p><a href="https://ritt-happens.de" target="_blank" rel="noopener">RITT HAPPENS</a>, Lukas Rittmaier</p>
'''
    return legal('../', 'impressum', 'Impressum', 'Impressum von BELTEX COMMERCE, Inh. Maria Wolf, Bad Marienberg.', body)


def datenschutz_page():
    body = '''
    <p class="legal__intro">Wir freuen uns über Ihr Interesse an unserer Website. Der Schutz Ihrer Daten ist uns wichtig. Hier erfahren Sie, welche personenbezogenen Daten beim Besuch dieser Website verarbeitet werden, wofür und auf welcher Rechtsgrundlage.</p>

    <h2>1. Verantwortlicher</h2>
    <p>BELTEX COMMERCE<br>Inh. Maria Wolf<br>Berliner Straße 21<br>56470 Bad Marienberg<br>Telefon: +49 151 70869002<br>E-Mail: <a href="mailto:info@beltex.org">info@beltex.org</a></p>
    <p>Einen Datenschutzbeauftragten haben wir nicht bestellt, weil wir dazu gesetzlich nicht verpflichtet sind.</p>

    <h2>2. Hosting und Server-Logfiles</h2>
    <p>Diese Website wird bei der STRATO AG, Otto-Ostrowski-Straße 7, 10249 Berlin, gehostet. Mit STRATO besteht ein Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO.</p>
    <p>Bei jedem Aufruf der Website speichert der Server automatisch Informationen, die Ihr Browser übermittelt. Dazu gehören die IP-Adresse, Datum und Uhrzeit des Zugriffs, die aufgerufene Seite, die Seite, von der Sie kommen, sowie Browser und Betriebssystem. Diese Daten brauchen wir, um die Website sicher und stabil bereitzustellen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Unser berechtigtes Interesse liegt im sicheren Betrieb der Website. Die Logfiles werden nach spätestens sieben Tagen gelöscht, sofern sie nicht zur Aufklärung eines Sicherheitsvorfalls gebraucht werden.</p>

    <h2>3. Verschlüsselung</h2>
    <p>Die Verbindung zu dieser Website ist per TLS verschlüsselt. Sie erkennen das am Schloss-Symbol und an „https“ in der Adresszeile Ihres Browsers.</p>

    <h2>4. Kontaktformular und E-Mail</h2>
    <p>Wenn Sie uns über das Formular oder per E-Mail schreiben, verarbeiten wir Ihre Angaben, um Ihre Anfrage zu beantworten. Pflicht sind nur Name und E-Mail-Adresse, alle anderen Angaben sind freiwillig. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, wenn es um ein Angebot oder einen Auftrag geht, sonst Art. 6 Abs. 1 lit. f DSGVO. Wir löschen Ihre Daten, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungsfristen mehr bestehen.</p>
    <p>Geht es um ein Projekt, geben wir Ihre Angaben an unseren zertifizierten Verarbeitungspartner, die Stratec Industrieboden GmbH, weiter, damit er Sie beraten und ein Angebot erstellen kann. Das geschieht nur, soweit es für Ihre Anfrage nötig ist.</p>

    <h2>5. Cookies und Analyse</h2>
    <p>Diese Website setzt keine Cookies zu Analyse- oder Werbezwecken und verwendet keine Tracking-Dienste.</p>

    <h2>6. Schriftarten</h2>
    <p>Die Schriftarten auf dieser Website sind lokal auf unserem Server gespeichert. Beim Laden der Seiten wird keine Verbindung zu Servern von Google oder anderen Anbietern aufgebaut.</p>

    <h2>7. YouTube-Video</h2>
    <p>Auf der Seite Anwendung zeigen wir ein Video von YouTube, einem Dienst der Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Das Video wird erst geladen, wenn Sie es anklicken. Vorher werden keine Daten an YouTube übertragen. Wir nutzen den erweiterten Datenschutzmodus (youtube-nocookie.com).</p>
    <p>Sobald Sie das Video starten, wird eine Verbindung zu YouTube aufgebaut. Dabei werden unter anderem Ihre IP-Adresse und die besuchte Seite übertragen. Sind Sie bei Google angemeldet, kann YouTube den Abruf Ihrem Konto zuordnen. Eine Übermittlung in die USA ist möglich. Google ist unter dem EU-US Data Privacy Framework zertifiziert. Rechtsgrundlage ist Ihre Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1 TDDDG, die Sie mit dem Klick erteilen. Mehr dazu in der <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Datenschutzerklärung von Google</a>.</p>

    <h2>8. Externe Links</h2>
    <p>Wir verlinken auf Angebote Dritter, etwa das Projektbuch von Curecrete oder die Website von Stratec. Erst wenn Sie einen solchen Link anklicken, werden Daten an den jeweiligen Anbieter übertragen. Für dessen Datenverarbeitung ist der Anbieter verantwortlich.</p>

    <h2>9. Ihre Rechte</h2>
    <p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch gegen die Verarbeitung (Art. 21). Eine erteilte Einwilligung können Sie jederzeit für die Zukunft widerrufen. Eine formlose Nachricht an <a href="mailto:info@beltex.org">info@beltex.org</a> genügt.</p>

    <h2>10. Beschwerderecht</h2>
    <p>Sie können sich bei einer Datenschutz-Aufsichtsbehörde beschweren. Für uns zuständig ist der Landesbeauftragte für den Datenschutz und die Informationsfreiheit Rheinland-Pfalz, Hintere Bleiche 34, 55116 Mainz.</p>

    <p class="legal__date">Stand: November 2026</p>
'''
    return legal('../', 'datenschutz', 'Datenschutz', 'Datenschutzerklärung der Website von Ashford Formula Deutschland, BELTEX COMMERCE.', body)


def build_rest(root):
    def w(rel, html):
        os.makedirs(os.path.join(root, rel), exist_ok=True)
        open(os.path.join(root, rel, 'index.html'), 'w').write(html)
    for s, *_ in PRODUCTS:
        w(os.path.join('produkte', s), product_page(s))
    w('projekte', projekte_page())
    w('downloads', downloads_page(root))
    w('kontakt', kontakt_page())
    w('impressum', impressum_page())
    w('datenschutz', datenschutz_page())
