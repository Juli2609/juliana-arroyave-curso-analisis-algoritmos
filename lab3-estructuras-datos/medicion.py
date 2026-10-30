"""Mediciones de busqueda: lista enlazada frente a tabla hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

CARPETA_GRAFICAS = Path(__file__).parent / "graficas"
ESTADOS = ["en bodega", "en reparto", "entregado"]
BUSQUEDAS = 200
REPETICIONES = 3
SEMILLA_EXISTENTES = 42
SEMILLA_INEXISTENTES = 7


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias_existentes(n: int, semilla: int) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador.

    Returns:
        Lista de n enteros distintos de diez digitos.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo.

    Args:
        numero: entero a evaluar.

    Returns:
        True si es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor.

    Args:
        objetivo: valor alrededor del cual se busca.

    Returns:
        El primo mas cercano a `objetivo`.
    """
    distancia = 0
    while True:
        if es_primo(objetivo - distancia):
            return objetivo - distancia
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        distancia += 1


def construir_estructuras(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una lista y una tabla con las mismas guias.

    Args:
        guias: guias a insertar.
        m: numero de casillas de la tabla.

    Returns:
        La lista enlazada y la tabla hash ya pobladas.
    """
    azar = random.Random(SEMILLA_EXISTENTES)
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar_mismo_estado(
    lista: ListaEnlazada, tabla: TablaHash, guias: list[int]
) -> None:
    """Comprueba que lista y tabla devuelvan lo mismo en una muestra.

    Args:
        lista: lista enlazada poblada.
        tabla: tabla hash poblada con las mismas guias.
        guias: guias existentes de las que se toma la muestra.
    """
    muestra = guias[:200]
    for guia in muestra:
        assert lista.buscar(guia) == tabla.buscar(guia)
        assert lista.buscar(guia) is not None


def tiempo_medio_busqueda(estructura, guias: list[int]) -> float:
    """Mide el tiempo medio por busqueda, cronometrando solo las busquedas.

    Args:
        estructura: objeto con un metodo `buscar`.
        guias: guias a buscar.

    Returns:
        Tiempo medio por busqueda en segundos (promedio de las repeticiones).
    """
    promedios: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in guias:
            estructura.buscar(guia)
        fin = time.perf_counter()
        promedios.append((fin - inicio) / len(guias))
    return sum(promedios) / len(promedios)


def experimento_a() -> None:
    """Experimento A: tiempo de busqueda de la lista y la tabla frente a n."""
    valores_n = [100, 500, 1000, 5000, 10000, 20000, 50000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    print("Experimento A (busquedas de guias inexistentes)")
    print(f"{'n':>8} {'m':>8} {'lista (us)':>12} {'tabla (us)':>12}")
    for n in valores_n:
        m = primo_cercano(n // 2)
        guias = generar_guias_existentes(n, SEMILLA_EXISTENTES)
        lista, tabla = construir_estructuras(guias, m)
        verificar_mismo_estado(lista, tabla, guias)
        inexistentes = generar_guias_inexistentes(
            set(guias), BUSQUEDAS, SEMILLA_INEXISTENTES
        )
        t_lista = tiempo_medio_busqueda(lista, inexistentes) * 1e6
        t_tabla = tiempo_medio_busqueda(tabla, inexistentes) * 1e6
        tiempos_lista.append(t_lista)
        tiempos_tabla.append(t_tabla)
        print(f"{n:>8} {m:>8} {t_lista:>12.3f} {t_tabla:>12.3f}")

    plt.figure(figsize=(8, 5))
    plt.plot(valores_n, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(valores_n, tiempos_tabla, marker="s", label="Tabla hash")
    plt.title("Tiempo de busqueda: lista enlazada frente a tabla hash")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Experimento B: efecto del factor de carga en la tabla hash."""
    n = 20000
    alfas_objetivo = [0.25, 0.5, 1, 2, 4, 10]
    guias = generar_guias_existentes(n, SEMILLA_EXISTENTES)
    inexistentes = generar_guias_inexistentes(
        set(guias), BUSQUEDAS, SEMILLA_INEXISTENTES
    )
    alfas: list[float] = []
    tiempos: list[float] = []

    print("\nExperimento B (n = 20000, guias inexistentes)")
    print(f"{'m':>8} {'alfa':>8} {'tabla (us)':>12}")
    for alfa in alfas_objetivo:
        m = primo_cercano(round(n / alfa))
        _, tabla = construir_estructuras(guias, m)
        t_tabla = tiempo_medio_busqueda(tabla, inexistentes) * 1e6
        alfas.append(tabla.factor_carga())
        tiempos.append(t_tabla)
        print(f"{m:>8} {tabla.factor_carga():>8.2f} {t_tabla:>12.3f}")

    plt.figure(figsize=(8, 5))
    plt.plot(alfas, tiempos, marker="o", label="Tabla hash (n = 20000)")
    plt.title("Tiempo de busqueda en la tabla hash frente al factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    experimento_a()
    experimento_b()
    print("\nGraficas guardadas en la carpeta graficas/")