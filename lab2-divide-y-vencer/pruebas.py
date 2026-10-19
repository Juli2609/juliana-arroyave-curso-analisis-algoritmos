"""Pruebas del subarreglo maximo: fuerza bruta vs divide y venceras."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def maximo(valores):
    """Atajo: corre divide y venceras sobre toda la lista."""
    return subarreglo_maximo(valores, 0, len(valores) - 1)


# 1. Serie de ocho dias de la situacion problema (suma 17).
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert maximo(serie)[2] == 17

# 2. Un solo elemento.
assert subarreglo_fuerza_bruta([7])[2] == 7
assert maximo([7])[2] == 7

# 3. Todos los valores negativos (gana el menos negativo).
negativos = [-5, -2, -9]
assert subarreglo_fuerza_bruta(negativos)[2] == -2
assert maximo(negativos)[2] == -2

# 4. Todos los valores positivos (gana la lista completa).
positivos = [4, 1, 6, 3]
assert subarreglo_fuerza_bruta(positivos)[2] == 14
assert maximo(positivos)[2] == 14

# 5. El mejor tramo cruza el punto medio.
cruce = [-2, 3, 4, 5, 6, -1]
assert subarreglo_fuerza_bruta(cruce)[2] == 18
assert maximo(cruce)[2] == 18
assert maximo(cruce)[:2] == (1, 4)  # aqui no hay empates, los indices son unicos

# 6. suma_cruzada por separado, sobre el mismo caso.
from subarreglo import suma_cruzada

assert suma_cruzada(cruce, 0, 2, 5) == (1, 4, 18)

# 7. Ninguna funcion modifica la lista recibida.
copia = list(serie)
subarreglo_fuerza_bruta(serie)
maximo(serie)
assert serie == copia

# 8. Listas aleatorias: ambas funciones deben dar la misma suma.
random.seed(42)
for _ in range(30):
    n = random.randint(1, 40)
    datos = [random.randint(-100, 100) for _ in range(n)]
    suma_bruta = subarreglo_fuerza_bruta(datos)[2]
    suma_dyv = maximo(datos)[2]
    assert suma_bruta == suma_dyv, f"Difieren en {datos}"

print("Todas las pruebas pasaron")