# -*- coding: utf-8 -*-
from build import *

def aplic(n, tit, txt, fuente):
    return """<div class="tarjeta" style="margin-bottom:16px">
  <div class="paso" style="margin-bottom:0">
    <div class="n">%s</div>
    <div><h3 style="margin-bottom:8px">%s</h3>
    <p style="margin-bottom:10px">%s</p>
    <p class="small tenue" style="margin-bottom:0">%s</p></div>
  </div></div>""" % (n, tit, txt, fuente)

APLICACIONES = "".join([
 aplic("1", "Recuperar y sintetizar literatura sin perder la fuente",
   "Es la aplicaci&oacute;n que da tema a este portafolio. Un sistema de recuperaci&oacute;n aumentada indexa un conjunto "
   "de documentos &mdash;los art&iacute;culos de un curso, las actas de un congreso, un repositorio institucional&mdash; "
   "y responde preguntas <strong>citando el fragmento del que sali&oacute; cada respuesta</strong>. La diferencia con "
   "preguntarle a un modelo a secas es que aqu&iacute; se puede ir a comprobar. En lo acad&eacute;mico esa diferencia lo es "
   "todo: una afirmaci&oacute;n sin procedencia no sirve ni en un trabajo ni en una tesis.",
   "Sustento: Peng et al. (2024) y Edge et al. (2024) describen el m&eacute;todo; Polo-Bautista y Casique V&aacute;squez (2025) miden su efecto sobre la precisi&oacute;n y la alucinaci&oacute;n."),
 aplic("2", "Retroalimentaci&oacute;n personalizada y tutor&iacute;a a escala",
   "Sistemas que analizan las respuestas de un estudiante y devuelven correcci&oacute;n inmediata, ajustando la "
   "dificultad. Su valor real no es corregir m&aacute;s r&aacute;pido, es <strong>corregir a tiempo</strong>: una "
   "retroalimentaci&oacute;n que llega dos semanas despu&eacute;s ya no cambia la conducta de estudio. Le&iacute;da a la luz de la teor&iacute;a "
   "de esta unidad, es intervenir sobre la <em>persuasi&oacute;n verbal</em> y sobre las experiencias de dominio, que "
   "son dos de las cuatro fuentes de la autoeficacia.",
   "Sustento: Jara y Ochoa (2020) revisan los sistemas de tutor&iacute;a inteligente implementados en la regi&oacute;n y sus condiciones de funcionamiento."),
 aplic("3", "Accesibilidad: transcripci&oacute;n, subtitulado y traducci&oacute;n",
   "El reconocimiento autom&aacute;tico del habla y la traducci&oacute;n neuronal convierten una clase grabada en texto "
   "buscable, subtitulado y traducible. Es la aplicaci&oacute;n que m&aacute;s me toca de cerca: una parte enorme de la "
   "literatura de mi campo est&aacute; en ingl&eacute;s, y en el altiplano el castellano no es la primera lengua de mucha "
   "gente. Aqu&iacute; la IA no reemplaza a nadie; <strong>quita una barrera de entrada</strong>.",
   "Sustento: UNESCO (2023) enmarca estos usos en su principio de inclusi&oacute;n y diversidad ling&uuml;&iacute;stica."),
 aplic("4", "Anal&iacute;tica del aprendizaje y alerta temprana",
   "Modelos que cruzan asistencia, entregas y actividad en el aula virtual para se&ntilde;alar a qui&eacute;n conviene "
   "acompa&ntilde;ar antes de que abandone. Es tambi&eacute;n donde m&aacute;s claro est&aacute; el riesgo: el mismo sistema que "
   "avisa a tiempo puede etiquetar a un estudiante y condicionar c&oacute;mo se le trata. Por eso UNESCO insiste en "
   "la <strong>intervenci&oacute;n humana</strong>: la alerta la da la m&aacute;quina, la decisi&oacute;n la toma una persona.",
   "Sustento: Jara y Ochoa (2020) sobre administraci&oacute;n de sistemas educativos; UNESCO (2023) sobre gobernanza y enfoque human&iacute;stico."),
])

HERRAMIENTAS = """
<div class="tabla-scroll"><table>
<thead><tr><th style="width:215px">Herramienta</th><th>Para qu&eacute; la us&eacute; aqu&iacute;</th><th style="width:230px">Qu&eacute; mejor&oacute;, en concreto</th></tr></thead>
<tbody>
<tr>
  <td><strong>Asistente conversacional con b&uacute;squeda</strong><br><span class="small tenue">Mapeo del campo y localizaci&oacute;n de candidatas</span></td>
  <td>Traducir el tema a los t&eacute;rminos con los que se publica, proponer d&oacute;nde buscarlos y contrastar lo que dec&iacute;a cada candidata frente a las dem&aacute;s.</td>
  <td>La bibliograf&iacute;a pas&oacute; de <strong>tres fuentes a seis</strong>, y aparecieron dos que yo no habr&iacute;a buscado: el informe del BID y la gu&iacute;a de la UNESCO, que son las que sostienen la parte de equidad.</td>
</tr>
<tr>
  <td><strong>Extracci&oacute;n autom&aacute;tica de entidades y relaciones</strong><br><span class="small tenue">Construcci&oacute;n del grafo</span></td>
  <td>Leer las fichas de las seis fuentes y proponer qu&eacute; entidades hay (fuentes, conceptos, repositorios, licencias) y c&oacute;mo se relacionan entre s&iacute;.</td>
  <td>Hizo visible una relaci&oacute;n que yo no hab&iacute;a escrito: <strong>&laquo;acceso abierto&raquo; une la fuente de la UNESCO con la del BID</strong>. Las dos institucionales, las dos sobre equidad. Eso reorganiz&oacute; un p&aacute;rrafo de la p&aacute;gina&nbsp;3.</td>
</tr>
<tr>
  <td><strong>Revisi&oacute;n asistida</strong><br><span class="small tenue">Control de afirmaciones y enlaces</span></td>
  <td>Recorrer el texto preguntando por cada afirmaci&oacute;n: &iquest;de qu&eacute; fuente sale? &iquest;el enlace resuelve? &iquest;la fecha es la que dice?</td>
  <td>Detect&oacute; que <strong>dos de mis cuatro fuentes t&eacute;cnicas eran preprints sin arbitraje</strong> y yo las estaba tratando igual que a la arbitrada. De ah&iacute; sali&oacute; la advertencia de la p&aacute;gina&nbsp;2 y el cambio en c&oacute;mo se citan.</td>
</tr>
</tbody></table></div>"""

ANTES = """
<div class="rejilla r2" style="margin-top:20px">
  <div class="tarjeta" style="border-color:rgba(160,54,82,.45)">
    <span class="pill no">Antes</span>
    <p style="margin:12px 0 0">&laquo;El art&iacute;culo concluye que los grafos de conocimiento son mejores para
    recuperar informaci&oacute;n.&raquo;</p>
    <p class="small tenue" style="margin:12px 0 0">Suena bien y es inservible: no dice mejores <em>en qu&eacute;</em>,
    ni a costa de qu&eacute;, ni con qu&eacute; alcance. Es la clase de frase que un modelo produce sin esfuerzo y que un
    lector no puede verificar.</p>
  </div>
  <div class="tarjeta" style="border-color:rgba(63,125,106,.5)">
    <span class="pill ok">Despu&eacute;s</span>
    <p style="margin:12px 0 0">&laquo;Concluye que integrar grafos produce respuestas m&aacute;s precisas, m&aacute;s
    concisas y sin alucinaciones, a cambio de un mayor tiempo de procesamiento; es una propuesta metodol&oacute;gica
    sobre un corpus acotado, no una medida universal.&raquo;</p>
    <p class="small tenue" style="margin:12px 0 0">Dice qu&eacute; se gana, qu&eacute; se paga y hasta d&oacute;nde llega la
    afirmaci&oacute;n. La mejora no vino de escribir m&aacute;s bonito: vino de volver a la fuente.</p>
  </div>
</div>"""

BODY = ("""
<section class="bloque"><div class="wrap">
  <h2>Cuatro aplicaciones en el &aacute;mbito acad&eacute;mico</h2>
  <p class="entrada">No como cat&aacute;logo de herramientas de moda, sino por lo que cada una cambia en el trabajo
  acad&eacute;mico &mdash; y con la fuente que lo sostiene.</p>
  """ + APLICACIONES + """
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Qu&eacute; us&eacute; en este portafolio, y qu&eacute; mejor&oacute;</h2>
  <p>La consigna ped&iacute;a usar alguna herramienta de inteligencia artificial para mejorar el contenido. Us&eacute;
  tres, y lo importante no es nombrarlas: es poder decir <strong>qu&eacute; cambi&oacute; en el trabajo por haberlas
  usado</strong>. Si no se puede se&ntilde;alar el cambio, la herramienta no aport&oacute; nada.</p>
  """ + HERRAMIENTAS + """
  <h3 style="margin-top:26px">La evidencia m&aacute;s clara</h3>
  <p>El tercer caso de la tabla produjo una correcci&oacute;n que se puede mostrar. Esta frase estaba en mi primer
  borrador y as&iacute; qued&oacute; despu&eacute;s de volver al art&iacute;culo:</p>
  """ + ANTES + """
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Lo que no delegu&eacute;, y por qu&eacute;</h2>
  <p>La UNESCO (2023) construye su gu&iacute;a sobre un principio: <strong>intervenci&oacute;n humana</strong>. Aplicado a
  un trabajo universitario, eso se traduce en una l&iacute;nea concreta entre lo que una herramienta puede acelerar y
  lo que tiene que seguir siendo m&iacute;o, porque es justamente lo que se est&aacute; evaluando.</p>
  <div class="rejilla r2">
    <div class="tarjeta"><h3>La elecci&oacute;n del tema y del enfoque</h3><p class="small" style="margin-bottom:0">
    Una herramienta puede proponer veinte temas. Cu&aacute;l conecta con mi carrera y con esta asignatura, y qu&eacute;
    pregunta puedo sostener con las fuentes que tengo, lo decido yo.</p></div>
    <div class="tarjeta"><h3>El juicio cr&iacute;tico sobre cada fuente</h3><p class="small" style="margin-bottom:0">
    El apartado &laquo;l&iacute;mite cr&iacute;tico&raquo; de la p&aacute;gina&nbsp;2 es m&iacute;o. Decir qu&eacute; <em>no</em> puede
    sostener una fuente exige haberla le&iacute;do, no haberla resumido.</p></div>
    <div class="tarjeta"><h3>La verificaci&oacute;n</h3><p class="small" style="margin-bottom:0">
    Cada DOI y cada enlace de este portafolio se abri&oacute; para comprobar que resuelve y que el a&ntilde;o, el volumen
    y las p&aacute;ginas coinciden. Es la regla de todo el trabajo: <strong>un fallo que no da error es peor que uno
    que s&iacute; lo da</strong>, y una cita inventada no da error.</p></div>
    <div class="tarjeta"><h3>Las conclusiones</h3><p class="small" style="margin-bottom:0">
    Lo que aprend&iacute; en cada p&aacute;gina, y la lectura desde Puno sobre acceso y conectividad, no sale de ninguna
    fuente ni de ninguna herramienta. Sale de trabajar aqu&iacute;.</p></div>
  </div>
  <div class="nota" style="margin-top:20px"><strong>El criterio, en una frase.</strong> Una herramienta de IA es
  pertinente cuando <em>acelera algo que yo puedo verificar</em>. En cuanto produce algo que yo no puedo
  comprobar &mdash;una cita, un dato, una conclusi&oacute;n&mdash;, deja de ser una ayuda y pasa a ser exactamente el
  problema que este portafolio estudia.</div>
</div></section>
""")

page("04-ia.html", "4 &middot; Uso de inteligencia artificial &middot; Portafolio digital",
     "Paso 4 de 5",
     "Uso de inteligencia artificial",
     "Cuatro aplicaciones de la IA en el &aacute;mbito acad&eacute;mico con la fuente que las sostiene, las tres herramientas que us&eacute; en este portafolio con la mejora concreta de cada una, y la l&iacute;nea de lo que no se delega.",
     BODY)
