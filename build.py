import html
NAV=[("index.html","მთავარი"),("support.html","მხარდაჭერა"),("donations.html","დონაციები"),("courses.html","კურსები"),("files.html","ფაილები"),("about.html","შესახებ"),("join.html","შემოგვიერთდით"),("contact.html","კონტაქტი")]
TOPO='<svg class="topo" viewBox="0 0 1200 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'+"".join(f'<path d="M-50 {80+i*40} C 200 {20+i*45}, 380 {170+i*30}, 620 {90+i*38} S 1000 {10+i*40}, 1260 {110+i*34}"/>' for i in range(14))+'</svg>'
def page(fn,title,body,desc=""):
    nav="".join(f'<a href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a>' for h,t in NAV)
    open(fn,"w").write(f'''<!doctype html><html lang="ka"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc or 'GIS GEORGIA — Open Source GIS საზოგადოება საქართველოში'}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Georgian:wght@400;600;800&display=swap">
<link rel="stylesheet" href="style.css"></head><body>
<header class="top"><div class="wrap"><a class="brand" href="index.html"><i></i>GIS GEORGIA</a>
<button id="menu" aria-label="მენიუ">☰</button><nav id="nav">{nav}<button id="theme" aria-label="თემა">◐</button></nav></div></header>
{body}
<footer><div class="wrap"><span>© GIS GEORGIA · 2014–2026</span><span><a href="https://github.com/GIS-GEORGIA">GitHub</a> · <a href="https://t.me/GIS_GEO">Telegram</a> · <a href="mailto:kapan.gio777@gmail.com">kapan.gio777@gmail.com</a></span></div></footer>
<script>
const r=document.documentElement;try{{const t=localStorage.getItem('t');if(t)r.dataset.theme=t}}catch(e){{}}
document.getElementById('theme').onclick=()=>{{const d=r.dataset.theme?r.dataset.theme==='dark':matchMedia('(prefers-color-scheme:dark)').matches;r.dataset.theme=d?'light':'dark';try{{localStorage.setItem('t',r.dataset.theme)}}catch(e){{}}}};
document.getElementById('menu').onclick=()=>document.getElementById('nav').classList.toggle('open');
document.querySelectorAll('[data-copy]').forEach(b=>b.onclick=()=>{{navigator.clipboard.writeText(b.dataset.copy);const o=b.textContent;b.textContent='✓';setTimeout(()=>b.textContent=o,1200)}});
</script></body></html>''')

REPOS=[("qgis-plugins-repo","QGIS პლაგინების რეპოზიტორია GIS GEORGIA-ს გუნდისგან","Python"),
("qgis-geogit","პროექტის ვერსიების კონტროლი QGIS-ში (git + LFS), რუკების diff და GeoPackage merge","Python"),
("qgis-mcp","Claude Code-ით QGIS-ის მართვა — პლაგინი, MCP სერვერი, headless რეჟიმი","Python"),
("pyqgis-devbridge","PyQGIS დეველოპმენტის გარემო და live debugging VS Code/PyCharm-ში","Python"),
("postgis-manager","QGIS პლაგინი და დამოუკიდებელი აპი ქართულ/ინგლისური ინტერფეისით","Python"),
("gis-toolkit","ორენოვანი GIS ინსტრუმენტარიუმი: ნაwritten ნprinciple".replace("ნაwritten ნprinciple","ნაკვეთების ძებნა და კოორდინატების ამოღება"),"Python"),
("fiberq-ka","FiberQ QGIS პლაგინის ქართული თარგმანი და სასწავლო ბაზა","HTML"),
("amindi","მრავალმოდელიანი ამინდის პროგნოზი საქართველოსთვის (Flutter)","Dart"),
("niveliri","ნიველირის გამოთვლის კალკულატორი (ქართ./ინგლ.)","Dart"),
("parcel-vertices","ნაკვეთის წვეროების კოორდინატები (WGS84/UTM) და DXF ექსპორტი","Dart"),
("Fuel_calculator","საწვავის ხარჯის კალკულატორი A→B რუკით და 8 კომპანიის ფასებით","HTML"),
("car","საქართველოს გზების მდგომარეობის ინტერაქტიული რუკა და ჯარიმების ცნობარი","JavaScript"),
("qgis-ge-launcher","ბრაუზერის გაფართოება qgis.ge-სა და GitHub-ზე სწრაფი წვდომისთვის","JavaScript"),
("postgis-docker-starter","PostGIS-ის სწრაფი სტარტი Docker-ით","Docker"),
("agrohub","GeoFruct — ქართველი ხილის მწარმოებლების კატალოგი","TypeScript"),
("gca-website","საქართველოს კარტოგრაფთა ასოციაციის ვებსაიტი","TypeScript")]
cards="".join(f'<a class="card" href="https://github.com/GIS-GEORGIA/{n}"><span class="tag">{l}</span><h3>{n}</h3><p>{d}</p></a>' for n,d,l in REPOS)
SOC=[("Facebook გვერდი","http://bit.ly/2HfKw7N"),("Facebook ჯგუფი","http://bit.ly/2W2rYjC"),("Messenger ჩატი","http://m.me/GISGeorgia"),("Instagram","https://www.instagram.com/gis_georgia/"),("X ჯგუფი","https://bit.ly/3l8gciU"),("Telegram არხი","http://bit.ly/2E4HeCu"),("Telegram ჩატი","https://t.me/GIS_GEO"),("LinkedIn გვერდი","https://bit.ly/3bffU2z"),("LinkedIn ჯგუფი","http://bit.ly/2vTdfZH"),("YouTube არხი","http://bit.ly/2PxEGFl"),("Overclockers ფორუმი","http://bit.ly/2JrkIFz"),("GitHub","https://github.com/GIS-GEORGIA")]
soc="".join(f'<a class="card" href="{u}"><h3>{t} ↗</h3></a>' for t,u in SOC)

page("index.html","GIS GEORGIA — Open Source GIS საქართველოში",f'''
<div class="hero">{TOPO}<div class="wrap"><span class="eyebrow">Open Source GIS საზოგადოება</span>
<h1>რუკები, გეოდატა და ღია კოდი საქართველოსთვის</h1>
<p class="lead">GIS GEORGIA 2014 წლიდან აერთიანებს გეოინფორმატიკით დაინტერესებულ ადამიანებს: საზოგადოება, სასწავლო მასალები, QGIS პლაგინები და ღია პროექტები.</p>
<div class="btns"><a class="btn" href="join.html">შემოგვიერთდი</a><a class="btn ghost" href="https://github.com/GIS-GEORGIA">GitHub-ზე ნახე</a><a class="btn ghost" href="support.html">მხარდაჭერა</a></div>
<div class="stats"><div><b>2014</b><span>დაარსება</span></div><div><b>23+</b><span>ღია რეპოზიტორია</span></div><div><b>11</b><span>პლატფორმა</span></div></div></div></div>
<section class="alt"><div class="wrap"><h2>პროექტები</h2><p class="sub">ჩვენი შემოქმედება GitHub-ზე — პლაგინები, აპები და ინსტრუმენტები.</p><div class="grid">{cards}</div>
<p style="margin-top:24px"><a href="https://github.com/GIS-GEORGIA?tab=repositories">ყველა რეპოზიტორია →</a></p></div></section>
<section><div class="wrap"><h2>შემოგვიერთდი</h2><p class="sub">იპოვე ჩვენი საზოგადოება შენთვის სასურველ პლატფორმაზე.</p><div class="grid">{soc}</div></div></section>''')

def pay(label,v): return f'<div class="card"><h3>{label}</h3><div class="pay"><span>{v}</span><button data-copy="{v}">კოპირება</button></div></div>'
page("support.html","მხარდაჭერა — GIS GEORGIA",f'''<div class="wrap page"><span class="eyebrow">მხარდაჭერა</span><h1>დაგვიჭირე მხარი</h1>
<p class="lead">GIS GEORGIA არის არაკომერციული, ენთუზიაზმზე დაფუძნებული საზოგადოება. შენი დახმარება გვაძლევს საშუალებას, გავაგრძელოთ სასწავლო მასალების, ღია ხელსაწყოების და პროექტების განვითარება.</p>
<div class="btns"><a class="btn" href="https://paypal.me/kapanadzeg">PayPal</a><a class="btn ghost" href="https://ko-fi.com/ezdanapak">Ko-fi ☕</a></div></div>
<section><div class="wrap"><h2>საბანკო გადარიცხვა</h2><p class="sub">დააჭირე „კოპირებას“ ანგარიშის ნომრის დასაკოპირებლად.</p><div class="grid">
{pay("თიბისი ბანკი","GE40TB7805436515100030")}
{pay("საქართველოს ბანკი","GE12BG0000000345931015")}</div></div></section>''')

page("donations.html","დონაციები — GIS GEORGIA",'''<div class="wrap page"><span class="eyebrow">დონაციები</span><h1>პროექტები, რომლებსაც ვუჭერთ მხარს</h1>
<p class="lead">ღია პროგრამული უზრუნველყოფის ეკოსისტემა ცოცხლობს მხარდაჭერით. GIS GEORGIA მხარს უჭერს ღია GIS პროექტებს.</p></div>
<section><div class="wrap"><div class="grid"><a class="card" href="https://qgis.org/funding/donate/"><span class="tag">ღია GIS</span><h3>QGIS ↗</h3><p>მსოფლიოში ყველაზე პოპულარული ღია GIS პროგრამა.</p></a>
<a class="card" href="https://www.osgeo.org/about/sponsors/"><span class="tag">ფონდი</span><h3>OSGeo ↗</h3><p>Open Source Geospatial Foundation.</p></a></div>
<p class="sub" style="margin-top:24px">აქ დაემატება დანარჩენი მხარდაჭერილი პროექტები.</p></div></section>''')

TL=[("2014-10-01","Facebook ჯგუფი"),("2017-01-07","ვებსაიტი"),("2017-07-26","Facebook გვერდი"),("2018-10-27","ფორუმი"),("2019-02-10","LinkedIn ჯგუფი"),("2020-01-08","LinkedIn გვერდი"),("2020-08-04","Instagram"),("2021","Discord სერვერი"),("2022-05-13","X საზოგადოება"),("2022-05-23","SuperMap-თან თანამშრომლობა"),("2024-05-19","qgis.ge დომენი"),("2025-05-15","QGIS Plugins რეპოზიტორია და GitHub")]
tl="".join(f"<li><time>{d}</time>{t}</li>" for d,t in TL)
page("about.html","შესახებ — GIS GEORGIA",f'''<div class="wrap page"><span class="eyebrow">შესახებ</span><h1>ჩვენი გზა</h1><p class="lead">ერთი Facebook ჯგუფიდან — ღია GIS ეკოსისტემამდე.</p></div>
<section><div class="wrap"><ul class="tl">{tl}</ul></div></section>''')

page("join.html","შემოგვიერთდით — GIS GEORGIA",f'''<div class="wrap page"><span class="eyebrow">საზოგადოება</span><h1>შემოგვიერთდით</h1><p class="lead">ჩვენი რესურსები სხვადასხვა პლატფორმაზეა გადანაწილებული — აირჩიე შენთვის მოსახერხებელი.</p></div>
<section><div class="wrap"><div class="grid">{soc}</div></div></section>''')

LINKS=[("BTU","https://btu.edu.ge/our_team/giorgi-kapanadze/"),("LinkedIn","https://linkedin.com/in/ezdanapak/"),("Telegram","https://t.me/GKGIS"),("OSGeo","https://osgeo.org/member/kapanadze/"),("Medium","https://kapanadze.medium.com"),("Observable","https://observablehq.com/@kapannn"),("DEV","https://dev.to/kapanadze"),("Substack","https://kapanadze.substack.com"),("Gitee","https://gitee.com/KAPANADZE")]
page("contact.html","კონტაქტი — GIS GEORGIA",f'''<div class="wrap page"><span class="eyebrow">კონტაქტი</span><h1>გიორგი კაპანაძე</h1><p class="lead">GIS GEORGIA-ს ავტორი და სულისჩამდგმელი.</p>
<div class="btns"><a class="btn" href="mailto:kapan.gio777@gmail.com">ელფოსტა</a><a class="btn ghost" href="tel:+995579320618">(+995) 579 32 06 18</a></div></div>
<section class="alt"><div class="wrap"><h2>სერვისები</h2><p class="sub">GIS საქმიანობისთვის</p><div class="grid">
<div class="card"><h3>GIS Consultant</h3><p>გეოსივრცული სტრატეგიები, სტანდარტები, ყოველდღიური ამოცანები და ავტომატიზაცია.</p></div>
<div class="card"><h3>GIS Recruiter</h3><p>გეოსივრცული გუნდის აწყობაში დახმარება.</p></div>
<div class="card"><h3>GIS Training</h3><p>ტექნიკური ექსპერტიზის განვითარება.</p></div>
<div class="card"><h3>GIS Coach</h3><p>კარიერული გზის დაგეგმვა.</p></div></div></div></section>
<section><div class="wrap"><h2>ბიოგრაფია</h2><ul class="clean">
<li>გეოგრაფიის მაგისტრი გეოგრაფიული ინფორმაციული სისტემების ტექნოლოგიებში.</li>
<li>საქართველოს ტექნიკური უნივერსიტეტის დოქტორანტი.</li>
<li>ბიზნესისა და ტექნოლოგიების უნივერსიტეტის ასისტენტ-პროფესორი GIS მიმართულებით.</li>
<li>საქართველოს ეროვნული უნივერსიტეტის მოწვეული სპეციალისტი — GIS ტურიზმში.</li>
<li>საქართველოს ტექნიკური უნივერსიტეტის მოწვეული სპეციალისტი — GIS-ის საფუძვლები.</li>
<li>საქართველოს კარტოგრაფთა ასოციაციის სამეცნიერო საბჭოს წევრი.</li></ul>
<h2 style="margin-top:32px">პროფილები</h2><div class="btns">{"".join(f'<a class="btn ghost" href="{u}">{t}</a>' for t,u in LINKS)}</div></div></section>''')

SES=[("თეორია და გეორეფერენცია","კოორდინატები, პროექციები, EPSG კოდები; ძველი და ახალი ტოპორუკების, საკადასტრო გეგმებისა და კოსმოსური სურათების გეორეფერენცია"),
("Shapefile და ციფრულება","ფაილის სტრუქტურა, UTM ზონის არჩევა, პროექტის საქაღალდეების ორგანიზება"),
("რედაქტირების ხელსაწყოები","Quick Map Services, snapping, წვეროების რედაქტირება, გეომეტრიული ოპერაციები, SVG სიმბოლოები, ატრიბუტთა ცხრილი"),
("მონაცემთა წყაროები","OpenStreetMap, DIVA-GIS, NSDI კატალოგი, GPS კოორდინატების იმპორტი, ტოპოლოგიის შემოწმება"),
("გეომონაცემთა ბაზები","GeoPackage, SQLite, ველების კალკულატორი, გეომეტრიული გაზომვები"),
("SQL და შერჩევა","SQL საფუძვლები, სივრცული და ატრიბუტული შერჩევა"),
("სერვისები","GeoServer (WMS/WFS), GeoNode, GeoNetwork"),
("რასტრები","აერო და კოსმოსური სურათები, გარჩევადობა, NDVI და NBR ინდექსები, რელიეფის ანალიზი"),
("მეტამონაცემები და დრო","მეტამონაცემები, INSPIRE, NSDI, დროითი ვიზუალიზაცია, KML/GML/GeoJSON/TAB"),
("ლეიაუტები","რუკის კომპოზიცია: ჩრდილოეთის ისარი, ლეგენდა, სათაური, კოორდინატთა ბადე, შაბლონები")]
ses="".join(f'<div class="card"><span class="tag">სესია {i}</span><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(SES,1))
page("courses.html","კურსები — GIS GEORGIA",f'''<div class="wrap page"><span class="eyebrow">QGIS კურსები</span><h1>ისწავლე QGIS ნულიდან</h1>
<p class="lead">საბაზო კურსი 10 სესიისგან, PyQGIS პროგრამირება და არაფორმალური განათლება. სხვადასხვა კურსის ჩანაწერები ხელმისაწვდომია ვიდეოებად: Autodesk, ArcGIS, QGIS, Drone Photogrammetry, Python, MATLAB, FME, PostgreSQL/PostGIS, GeoServer, Docker.</p>
<div class="btns"><a class="btn" href="https://bit.ly/3MfoLq8">კურსების ჩანაწერები</a><a class="btn ghost" href="https://osdoc.qgis.ge">osdoc.qgis.ge სახელმძღვანელოები</a></div></div>
<section class="alt"><div class="wrap"><h2>QGIS Basic Course</h2><p class="sub">10 სესიის პროგრამა</p><div class="grid">{ses}</div></div></section>
<section><div class="wrap"><h2>PyQGIS</h2><p class="sub">Python QGIS-ში: ატრიბუტების ველების მართვა iface.activeLayer()-ით, Python კლასები და მემკვიდრეობა, PyQGIS კლასების გამოყენება (მანძილის გამოთვლა). მასალა მუშავდება.</p>
<h2 style="margin-top:32px">სერტიფიკატები</h2><ul class="clean"><li><b>არაოფიციალური:</b> LinkedIn Learning-ის QGIS კურსი და სერტიფიკატი პროფილზე. ყურადღება: ფასიანი საცდელი პერიოდი მოითხოვს ბარათს — 29 დღის შემდეგ გააუქმეთ გამოწერა.</li><li><b>ოფიციალური:</b> QGIS.org ასოციაციის მეშვეობით.</li></ul></div></section>''')

def lk(items): return "".join(f'<a class="card" href="{u}"><h3>{t} ↗</h3><p>{d}</p></a>' for t,u,d in items)
RAS=[("USGS Historical Topo Explorer","https://ngmdb.usgs.gov/topoview/","ისტორიული ტოპოგრაფიული რუკები"),
("ArcGIS Wayback","https://livingatlas.arcgis.com/wayback/","World Imagery-ის ისტორიული ვერსიები"),
("SRTM (USGS)","https://earthexplorer.usgs.gov/","რელიეფის ციფრული მოდელი"),
("OpenTopography","https://opentopography.org","DEM და LiDAR მონაცემები"),
("OpenAerialMap","https://openaerialmap.org","ღია აერო/დრონის სურათები"),
("OpenDroneMap","https://opendronemap.org","დრონის ფოტოგრამეტრია"),
("Sentinel Hub","https://www.sentinel-hub.com","Sentinel-ის სურათები"),
("Landsat Viewer","https://landsatlook.usgs.gov/explore","Landsat არქივი"),
("Copernicus Climate Data Store","https://cds.climate.copernicus.eu","კლიმატური მონაცემები"),
("NASA Remote Sensing Toolkit","https://nasa-rst.org","შორეული ზონდირების ხელსაწყოები")]
VEC=[("National Agency of Public Registry","https://maps.gov.ge","საჯარო რეესტრის რუკა"),
("MEPA პორტალი","https://portal.mepa.gov.ge","გარემოს დაცვისა და სოფლის მეურნეობის სამინისტრო"),
("Cultural Heritage","https://memkvidreoba.gov.ge","კულტურული მემკვიდრეობის პორტალი"),
("Geofabrik","https://download.geofabrik.de","OSM მონაცემები ქვეყნების მიხედვით"),
("Natural Earth","https://www.naturalearthdata.com","მსოფლიოს საჯარო ვექტორული მონაცემები"),
("DIVA-GIS","https://diva-gis.org/data","ქვეყნების მონაცემები"),
("GADM","https://gadm.org","ადმინისტრაციული საზღვრები"),
("Marine Regions","https://www.marineregions.org","საზღვაო რეგიონები"),
("Kepler.gl","https://kepler.gl","ვებ-ვიზუალიზაცია"),
("Maputnik","https://maputnik.github.io","MapLibre სტილის რედაქტორი"),
("Lizmap","https://www.lizmap.com","QGIS პროექტი ვებში"),
("STAC Browser","https://radiantearth.github.io/stac-browser/","STAC კატალოგები")]
PRG=[("OBS Studio","https://obsproject.com/","ვიდეოს ჩაწერა, უფასო"),("ShareX","https://getsharex.com/","ფოტო და ვიდეო ეკრანიდან"),("LightShot","https://app.prntscr.com/en/index.html","სწრაფი სქრინშოტები"),
("Automating GIS processes","https://autogis-site.readthedocs.io/en/2020_/index.html","Python GIS სახელმძღვანელო (2020)"),("Geo-Python","https://geo-python-site.readthedocs.io/en/latest/","Geo-Python 2022"),
("Solara","https://github.com/widgetti/solara","Pure Python, React-სტილის framework"),("Earth Engine Web Apps","https://giswqs-solara-geemap.hf.space/","geemap + Solara"),("PDFCraft","https://github.com/PDFCraftTool/pdfcraft","PDF ხელსაწყო")]
page("files.html","ფაილები და რესურსები — GIS GEORGIA",f'''<div class="wrap page"><span class="eyebrow">რესურსები</span><h1>მონაცემები და ხელსაწყოები</h1><p class="lead">რასტრული და ვექტორული მონაცემების წყაროები, პროგრამები და სასწავლო რესურსები ერთ ადგილას.</p></div>
<section class="alt"><div class="wrap"><h2>რასტრი</h2><p class="sub">სურათები, რელიეფი, დისტანციური ზონდირება</p><div class="grid">{lk(RAS)}</div></div></section>
<section><div class="wrap"><h2>ვექტორი</h2><p class="sub">ინტერაქტიული რუკები, მონაცემთა წყაროები, ვებ-ხელსაწყოები</p><div class="grid">{lk(VEC)}</div></div></section>
<section class="alt"><div class="wrap"><h2>პროგრამები და Python</h2><p class="sub">უფასო ხელსაწყოები და სასწავლო რესურსები</p><div class="grid">{lk(PRG)}</div></div></section>''')
