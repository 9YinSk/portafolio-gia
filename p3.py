# -*- coding: utf-8 -*-
from build import *

FORMATOS = """
<div class="tabla-scroll"><table>
<thead><tr><th style="width:140px">Formato</th><th>Pieza</th><th style="width:180px">Elaboraci&oacute;n</th></tr></thead>
<tbody>
<tr><td><span class="pill">Texto</span></td><td>S&iacute;ntesis propia del tema, fichas cr&iacute;ticas de las seis fuentes y bit&aacute;cora de problemas</td><td>Propia</td></tr>
<tr><td><span class="pill">Imagen</span></td><td>Cuatro infograf&iacute;as de esta asignatura: definici&oacute;n, comparaci&oacute;n metodol&oacute;gica, mapa de licencias y grafo trazado</td><td>Propia &middot; CC BY 4.0</td></tr>
<tr><td><span class="pill">Video</span></td><td>Dos videos incrustados con el reproductor oficial de YouTube</td><td>De terceros &middot; citados</td></tr>
<tr><td><span class="pill">Gr&aacute;fico</span></td><td>Cuatro gr&aacute;ficos vectoriales: fuentes de la autoeficacia, embudo de cribado, anatom&iacute;a del grafo y l&iacute;nea de formaci&oacute;n</td><td>Propia &middot; CC BY 4.0</td></tr>
<tr><td><span class="pill">Interactivo</span></td><td>Grafo de conocimiento navegable, construido con las fuentes y los conceptos de este portafolio</td><td>Propia &middot; CC BY 4.0</td></tr>
</tbody></table></div>"""

GRAFO = """
<div class="tarjeta" style="padding:16px">
  <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:10px">
    <div class="kicker" style="margin:0">Grafo de conocimiento de este portafolio</div>
    <div class="small tenue" id="g-stats" style="font-size:13.5px">cargando&hellip;</div>
  </div>
  <canvas id="g" style="width:100%;height:520px;display:block;border-radius:10px;background:radial-gradient(600px 380px at 60% 20%,rgba(110,31,51,.30),transparent 65%),#0a080d;cursor:grab;touch-action:none"></canvas>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:12px;align-items:center">
    <span class="small tenue" style="font-size:13px">Pasa el cursor por un nodo para aislar sus relaciones &middot; arr&aacute;stralo para moverlo</span>
    <span style="flex:1"></span>
    <span id="g-leyenda" style="display:flex;gap:12px;flex-wrap:wrap"></span>
  </div>
</div>
<p class="small tenue" style="margin-top:10px"><strong>Pieza interactiva 1.</strong> Elaboraci&oacute;n propia.
Las posiciones no est&aacute;n dibujadas: las decide una simulaci&oacute;n de fuerzas &mdash;repulsi&oacute;n entre todos los
nodos y resortes en las aristas&mdash; que corre en el navegador. Si dos nodos quedan cerca, es porque el grafo
los relaciona. CC BY 4.0.</p>
"""

CHART = """
<figure>
<div class="tarjeta">
  <div class="kicker" style="margin-bottom:14px">Anatom&iacute;a del grafo, por tipo de entidad</div>
  <div id="chart"></div>
  <p class="small tenue" style="margin:12px 0 0">Las barras se calculan leyendo el mismo conjunto de datos que
  dibuja el grafo de arriba: si a&ntilde;ado una fuente, cambian solas. Es la diferencia entre un gr&aacute;fico y una
  imagen de un gr&aacute;fico.</p>
</div>
<figcaption><strong>Gr&aacute;fico 3.</strong> Elaboraci&oacute;n propia, generado a partir de los datos del grafo. CC BY 4.0.</figcaption>
</figure>"""

JS = """
<script>
(function(){
var N=[
 {id:"hogan",   t:"fuente", l:"Hogan et al. (2021)"},
 {id:"polo",    t:"fuente", l:"Polo-Bautista y Casique (2025)"},
 {id:"edge",    t:"fuente", l:"Edge et al. (2024)"},
 {id:"peng",    t:"fuente", l:"Peng et al. (2024)"},
 {id:"unesco",  t:"fuente", l:"UNESCO (2023)"},
 {id:"bid",     t:"fuente", l:"Jara y Ochoa (2020)"},

 {id:"kg",      t:"concepto", l:"Grafo de conocimiento"},
 {id:"rag",     t:"concepto", l:"RAG"},
 {id:"grag",    t:"concepto", l:"GraphRAG"},
 {id:"aluc",    t:"concepto", l:"Alucinaci\\u00f3n"},
 {id:"traz",    t:"concepto", l:"Trazabilidad"},
 {id:"com",     t:"concepto", l:"Comunidades"},
 {id:"ri",      t:"concepto", l:"Recuperaci\\u00f3n de informaci\\u00f3n"},
 {id:"brecha",  t:"concepto", l:"Brecha de acceso"},
 {id:"autoef",  t:"concepto", l:"Autoeficacia"},

 {id:"scielo",  t:"repo", l:"SciELO"},
 {id:"arxiv",   t:"repo", l:"arXiv"},
 {id:"unesdoc", t:"repo", l:"UNESDOC"},
 {id:"repobid", t:"repo", l:"Publicaciones BID"},
 {id:"springer",t:"repo", l:"Springer"},

 {id:"ccbyncnd",t:"licencia", l:"CC BY-NC-ND 4.0"},
 {id:"ccby",    t:"licencia", l:"CC BY 4.0"},
 {id:"tdr",     t:"licencia", l:"Derechos reservados"},
 {id:"aa",      t:"licencia", l:"Acceso abierto"},
 {id:"arxivlic",t:"licencia", l:"Licencia arXiv"},

 {id:"nlm",     t:"herramienta", l:"Cuaderno con IA"},
 {id:"whisper", t:"herramienta", l:"Transcripci\\u00f3n autom\\u00e1tica"},
 {id:"propia",  t:"herramienta", l:"Grafo propio"}
];
var E=[
 ["hogan","kg"],["hogan","springer"],["hogan","tdr"],
 ["polo","kg"],["polo","ri"],["polo","aluc"],["polo","scielo"],["polo","ccbyncnd"],
 ["edge","grag"],["edge","com"],["edge","arxiv"],["edge","arxivlic"],
 ["peng","grag"],["peng","rag"],["peng","aluc"],["peng","arxiv"],["peng","arxivlic"],
 ["unesco","unesdoc"],["unesco","aa"],["unesco","brecha"],
 ["bid","repobid"],["bid","aa"],["bid","brecha"],
 ["grag","kg"],["grag","rag"],["rag","ri"],["rag","aluc"],["aluc","traz"],
 ["traz","ri"],["com","kg"],["kg","ri"],
 ["propia","kg"],["propia","com"],["propia","ccby"],
 ["nlm","rag"],["nlm","traz"],["whisper","brecha"],
 ["autoef","traz"],["autoef","propia"]
];
var COL={fuente:"#d4a04a",concepto:"#e6dccb",repo:"#5d8fc7",licencia:"#5fbf9c",herramienta:"#c4667f"};
var NOM={fuente:"Fuente",concepto:"Concepto",repo:"Repositorio",licencia:"Licencia",herramienta:"Herramienta"};

var idx={}; N.forEach(function(n,i){idx[n.id]=i; n.deg=0;});
var links=E.map(function(e){ N[idx[e[0]]].deg++; N[idx[e[1]]].deg++; return {s:idx[e[0]],t:idx[e[1]]}; });
var adj={}; links.forEach(function(l){ (adj[l.s]=adj[l.s]||{})[l.t]=1; (adj[l.t]=adj[l.t]||{})[l.s]=1; });

document.getElementById("g-stats").textContent = N.length+" nodos \\u00b7 "+links.length+" aristas \\u00b7 "+Object.keys(NOM).length+" tipos de entidad";
document.getElementById("g-leyenda").innerHTML = Object.keys(NOM).map(function(k){
  return '<span class="small" style="font-size:13px;color:var(--lino-tenue)"><span style="display:inline-block;width:9px;height:9px;border-radius:50%;background:'+COL[k]+';margin-right:6px"></span>'+NOM[k]+'</span>';
}).join("");

// ---- grafico de barras (mismos datos) ----
var conteo={}; N.forEach(function(n){conteo[n.t]=(conteo[n.t]||0)+1;});
var maxc=Math.max.apply(null,Object.keys(conteo).map(function(k){return conteo[k];}));
document.getElementById("chart").innerHTML = Object.keys(NOM).map(function(k){
  var v=conteo[k]||0, w=(v/maxc*100).toFixed(1);
  return '<div style="display:flex;align-items:center;gap:12px;margin-bottom:11px">'+
   '<span style="flex:0 0 116px;font-family:Barlow Condensed,sans-serif;letter-spacing:1.4px;text-transform:uppercase;font-size:13.5px;color:var(--lino-tenue)">'+NOM[k]+'</span>'+
   '<span style="flex:1;height:22px;background:rgba(255,255,255,.05);border-radius:5px;overflow:hidden;display:block">'+
   '<span style="display:block;height:100%;width:'+w+'%;background:linear-gradient(90deg,'+COL[k]+'aa,'+COL[k]+')"></span></span>'+
   '<span style="flex:0 0 28px;font-family:Barlow Condensed,sans-serif;font-size:19px;font-weight:700;color:'+COL[k]+';text-align:right">'+v+'</span></div>';
}).join("");

// ---- simulacion de fuerzas ----
var cv=document.getElementById("g"), cx=cv.getContext("2d"), W=0,H=0,dpr=1;
function medir(){ dpr=Math.min(window.devicePixelRatio||1,2); var r=cv.getBoundingClientRect();
  W=r.width; H=r.height; cv.width=W*dpr; cv.height=H*dpr; cx.setTransform(dpr,0,0,dpr,0,0); }
medir(); window.addEventListener("resize",medir);

N.forEach(function(n,i){ var a=i/N.length*Math.PI*2; n.x=W/2+Math.cos(a)*Math.min(W,H)*0.32;
  n.y=H/2+Math.sin(a)*Math.min(W,H)*0.32; n.vx=0; n.vy=0; n.r=5+Math.min(n.deg,8)*1.05; });

var sobre=null, arrastra=null, alfa=1;
function paso(){
  var i,j,a,b,dx,dy,d,f;
  for(i=0;i<N.length;i++){ for(j=i+1;j<N.length;j++){ a=N[i];b=N[j];
    dx=b.x-a.x; dy=b.y-a.y; d=Math.sqrt(dx*dx+dy*dy)||0.01;
    f=1400/(d*d); if(d<1)d=1; dx/=d; dy/=d;
    a.vx-=dx*f; a.vy-=dy*f; b.vx+=dx*f; b.vy+=dy*f; } }
  for(i=0;i<links.length;i++){ a=N[links[i].s]; b=N[links[i].t];
    dx=b.x-a.x; dy=b.y-a.y; d=Math.sqrt(dx*dx+dy*dy)||0.01; f=(d-110)*0.0045;
    dx/=d; dy/=d; a.vx+=dx*f*d*0.55; a.vy+=dy*f*d*0.55; b.vx-=dx*f*d*0.55; b.vy-=dy*f*d*0.55; }
  for(i=0;i<N.length;i++){ a=N[i];
    a.vx+=(W/2-a.x)*0.0022; a.vy+=(H/2-a.y)*0.0026;
    if(a===arrastra){a.vx=0;a.vy=0;continue;}
    a.vx*=0.86; a.vy*=0.86;
    a.x+=Math.max(-6,Math.min(6,a.vx*alfa)); a.y+=Math.max(-6,Math.min(6,a.vy*alfa));
    a.x=Math.max(a.r+58,Math.min(W-a.r-58,a.x)); a.y=Math.max(a.r+14,Math.min(H-a.r-14,a.y)); }
  alfa*=0.982;
}
function vecino(i){ return sobre===null || sobre===i || (adj[sobre]&&adj[sobre][i]); }
function pintar(){
  cx.clearRect(0,0,W,H);
  links.forEach(function(l){
    var on = sobre===null || l.s===sobre || l.t===sobre;
    cx.strokeStyle = on ? "rgba(212,160,74,.50)" : "rgba(212,160,74,.10)";
    cx.lineWidth = on?1.3:0.7; cx.beginPath();
    cx.moveTo(N[l.s].x,N[l.s].y); cx.lineTo(N[l.t].x,N[l.t].y); cx.stroke();
  });
  N.forEach(function(n,i){
    var on=vecino(i);
    cx.globalAlpha = on?1:0.22;
    cx.beginPath(); cx.arc(n.x,n.y,n.r,0,6.2832);
    cx.fillStyle=COL[n.t]; cx.fill();
    if(i===sobre){ cx.lineWidth=2; cx.strokeStyle="#fff"; cx.stroke(); }
    if(n.deg>=3 || on){
      cx.font=(i===sobre?"600 ":"400 ")+"12.5px Barlow, sans-serif";
      cx.fillStyle=(i===sobre)?"#fff":"rgba(230,220,203,.88)";
      cx.textAlign="center"; cx.fillText(n.l, n.x, n.y-n.r-6);
    }
    cx.globalAlpha=1;
  });
}
var vivo=false, extra=0;
function despertar(n){ extra=Math.max(extra, n||24); if(!vivo){ vivo=true; requestAnimationFrame(bucle); } }
function bucle(){
  var mover = alfa>0.05 || arrastra;
  if(mover) paso();
  pintar();
  if(extra>0) extra--;
  if(mover || extra>0) requestAnimationFrame(bucle); else vivo=false;
}
despertar(0);
window.addEventListener("resize",function(){ despertar(60); });

function pos(ev){ var r=cv.getBoundingClientRect();
  var p = ev.touches? ev.touches[0] : ev; return {x:p.clientX-r.left, y:p.clientY-r.top}; }
function buscar(p){ for(var i=0;i<N.length;i++){ var dx=N[i].x-p.x, dy=N[i].y-p.y;
  if(dx*dx+dy*dy < (N[i].r+9)*(N[i].r+9)) return i; } return null; }
cv.addEventListener("mousemove",function(e){ var p=pos(e);
  if(arrastra){ arrastra.x=p.x; arrastra.y=p.y; alfa=Math.max(alfa,0.6); despertar(6); return; }
  var i=buscar(p); if(i!==sobre){ sobre=i; cv.style.cursor=i===null?"grab":"pointer"; despertar(2); } });
cv.addEventListener("mouseleave",function(){ sobre=null; arrastra=null; despertar(2); });
cv.addEventListener("mousedown",function(e){ var i=buscar(pos(e)); if(i!==null){ arrastra=N[i]; cv.style.cursor="grabbing"; despertar(30); } });
window.addEventListener("mouseup",function(){ arrastra=null; cv.style.cursor="grab"; });
cv.addEventListener("touchstart",function(e){ var p=pos(e); var i=buscar(p); if(i!==null){ arrastra=N[i]; sobre=i; despertar(30); e.preventDefault(); } },{passive:false});
cv.addEventListener("touchmove",function(e){ if(arrastra){ var p=pos(e); arrastra.x=p.x; arrastra.y=p.y; alfa=Math.max(alfa,0.6); despertar(6); e.preventDefault(); } },{passive:false});
cv.addEventListener("touchend",function(){ arrastra=null; });
})();
</script>"""

LINEA = """
<figure>
<svg viewBox="0 0 980 300" role="img" aria-label="Plan de formacion continua en tres horizontes" style="width:100%;height:auto;border:1px solid var(--borde);border-radius:12px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012))">
  <text x="40" y="44" fill="#d4a04a" font-family="Barlow Condensed, sans-serif" font-size="17" letter-spacing="3">FORMACI&Oacute;N CONTINUA: TRES HORIZONTES</text>
  <line x1="40" y1="118" x2="940" y2="118" stroke="#d4a04a" stroke-opacity=".35" stroke-width="2"/>
  <g font-family="Barlow Condensed, sans-serif">
    <circle cx="180" cy="118" r="9" fill="#d4a04a"/><circle cx="490" cy="118" r="9" fill="#a03652"/><circle cx="800" cy="118" r="9" fill="#3f7d6a"/>
    <text x="180" y="98" fill="#fff" font-size="19" font-weight="700" text-anchor="middle">Este ciclo</text>
    <text x="490" y="98" fill="#fff" font-size="19" font-weight="700" text-anchor="middle">Pr&oacute;ximos 6 meses</text>
    <text x="800" y="98" fill="#fff" font-size="19" font-weight="700" text-anchor="middle">Permanente</text>
  </g>
  <g font-family="Barlow, sans-serif" font-size="14.5" fill="#e6dccb">
    <text x="180" y="152" text-anchor="middle">Curso abierto de aprendizaje</text>
    <text x="180" y="172" text-anchor="middle">autom&aacute;tico sobre grafos</text>
    <text x="180" y="192" text-anchor="middle">(clases p&uacute;blicas de Stanford</text>
    <text x="180" y="212" text-anchor="middle">CS224W, gratuitas)</text>
    <text x="490" y="152" text-anchor="middle">Certificaci&oacute;n gratuita de</text>
    <text x="490" y="172" text-anchor="middle">bases de datos de grafos</text>
    <text x="490" y="192" text-anchor="middle">(GraphAcademy de Neo4j)</text>
    <text x="490" y="212" text-anchor="middle">y un proyecto propio</text>
    <text x="800" y="152" text-anchor="middle">Alertas de novedades por</text>
    <text x="800" y="172" text-anchor="middle">tema en Google Acad&eacute;mico</text>
    <text x="800" y="192" text-anchor="middle">y revisi&oacute;n mensual de</text>
    <text x="800" y="212" text-anchor="middle">SciELO y arXiv</text>
  </g>
  <g font-family="Barlow, sans-serif" font-size="13.5" fill="#a89c8b">
    <text x="40" y="262">La necesidad formativa que detect&eacute; no es &laquo;saber m&aacute;s de IA&raquo;: es &aacute;lgebra lineal y teor&iacute;a de grafos, que es lo que me frena</text>
    <text x="40" y="282">cuando intento leer los art&iacute;culos t&eacute;cnicos completos en vez de solo su introducci&oacute;n y sus conclusiones.</text>
  </g>
</svg>
<figcaption><strong>Gr&aacute;fico 4.</strong> Elaboraci&oacute;n propia. Plan de formaci&oacute;n continua con recursos abiertos
y gratuitos, ordenados por horizonte temporal. CC BY 4.0.</figcaption>
</figure>"""

BODY = ("""
<section class="bloque"><div class="wrap">
  <h2>Los cinco formatos, y por qu&eacute; cada uno</h2>
  <p class="entrada">Un formato no se elige porque quede bien: se elige porque hay algo que <em>solo</em> ese
  formato puede mostrar. Una relaci&oacute;n entre veintiocho entidades no cabe en un p&aacute;rrafo, y una definici&oacute;n
  precisa no se sostiene en una imagen.</p>
  """ + FORMATOS + """
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Texto &middot; La s&iacute;ntesis</h2>
  <p>Un modelo de lenguaje aprende regularidades del idioma, no hechos verificables. Por eso responde siempre:
  cuando no tiene el dato, produce igualmente la continuaci&oacute;n m&aacute;s probable. El resultado es un p&aacute;rrafo
  bien escrito que puede ser falso, y que <strong>no avisa de que lo es</strong>.</p>
  <p>La respuesta t&eacute;cnica se llama <strong>recuperaci&oacute;n aumentada (RAG)</strong>: antes de responder, el
  sistema busca fragmentos en una base documental y los pone delante del modelo. As&iacute; la respuesta se apoya en
  algo que existe y se puede enlazar. Peng et al. (2024) resumen el motivo del subcampo entero: mitigar la
  alucinaci&oacute;n, la falta de conocimiento especializado y la informaci&oacute;n desactualizada.</p>
  <p>El l&iacute;mite aparece con las preguntas globales. Edge et al. (2024) lo plantean con un ejemplo simple:
  &laquo;&iquest;cu&aacute;les son los temas principales de este conjunto de documentos?&raquo; no se resuelve buscando,
  porque la respuesta no est&aacute; en ning&uacute;n fragmento &mdash; est&aacute; repartida en todos. Su propuesta es construir
  antes un <strong>grafo de entidades y relaciones</strong>, detectar <strong>comunidades</strong> dentro de &eacute;l y
  resumir cada comunidad, de modo que el sistema tenga de antemano una respuesta para las preguntas de conjunto.</p>
  <p>&iquest;Funciona? La fuente arbitrada es la que puede responder eso. Polo-Bautista y Casique V&aacute;squez (2025)
  comparan las dos v&iacute;as y concluyen que integrar grafos produce respuestas m&aacute;s precisas, m&aacute;s concisas y
  <strong>sin alucinaciones</strong>, a cambio de un <strong>mayor tiempo de procesamiento</strong>. Esa es la frase
  que me interesa, porque no dice &laquo;mejor&raquo;: dice qu&eacute; se gana y qu&eacute; se paga. Cuando el dato tiene que
  ser cierto, conviene el camino lento.</p>
  <div class="nota">Y hay una condici&oacute;n previa que desde Puno no se puede pasar por alto. Jara y Ochoa (2020)
  y la UNESCO (2023) coinciden en ella: estas herramientas dan por supuesta una conexi&oacute;n estable y una
  infraestructura que no est&aacute; repartida por igual. Una plataforma que valida en l&iacute;nea y carga video funciona
  bien con fibra y es inservible donde la se&ntilde;al se cae a mitad de una entrega.
  <strong>La accesibilidad no es un asunto aparte de la calidad: la condiciona.</strong></div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Interactivo &middot; El grafo de este portafolio</h2>
  <p>Aqu&iacute; no describo el m&eacute;todo: lo aplico. Model&eacute; las fuentes, los conceptos, los repositorios, las
  licencias y las herramientas de este trabajo como un grafo y lo dej&eacute; navegable. Al pasar por un nodo, el
  grafo <strong>a&iacute;sla sus relaciones</strong> y se puede leer una vecindad a la vez.</p>
  """ + GRAFO + """
  <p style="margin-top:18px">Lo interesante es lo que se ve sin haberlo escrito.
  <strong>&laquo;Alucinaci&oacute;n&raquo; queda entre &laquo;RAG&raquo; y &laquo;trazabilidad&raquo;</strong>, que es justo el
  problema que este portafolio estudia. Y <strong>&laquo;acceso abierto&raquo; conecta la fuente de la UNESCO con la
  del BID</strong>: las dos institucionales, las dos sobre equidad. Ninguna de las dos cosas la decid&iacute; yo al
  colocar los nodos &mdash; las decidi&oacute; la estructura.</p>
  """ + CHART + """
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Imagen &middot; Piezas gr&aacute;ficas de elaboraci&oacute;n propia</h2>
  <p>Cuatro l&aacute;minas producidas para esta asignatura. Est&aacute;n compuestas en HTML y CSS y exportadas a imagen:
  cambiar un dato es cambiar una l&iacute;nea y volver a generarlas, no retocar un archivo a mano.</p>
  <figure><img src="assets/pa1-fig1.png" alt="Infograf&iacute;a: qu&eacute; es un grafo de conocimiento" loading="lazy">
  <figcaption><strong>Figura 1.</strong> Qu&eacute; es un grafo de conocimiento: la diferencia entre guardar documentos
  sueltos y guardar entidades con sus relaciones. Sintetizada a partir de Hogan et al. (2021) y
  Polo-Bautista y Casique V&aacute;squez (2025). Elaboraci&oacute;n propia, CC BY 4.0.</figcaption></figure>
  <figure><img src="assets/pa1-fig2.png" alt="Diagrama comparativo entre RAG cl&aacute;sico y GraphRAG" loading="lazy">
  <figcaption><strong>Figura 2.</strong> RAG cl&aacute;sico frente a GraphRAG, paso a paso y en dos v&iacute;as paralelas.
  Reelabora en diagrama una comparaci&oacute;n que el art&iacute;culo original expone en prosa; no reproduce ninguna de sus
  figuras, porque su licencia ND no lo permite. Elaboraci&oacute;n propia, CC BY 4.0.</figcaption></figure>
  <figure><img src="assets/pa1-fig3.png" alt="Mapa de licencias de las fuentes" loading="lazy">
  <figcaption><strong>Figura 3.</strong> Auditor&iacute;a de licencias: qu&eacute; permite cada fuente, m&aacute;s all&aacute; de si se
  puede leer gratis. Elaboraci&oacute;n propia, CC BY 4.0.</figcaption></figure>
  <figure><img src="assets/pa1-fig4.png" alt="Grafo de conocimiento trazado con una simulaci&oacute;n de fuerzas" loading="lazy">
  <figcaption><strong>Figura 4.</strong> Versi&oacute;n est&aacute;tica del grafo, trazada con una simulaci&oacute;n de fuerzas
  escrita en Python. Es el antecedente directo de la pieza interactiva de esta misma p&aacute;gina.
  Elaboraci&oacute;n propia, CC BY 4.0.</figcaption></figure>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Video</h2>
  <p>Los dos videos se incrustan con el <strong>reproductor oficial de YouTube</strong>. Es una decisi&oacute;n de
  licencia, no de comodidad: descargar el video y volver a subirlo ser&iacute;a una copia no autorizada; incrustarlo
  mantiene la atribuci&oacute;n, las m&eacute;tricas y el control en su autor.</p>
  <div class="rejilla r2">
    <div>
      <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/5AIOoM3sD2E" title="RAG en grafos: el poder de los LLM en datos conectados" loading="lazy" allowfullscreen></iframe></div>
      <p class="small tenue" style="margin-top:9px">Feregrino. (24 de septiembre de 2024). <em>RAG en grafos: El poder
      de los LLMs en datos conectados</em> [Video]. YouTube. Explicaci&oacute;n en espa&ntilde;ol de c&oacute;mo se combinan los
      grafos con los modelos de lenguaje.</p>
    </div>
    <div>
      <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/v54XHqP-WAU" title="Repositorios de recursos educativos digitales" loading="lazy" allowfullscreen></iframe></div>
      <p class="small tenue" style="margin-top:9px">Fernando, J. (31 de agosto de 2020). <em>Repositorios de Recursos
      Educativos Digitales</em> [Video]. YouTube. Recurso obligatorio de la unidad; es el que ordena la diferencia
      entre buscador y repositorio que uso en la p&aacute;gina&nbsp;2.</p>
    </div>
  </div>
</div></section>

<section class="bloque"><div class="wrap">
  <h2>Formaci&oacute;n continua</h2>
  <p>Detectar la necesidad formativa es m&aacute;s &uacute;til que declararla. Al leer las fuentes de este portafolio me
  encontr&eacute; con un l&iacute;mite concreto: <strong>entiendo la introducci&oacute;n y las conclusiones de los art&iacute;culos
  t&eacute;cnicos, y me pierdo en la secci&oacute;n de m&eacute;todo</strong>, donde est&aacute; el &aacute;lgebra. No es un problema de IA,
  es de matem&aacute;tica de base. Ese es el hueco que hay que cerrar, y de ah&iacute; sale el plan.</p>
  """ + LINEA + """
  <div class="rejilla r3" style="margin-top:6px">
    <div class="tarjeta"><h3>Gratuito, de verdad</h3><p class="small" style="margin-bottom:0">Los tres recursos
    son abiertos: clases universitarias publicadas en video, una academia gratuita de un fabricante y alertas de
    repositorio. Ninguno depende de pagar una suscripci&oacute;n en d&oacute;lares.</p></div>
    <div class="tarjeta"><h3>Con producto, no con horas</h3><p class="small" style="margin-bottom:0">Cada bloque
    termina en algo que se puede ense&ntilde;ar &mdash;un proyecto, un grafo, una nota&mdash;, porque las horas de video
    vistas no son evidencia de nada.</p></div>
    <div class="tarjeta"><h3>Asincr&oacute;nico a prop&oacute;sito</h3><p class="small" style="margin-bottom:0">Tengo clases
    ma&ntilde;ana y tarde. Cualquier plan que dependa de asistir a algo en vivo se cae la primera semana; por eso todo
    lo elegido se puede hacer a deshora y sin conexi&oacute;n estable.</p></div>
  </div>
  <div class="nota" style="margin-top:20px"><strong>Lo que aprend&iacute; en esta p&aacute;gina.</strong> Producir en varios
  formatos no es repetir el mismo contenido de cinco maneras. Cuando el grafo interactivo mostr&oacute; que
  &laquo;alucinaci&oacute;n&raquo; ca&iacute;a entre &laquo;RAG&raquo; y &laquo;trazabilidad&raquo;, ese hallazgo no exist&iacute;a en
  ninguno de mis textos: lo produjo el formato.</div>
</div></section>
""")

page("03-contenido.html", "3 &middot; Desarrollo del contenido &middot; Portafolio digital",
     "Paso 3 de 5",
     "Desarrollo del contenido",
     "Contenido en cinco formatos &mdash;texto, imagen, video, gr&aacute;fico e interactivo&mdash; y el plan de formaci&oacute;n continua que sale de una necesidad detectada, no declarada.",
     BODY, extra=JS)
