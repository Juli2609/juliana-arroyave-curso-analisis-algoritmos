def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = float("-inf")

    for i in range(len(valores)):
        suma = 0
        for j in range(i, len(valores)):
            suma += valores[j]
            if suma > mejor_suma:
                mejor_inicio = i
                mejor_fin = j
                mejor_suma = suma

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    # Barrido hacia la izquierda: el tramo debe terminar en "medio".
    mejor_izq = float("-inf")
    suma = 0
    inicio_mejor = medio
    for i in range(medio, inicio - 1, -1):
        suma += valores[i]
        if suma > mejor_izq:
            mejor_izq = suma
            inicio_mejor = i

    # Barrido hacia la derecha: el tramo debe empezar en "medio + 1".
    mejor_der = float("-inf")
    suma = 0
    fin_mejor = medio + 1
    for j in range(medio + 1, fin + 1):
        suma += valores[j]
        if suma > mejor_der:
            mejor_der = suma
            fin_mejor = j

    return inicio_mejor, fin_mejor, mejor_izq + mejor_der