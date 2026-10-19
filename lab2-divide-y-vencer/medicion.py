"""Medicion del tiempo de ejecucion: fuerza bruta vs divide y venceras."""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 42
RUTA_GRAFICA = Path(__file__).parent / "graficas" / "tiempo_vs_n.png"


def medir(funcion, *args) -> float:
    """Mide en milisegundos una sola llamada a la funcion.

    Args:
        funcion: funcion a cronometrar.
        *args: argumentos con los que se llama.

    Returns:
        Tiempo transcurrido en milisegundos.
    """
    inicio = time.perf_counter()
    funcion(*args)
    fin = time.perf_counter()
    return (fin - inicio) * 1000


def main() -> None:
    """Corre el experimento, imprime la tabla y guarda la grafica."""
    random.seed(SEMILLA)
    tiempos_bruta = []
    tiempos_dyv = []

    print(f"{'n':>6} {'bruta (ms)':>12} {'dyv (ms)':>12}")
    for n in TAMANOS:
        # La misma lista para ambos algoritmos; se genera fuera del cronometro.
        datos = [random.randint(-100, 100) for _ in range(n)]

        # Verificacion: ambos deben devolver la misma suma.
        suma_bruta = subarreglo_fuerza_bruta(datos)[2]
        suma_dyv = subarreglo_maximo(datos, 0, n - 1)[2]
        assert suma_bruta == suma_dyv, f"Difieren sumas para n={n}"

        # Mediana de varias repeticiones para reducir el ruido del sistema.
        t_bruta = statistics.median(
            medir(subarreglo_fuerza_bruta, datos) for _ in range(REPETICIONES)
        )
        t_dyv = statistics.median(
            medir(subarreglo_maximo, datos, 0, n - 1)
            for _ in range(REPETICIONES)
        )
        tiempos_bruta.append(t_bruta)
        tiempos_dyv.append(t_dyv)
        print(f"{n:>6} {t_bruta:>12.3f} {t_dyv:>12.3f}")

    plt.figure(figsize=(8, 5))
    plt.plot(TAMANOS, tiempos_bruta, marker="o", label="Fuerza bruta")
    plt.plot(TAMANOS, tiempos_dyv, marker="s", label="Divide y venceras")
    plt.title("Tiempo de ejecucion vs tamano de entrada")
    plt.xlabel("Tamano de entrada n (numero de dias)")
    plt.ylabel("Tiempo de ejecucion (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICA, dpi=150)
    print(f"Grafica guardada en {RUTA_GRAFICA}")


if __name__ == "__main__":
    main()