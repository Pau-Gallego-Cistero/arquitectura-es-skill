# Pliegos Técnicos y Concursos de Arquitectura (España) 🏛️📐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Normativa: España](https://img.shields.io/badge/Normativa-España%20(LCSP%20%7C%20CTE)-blue)](https://www.codigotecnico.org/)
[![AI Ready](https://img.shields.io/badge/AI%20Skill-Claude%20%7C%20Cursor%20%7C%20Custom%20GPT-emerald)](#c%C3%B3mo-usar-esta-skill)

Asistente y sistema de instrucciones especializadas para redactar, auditar y optimizar **pliegos de prescripciones técnicas (PPT/PLEC)**, **ofertas técnicas de licitadores (Sobre B / Criterios de juicio de valor)** y **memorias de paneles de concursos de ideas**, bajo el marco legal y técnico de la edificación en España.

Diseñado bajo una estricta política de **tolerancia cero con la alucinación normativa**: ninguna norma se inventa, los datos dudosos se marcan explícitamente y las superficies se auditan matemáticamente.

---

## 🎯 ¿Para quién es?

* **Administraciones Públicas y Técnicos Municipales:** Redacción de pliegos de prescripciones técnicas (PPT/PLEC) blindados, claros y coordinados con el PCAP sin mezclar criterios de adjudicación.
* **Estudios de Arquitectura y Licitadores:** Estructuración de memorias técnicas de juicio de valor (Sobre B), propuestas de valor añadido y cumplimiento de restricciones estrictas de páginas/formatos.
* **Concursantes:** Memorias ejecutivas para paneles DIN A1/A0 y validación aritmética de programas funcionales y cuadros de superficies.

---

## ⚖️ Principio fundamental: No inventar normativa

El mayor riesgo de utilizar modelos de lenguaje en licitaciones públicas es la invención de artículos, tablas de transmitancias, resistencias al fuego o plazos legales. 

Este repositorio implementa un protocolo de etiquetado obligatorio:
1. **Verificado:** Consultado y contrastado en fuente oficial durante la sesión (BOE texto consolidado, CTE, boletín autonómico).
2. **`[VERIFICAR]`:** La norma se identifica en el marco regulatorio pero requiere que el usuario contraste la vigencia, redactado o tabla exacta antes de firmar.
3. **`[NO CONSTA]`:** No se presupone ni extrapola aplicación normativa sin certeza técnica comprobada.

---

## 🧭 Los 5 Modos de Operación

| Modo | Objetivo | Enfoque principal |
|---|---|---|
| **Modo A** | **PPT para la Administración** | Prescripciones verificables, delimitación clara frente al PCAP, sin adjetivos vagos ni criterios de adjudicación dentro del pliego técnico. |
| **Modo B** | **Oferta Técnica / Sobre B (Licitador)** | Estructura *Diagnosis (A, B, C) ➔ Propuesta (A, B, C)*, trazabilidad frente a baremo de juicio de valor, mejoras sin autopuntuación ficticia. |
| **Modo C** | **Memoria de Panel de Concurso** | Textos sintéticos (60–90 palabras por bloque), narrativa en 3–4 decisiones (*Organizar, Conectar, Sostener*), cuadro de superficies cuadrado y anonimato garantizado. |
| **Modo D** | **Búsqueda y Resumen Normativo** | Ficha de verificación legal (LCSP, CTE, RITE, REBT, accesibilidad, residuo, planes urbanísticos). Distinción expresa entre texto de la norma e interpretación técnica. |
| **Modo E** | **Auditoría y Revisión de Borradores** | Checklist exhaustivo de erratas, marcadores pendientes (`FALTA`, `NOM`), discordancias entre planos/memoria y errores de suma. |

---

## 📂 Estructura del Repositorio

```bash
├── SKILL.md                          # Instrucciones directrices para el agente/LLM
├── README.md
├── references/
│   ├── 01-protocolo-normativa.md     # Protocolo de verificación y etiquetado legal
│   ├── 02-mapa-normativo-espana.md   # Mapa índice de legislación estatal, autonómica y local
│   ├── 03-estructura-pliegos-y-ofertas.md # Estructuras tipo para PPT, Sobre B y PCAP
│   ├── 04-guia-memorias-paneles.md   # Redacción y síntesis de paneles de concurso A1/A0
│   └── 05-estilo-y-errores-frecuentes.md  # Registro técnico, glosario ES/CA y checklist
├── assets/
│   ├── plantilla-PPT.docx            # Base editable para PPT
│   ├── plantilla-oferta-tecnica.docx # Base editable para Sobre B
│   ├── plantilla-memoria-panel.docx  # Base editable para concursos
│   ├── ficha-verificacion-normativa.docx
│   └── plantilla-cuadro-superficies.csv
└── scripts/
    └── check_superficies.py          # Script de validación aritmética de superficies
