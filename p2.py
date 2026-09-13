# -*- coding: utf-8 -*-
from build import *

EMBUDO = """
<figure>
<svg viewBox="0 0 980 340" role="img" aria-label="Embudo de cribado: de los resultados revisados a las seis fuentes citadas" style="width:100%;height:auto;border:1px solid var(--borde);border-radius:12px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012))">
  <text x="40" y="44" fill="#d4a04a" font-family="Barlow Condensed, sans-serif" font-size="17" letter-spacing="3">EL CRIBADO, PASO A PASO</text>
  <g font-family="Barlow Condensed, sans-serif">
    <rect x="40"  y="74" width="880" height="44" rx="10" fill="#6e1f33" fill-opacity=".72" stroke="#d4a04a" stroke-opacity=".4"/>
    <rect x="130" y="132" width="700" height="44" rx="10" fill="#6e1f33" fill-opacity=".62" stroke="#d4a04a" stroke-opacity=".4"/>
    <rect x="225" y="190" width="510" height="44" rx="10" fill="#8d2b43" fill-opacity=".6" stroke="#d4a04a" stroke-opacity=".45"/>
    <rect x="330" y="248" width="300" height="44" rx="10" fill="#d4a04a" fill-opacity=".9"/>
    <text x="480" y="103" fill="#fff" font-size="20" font-weight="600" text-anchor="middle">~40 resultados revisados en seis repositorios</text>
    <text x="480" y="161" fill="#fff" font-size="20" font-weight="600" text-anchor="middle">18 del tipo buscado (libro, art&iacute;culo arbitrado, informe, video)</text>
    <text x="480" y="219" fill="#fff" font-size="20" font-weight="600" text-anchor="middle">11 con autor&iacute;a identificable y licencia declarada</text>
    <text x="480" y="277" fill="#0c0a0f" font-size="21" font-weight="700" text-anchor="middle">6 citadas en este portafolio</text>
  </g>
  <g font-family="Barlow, sans-serif" font-size="13.5" fill="#a89c8b">
    <text x="40" y="310">Se descartaron: entradas de blog sin autor, res&uacute;menes de terceros en sitios de apuntes, y documentos sin fecha ni entidad responsable.</text>
  </g>
</svg>
<figcaption><strong>Gr&aacute;fico 2.</strong> Elaboraci&oacute;n propia. El cribado no es una b&uacute;squeda, son cuatro filtros
aplicados en orden; el que m&aacute;s descarta es el tercero. CC BY 4.0.</figcaption>
</figure>"""

REPOS = """
<div class="tabla-scroll"><table>
<thead><tr><th style="width:170px">Repositorio</th><th style="width:135px">Qu&eacute; es</th><th>Por qu&eacute; lo us&eacute; y qu&eacute; sali&oacute; de &eacute;l</th></tr></thead>
<tbody>
<tr><td><strong>SciELO</strong></td><td>Biblioteca regional de revistas arbitradas</td><td>Es el sitio donde aparece literatura acad&eacute;mica <em>en espa&ntilde;ol</em> y con DOI. De aqu&iacute; sali&oacute; el art&iacute;culo arbitrado que sostiene la comparaci&oacute;n central del trabajo.</td></tr>
<tr><td><strong>arXiv</strong></td><td>Repositorio de preprints</td><td>En este campo la literatura t&eacute;cnica aparece aqu&iacute; uno o dos a&ntilde;os antes que en revista. Lo uso sabiendo lo que es: <strong>no est&aacute; arbitrado</strong> (ver la advertencia de m&aacute;s abajo).</td></tr>
<tr><td><strong>UNESDOC</strong></td><td>Repositorio documental de la UNESCO</td><td>Para la parte normativa: qu&eacute; recomienda un organismo internacional sobre el uso de IA generativa en educaci&oacute;n.</td></tr>
<tr><td><strong>Publicaciones del BID</strong></td><td>Repositorio de un banco de desarrollo</td><td>Para la mirada regional latinoamericana sobre efectos de la IA en los sistemas educativos.</td></tr>
<tr><td><strong>Google Acad&eacute;mico</strong></td><td>Buscador acad&eacute;mico</td><td>No como fuente, sino como <em>&iacute;ndice</em>: sirve para ver cu&aacute;ntas veces se cita un trabajo y para llegar al repositorio donde est&aacute; de verdad.</td></tr>
<tr><td><strong>Biblioteca virtual UC</strong></td><td>Recursos suscritos por la universidad</td><td>Para contrastar los t&eacute;rminos del tema con manuales, y para el material obligatorio de la unidad.</td></tr>
</tbody></table></div>"""

CRITERIOS = """
<div class="tabla-scroll"><table>
<thead><tr><th style="width:150px">Criterio</th><th>Pregunta que me hice</th><th style="width:210px">Qu&eacute; descart&oacute;</th></tr></thead>
<tbody>
<tr><td><strong>Autor&iacute;a</strong></td><td>&iquest;Hay una persona o institución que responda por esto?</td><td>Res&uacute;menes en sitios de apuntes sin firma</td></tr>
<tr><td><strong>Vigencia</strong></td><td>&iquest;Sigue siendo cierto? En este tema, tres a&ntilde;os es mucho.</td><td>Comparativas de 2019 &mdash; anteriores a los modelos actuales</td></tr>
<tr><td><strong>Verificabilidad</strong></td><td>&iquest;Puedo llegar al dato original: DOI, repositorio, identificador?</td><td>Art&iacute;culos de divulgaci&oacute;n que citan &laquo;estudios&raquo; sin enlace</td></tr>
<tr><td><strong>Arbitraje</strong></td><td>&iquest;Lo revis&oacute; alguien m&aacute;s antes de publicarse?</td><td>Nada: los preprints se conservan, pero <em>etiquetados</em></td></tr>
<tr><td><strong>Licencia</strong></td><td>&iquest;Qu&eacute; me permite hacer con esto, adem&aacute;s de leerlo?</td><td>Nada, pero decidi&oacute; <em>c&oacute;mo</em> se us&oacute; cada fuente (p&aacute;gina&nbsp;5)</td></tr>
</tbody></table></div>"""

def ficha(tipo, titulo, cita, aporta, limite, licencia, enlace, etiqueta_lic="pill"):
    return """<div class="tarjeta" style="margin-bottom:16px">
  <span class="pill">%s</span>
  <h3 style="margin-top:12px">%s</h3>
  <p class="ref" style="margin-top:10px">%s</p>
  <p class="small" style="margin-bottom:8px"><strong>Qu&eacute; aporta:</strong> %s</p>
  <p class="small" style="margin-bottom:8px"><strong>L&iacute;mite cr&iacute;tico:</strong> %s</p>
  <p class="small" style="margin-bottom:0"><strong>Licencia y uso:</strong> %s &nbsp;&middot;&nbsp; <a href="%s" target="_blank" rel="noopener">Ir a la fuente</a></p>
</div>""" % (tipo, titulo, cita, aporta, limite, licencia, enlace)

FICHAS = "".join([
 ficha("Libro &middot; obra de referencia",
   "La definici&oacute;n can&oacute;nica de grafo de conocimiento",
   "Hogan, A., Blomqvist, E., Cochez, M., d&rsquo;Amato, C., de Melo, G., Guti&eacute;rrez, C., Kirrane, S., Labra Gayo, J. E., Navigli, R., Neumaier, S., Ngonga Ngomo, A.-C., Polleres, A., Rashid, S. M., Rula, A., Schmelzeisen, L., Sequeda, J., Staab, S., y Zimmermann, A. (2021). <em>Knowledge graphs</em>. Springer. https://doi.org/10.2200/S01125ED1V01Y202109DSK022",
   "Es la obra que fija el vocabulario del campo: qu&eacute; es un nodo, una arista y un esquema, y c&oacute;mo se consulta un grafo. Todo lo dem&aacute;s del portafolio se apoya en estas definiciones. Dos de sus autores, Aidan Hogan y Claudio Guti&eacute;rrez, son de la Universidad de Chile.",
   "Es de 2021, anterior a la explosi&oacute;n de los modelos de lenguaje actuales. Sirve para definir el objeto, <strong>no</strong> para afirmar nada sobre el rendimiento de los sistemas de hoy; para eso us&eacute; las fuentes 3 y 4.",
   "Todos los derechos reservados, con <strong>versi&oacute;n de lectura libre</strong> publicada por los propios autores en kgbook.org. Se enlaza y se parafrasea; no se reproduce.",
   "https://kgbook.org"),
 ficha("Art&iacute;culo arbitrado &middot; la fuente central",
   "La comparaci&oacute;n que sostiene el argumento",
   "Polo-Bautista, L. R., y Casique V&aacute;squez, R. (2025). Propuesta metodol&oacute;gica para la recuperaci&oacute;n de informaci&oacute;n documental: integraci&oacute;n de grafos de conocimiento y redes neuronales. <em>Investigaci&oacute;n Bibliotecol&oacute;gica: archivonom&iacute;a, bibliotecolog&iacute;a e informaci&oacute;n, 39</em>(105), 141-163. https://doi.org/10.22201/iibi.24488321xe.2025.105.59051",
   "Art&iacute;culo arbitrado de la UNAM, de 2025 y en espa&ntilde;ol. Compara la recuperaci&oacute;n con redes neuronales de grafos frente al enfoque tradicional y concluye que integrar grafos da respuestas <strong>m&aacute;s precisas, m&aacute;s concisas y sin alucinaciones</strong>, pero con <strong>mayor tiempo de procesamiento</strong>. Esa frase &mdash;lo que se gana y lo que se paga&mdash; es el eje del trabajo.",
   "Es una propuesta metodol&oacute;gica sobre un corpus documental acotado, no un <em>benchmark</em> a gran escala. Su conclusi&oacute;n es s&oacute;lida como direcci&oacute;n, y no debe leerse como una medida universal de cu&aacute;nto mejora.",
   "<strong>CC BY-NC-ND 4.0.</strong> La cl&aacute;usula ND proh&iacute;be publicar versiones modificadas, as&iacute; que no se reproduce ni se adapta ninguna figura: se parafrasea y se cita, que s&iacute; est&aacute; permitido.",
   "https://doi.org/10.22201/iibi.24488321xe.2025.105.59051"),
 ficha("Preprint &middot; fuente t&eacute;cnica primaria",
   "El sistema que populariz&oacute; el t&eacute;rmino GraphRAG",
   "Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., Metropolitansky, D., Ness, R. O., y Larson, J. (2024). <em>From local to global: A graph RAG approach to query-focused summarization</em> (arXiv:2404.16130). arXiv. https://arxiv.org/abs/2404.16130",
   "Describe el problema que la recuperaci&oacute;n cl&aacute;sica no resuelve: las <strong>preguntas globales</strong> sobre un corpus entero (&laquo;&iquest;de qu&eacute; trata todo esto?&raquo;), que no son un problema de b&uacute;squeda sino de resumen. La soluci&oacute;n que propone &mdash;agrupar el grafo en comunidades y resumir cada una&mdash; es la que us&eacute; en mi propia herramienta.",
   "<strong>Es un preprint: no est&aacute; arbitrado</strong>, y lo firman autores de la empresa que publica el sistema, as&iacute; que hay inter&eacute;s de parte. Lo cito para describir el m&eacute;todo, nunca como evidencia de que sea superior; esa afirmaci&oacute;n la dejo en manos de la fuente arbitrada.",
   "arXiv, licencia de distribuci&oacute;n no exclusiva. Se enlaza al repositorio oficial; no se reproduce.",
   "https://arxiv.org/abs/2404.16130"),
 ficha("Preprint &middot; revisi&oacute;n sistem&aacute;tica",
   "El mapa completo del campo",
   "Peng, B., Zhu, Y., Liu, Y., Bo, X., Shi, H., Hong, C., Zhang, Y., y Tang, S. (2024). <em>Graph retrieval-augmented generation: A survey</em> (arXiv:2408.08921). arXiv. https://arxiv.org/abs/2408.08921",
   "Una revisi&oacute;n que ordena decenas de sistemas en un mismo esquema de tres fases (indexaci&oacute;n, recuperaci&oacute;n y generaci&oacute;n). Me sirvi&oacute; para comprobar que el problema que me interesa est&aacute; bien planteado y no es una rareza: la alucinaci&oacute;n y el conocimiento desactualizado son el motivo declarado de todo el subcampo.",
   "Tambi&eacute;n es preprint, y una revisi&oacute;n envejece r&aacute;pido en un campo que se mueve por meses. Vale como panor&aacute;mica de 2024; no como estado del arte permanente.",
   "arXiv, licencia de distribuci&oacute;n no exclusiva. Se enlaza; no se reproduce.",
   "https://arxiv.org/abs/2408.08921"),
 ficha("Informe institucional &middot; normativo",
   "Qu&eacute; recomienda la UNESCO sobre la IA generativa",
   "UNESCO. (2023). <em>Gu&iacute;a para el uso de IA generativa en educaci&oacute;n e investigaci&oacute;n</em>. Organizaci&oacute;n de las Naciones Unidas para la Educaci&oacute;n, la Ciencia y la Cultura. https://unesdoc.unesco.org/ark:/48223/pf0000389227",
   "Aporta el marco de uso responsable con el que contrasto mis propias decisiones en la p&aacute;gina&nbsp;4: enfoque human&iacute;stico, intervenci&oacute;n humana, inclusi&oacute;n y equidad. Es el documento que convierte &laquo;usar IA&raquo; en una decisi&oacute;n con criterios, y no en una preferencia.",
   "Es una gu&iacute;a de pol&iacute;tica, no un estudio emp&iacute;rico: recomienda, no mide. No sirve para sostener ninguna afirmaci&oacute;n sobre resultados de aprendizaje.",
   "Publicaci&oacute;n de <strong>acceso abierto</strong> de la UNESCO en su repositorio UNESDOC. Aqu&iacute; solo se enlaza y se cita; no se reproduce ning&uacute;n fragmento extenso ni ninguna figura.",
   "https://unesdoc.unesco.org/ark:/48223/pf0000389227"),
 ficha("Informe regional &middot; lectura obligatoria de la unidad",
   "Los efectos de la IA en la educaci&oacute;n de la regi&oacute;n",
   "Jara, I., y Ochoa, J. M. (2020). <em>Usos y efectos de la inteligencia artificial en educaci&oacute;n</em>. Banco Interamericano de Desarrollo. https://publications.iadb.org/es/usos-y-efectos-de-la-inteligencia-artificial-en-educacion",
   "Es el material obligatorio de la unidad. Baja el tema desde el discurso global a Am&eacute;rica Latina: qu&eacute; se ha implementado de verdad, qu&eacute; requisitos de infraestructura tiene y cu&aacute;les son los riesgos de equidad. Es la fuente que me permite hablar de Puno sin salirme del marco del curso.",
   "Es de 2020, previo a la IA generativa de uso masivo. Sus casos son de sistemas anteriores; lo uso por el an&aacute;lisis de condiciones y de brechas, que sigue vigente, y no por el cat&aacute;logo de herramientas.",
   "Documento institucional de acceso abierto en el repositorio del BID. Se enlaza y se cita; no se reproduce.",
   "https://publications.iadb.org/es/usos-y-efectos-de-la-inteligencia-artificial-en-educacion"),
])

BODY = """
<section class="bloque"><div class="wrap">
  <h2>La estrategia, antes de buscar</h2>
  <p class="entrada">Buscar bien no es escribir mejor en el buscador: es decidir <strong>d&oacute;nde</strong> se busca
  y <strong>qu&eacute; se acepta</strong> antes de ver el primer resultado. Si esos dos criterios se fijan despu&eacute;s,
  uno termina justificando lo que encontr&oacute;.</p>
  <div class="paso"><div class="n">1</div><div><h3>Traducir el tema a conceptos, no a palabras</h3>
  <p style="margin-bottom:0">El tema en lenguaje natural &mdash;&laquo;que la IA no invente&raquo;&mdash; no sirve
  para buscar. Los conceptos s&iacute;: <em>grafo de conocimiento</em>, <em>recuperaci&oacute;n de informaci&oacute;n</em>,
  <em>generaci&oacute;n aumentada</em>, <em>alucinaci&oacute;n</em>. Cada uno tiene su t&eacute;rmino en ingl&eacute;s, que es
  donde est&aacute; la mayor parte de la literatura t&eacute;cnica.</p></div></div>
  <div class="paso"><div class="n">2</div><div><h3>Construir la ecuaci&oacute;n de b&uacute;squeda</h3>
  <p style="margin-bottom:0">Combinando sin&oacute;nimos con <code>OR</code> y conceptos con <code>AND</code>:<br>
  <code style="display:inline-block;margin-top:8px;background:rgba(255,255,255,.06);padding:8px 12px;border-radius:8px;font-size:14.5px">("knowledge graph" OR "grafo de conocimiento") AND ("retrieval augmented" OR "recuperaci&oacute;n de informaci&oacute;n") AND (hallucination OR alucinaci&oacute;n)</code></p></div></div>
  <div class="paso"><div class="n">3</div><div><h3>Buscar en el repositorio, no en el buscador</h3>
  <p style="margin-bottom:0">Esta es la lecci&oacute;n que me cost&oacute; el trabajo anterior. En un buscador general las
  primeras b&uacute;squedas devolv&iacute;an solo literatura en ingl&eacute;s sin DOI verificable. Cambiando a repositorios
  indexados apareci&oacute; lo que buscaba: arbitrado, en espa&ntilde;ol, con DOI y con licencia declarada.
  <strong>El problema no era c&oacute;mo buscaba, era d&oacute;nde.</strong></p></div></div>
  <div class="paso"><div class="n">4</div><div><h3>Cribar con criterios escritos de antemano</h3>
  <p style="margin-bottom:0">Los cinco de la tabla de m&aacute;s abajo, aplicados en orden.</p></div></div>
  %(embudo)s
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Bancos bibliogr&aacute;ficos y repositorios consultados</h2>
  %(repos)s
  <div class="nota" style="margin-top:18px"><strong>Sobre los preprints.</strong> Dos de mis seis fuentes vienen
  de arXiv, que <em>no</em> es una revista arbitrada: publica antes de la revisi&oacute;n por pares. No las escond&iacute;
  ni las descart&eacute;: en este campo la literatura t&eacute;cnica aparece ah&iacute; primero, as&iacute; que las conservo
  <strong>etiquetadas como lo que son</strong> y me apoyo en ellas para describir m&eacute;todos, nunca para sostener
  que un m&eacute;todo sea mejor que otro. Esa afirmaci&oacute;n la sostiene la fuente arbitrada.</div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Criterios de selecci&oacute;n</h2>
  %(criterios)s
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Las seis fuentes, con su l&iacute;mite</h2>
  <p>Una ficha por fuente. Incluyo a prop&oacute;sito un apartado que no se suele poner:
  <strong>qu&eacute; <em>no</em> puede sostener cada una</strong>. Seleccionar de forma cr&iacute;tica es saber d&oacute;nde
  deja de valer una fuente, no acumular las que est&aacute;n de acuerdo conmigo.</p>
  %(fichas)s
  <div class="nota"><strong>Lo que aprend&iacute; en esta p&aacute;gina.</strong> El filtro que m&aacute;s descarta no es el de
  calidad, es el de <em>trazabilidad</em>: casi todo lo que se cae, se cae porque no se puede llegar al dato
  original. Y una fuente que no se puede rastrear se parece mucho a una respuesta inventada.</div>
</div></section>
""" % dict(embudo=EMBUDO, repos=REPOS, criterios=CRITERIOS, fichas=FICHAS)

page("02-busqueda.html", "2 &middot; B&uacute;squeda y selecci&oacute;n de informaci&oacute;n &middot; Portafolio digital",
     "Paso 2 de 5",
     "B&uacute;squeda y selecci&oacute;n de informaci&oacute;n",
     "La estrategia de b&uacute;squeda paso a paso, los seis repositorios consultados, los criterios de cribado y la ficha cr&iacute;tica de cada fuente &mdash; incluido lo que cada una <em>no</em> puede sostener.",
     BODY)
