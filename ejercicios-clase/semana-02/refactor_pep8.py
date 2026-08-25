def calcular_promedio(lista: list[float]) -> float:
    """
    Calcula el promedio (media aritmética) de una lista de números.

    Parámetros:
        lista (list[float]): Lista de números (enteros o flotantes)
            de la cual se calculará el promedio.

    Retorna:
        float: El promedio de los elementos de la lista.
    """
    suma = 0
    for x in lista:
        suma = suma + x
    return suma / len(lista)


def main() -> None:
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))


if __name__ == "__main__":
    main()