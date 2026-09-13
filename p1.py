# -*- coding: utf-8 -*-
from build import *

SVG_BANDURA = """
<figure>
<svg viewBox="0 0 980 430" role="img" aria-label="Las cuatro fuentes de la autoeficacia segun Bandura y la evidencia de cada una en este trabajo" style="width:100%;height:auto;border:1px solid var(--borde);border-radius:12px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012))">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#6e1f33"/><stop offset="1" stop-color="#a03652"/>
    </linearGradient>
  </defs>
  <text x="40" y="46" fill="#d4a04a" font-family="Barlow Condensed, sans-serif" font-size="17" letter-spacing="3">LAS CUATRO FUENTES DE LA AUTOEFICACIA (BANDURA, 1977)</text>
  <text x="40" y="72" fill="#a89c8b" font-family="Barlow, sans-serif" font-size="15">Debajo de cada fuente, la evidencia concreta que aporta este portafolio.</text>

  <g font-family="Barlow Condensed, sans-serif">
    <rect x="40"  y="100" width="212" height="76" rx="12" fill="url(#g1)" stroke="#d4a04a" stroke-opacity=".45"/>
    <rect x="272" y="100" width="212" height="76" rx="12" fill="url(#g1)" stroke="#d4a04a" stroke-opacity=".45"/>
    <rect x="504" y="100" width="212" height="76" rx="12" fill="url(#g1)" stroke="#d4a04a" stroke-opacity=".45"/>
    <rect x="736" y="100" width="212" height="76" rx="12" fill="url(#g1)" stroke="#d4a04a" stroke-opacity=".45"/>
    <text x="146" y="132" fill="#fff" font-size="21" font-weight="700" text-anchor="middle">Experiencias</text>
    <text x="146" y="156" fill="#fff" font-size="21" font-weight="700" text-anchor="middle">de dominio</text>
    <text x="378" y="132" fill="#fff" font-size="21" font-weight="700" text-anchor="middle">Experiencias</text>
    <text x="378" y="156" fill="#fff" font-size="21" font-weight="700" text-anchor="middle">vicarias</text>
    <text x="610" y="144" fill="#fff" font-size="21" font-weight="700" text-anchor="middle">Persuasion verbal</text>
    <text x="842" y="132" fill="#fff" font-size="21" font-weight="700" text-anchor="middle">Estados fisiologicos</text>
    <text x="842" y="156" fill="#fff" font-size="21" font-weight="700" text-anchor="middle">y emocionales</text>
  </g>

  <g stroke="#d4a04a" stroke-opacity=".55" stroke-width="1.5">
    <line x1="146" y1="176" x2="146" y2="206"/><line x1="378" y1="176" x2="378" y2="206"/>
    <line x1="610" y1="176" x2="610" y2="206"/><line x1="842" y1="176" x2="842" y2="206"/>
  </g>

  <g font-family="Barlow, sans-serif" font-size="14.5" fill="#e6dccb">
    <rect x="40"  y="206" width="212" height="176" rx="12" fill="rgba(255,255,255,.05)" stroke="#d4a04a" stroke-opacity=".22"/>
    <rect x="272" y="206" width="212" height="176" rx="12" fill="rgba(255,255,255,.05)" stroke="#d4a04a" stroke-opacity=".22"/>
    <rect x="504" y="206" width="212" height="176" rx="12" fill="rgba(255,255,255,.05)" stroke="#d4a04a" stroke-opacity=".22"/>
    <rect x="736" y="206" width="212" height="176" rx="12" fill="rgba(255,255,255,.05)" stroke="#d4a04a" stroke-opacity=".22"/>
    <text x="58"  y="234" fill="#d4a04a" font-family="Barlow Condensed, sans-serif" font-size="15" letter-spacing="1.8">LA MAS FUERTE</text>
    <text x="58"  y="262">Cinco fallos tecnicos</text><text x="58" y="282">del PA1 resueltos y</text>
    <text x="58"  y="302">documentados, no</text><text x="58" y="322">esquivados. Es la</text>
    <text x="58"  y="342">bitacora, no el</text><text x="58" y="362">recuerdo.</text>
    <text x="290" y="234" fill="#d4a04a" font-family="Barlow Condensed, sans-serif" font-size="15" letter-spacing="1.8">VER A OTROS</text>
    <text x="290" y="262">Los autores del libro</text><text x="290" y="282">de referencia del campo</text>
    <text x="290" y="302">son de la Universidad</text><text x="290" y="322">de Chile: el tema no</text>
    <text x="290" y="342">es ajeno a la region.</text>
    <text x="522" y="234" fill="#d4a04a" font-family="Barlow Condensed, sans-serif" font-size="15" letter-spacing="1.8">RETROALIMENTACION</text>
    <text x="522" y="262">El portafolio se abre a</text><text x="522" y="282">comentarios de los</text>
    <text x="522" y="302">companeros en el foro</text><text x="522" y="322">antes de darlo por</text>
    <text x="522" y="342">terminado (pagina 5).</text>
    <text x="754" y="234" fill="#d4a04a" font-family="Barlow Condensed, sans-serif" font-size="15" letter-spacing="1.8">REGULARSE</text>
    <text x="754" y="262">Trabajar con entregas</text><text x="754" y="282">simultaneas sin que la</text>
    <text x="754" y="302">prisa decida la calidad:</text><text x="754" y="322">por eso hay un plan por</text>
    <text x="754" y="342">dias, y no una noche</text><text x="754" y="362">entera.</text>
  </g>
</svg>
<figcaption><strong>Gr&aacute;fico 1.</strong> Elaboraci&oacute;n propia a partir de Bandura (1977). Las cuatro fuentes de las
creencias de eficacia personal, contrastadas con la evidencia disponible en este trabajo. CC BY 4.0.</figcaption>
</figure>"""

PLAN = """
<div class="tabla-scroll"><table>
<thead><tr><th style="width:118px">Fecha</th><th>Actividad de aprendizaje</th><th style="width:150px">Producto</th><th style="width:106px">Estado</th></tr></thead>
<tbody>
<tr><td>1 &ndash; 4 set</td><td>Lectura del material obligatorio de la unidad: inteligencia emocional en la educaci&oacute;n universitaria, y usos y efectos de la IA en educaci&oacute;n. Fichas de lectura.</td><td>Fichas</td><td><span class="pill ok">Hecho</span></td></tr>
<tr><td>5 set</td><td>B&uacute;squeda en repositorios: definici&oacute;n de la ecuaci&oacute;n de b&uacute;squeda y cribado de resultados en SciELO, arXiv y unesdoc.</td><td>Lista de candidatas</td><td><span class="pill ok">Hecho</span></td></tr>
<tr><td>6 set</td><td>Producci&oacute;n del muro digital del PA1 y de las cuatro piezas gr&aacute;ficas. Bit&aacute;cora de los cinco problemas t&eacute;cnicos.</td><td>PA1 entregado</td><td><span class="pill ok">Hecho</span></td></tr>
<tr><td>7 &ndash; 10 set</td><td>Autoevaluaci&oacute;n N.&ordm;&nbsp;2 y participaci&oacute;n en el foro formativo, leyendo antes los aportes de los compa&ntilde;eros.</td><td>Foro y autoevaluaci&oacute;n</td><td><span class="pill ok">Hecho</span></td></tr>
<tr><td>11 &ndash; 12 set</td><td>Ampliaci&oacute;n de las fuentes de tres a seis y auditor&iacute;a de la licencia de cada una.</td><td>Fichas cr&iacute;ticas</td><td><span class="pill ok">Hecho</span></td></tr>
<tr><td>13 set</td><td>Construcci&oacute;n y publicaci&oacute;n del portafolio digital; difusi&oacute;n en el foro para retroalimentaci&oacute;n entre pares.</td><td>PA2 entregado</td><td><span class="pill ok">Hecho</span></td></tr>
<tr><td>14 &ndash; 20 set</td><td>Incorporar la retroalimentaci&oacute;n recibida y cerrar el ciclo con la mejora aplicada.</td><td>Versi&oacute;n 2 del sitio</td><td><span class="pill">En curso</span></td></tr>
<tr><td>Continuo</td><td>Formaci&oacute;n continua: curso abierto de aprendizaje autom&aacute;tico sobre grafos y alertas de novedades del tema (ver p&aacute;gina&nbsp;3).</td><td>Bit&aacute;cora de estudio</td><td><span class="pill">Permanente</span></td></tr>
</tbody></table></div>"""

BODY = """
<section class="bloque"><div class="wrap">
  <h2>El tema, y por qu&eacute; este</h2>
  <p class="entrada">Eleg&iacute; <strong>grafos de conocimiento y generaci&oacute;n aumentada por recuperaci&oacute;n (RAG)</strong>:
  el conjunto de t&eacute;cnicas que se usan para que un modelo de lenguaje responda a partir de fuentes verificables
  en lugar de hacerlo a partir de su propia memoria.</p>
  <p>La raz&oacute;n no es solo que sea el problema que m&aacute;s me interesa de mi carrera. Es que <strong>es exactamente
  el objeto de esta asignatura</strong>. Un sistema RAG hace, automatizado, lo mismo que se nos pide a nosotros
  en un trabajo acad&eacute;mico: buscar en un corpus, seleccionar lo pertinente, procesarlo y responder
  <em>citando de d&oacute;nde sali&oacute;</em>. Cuando ese &uacute;ltimo paso falla, al sistema se le llama alucinaci&oacute;n;
  cuando nos falla a nosotros, se llama plagio o error de fuente. Es el mismo fallo con dos nombres.</p>
  <p>El tema permit&iacute;a adem&aacute;s algo que uno m&aacute;s c&oacute;modo no habr&iacute;a permitido:
  <strong>aplicar el m&eacute;todo en vez de describirlo</strong>. En la p&aacute;gina 3 no explico qu&eacute; es un grafo de
  conocimiento: hay uno construido con las fuentes de este mismo portafolio, y se puede tocar.</p>
  <div class="nota"><strong>Delimitaci&oacute;n.</strong> No abarco todo el campo. Me limito a una pregunta:
  &laquo;&iquest;qu&eacute; se gana y qu&eacute; cuesta a&ntilde;adir estructura de grafo a un sistema de recuperaci&oacute;n?&raquo;,
  porque es la que puedo sostener con fuentes arbitradas y con una prueba propia, y no con opini&oacute;n.</div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Autoeficacia en el desempe&ntilde;o cognitivo y emocional</h2>
  <p>La unidad parte de Bandura. Su tesis es que lo que decide el esfuerzo y la persistencia no es la
  habilidad que uno tiene, sino <strong>la que uno cree tener</strong>:</p>
  <blockquote>Las expectativas de eficacia personal determinan cu&aacute;nto esfuerzo invertir&aacute;n las personas
  y cu&aacute;nto tiempo lo sostendr&aacute;n frente a los obst&aacute;culos y las experiencias adversas.
  <cite>Bandura (1977, p.&nbsp;194), traducci&oacute;n propia</cite></blockquote>
  <p>Me interesa la parte que se suele saltar: Bandura dice tambi&eacute;n <strong>de d&oacute;nde sale esa creencia</strong>,
  y la fuente m&aacute;s potente no es animarse, son las <em>experiencias de dominio</em>: haber resuelto antes algo
  parecido. Eso convierte la autoeficacia en algo que se puede construir a prop&oacute;sito y, sobre todo, en algo
  que se puede documentar.</p>
  %(svg)s
  <h3>Mi evidencia, no mi declaraci&oacute;n</h3>
  <p>Decir &laquo;conf&iacute;o en mis capacidades&raquo; no demuestra nada. Lo que s&iacute; demuestra algo es una
  <strong>bit&aacute;cora</strong>. En el trabajo anterior de esta misma asignatura anot&eacute; cinco fallos t&eacute;cnicos
  mientras los resolv&iacute;a: un exportador de im&aacute;genes que se negaba a escribir el archivo, una l&aacute;mina que
  sal&iacute;a cortada, un grafo que se dibujaba solo en media imagen, tildes que desaparec&iacute;an en una sustituci&oacute;n
  de texto y una b&uacute;squeda bibliogr&aacute;fica que no devolv&iacute;a nada en espa&ntilde;ol.</p>
  <p>De los cinco, el que m&aacute;s me ense&ntilde;&oacute; fue el de las tildes, porque
  <strong>el programa no daba ning&uacute;n error</strong>: dec&iacute;a &laquo;no encontrado&raquo; y segu&iacute;a. Un fallo
  silencioso es peor que uno ruidoso, y la &uacute;nica defensa es verificar la salida en lugar de confiar en que no
  hubo aviso. Es la misma desconfianza que hay que tenerle a un modelo de lenguaje que responde con seguridad.</p>
  <div class="rejilla r2" style="margin-top:20px">
    <div class="tarjeta"><h3>Lo cognitivo</h3><p class="small" style="margin-bottom:0">Ante un problema nuevo,
    partirlo hasta que una de las partes sea comprobable. Los cinco fallos ten&iacute;an algo en com&uacute;n: la causa
    que yo supon&iacute;a no era la real, y aparec&iacute;a midiendo, no razonando.</p></div>
    <div class="tarjeta"><h3>Lo emocional</h3><p class="small" style="margin-bottom:0">Llevo tres asignaturas
    con entregas que caen la misma semana. Lo que me funciona no es &laquo;tener &aacute;nimo&raquo;: es quitarle a la
    prisa la capacidad de decidir. Plan por d&iacute;as, lo que depende de otros primero, y el trabajo que exige
    concentraci&oacute;n fuera de la franja de clases.</p></div>
  </div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Planificaci&oacute;n de las actividades de aprendizaje</h2>
  <p>Este es el plan real de la unidad, con lo que ya est&aacute; cerrado y lo que sigue abierto. Lo que importa no
  es el cronograma en s&iacute;: es que las actividades que <strong>dependen de otras personas</strong> &mdash;el foro, la
  retroalimentaci&oacute;n entre pares&mdash; se colocaron al principio y no al final, porque son las &uacute;nicas que no
  puedo acelerar por mi cuenta.</p>
  %(plan)s
  <div class="nota" style="margin-top:18px"><strong>Lo que aprend&iacute; en esta p&aacute;gina.</strong> Planificar no es
  repartir horas: es identificar qu&eacute; tareas tienen dependencia externa y ponerlas primero. Una entrega no se
  atrasa por lo que falta hacer, se atrasa por lo que falta <em>esperar</em>.</div>
</div></section>
""" % dict(svg=SVG_BANDURA, plan=PLAN)

page("01-definicion.html", "1 &middot; Definici&oacute;n del proyecto &middot; Portafolio digital",
     "Paso 1 de 5",
     "Definici&oacute;n del proyecto",
     "Qu&eacute; tema eleg&iacute; y por qu&eacute;, qu&eacute; evidencia tengo de autoeficacia en el desempe&ntilde;o cognitivo y emocional, y c&oacute;mo planifiqu&eacute; las actividades de aprendizaje de la unidad.",
     BODY)
