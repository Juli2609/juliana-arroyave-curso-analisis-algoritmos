# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Juliana Arroyave Arango · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `c3ac329`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 23 / 25 |
| Corrección de la implementación | 12 / 20 |
| Calidad del análisis de las gráficas | 14 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica que un servidor más rápido solo aplaza el problema porque el trabajo de insertion sort crece mucho más rápido que los datos.
- Su segundo ejemplo (seguimiento de equipos con 15.000 a 20.000 movimientos al mes y un correo que tardaba 20 minutos) es propio y tiene datos y restricción.
- En la Parte 2 relaciona tiempo de ejecución con consumo de energía repetido cada madrugada, nombra perjuicios al paciente y al operador del centro de contacto y dice quién asume el costo.

**Lo que puede mejorar:**
- Dice que el proceso actual tarda "cerca de 10 horas" sin explicar de dónde sale ese dato.
- La parte ambiental queda general: faltó un ejemplo con números (horas por día multiplicadas por años).

## 2. Calidad de la explicación teórica (23 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio indicando sobre qué entradas y con qué tamaño fijo, y justifica que usaría el peor caso por la ventana estricta.
- Dejó la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando la condición del caso 2.
- Hace el conteo línea a línea de insertion sort y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- En el conteo de insertion sort, algunas líneas se agruparon (por ejemplo 6, 7 y 8) y no se explica con calma cada una.

## 3. Corrección de la implementación (12 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista recibida y cuentan solo comparaciones entre elementos. El merge sort tiene su propia mezcla recursiva.
- Los generadores dan listas sin repetidos, con semilla, y el escenario B sí deja el 2 % desordenado al final.

**Lo que puede mejorar:**
- `generar_casi_ordenado` usa `sorted()`. La rúbrica prohíbe esa función en el código entregado; podía armar la parte ordenada con `range` en orden inverso.
- Faltan docstrings completos y tipos en `medir`, `medir_tiempo` y `main`, y `medir` tiene un `if/else` con las dos ramas iguales.
- Los cuatro archivos `.py` terminan sin salto de línea final (falla menor de PEP 8).

## 4. Calidad del análisis de las gráficas (14 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes con unidades y leyenda, y los escenarios van en los mismos ejes.
- Identifica con evidencia el peor caso (C), el mejor (B) y el promedio (A), y lo contrasta con su predicción.
- En 4.2 concluye que merge sort conviene y lo relaciona con Θ(n²) frente a Θ(n log n), explicando por qué merge sort pierde ventaja con tamaños pequeños.
- En 4.3 recomienda merge sort, responde a la propuesta del servidor con un dato medido (6.400 registros: 3,31 s contra 0,032 s) y habla de memoria extra y del riesgo del escenario B.

**Lo que puede mejorar:**
- La extrapolación a 1.200.000 registros no se muestra: dice que insertion sort tardaría unas 10 horas, pero no explica el cálculo. Con su propia medición de 6.400 registros y un crecimiento cuadrático, el resultado sería mucho mayor.
- Para merge sort no da ninguna cifra de tiempo estimado, solo dice que crece menos; debía decir si cabe en las cuatro horas.
- En 4.2 describa lo que hace cada curva con valores de la gráfica.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos coinciden con la estructura pedida; las gráficas se ven incrustadas con ruta relativa.
- Hay instrucciones de reproducción y enlaces al código en cada parte práctica.

**Lo que puede mejorar:**
- Solo hay un commit que toca el laboratorio, con todo junto; se piden al menos cinco commits descriptivos que muestren el avance.

## ¿El código funciona?
Sí. Los scripts corren sin errores, ordenan bien los tres escenarios y generan las gráficas.

## Para el próximo laboratorio
- Haga commits pequeños y frecuentes a medida que avanza (al menos uno por parte).
- Evite `sorted()` en cualquier parte del código, también en los generadores de datos.
- Muestre el cálculo de toda estimación: qué dato midió, por cuánto multiplica el tamaño y qué crecimiento supone.
- Complete docstrings y tipos en todas las funciones y termine los archivos con salto de línea.
- Respalde con cifras los datos que cita (como las 10 horas) y los argumentos de impacto ambiental.
