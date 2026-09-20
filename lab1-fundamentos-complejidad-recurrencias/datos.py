"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    indices = list(range(1, n + 1))
    rng.shuffle(indices)
    return indices


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    rng = random.Random(semilla)
    indices = list(range(1, n + 1))

    corte = int(n * 0.98)
    # El 98% inicial queda ordenado de mayor a menor (el orden que
    # insertion_sort debe producir); el 2% restante se anexa desordenado.
    parte_ordenada = sorted(indices[:corte], reverse=True)
    parte_desordenada = indices[corte:]
    rng.shuffle(parte_desordenada)

    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros, en el orden inverso al
        que el algoritmo debe producir (insertion_sort ordena de mayor
        a menor, por lo que este lote llega de menor a mayor).
    """
    return list(range(1, n + 1))