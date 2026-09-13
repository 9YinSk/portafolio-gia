# -*- coding: utf-8 -*-
"""Genera el portafolio digital (PA2 - Gestion de la Informacion y del Aprendizaje)."""
import io, os, sys
sys.stdout.reconfigure(encoding='utf-8')

AUTOR = "Gean Piere Silva Fernández"
CARRERA = "Ciencias de la Computación"
SITIO = "https://9yinsk.github.io/portafolio-gia/"

NAV = [
    ("index.html",          "Inicio"),
    ("01-definicion.html",  "1 · Definición"),
    ("02-busqueda.html",    "2 · Búsqueda"),
    ("03-contenido.html",   "3 · Contenido"),
    ("04-ia.html",          "4 · Inteligencia artificial"),
    ("05-publicacion.html", "5 · Publicación"),
]

RAYOS = """<svg class="rayos" viewBox="0 0 1200 520" preserveAspectRatio="none" aria-hidden="true">
<g stroke="#d4a04a" stroke-width="1" opacity=".55">
<line x1="1200" y1="0" x2="640" y2="520"/><line x1="1200" y1="70" x2="800" y2="520"/>
<line x1="1200" y1="180" x2="980" y2="520"/><line x1="1120" y1="0" x2="420" y2="520"/>
<line x1="1010" y1="0" x2="240" y2="520"/>
</g></svg>"""

def nav(act):
    ls = []
    for href, txt in NAV:
        c = "lk act" if href == act else "lk"
        ls.append('<a class="%s" href="%s">%s</a>' % (c, href, txt))
    return ('<nav class="nav"><div class="nav-in">'
            '<a class="marca" href="index.html"><em>&#9679;</em> Portafolio digital</a>'
            + "".join(ls) + '</div></nav>')

def rutas(act):
    i = [h for h, _ in NAV].index(act)
    out = '<div class="wrap"><div class="rutas">'
    out += ('<a href="%s">&#8592; %s</a>' % (NAV[i-1][0], NAV[i-1][1])) if i > 0 else '<span></span>'
    out += ('<a href="%s">%s &#8594;</a>' % (NAV[i+1][0], NAV[i+1][1])) if i < len(NAV)-1 else ''
    return out + '</div></div>'

PIE = """<div class="wrap"><div class="pie">
<p><strong>%s</strong> &middot; %s &middot; Universidad Continental<br>
Portafolio digital elaborado para el <strong>Producto Académico N.º 2</strong> de la asignatura
<em>Gestión de la Información y del Aprendizaje</em> &middot; Unidad 2 &middot; Setiembre de 2026.</p>
<p class="small">Los textos y las piezas gráficas de elaboración propia de este sitio se publican bajo
<a href="https://creativecommons.org/licenses/by/4.0/deed.es" rel="license">Creative Commons Atribución 4.0 Internacional (CC BY 4.0)</a>.
Los materiales citados conservan la licencia de sus autores; ninguno se reproduce, se enlaza a la fuente original.
El código de este sitio está en <a href="https://github.com/9YinSk/portafolio-gia">github.com/9YinSk/portafolio-gia</a>.</p>
</div></div>""" % (AUTOR, CARRERA)

SHELL = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="author" content="%(autor)s">
<link rel="stylesheet" href="assets/sitio.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><circle cx='16' cy='16' r='13' fill='%%236e1f33' stroke='%%23d4a04a' stroke-width='2'/><circle cx='16' cy='16' r='4' fill='%%23d4a04a'/></svg>">
</head>
<body>
%(nav)s
<header class="hero"><div class="filete"></div>%(rayos)s
  <div class="wrap">
    <div class="kicker">%(kicker)s</div>
    <h1>%(h1)s</h1>
    <p class="entrada" style="margin-top:18px">%(sub)s</p>
  </div>
</header>
<main>%(body)s</main>
%(rutas)s
%(pie)s
%(extra)s
</body></html>"""

def page(fn, title, kicker, h1, sub, body, desc="", extra=""):
    html = SHELL % dict(title=title, desc=desc or sub[:150], autor=AUTOR, nav=nav(fn),
                        rayos=RAYOS, kicker=kicker, h1=h1, sub=sub, body=body,
                        rutas=rutas(fn), pie=PIE, extra=extra)
    with io.open(fn, "w", encoding="utf-8") as f:
        f.write(html)
    print("  %-22s %6d bytes" % (fn, len(html.encode("utf-8"))))

# =====================================================================  INICIO
FOTO = """<div class="tarjeta" style="display:flex;gap:22px;align-items:center;flex-wrap:wrap">
  <div style="flex:0 0 148px">
    <img src="assets/foto.jpg" alt="Fotografía de %s" id="foto"
         style="width:148px;height:148px;object-fit:cover;border-radius:50%%;border:2px solid var(--oro)"
         onerror="this.outerHTML='&lt;div id=\'mono\' style=&quot;width:148px;height:148px;border-radius:50%%;border:2px solid var(--oro);display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed;font-size:54px;font-weight:700;color:#d4a04a;background:linear-gradient(180deg,rgba(110,31,51,.55),rgba(12,10,15,.6))&quot;&gt;GS&lt;/div&gt;'">
  </div>
  <div style="flex:1 1 300px">
    <h3 style="margin-bottom:4px">%s</h3>
    <p class="small tenue" style="margin-bottom:12px">Estudiante de %s &middot; Universidad Continental &middot; Puno, Perú</p>
    <p style="margin-bottom:0">Vivo a orillas del lago Titicaca, a 3&nbsp;800&nbsp;metros. Mi objetivo a cinco años es
    <strong>desarrollar sistemas de inteligencia artificial aplicados a la gestión del conocimiento</strong>:
    construir desde el altiplano herramientas que hoy solo se hacen en otros sitios.</p>
  </div>
</div>""" % (AUTOR, AUTOR, CARRERA)

MAPA = ""
_desc = {
 "01-definicion.html": ("Definición del proyecto",
    "El tema, por qué lo elegí, qué evidencia tengo de autoeficacia en el desempeño cognitivo y emocional, y el plan de actividades de aprendizaje de la unidad."),
 "02-busqueda.html": ("Búsqueda y selección de información",
    "La estrategia de búsqueda paso a paso, los bancos bibliográficos y repositorios usados, y la ficha crítica de cada una de las seis fuentes."),
 "03-contenido.html": ("Desarrollo del contenido",
    "Contenido multiformato: texto, infografías propias, video, gráficos de datos y un grafo de conocimiento interactivo. Incluye el plan de formación continua."),
 "04-ia.html": ("Uso de inteligencia artificial",
    "Cuatro aplicaciones de la IA en el ámbito académico y las tres herramientas que usé en este portafolio, con la evidencia de qué mejoró cada una."),
 "05-publicacion.html": ("Publicación y difusión",
    "Dónde está publicado, cómo se compartió para recibir retroalimentación, la auditoría de licencias y las referencias en APA 7."),
}
for h, t in NAV[1:]:
    ti, de = _desc[h]
    MAPA += ('<a href="%s" class="tarjeta" style="border-bottom:1px solid var(--borde);display:block">'
             '<div class="kicker" style="margin-bottom:8px">%s</div>'
             '<h3 style="margin-bottom:6px">%s</h3>'
             '<p class="small tenue" style="margin-bottom:0">%s</p></a>') % (h, t.split(" · ")[0], ti, de)

BODY_INICIO = """
<section class="bloque"><div class="wrap">
  <h2>Presentación</h2>
  %(foto)s
  <div style="height:18px"></div>
  <div class="rejilla r3">
    <div class="tarjeta"><div class="cifra">6<small>fuentes citadas</small></div></div>
    <div class="tarjeta"><div class="cifra">5<small>formatos de contenido</small></div></div>
    <div class="tarjeta"><div class="cifra">100&nbsp;%%<small>recursos con licencia auditada</small></div></div>
  </div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Qué es este portafolio</h2>
  <p class="entrada">Este sitio reúne lo que sé buscar, seleccionar y procesar. No es un currículum:
  es la <strong>evidencia</strong> de un método de trabajo con la información, aplicada a un tema concreto
  de mi carrera.</p>
  <p>El tema es <strong>cómo se organiza la información para que un sistema de inteligencia artificial no
  invente</strong>. Los modelos de lenguaje responden siempre, incluso cuando no tienen el dato; a eso se le
  llama <em>alucinación</em>. Los grafos de conocimiento y la generación aumentada por recuperación (RAG) son
  la respuesta técnica a ese problema, y son —literalmente— gestión de la información.</p>
  <p>Cada página cubre uno de los pasos que pedía la consigna, y cada una termina con lo que aprendí en ella.</p>
  <div style="height:8px"></div>
  <div class="rejilla r2">%(mapa)s</div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Acceso</h2>
  <div class="rejilla r2">
    <div class="tarjeta">
      <h3>Para el docente</h3>
      <p class="small" style="margin-bottom:0">El sitio es <strong>público</strong>: se abre con el enlace, sin
      cuenta, sin solicitud de permiso y sin inicio de sesión. No hay nada que autorizar. Funciona en
      computadora y en teléfono.</p>
    </div>
    <div class="tarjeta">
      <h3>Dónde está publicado</h3>
      <p class="small" style="margin-bottom:0">En <strong>GitHub&nbsp;Pages</strong>, una plataforma gratuita de
      publicación web. Elegí esta y no un constructor visual porque en Ciencias de la Computación el portafolio
      que revisa un empleador es, casi siempre, el repositorio: el sitio y su código fuente viven en el mismo
      sitio y cualquiera puede revisar cómo está hecho.</p>
    </div>
  </div>
</div></section>
""" % dict(foto=FOTO, mapa=MAPA)

page("index.html",
     "Portafolio digital &middot; %s" % AUTOR,
     "Gestión de la Información y del Aprendizaje &middot; Unidad 2",
     "Grafos de conocimiento y RAG",
     "Portafolio digital de %s, estudiante de %s. Cómo se organiza la información para que una inteligencia artificial no invente." % (AUTOR, CARRERA),
     BODY_INICIO,
     desc="Portafolio digital de %s (%s, Universidad Continental) sobre grafos de conocimiento y RAG." % (AUTOR, CARRERA))
