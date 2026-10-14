#!/usr/bin/env python3
"""Comprueba que un cuadro de superficies cuadra.

Entrada: CSV con cabecera. Columnas:
  grupo,espacio,programa,propuesta
y filas especiales (columna 'grupo' con estas palabras clave, sin distinguir mayusculas):
  SUBTOTAL:<nombre del grupo>   -> subtotal declarado de ese grupo
  TOTAL_UTIL_ESPACIOS           -> total declarado de la suma de grupos de espacios
  CIRCULACIONES                 -> total de circulaciones declarado
  CONEXION                      -> conexion entre edificios u otros computables
  TOTAL_UTIL                    -> total util declarado (espacios + circulaciones + conexion)
  TOTAL_CONSTRUIDA              -> total construido declarado
  CONSTRUIDA:<nombre>           -> partes que suman la superficie construida (p. ej. planta baja)

Los numeros pueden usar coma o punto decimal. Las celdas vacias o '-' se ignoran.
Uso:
  python check_superficies.py cuadro.csv [--tol 0.5]
Salida: informe de coincidencias y diferencias. Codigo de salida 1 si hay diferencias.
"""
import argparse
import csv
import sys


def num(value):
    if value is None:
        return None
    v = str(value).strip().replace("\u00a0", "").replace(" ", "")
    if v in ("", "-", "—", "n/a", "N/A"):
        return None
    # 1.234,5 -> 1234.5 ; 1,5 -> 1.5 ; 1.5 -> 1.5
    if "," in v and "." in v:
        v = v.replace(".", "").replace(",", ".")
    elif "," in v:
        v = v.replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path")
    ap.add_argument("--tol", type=float, default=0.5, help="tolerancia en m2 (por defecto 0,5)")
    args = ap.parse_args()

    groups = {}            # grupo -> {"programa": suma, "propuesta": suma}
    declared = {}          # clave -> {"programa": v, "propuesta": v}
    construida_parts = []  # partes de superficie construida

    with open(args.csv_path, newline="", encoding="utf-8-sig") as fh:
        sample = fh.read(2048)
        fh.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t") if sample else csv.excel
        reader = csv.DictReader(fh, dialect=dialect)
        required = {"grupo", "espacio", "programa", "propuesta"}
        if not reader.fieldnames or not required.issubset({f.strip().lower() for f in reader.fieldnames}):
            print("ERROR: la cabecera debe contener: grupo, espacio, programa, propuesta", file=sys.stderr)
            return 2
        for raw in reader:
            row = {k.strip().lower(): v for k, v in raw.items()}
            grupo = (row.get("grupo") or "").strip()
            espacio = (row.get("espacio") or "").strip()
            prog, prop = num(row.get("programa")), num(row.get("propuesta"))
            key = grupo.upper()
            if key.startswith("SUBTOTAL:"):
                declared[("SUBTOTAL", grupo.split(":", 1)[1].strip())] = {"programa": prog, "propuesta": prop}
            elif key.startswith("CONSTRUIDA:"):
                construida_parts.append((grupo.split(":", 1)[1].strip(), prop))
            elif key in ("TOTAL_UTIL_ESPACIOS", "CIRCULACIONES", "CONEXION", "TOTAL_UTIL", "TOTAL_CONSTRUIDA"):
                declared[(key, "")] = {"programa": prog, "propuesta": prop}
            elif grupo:
                g = groups.setdefault(grupo, {"programa": 0.0, "propuesta": 0.0})
                if prog is not None:
                    g["programa"] += prog
                if prop is not None:
                    g["propuesta"] += prop

    problems = 0

    def check(label, calc, decl):
        nonlocal problems
        if decl is None:
            return
        diff = round(decl - calc, 2)
        ok = abs(diff) <= args.tol
        mark = "OK " if ok else "DIF"
        if not ok:
            problems += 1
        print(f"[{mark}] {label}: calculado {calc:.2f} | declarado {decl:.2f} | diferencia {diff:+.2f}")

    print("== Subtotales por grupo ==")
    for g, vals in groups.items():
        d = declared.get(("SUBTOTAL", g), {})
        check(f"{g} (programa)", vals["programa"], d.get("programa"))
        check(f"{g} (propuesta)", vals["propuesta"], d.get("propuesta"))

    for col in ("programa", "propuesta"):
        espacios = sum(v[col] for v in groups.values())
        print(f"\n== Totales ({col}) ==")
        d_esp = declared.get(("TOTAL_UTIL_ESPACIOS", ""), {}).get(col)
        check("Total util de espacios", espacios, d_esp)
        circ = declared.get(("CIRCULACIONES", ""), {}).get(col) or 0.0
        con = declared.get(("CONEXION", ""), {}).get(col) or 0.0
        base = d_esp if d_esp is not None else espacios
        check("Total util (espacios + circulaciones + conexion)", base + circ + con,
              declared.get(("TOTAL_UTIL", ""), {}).get(col))

    if construida_parts:
        print("\n== Superficie construida (propuesta) ==")
        suma = sum(v for _, v in construida_parts if v is not None)
        check("Suma de partes construidas", suma, declared.get(("TOTAL_CONSTRUIDA", ""), {}).get("propuesta"))

    # Desviacion programa vs propuesta (informativo)
    print("\n== Desviacion programa -> propuesta (informativo) ==")
    for g, v in groups.items():
        if v["programa"]:
            pct = (v["propuesta"] - v["programa"]) / v["programa"] * 100
            print(f"  {g}: programa {v['programa']:.2f} | propuesta {v['propuesta']:.2f} | {pct:+.1f} %")

    print(f"\nResultado: {'sin diferencias' if problems == 0 else str(problems) + ' diferencia(s) a revisar'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
