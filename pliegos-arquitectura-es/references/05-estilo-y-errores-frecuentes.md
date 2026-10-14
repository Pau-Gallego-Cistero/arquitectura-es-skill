# Estilo, glosario y checklist de revisión

## Contenido

1. Registro y estilo
2. Glosario castellano / catalán
3. Checklist de revisión (Modo E)
4. Errores detectados en los documentos de referencia
5. Formato de entrega de la revisión

## 1. Registro y estilo

- **Técnico y sobrio.** Verbos de acción ("se plantea", "se resuelve", "se dispone"), voz impersonal o primera persona del plural según convención de la convocatoria.
- **Concreción antes que adjetivo.** Sustituye "excelente aislamiento" por "aislamiento de [espesor] en [elemento]", o elimina el adjetivo.
- **Cifras con unidad y base.** "Reducción estimada del consumo de energía primaria no renovable: [X] % (estimación preliminar, [método])".
- **Sin absolutos** (garantiza, perfecto, óptimo, sin ningún impacto) salvo respaldo.
- **Párrafos cortos** y listas solo cuando hay elementos paralelos (fases, entregables, mejoras).
- **Mismos nombres para las mismas cosas** en todo el documento (un espacio no cambia de nombre entre el cuadro y el texto).
- **Siglas**: se definen la primera vez (PPT, PCAP, DIB, DF, OEE, BIM…), y solo si el lector las conoce; en documentos de licitación mantén las siglas del propio pliego.
- **Tiempos**: presente para lo que el proyecto hace ("el edificio se abre…"); futuro para lo que el contratista hará ("se entregará…").
- **Idioma de la convocatoria.** No mezcles idiomas; los términos técnicos se escriben en el idioma del documento.

## 2. Glosario castellano / catalán

| Castellano | Català |
|---|---|
| pliego de prescripciones técnicas (PPT) | plec de prescripcions tècniques (PPT) |
| pliego de cláusulas administrativas particulares (PCAP) | plec de clàusules administratives particulars (PCAP) |
| criterios de adjudicación | criteris d'adjudicació |
| juicio de valor / evaluables automáticamente | judici de valor / avaluables de forma automàtica |
| acuerdo marco | acord marc |
| lote | lot |
| órgano de contratación | òrgan de contractació |
| oferta técnica / documentación técnica | oferta tècnica / documentació tècnica |
| memoria descriptiva / constructiva | memòria descriptiva / constructiva |
| anteproyecto / proyecto básico / proyecto de ejecución | avantprojecte / projecte bàsic / projecte executiu |
| estudio de seguridad y salud | estudi de seguretat i salut |
| gestión de residuos | gestió de residus |
| control de calidad | control de qualitat |
| superficie útil / construida | superfície útil / construïda |
| programa funcional | programa funcional |
| circulaciones | circulacions |
| aulario / aula / aula de refuerzo | aulari / aula / aula de reforç |
| vestíbulo / vestuario | vestíbul / vestidor |
| porche / pasarela | porxo / passera |
| patio / jardín / bosque | pati / jardí / bosc |
| forjado / losa / placa alveolar | forjat / llosa / placa alveolar |
| cerramiento / fachada ventilada | tancament / façana ventilada |
| cubierta / falso techo | coberta / fals sostre |
| aislamiento / puente térmico | aïllament / pont tèrmic |
| carpintería (rotura de puente térmico) | fusteria (trencament de pont tèrmic) |
| inercia térmica / ventilación cruzada | inèrcia tèrmica / ventilació creuada |
| aerotermia / fotovoltaica | aerotèrmia / fotovoltaica |
| aguas pluviales / aguas grises | aigües pluvials / aigües grises |
| bomberos / licencia ambiental | bombers / llicència ambiental |
| días naturales / hitos / entrega | dies naturals / fites / lliurament |
| alzados / secciones / plantas | alçats / seccions / plantes |

Normativa, nombres de normas y organismos: se escriben **tal como figuran oficialmente**; no se traducen.

## 3. Checklist de revisión (Modo E)

**Estructura**
- [ ] El documento sigue la estructura exigida por el pliego o las bases (apartados, orden, extensión, formato).
- [ ] Cada punto crítico de la diagnosis tiene su propuesta con la misma numeración.
- [ ] Cada criterio de adjudicación tiene su respuesta localizable.
- [ ] Numeración sin duplicados, saltos ni apartados fuera de orden.

**Contenido**
- [ ] Sin marcadores de posición (`NOM`, `[…]`, `FALTA ESQUEMA`, `TBD`) ni texto de borrador.
- [ ] Sin frases cortadas, palabras dañadas por reemplazos globales ni caracteres extraños.
- [ ] Siglas definidas o conocidas por el lector.
- [ ] Nada se promete sin posibilidad de cumplimiento (certificaciones, ahorros, plazos).
- [ ] Mejoras vinculadas a un criterio, un entregable y una forma de comprobarlas.
- [ ] Sin autopuntuación ni lenguaje que invada la competencia del evaluador.

**Cifras**
- [ ] Cuadro de superficies cuadrado (`scripts/check_superficies.py`).
- [ ] Plazos de las fases suman el total; coinciden con PPT y con las reducciones ofrecidas.
- [ ] Cifras coherentes entre texto, planos y cuadros.
- [ ] Todo valor estimado está marcado como estimado.

**Normativa**
- [ ] Toda referencia con estado (Verificado / [VERIFICAR] / [NO CONSTA]).
- [ ] Sin artículos ni valores límite de memoria.
- [ ] Capa autonómica y local considerada.
- [ ] Lista final de verificaciones pendientes.

**Forma**
- [ ] Idioma único; terminología consistente.
- [ ] Pies de imagen informativos.
- [ ] Sin datos personales de terceros ni de documentos de referencia.
- [ ] En concursos anónimos, sin elementos que identifiquen al equipo.

## 4. Errores detectados en los documentos de referencia

Resumen de los problemas encontrados al leerlos. Sirven de lista de comprobación para evitarlos en documentos nuevos:

1. **Marcadores sin completar**: nombres sustituidos por `NOM`/`Nom1`/`Nom2` en el organigrama y en las tablas de funciones, y una nota `FALTA ESQUEMA` dentro del texto.
2. **Palabras dañadas por reemplazo global** en un apartado de climatización (el fragmento "energ-" quedó convertido en "6nerg", de modo que el texto es ilegible en varios párrafos).
3. **Numeración desordenada o repetida**: en un plan de entrega aparecen apartados "2.2.E" antes de "2.2.D" y la fase siguiente reutiliza "2.2.E", "2.2.F"…; en otra oferta el apartado "2.3-B" aparece tras un "2.2-A"; en otra, "3-2 B" y "3-2 C" repiten el prefijo.
4. **Cifras que no cuadran**: en un cuadro de superficies, la suma de las partes de la columna "propuesta" (espacios 1.585 m², circulaciones 431 m², conexión entre edificios 140 m²) da 2.156 m², mientras que el total indicado es 2.165 m²: parece una transposición de cifras. Comprobar siempre con el script.
5. **Duraciones incoherentes**: una fase indicada como semanas 8 a 19 (12 semanas) figura con duración "4 meses".
6. **Etiquetas confusas**: un apartado titulado "Sistemas activos" introduce soluciones calificadas de "pasivos" en el texto.
7. **Autopuntuación**: una propuesta de sostenibilidad se otorga puntuaciones ("40/40", "15/20", "10/10"). Esa valoración corresponde al órgano evaluador.
8. **Afirmaciones absolutas o sin respaldo**: "garantizar una clasificación energética A", porcentajes de ahorro sin método, "edificio pasivo" sin definir.
9. **Erratas visibles**: palabras mal escritas en rótulos y cuadros (en aulas, programas y títulos de sala), mayúsculas inconsistentes, espacios y signos sobrantes.
10. **Referencias cruzadas rotas**: textos que remiten a "la fase", a "los puntos en rojo" o a esquemas que no están en la versión entregada.
11. **Datos personales** en anexos de proposición (nombre, identificación fiscal, dirección) que no deben copiarse a otros documentos.

## 5. Formato de entrega de la revisión

Agrupar por gravedad:
- **Bloqueante** (puede excluir la oferta o invalidar el documento): incumplimiento de formato o extensión, datos del sobre automático en el de juicio de valor, referencias normativas derogadas, cifras que no cuadran en documentos que se evalúan por ellas.
- **Importante**: apartados sin respuesta a un criterio, promesas sin respaldo, numeración rota, siglas sin definir.
- **Menor**: erratas, estilo, uniformidad.

Para cada hallazgo: ubicación, problema, corrección propuesta y, si es normativo, estado de verificación.
