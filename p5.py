# -*- coding: utf-8 -*-
from build import *

LICENCIAS = """
<div class="tabla-scroll"><table>
<thead><tr><th style="width:230px">Recurso</th><th style="width:175px">Licencia real</th><th>Qu&eacute; se hizo con &eacute;l, y por qu&eacute; estaba permitido</th></tr></thead>
<tbody>
<tr><td>Hogan et al. (2021), <em>Knowledge graphs</em></td><td><span class="pill no">Derechos reservados</span><br><span class="small tenue">lectura libre en kgbook.org</span></td><td>Se <strong>enlaza y se parafrasea</strong>. Que un libro se pueda leer sin pagar no significa que se pueda copiar: gratis y libre no son lo mismo. No se reproduce ning&uacute;n fragmento ni ninguna figura.</td></tr>
<tr><td>Polo-Bautista y Casique V&aacute;squez (2025)</td><td><span class="pill">CC BY-NC-ND 4.0</span></td><td>Se cita y se parafrasea. La cl&aacute;usula <strong>ND</strong> proh&iacute;be publicar versiones modificadas, as&iacute; que la Figura&nbsp;2 de este portafolio <strong>no adapta ninguna figura suya</strong>: es una representaci&oacute;n nueva de una comparaci&oacute;n que el art&iacute;culo expone en prosa. Reelaborar no es copiar y retocar.</td></tr>
<tr><td>Edge et al. (2024), preprint</td><td><span class="pill">Licencia de distribuci&oacute;n arXiv</span></td><td>Se enlaza al repositorio oficial y se parafrasea el m&eacute;todo. No se reproduce texto ni figuras.</td></tr>
<tr><td>Peng et al. (2024), preprint</td><td><span class="pill">Licencia de distribuci&oacute;n arXiv</span></td><td>Igual que el anterior: enlace y par&aacute;frasis citada.</td></tr>
<tr><td>UNESCO (2023), gu&iacute;a</td><td><span class="pill ok">Acceso abierto</span></td><td>Se enlaza al repositorio UNESDOC y se citan sus principios. No se reproduce el documento ni fragmentos extensos.</td></tr>
<tr><td>Jara y Ochoa (2020), BID</td><td><span class="pill ok">Acceso abierto</span></td><td>Se enlaza al repositorio del BID y se cita. No se reproduce.</td></tr>
<tr><td>Videos de YouTube (2)</td><td><span class="pill">Licencia est&aacute;ndar de YouTube</span></td><td>Se incrustan con el <strong>reproductor oficial</strong>, que es el uso que la propia plataforma habilita. No se descargan ni se vuelven a subir: eso s&iacute; ser&iacute;a una copia no autorizada.</td></tr>
<tr><td>Tipograf&iacute;a Barlow</td><td><span class="pill ok">SIL Open Font License 1.1</span></td><td>Se usa en el sitio y en las l&aacute;minas. La licencia lo permite expresamente, incluso con fines comerciales.</td></tr>
<tr><td>Figuras 1 a 4 y gr&aacute;ficos 1 a 4</td><td><span class="pill ok">CC BY 4.0</span><br><span class="small tenue">elaboraci&oacute;n propia</span></td><td>Son m&iacute;os y los libero con la licencia m&aacute;s abierta que todav&iacute;a exige cr&eacute;dito, porque est&aacute;n construidos sobre trabajo de otros que tambi&eacute;n lo exig&iacute;a.</td></tr>
<tr><td>Grafo interactivo y c&oacute;digo del sitio</td><td><span class="pill ok">CC BY 4.0</span></td><td>Elaboraci&oacute;n propia. El c&oacute;digo fuente est&aacute; publicado y se puede revisar.</td></tr>
</tbody></table></div>"""

REFS = """
<p class="ref">Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. <em>Psychological Review, 84</em>(2), 191-215. https://doi.org/10.1037/0033-295X.84.2.191</p>
<p class="ref">Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., Metropolitansky, D., Ness, R. O., y Larson, J. (2024). <em>From local to global: A graph RAG approach to query-focused summarization</em> (arXiv:2404.16130). arXiv. https://arxiv.org/abs/2404.16130</p>
<p class="ref">Feregrino. (24 de septiembre de 2024). <em>RAG en grafos: El poder de los LLMs en datos conectados</em> [Video]. YouTube. https://www.youtube.com/watch?v=5AIOoM3sD2E</p>
<p class="ref">Fernando, J. (31 de agosto de 2020). <em>Repositorios de Recursos Educativos Digitales</em> [Video]. YouTube. https://www.youtube.com/watch?v=v54XHqP-WAU</p>
<p class="ref">Hogan, A., Blomqvist, E., Cochez, M., d&rsquo;Amato, C., de Melo, G., Guti&eacute;rrez, C., Kirrane, S., Labra Gayo, J. E., Navigli, R., Neumaier, S., Ngonga Ngomo, A.-C., Polleres, A., Rashid, S. M., Rula, A., Schmelzeisen, L., Sequeda, J., Staab, S., y Zimmermann, A. (2021). <em>Knowledge graphs</em>. Springer. https://doi.org/10.2200/S01125ED1V01Y202109DSK022</p>
<p class="ref">Jara, I., y Ochoa, J. M. (2020). <em>Usos y efectos de la inteligencia artificial en educaci&oacute;n</em>. Banco Interamericano de Desarrollo. https://publications.iadb.org/es/usos-y-efectos-de-la-inteligencia-artificial-en-educacion</p>
<p class="ref">Peng, B., Zhu, Y., Liu, Y., Bo, X., Shi, H., Hong, C., Zhang, Y., y Tang, S. (2024). <em>Graph retrieval-augmented generation: A survey</em> (arXiv:2408.08921). arXiv. https://arxiv.org/abs/2408.08921</p>
<p class="ref">Polo-Bautista, L. R., y Casique V&aacute;squez, R. (2025). Propuesta metodol&oacute;gica para la recuperaci&oacute;n de informaci&oacute;n documental: integraci&oacute;n de grafos de conocimiento y redes neuronales. <em>Investigaci&oacute;n Bibliotecol&oacute;gica: archivonom&iacute;a, bibliotecolog&iacute;a e informaci&oacute;n, 39</em>(105), 141-163. https://doi.org/10.22201/iibi.24488321xe.2025.105.59051</p>
<p class="ref">Tribby, J. (2017). <em>Barlow</em> [Tipograf&iacute;a]. Google Fonts. SIL Open Font License 1.1. https://fonts.google.com/specimen/Barlow</p>
<p class="ref">UNESCO. (2023). <em>Gu&iacute;a para el uso de IA generativa en educaci&oacute;n e investigaci&oacute;n</em>. Organizaci&oacute;n de las Naciones Unidas para la Educaci&oacute;n, la Ciencia y la Cultura. https://unesdoc.unesco.org/ark:/48223/pf0000389227</p>"""

EVIDENCIA = """
<figure>
  <img src="assets/foro.png" alt="Captura de pantalla de la publicaci&oacute;n en el foro de novedades y consultas al docente, con el t&iacute;tulo Retroalimentaci&oacute;n entre pares PA2" loading="lazy"
       onerror="this.parentNode.innerHTML='&lt;div class=&quot;tarjeta&quot; style=&quot;text-align:center;padding:44px 24px&quot;&gt;&lt;div class=&quot;kicker&quot;&gt;Evidencia&lt;/div&gt;&lt;p style=&quot;margin:0&quot;&gt;Captura de la publicaci&amp;oacute;n en el foro &amp;laquo;Retroalimentaci&amp;oacute;n entre pares PA2&amp;raquo;.&lt;/p&gt;&lt;/div&gt;'">
  <figcaption><strong>Evidencia.</strong> Publicaci&oacute;n en el <em>Foro de novedades y consultas al docente</em> con el
  t&iacute;tulo &laquo;Retroalimentaci&oacute;n entre pares PA2&raquo;, compartiendo el enlace de este portafolio y pidiendo
  comentarios a los compa&ntilde;eros.</figcaption>
</figure>"""

BODY = ("""
<section class="bloque"><div class="wrap">
  <h2>D&oacute;nde est&aacute; publicado</h2>
  <p class="entrada">En <strong>GitHub&nbsp;Pages</strong>, una plataforma gratuita de publicaci&oacute;n de sitios web.
  El acceso es <strong>p&uacute;blico</strong>: se abre con el enlace, sin cuenta y sin solicitar permiso a nadie.</p>
  <div class="rejilla r2">
    <div class="tarjeta"><h3>Enlace del portafolio</h3>
      <p class="small" style="margin-bottom:0"><a href=\"""" + SITIO + """\">""" + SITIO + """</a></p></div>
    <div class="tarjeta"><h3>C&oacute;digo fuente</h3>
      <p class="small" style="margin-bottom:0"><a href="https://github.com/9YinSk/portafolio-gia">github.com/9YinSk/portafolio-gia</a><br>
      Cualquiera puede revisar c&oacute;mo est&aacute; hecho, incluida la simulaci&oacute;n de fuerzas del grafo.</p></div>
  </div>
  <h3 style="margin-top:26px">Por qu&eacute; esta plataforma y no un constructor visual</h3>
  <p>La consigna ped&iacute;a una plataforma gratuita y daba tres ejemplos. Eleg&iacute; una distinta por una raz&oacute;n de
  carrera: en Ciencias de la Computaci&oacute;n, el portafolio que revisa un empleador suele ser el repositorio.
  Publicando aqu&iacute;, <strong>el sitio y su c&oacute;digo viven en el mismo lugar</strong> y se puede verificar que el
  grafo interactivo est&aacute; programado y no es una imagen. Adem&aacute;s el sitio es est&aacute;tico y ligero, que en
  conexiones inestables como las de mi zona no es un detalle.</p>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Difusi&oacute;n y retroalimentaci&oacute;n entre pares</h2>
  <p>El portafolio se comparti&oacute; en el <strong>Foro de novedades y consultas al docente</strong> del aula
  virtual, con el t&iacute;tulo <strong>&laquo;Retroalimentaci&oacute;n entre pares PA2&raquo;</strong>, pidiendo comentarios
  a los compa&ntilde;eros antes de darlo por cerrado.</p>
  <p>No es un tr&aacute;mite de la consigna. Es la tercera fuente de autoeficacia de Bandura &mdash;la persuasi&oacute;n
  verbal&mdash; usada a prop&oacute;sito: un trabajo que nadie m&aacute;s ha mirado tiene puntos ciegos que su autor no
  puede ver, porque son exactamente aquello que da por obvio.</p>
  """ + EVIDENCIA + """
  <h3>Retroalimentaci&oacute;n recibida y mejora aplicada</h3>
  <div class="tabla-scroll"><table>
  <thead><tr><th style="width:190px">Compa&ntilde;ero</th><th>Comentario recibido</th><th style="width:260px">Qu&eacute; cambi&eacute; por eso</th></tr></thead>
  <tbody>
  <tr><td class="tenue">Pendiente</td><td class="tenue">Este apartado se completa con los comentarios reales que dejen los compa&ntilde;eros en el foro.</td><td class="tenue">&mdash;</td></tr>
  </tbody></table></div>
  <p class="small tenue" style="margin-top:10px">El ciclo no se cierra al publicar: se cierra cuando la
  retroalimentaci&oacute;n vuelve y modifica algo. Esta tabla se actualiza con lo que llegue.</p>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Auditor&iacute;a de copyright y licencias</h2>
  <p>Cada recurso usado en este portafolio, con su licencia real y lo que se hizo con &eacute;l. La confusi&oacute;n m&aacute;s
  com&uacute;n es tratar <strong>&laquo;gratis&raquo; y &laquo;libre&raquo; como lo mismo</strong>: de las seis fuentes de
  este trabajo, las seis se pueden leer sin pagar, pero <strong>solo una permite publicar una versi&oacute;n
  modificada</strong>, y ninguna permite reproducirla entera.</p>
  """ + LICENCIAS + """
  <div class="rejilla r2" style="margin-top:22px">
    <div class="tarjeta"><h3>Licencia de este portafolio</h3>
      <p class="small">Los textos y las piezas gr&aacute;ficas de elaboraci&oacute;n propia se publican bajo
      <a href="https://creativecommons.org/licenses/by/4.0/deed.es" rel="license"><strong>CC BY 4.0</strong></a>:
      cualquiera puede copiarlos, adaptarlos y usarlos incluso comercialmente, con una sola condici&oacute;n,
      reconocer la autor&iacute;a.</p>
      <p class="small" style="margin-bottom:0">Los materiales citados <strong>conservan la licencia de sus
      autores</strong> y no quedan cubiertos por esta.</p></div>
    <div class="tarjeta"><h3>C&oacute;mo citar este portafolio</h3>
      <p class="ref" style="margin-bottom:0">Silva Fern&aacute;ndez, G. P. (2026). <em>Grafos de conocimiento y RAG:
      portafolio digital</em> [Sitio web]. Universidad Continental. """ + SITIO + """</p></div>
  </div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Referencias</h2>
  <p class="small tenue">Formato APA, 7.&ordf; edici&oacute;n. Ordenadas alfab&eacute;ticamente. Todos los enlaces fueron
  comprobados antes de publicar.</p>
  """ + REFS + """
  <div class="nota" style="margin-top:22px"><strong>Lo que aprend&iacute; en esta p&aacute;gina.</strong> Citar no es un
  requisito de formato, es la misma exigencia que le pedimos a un sistema de IA: que se pueda ir a comprobar de
  d&oacute;nde sali&oacute; cada afirmaci&oacute;n. Un trabajo sin referencias trazables y un modelo que alucina fallan por la
  misma raz&oacute;n.</div>
</div></section>
""")

page("05-publicacion.html", "5 &middot; Publicaci&oacute;n y difusi&oacute;n &middot; Portafolio digital",
     "Paso 5 de 5",
     "Publicaci&oacute;n y difusi&oacute;n",
     "D&oacute;nde est&aacute; publicado y con qu&eacute; acceso, c&oacute;mo se comparti&oacute; para recibir retroalimentaci&oacute;n entre pares, la auditor&iacute;a de licencias recurso por recurso y las referencias en APA 7.",
     BODY)
