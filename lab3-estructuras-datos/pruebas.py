"""Pruebas de ListaEnlazada y TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash


def prueba_busqueda_basica() -> None:
    lista = ListaEnlazada()
    tabla = TablaHash(7)
    datos = {1000000010: "en bodega", 1000000024: "en reparto",
             1000000017: "en bodega", 1000000005: "entregado"}
    for guia, estado in datos.items():
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia, estado in datos.items():
        assert lista.buscar(guia) == estado      # exitosa
        assert tabla.buscar(guia) == estado
    assert lista.buscar(99) is None               # infructuosa
    assert tabla.buscar(99) is None


def prueba_colision_forzada() -> None:
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        assert guia % 7 == 3                      # las tres caen en la casilla 3
        tabla.insertar(guia, "en bodega")

    for guia in (10, 24, 17):
        assert tabla.buscar(guia) == "en bodega"
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7


def prueba_colecciones_aleatorias() -> None:
    azar = random.Random(42)
    for _ in range(25):                           # al menos 20
        n = azar.randint(1, 300)
        guias = azar.sample(range(10**9, 10**10), n)
        lista = ListaEnlazada()
        tabla = TablaHash(max(1, n // 2) | 1)
        for g in guias:
            estado = azar.choice(["en bodega", "en reparto", "entregado"])
            lista.insertar(g, estado)
            tabla.insertar(g, estado)

        for g in guias:                           # existentes
            assert lista.buscar(g) == tabla.buscar(g)
            assert lista.buscar(g) is not None
        existentes = set(guias)
        for _ in range(50):                       # inexistentes
            g = azar.randint(10**9, 10**10 - 1)
            if g not in existentes:
                assert lista.buscar(g) is None
                assert tabla.buscar(g) is None


if __name__ == "__main__":
    prueba_busqueda_basica()
    prueba_colision_forzada()
    prueba_colecciones_aleatorias()
    print("Todas las pruebas pasaron")