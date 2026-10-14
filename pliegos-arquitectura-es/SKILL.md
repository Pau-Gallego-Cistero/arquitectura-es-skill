---
name: pliegos-arquitectura-es
description: Redacta, optimiza y revisa pliegos técnicos (PPT / PLEC), ofertas técnicas de licitador (Sobre B, criterios de juicio de valor) y memorias de paneles de concursos de arquitectura para la administración pública en España; busca, resume y corrige normativa arquitectónica española (LCSP, CTE y DB, RITE, REBT, accesibilidad, seguridad y salud, residuos, normativa autonómica y local) verificando siempre la fuente y sin inventar nunca una norma. Úsala siempre que el usuario mencione pliego de prescripciones técnicas, PPT, PCAP, plec, licitación, concurso de proyectos o de ideas, oferta técnica, sobre B, panel de concurso, memoria descriptiva/constructiva/energética, criterios de adjudicación, acuerdo marco de estudios o proyectos, "revisa si esta normativa está vigente", "resume este DB/ordenanza" o "compleción del CTE", aunque no diga "skill" ni "pliego" de forma explícita.
---

# Pliegos técnicos y memorias de concurso de arquitectura (España)

Esta skill sirve a arquitectos que trabajan con contratación pública: tanto desde la **administración** (redactar el pliego) como desde el **licitador** (responder al pliego con una oferta técnica o con un panel de concurso). Los textos de referencia que dieron forma a la skill son seis documentos reales de concursos y licitaciones (paneles de institutos, escuelas y una ciudad de la música; ofertas técnicas de equipamientos deportivos). Su estructura y su tono están resumidos en `references/`. **Se imita la estructura y el registro, nunca se copia el texto ni los datos personales** (nombres, NIF, direcciones, equipos) de esos documentos.

## Regla n.º 1: no inventar normativa

La normativa es el punto donde un error cuesta más (un pliego recurrible, una memoria que incumple, una oferta excluida). Por eso:

1. **Nunca cites de memoria** un número de artículo, una fecha, un valor límite (anchos, resistencias al fuego, transmitancias, niveles acústicos, pendientes…) ni el título exacto de una norma si no lo has contrastado en esta sesión con una fuente. Si no has podido contrastarlo, escribe el nombre general de la norma y marca `[VERIFICAR]`.
2. **Si no sabes aplicar una norma, o no la conoces, dilo.** Escribe "no puedo confirmar cómo aplica esta norma a este caso" e indica qué documento hace falta (texto consolidado, ordenanza municipal, ficha del Consejo/Federación, etc.). No extrapoles desde una norma "parecida" ni rellenes huecos con lo que "suele decir" una norma.
3. **No inventes** disposiciones transitorias, fechas de entrada en vigor, órganos competentes ni modelos oficiales.
4. Etiqueta cada referencia normativa que escribas con uno de estos tres estados (ver `references/01-protocolo-normativa.md`):
   - **Verificado**: consultado en fuente oficial en esta sesión (indica fuente y fecha).
   - **[VERIFICAR]**: la norma existe a tu entender, pero no se ha contrastado texto, versión vigente o artículo.
   - **[NO CONSTA]**: no sabes si existe, si está vigente o cómo aplica; no se redacta ninguna afirmación sobre ella.
5. Si hay herramienta de búsqueda web, úsala para verificar (BOE texto consolidado, codigotecnico.org, boletín autonómico, plataforma de contratación). Si no la hay, entrega el documento con las marcas `[VERIFICAR]` visibles y una **lista final de verificaciones pendientes**. Nunca las quites para que "quede limpio".

## Primer paso: ¿desde qué lado se escribe?

Pregunta o deduce (una sola pregunta, si hace falta):

| Situación | Documento | Qué se hace |
|---|---|---|
| La administración (o su asesor) redacta el pliego | **PPT** (pliego de prescripciones técnicas) y su coordinación con el **PCAP** | Modo A |
| Un licitador responde a un pliego | **Oferta técnica / Sobre B** (criterios de juicio de valor), plan de trabajo, equipo, mejoras | Modo B |
| Concurso de proyectos o de ideas con paneles | **Memoria de panel** (A1/A0) + memorias descriptiva, constructiva, energética | Modo C |
| Hay que localizar, resumir o corregir normativa | **Ficha de normativa**, resumen, corrección de citas | Modo D |
| Ya existe un borrador | Revisión de calidad y coherencia | Modo E |

Los documentos de referencia aportados por el usuario son sobre todo ofertas técnicas y paneles (Modos B y C). Si el usuario habla de "pliego técnico", confirma si quiere **redactar el pliego** (administración) o **la documentación técnica que se entrega a la licitación** (licitador); no es lo mismo y la estructura cambia.

Idioma: escribe en el idioma de la convocatoria (castellano o catalán). Para catalán, usa el glosario de `references/05-estilo-y-errores-frecuentes.md`. El marco normativo es el **español** (estatal), más la capa **autonómica y local** que corresponda al lugar del encargo; esa capa se busca, no se recuerda.

## Modo A. Redactar u optimizar un PPT

1. Reúne: objeto, tipo de contrato (servicios, obras, acuerdo marco, concurso de proyectos), programa funcional, solar/edificio, presupuesto orientativo, plazos, hitos y entregables, órgano de contratación.
2. Parte de `assets/plantilla-PPT.docx` y de `references/03-estructura-pliegos-y-ofertas.md`.
3. Separa con nitidez lo que va en el PPT (qué se exige técnicamente y cómo se entrega) de lo que va en el PCAP (criterios de adjudicación, solvencia, penalidades, garantías). No metas criterios de adjudicación en el PPT.
4. Redacta las prescripciones de forma **verificable**: cada exigencia debe poder comprobarse al recibir el trabajo (formato, escala, contenido mínimo, plazo en días naturales o hábiles, fase y reunión de la que depende). Evita adjetivos sin criterio ("adecuado", "óptimo") salvo que se definan.
5. Las referencias normativas siguen la Regla n.º 1. Cierra con la lista de normas citadas y su estado.

## Modo B. Redactar la oferta técnica del licitador (Sobre B)

1. Pide el PCAP y el PPT (o los criterios de adjudicación) y el límite de extensión (p. ej. "3 DIN A3 + 1 DIN A3"). Respeta el límite al pie de la letra; una oferta que se pasa de páginas puede no valorarse.
2. Parte de `assets/plantilla-oferta-tecnica.docx`. Estructura base, tomada de las referencias:
   - **Diagnosis** (puntos críticos, agrupados en pocos conceptos y nombrados con letras A, B, C…).
   - **Propuestas**, con **la misma numeración** que la diagnosis: cada punto crítico tiene su solución.
   - **Proceso de elaboración**: fases, actividades, hitos/reuniones, aspectos críticos y plazos.
   - **Valor añadido / mejoras**, marcadas visualmente (las referencias usan color) y vinculadas a un criterio de adjudicación.
   - **Equipo y organización**: perfiles, funciones, responsabilidades, dedicación, coordinación.
3. Para cada criterio de juicio de valor del pliego, haz explícito dónde se responde (por ejemplo, un índice de correspondencia al principio). Así el evaluador encuentra los puntos sin buscar.
4. **No te autopuntúes.** Algunas ofertas de referencia incluyen una valoración con puntuación propia ("40/40"); esa puntuación corresponde al órgano evaluador. Describe cumplimiento y ventajas, no notas.
5. Los criterios evaluables automáticamente (reducción de plazos, mejora de equipo, precio) van en el sobre y modelo que indique el pliego (en las referencias, un anexo con modelo de proposición), no mezclados con la memoria de juicio de valor.
6. No ofrezcas lo que no puedas cumplir. Toda mejora de plazo, certificación (NZEB, A, LEED/BREEAM…) o ahorro (%) debe ser realista y trazable; si es una estimación, dilo ("estimado, por confirmar en fase de proyecto").

## Modo C. Memoria de panel de concurso

1. Parte de `assets/plantilla-memoria-panel.docx` y de `references/04-guia-memorias-paneles.md`.
2. Un panel es una **historia en tres o cuatro decisiones** que se ven en la planta, la sección y una imagen. La memoria no repite el panel: lo justifica. Estructura típica: lema → condicionantes → decisiones numeradas (verbo en infinitivo: *Organizar, Conectar, Dar continuidad*) → sistema constructivo → energía/sostenibilidad → programa y cuadro de superficies.
3. Cuantifica donde puedas y marca lo estimado. Las cifras de superficie deben **cuadrar**: ejecuta `scripts/check_superficies.py` sobre el cuadro antes de entregar (suma de partes, total útil, total construido, diferencia frente al programa).
4. Respeta el límite de caracteres/palabras de las bases si lo hay; el panel se lee de pie y de lejos: bloques de 60-90 palabras, subtítulos claros, pies de imagen que cuenten algo.
5. Anonimato: si el concurso es anónimo (lema), no incluyas nombre, logotipo ni datos del equipo en panel ni memoria.

## Modo D. Buscar, resumir y corregir normativa

1. Sigue `references/01-protocolo-normativa.md` y usa el mapa por materias de `references/02-mapa-normativo-espana.md` **solo como índice de dónde mirar**, no como fuente de contenido.
2. Para cada norma que se pida resumir, rellena `assets/ficha-verificacion-normativa.docx` (o su equivalente en el chat): título oficial, rango, publicación, estado (vigente/derogada/parcialmente), última modificación, ámbito de aplicación, qué exige de forma resumida, disposiciones transitorias relevantes, fuente y fecha de consulta.
3. **Corregir** significa dos cosas, y se hacen por separado:
   - **Corregir las citas**: detectar referencias derogadas, desactualizadas o mal citadas en un texto del usuario, proponer la cita correcta con su fuente y marcar lo que no puedas verificar.
   - **Corregir la redacción** del apartado normativo (claridad, coherencia, tiempos verbales, tono) sin alterar el sentido jurídico.
4. En los resúmenes distingue **lo que dice la norma** (con referencia) de **lo que se interpreta** (marcado como interpretación). No cites textualmente más de una frase corta; parafrasea.
5. Las normas UNE y otras de pago: no reproduzcas su contenido; indica que existen y que hay que consultarlas.

## Modo E. Revisión de un borrador

Pasa la checklist de `references/05-estilo-y-errores-frecuentes.md`: marcadores sin completar (`NOM`, `FALTA ESQUEMA`), numeración duplicada o salteada, cifras que no cuadran, siglas sin definir, promesas sin respaldo, contradicciones entre apartados, referencias normativas sin verificar, y erratas. Entrega los hallazgos agrupados por gravedad (bloqueante / importante / menor) con la corrección propuesta.

## Entregables

- Documento en el formato pedido; por defecto Word (.docx) si el usuario va a editarlo y presentarlo. Lee antes la skill `docx` si lo generas.
- Siempre, al final: **(1)** lista de referencias normativas con su estado (Verificado / [VERIFICAR] / [NO CONSTA]); **(2)** lista de supuestos hechos; **(3)** datos que faltan.
- No guardes ni repitas datos personales de los documentos de referencia.

## Tono

Técnico, preciso y sobrio, con verbos de acción y cifras. Frases cortas en panel; algo más desarrolladas en memoria. Sin superlativos ni promesas absolutas ("garantiza", "óptimo", "perfectamente") salvo que haya un respaldo medible. Detalles en `references/05-estilo-y-errores-frecuentes.md`.

## Mapa de archivos

- `references/01-protocolo-normativa.md`: cómo verificar, estados, fuentes, qué hacer cuando no se sabe.
- `references/02-mapa-normativo-espana.md`: índice por materias de qué normas mirar (sin contenido, sin artículos).
- `references/03-estructura-pliegos-y-ofertas.md`: PPT, PCAP, Sobre B/C, concurso de proyectos, patrones de las ofertas de referencia.
- `references/04-guia-memorias-paneles.md`: anatomía de los paneles y memorias de referencia.
- `references/05-estilo-y-errores-frecuentes.md`: registro, glosario ES/CA, checklist de revisión y errores detectados en las referencias.
- `assets/`: plantillas Word (`plantilla-PPT.docx`, `plantilla-oferta-tecnica.docx`, `plantilla-memoria-panel.docx`, `ficha-verificacion-normativa.docx`) y `plantilla-cuadro-superficies.csv` (entrada para el script).
- `scripts/check_superficies.py`: comprobador aritmético de cuadros de superficies (formato de entrada en `assets/plantilla-cuadro-superficies.csv`; uso: `python scripts/check_superficies.py cuadro.csv`).
