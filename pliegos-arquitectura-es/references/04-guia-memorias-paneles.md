# Guía de memorias y paneles de concurso

Basada en tres paneles de referencia: un instituto de secundaria (ampliación y reconversión), una escuela infantil y primaria, y una ciudad de la música en una antigua fábrica; más las memorias que acompañan a algunos de ellos.

## Contenido

1. Qué hace bien un panel
2. Anatomía del panel
3. Patrones de redacción observados
4. Memoria descriptiva: estructura
5. Memoria constructiva
6. Memoria energética y de sostenibilidad
7. Cuadro de superficies
8. Pies de imagen
9. Plantilla breve de cada bloque
10. Lo que no hay que copiar

## 1. Qué hace bien un panel

- **Una idea central con lema** ("Escala musical", "Versátil"). El lema resume la estrategia y se retoma en el texto.
- **Tres o cuatro decisiones** que organizan todo, visibles en planta, sección y axonometría.
- **Cifras clave** a la vista (superficie por alumno, % de ahorro, m² de naturaleza).
- **Texto breve** junto a cada gráfico, que explica qué se ve y por qué importa.
- **Datos que se pueden comprobar** (cotas, escalas, superficies, dimensiones constructivas).

## 2. Anatomía del panel

De arriba abajo, en los paneles de referencia:
1. Imagen principal (render exterior o interior), con lema y título del proyecto.
2. Bloques de estrategia ("Implantación", "Racionalidad en circulaciones", "Instalaciones", "Estrategia de programa") con un esquema pequeño cada uno.
3. Planos (plantas por niveles, secciones longitudinal y transversal) con escala gráfica.
4. Axonometría explotada o esquema constructivo/estructural.
5. Gráficos de energía o sostenibilidad (ahorro %, ciclo del agua, ventilación).
6. Cuadros de superficies o programa.
7. Renders secundarios con pies de imagen.
8. Cita inspiradora o referencia (opcional, en la escuela infantil: pedagogía).

## 3. Patrones de redacción observados

- **Decisiones numeradas con verbo en infinitivo y palabra clave en negrita.** Ejemplo de patrón: *1. Organizar el programa dentro de… 2. Conectar los tres edificios mediante… 3. Dar continuidad al camino…*
- **Frase de apertura con la decisión, frase siguiente con el efecto.** Ejemplo de patrón: *Se concentran los usos públicos en planta baja; la ciudad entra en el edificio.*
- **Binomios problema/solución**: condicionante → decisión que lo transforma en elemento del proyecto.
- **Uso de criterios oficiales** del cliente (por ejemplo, unos "criterios para edificios docentes públicos" de una fecha concreta) para justificar decisiones.
- **Vocabulario preciso**: orientación, inercia térmica, ventilación cruzada, doble piel ventilada, SUDS, bioclimático.
- **Cifras con unidad y contexto**: m², cotas, % de ahorro, modulación (retícula de pilares, canto de forjado).
- **Párrafos cortos** (60-90 palabras) y subtítulos que se entienden solos.

## 4. Memoria descriptiva: estructura

Dos versiones de referencia, útiles según la extensión disponible.

**Versión breve (concurso de proyecto)**
1. Condicionantes iniciales (3-4 numerados: solar, conexiones, trazados o infraestructuras existentes).
2. Cómo la propuesta recoge esos condicionantes y los criterios del cliente.
3. Decisiones numeradas (1, 2, 3) con una o dos frases de justificación.

**Versión extensa (propuesta de licitador)**
1. Contexto y ámbito de ejecución.
2. Conocimiento del lugar y condicionantes urbanos (topografía, paisaje, preexistencias).
3. Planteamiento constructivo y criterios arquitectónicos (volumetría, accesos, distribución por plantas).
4. Criterios medioambientales y de sostenibilidad.
5. Dificultades y puntos críticos del proyecto.
6. Soluciones propuestas y proyección futura.
7. Detalle de plantas con programa funcional.

## 5. Memoria constructiva

Orden útil: lógica general (modulación, prefabricación, rapidez de obra, posible ampliación futura) → sistema estructural → forjados → cerramientos → compartimentación → pavimentos → cubierta → instalaciones. Para cada elemento: material, dimensión clave y motivo (durabilidad, economía, relación con lo existente).

Evita afirmaciones de cumplimiento normativo ("cumple el CTE") sin la comprobación correspondiente; formula "se diseña para cumplir [norma] [VERIFICAR] y se justificará en proyecto" si todavía no hay cálculo.

## 6. Memoria energética y de sostenibilidad

Estructura recomendable (combina las referencias):
1. Objetivo (autonomía, reducción de demanda, confort).
2. Estrategias pasivas: orientación, protección solar, inercia, ventilación cruzada/nocturna, envolvente (aislamiento, doble piel, carpinterías con rotura de puente térmico), vegetación.
3. Estrategias activas: sistema de climatización eficiente, recuperación de calor, iluminación LED con regulación, fotovoltaica.
4. Agua: recogida de pluviales, aparatos de bajo consumo, SUDS.
5. Residuos y materiales: reciclaje, materiales de bajo impacto, durabilidad, mantenimiento.
6. Resultado esperado, **con su base**: "estimación preliminar" o "cálculo con [herramienta]" y su fecha.

Cuidado con: etiquetas energéticas garantizadas ("calificación A"), porcentajes de ahorro sin base de cálculo, "edificio pasivo" o "NZEB" sin definir qué se entiende por ello. Marca como estimado lo que no esté calculado.

## 7. Cuadro de superficies

Formato observado: **Programa** (requerido) frente a **Propuesta** (diseñado), por espacios y por grupos (aulas, administración, otros servicios), subtotales, circulaciones, total útil y total construido (con porches o espacios exteriores computados al porcentaje que fijen las bases).

Reglas:
- Una columna de programa y otra de propuesta, con la diferencia visible.
- Subtotales y totales deben cuadrar. Ejecuta `scripts/check_superficies.py`.
- Misma nomenclatura de espacios en cuadro, plantas y texto (códigos tipo P.1, A.3…).
- Indica criterio de cómputo (superficie útil frente a construida; cómo se computan porches, terrazas, cubiertas practicables).

## 8. Pies de imagen

Un buen pie dice **qué punto de vista** es y **qué quiere mostrar**: *Vista desde la plaza: la planta baja permeable activa el espacio público.* No usar "render del edificio" a secas.

## 9. Plantilla breve de cada bloque

**Bloque de estrategia (60-90 palabras)**
> **[Verbo en infinitivo + palabra clave].** [Decisión en una frase]. [Efecto sobre el uso, el lugar o el clima]. [Dato cuantificado si lo hay].

**Bloque de sección o sistema constructivo**
> [Elemento]: [material y dimensión]. [Motivo en una frase].

**Pie de imagen**
> [Punto de vista]. [Idea que muestra].

## 10. Lo que no hay que copiar

- Textos, datos o nombres de los documentos de referencia (son de otros autores).
- Erratas, frases cortadas y placeholders (ver `05-estilo-y-errores-frecuentes.md`).
- Cifras de otros proyectos como si fueran propias.
- Afirmaciones de rendimiento energético sin respaldo.
