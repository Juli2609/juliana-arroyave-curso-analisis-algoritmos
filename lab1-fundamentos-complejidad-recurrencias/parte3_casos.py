"""Medición experimental de insertion_sort sobre los tres escenarios de Tamiza (Parte 3)."""

import os
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

GENERADORES = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}


def medir(generador, n: int) -> tuple[float, int]:
    """Genera un lote de tamaño n y mide insertion_sort sobre él.

    Repite la medición REPETICIONES veces (usando la misma lista ya
    generada, sin volver a generarla) y devuelve el tiempo mediano y
    el número de comparaciones (que es determinístico para una misma
    entrada, así que es igual en todas las repeticiones).
    """
    # generar_inverso no acepta 'semilla'; los otros dos sí.
    if generador is generar_inverso:
        datos = generador(n)
    else:
        datos = generador(n)

    tiempos = []
    comparaciones = None
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comps = insertion_sort(datos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        comparaciones = comps  # es el mismo en todas las repeticiones

    return statistics.median(tiempos), comparaciones


def main() -> None:
    resultados: dict[str, dict[str, list]] = {
        nombre: {"n": [], "tiempo": [], "comparaciones": []}
        for nombre in GENERADORES
    }

    for nombre, generador in GENERADORES.items():
        for n in TAMANOS:
            tiempo_mediano, comparaciones = medir(generador, n)
            resultados[nombre]["n"].append(n)
            resultados[nombre]["tiempo"].append(tiempo_mediano)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(
                f"{nombre} | n={n:>5} | "
                f"tiempo={tiempo_mediano:.6f}s | comparaciones={comparaciones}"
            )

    os.makedirs("graficas", exist_ok=True)

    # Gráfica 1: comparaciones vs. tamaño de entrada
    plt.figure(figsize=(8, 5))
    for nombre, datos_escenario in resultados.items():
        plt.plot(datos_escenario["n"], datos_escenario["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion Sort: comparaciones vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n, número de registros)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Gráfica 2: tiempo vs. tamaño de entrada
    plt.figure(figsize=(8, 5))
    for nombre, datos_escenario in resultados.items():
        plt.plot(datos_escenario["n"], datos_escenario["tiempo"], marker="o", label=nombre)
    plt.title("Insertion Sort: tiempo de ejecución vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n, número de registros)")
    plt.ylabel("Tiempo de ejecución (segundos, mediana de 3 repeticiones)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()

    print("\nGráficas guardadas en graficas/parte3_comparaciones.png y graficas/parte3_tiempo.png")


if __name__ == "__main__":
    main()