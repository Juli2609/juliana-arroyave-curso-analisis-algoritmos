"""Medición comparativa entre insertion_sort y merge_sort sobre el escenario A (Parte 4)."""

import os
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ALGORITMOS = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}


def medir_tiempo(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo mediano de REPETICIONES ejecuciones del algoritmo sobre 'datos'."""
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(datos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return statistics.median(tiempos)


def main() -> None:
    resultados: dict[str, dict[str, list]] = {
        nombre: {"n": [], "tiempo": []} for nombre in ALGORITMOS
    }

    for n in TAMANOS:
        # Mismo lote (escenario A) para ambos algoritmos, generado una sola vez por n.
        datos = generar_aleatorio(n)
        for nombre, algoritmo in ALGORITMOS.items():
            tiempo_mediano = medir_tiempo(algoritmo, datos)
            resultados[nombre]["n"].append(n)
            resultados[nombre]["tiempo"].append(tiempo_mediano)
            print(f"{nombre:15s} | n={n:>5} | tiempo={tiempo_mediano:.6f}s")

    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(8, 5))
    for nombre, datos_algoritmo in resultados.items():
        plt.plot(datos_algoritmo["n"], datos_algoritmo["tiempo"], marker="o", label=nombre)
    plt.title("Insertion Sort vs. Merge Sort: tiempo de ejecución (escenario A - aleatorio)")
    plt.xlabel("Tamaño de entrada (n, número de registros)")
    plt.ylabel("Tiempo de ejecución (segundos, mediana de 3 repeticiones)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()

    print("\nGráfica guardada en graficas/parte4_tiempo.png")


if __name__ == "__main__":
    main()