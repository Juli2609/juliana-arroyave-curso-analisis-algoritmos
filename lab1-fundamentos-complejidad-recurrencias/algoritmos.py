"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.
    Ordena de mayor a menor indice de riesgo (mayor riesgo primero).

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # Se desplaza 'actual' hacia atras mientras sea mayor que
        # el elemento anterior (orden de mayor a menor).
        while j >= 0:
            comparaciones += 1
            if lista[j] < actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = actual

    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.
    Ordena de mayor a menor indice de riesgo (mayor riesgo primero).

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante la mezcla.
    """

    def _merge_sort(sublista: list[int]) -> tuple[list[int], int]:
        if len(sublista) <= 1:
            return sublista, 0

        medio = len(sublista) // 2
        izquierda, comps_izq = _merge_sort(sublista[:medio])
        derecha, comps_der = _merge_sort(sublista[medio:])
        combinada, comps_merge = _merge(izquierda, derecha)

        return combinada, comps_izq + comps_der + comps_merge

    def _merge(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
        resultado = []
        comparaciones = 0
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            comparaciones += 1
            if izquierda[i] >= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        # Uno de los dos ya se agotó; el resto se copia sin comparar.
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado, comparaciones

    lista_ordenada, comparaciones = _merge_sort(datos.copy())
    return lista_ordenada, comparaciones