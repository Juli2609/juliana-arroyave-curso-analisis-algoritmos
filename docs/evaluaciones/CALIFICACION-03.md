# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Juliana Arroyave Arango · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `96a63fe`

Muy buen trabajo: entregó todo completo, ordenado y con análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque haya más casillas que guías, usando el ejemplo de `10`, `24` y `17` con `m = 7`.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica con claridad por qué la tabla no sirve para rangos y estima la altura (cerca de 400.000) y las comparaciones del árbol degenerado frente al equilibrado (cerca de 19).
- Recomienda una combinación (tabla hash más árbol equilibrado) y declara que la cifra de 5.000.000 es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación para 5.000.000 de envíos da un tiempo para la lista, pero para la tabla solo dice "cerca de 1 µs" y para el árbol solo da el número de comparaciones, sin convertirlo en un tiempo.
  → *Cómo corregirlo:* para cada estructura, escriba un tiempo estimado y diga de qué dato medido o de qué forma de curva sale.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla, separando el costo fijo del recorrido.
- Nombra el supuesto de que la función hash reparte las guías de forma uniforme.
- Explica que, si todas caen en una casilla, la tabla se vuelve una lista de n nodos y el costo regresa a `Θ(n)`.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: las búsquedas exitosas e infructuosas devuelven lo correcto, la colisión con `m = 7` funciona y `factor_carga` da 3/7.
- La tabla reutiliza la lista en cada casilla y no usa `dict`, `set` ni `hash()`.
- Las pruebas cubren todo lo pedido, incluidas 25 colecciones aleatorias, y pasan.
- Las funciones de `estructuras.py` tienen docstrings con `Args` y `Returns` y type hints.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py`, la función `tiempo_medio_busqueda` no tiene type hint en el parámetro `estructura`.
  → *Cómo corregirlo:* anote el parámetro con un tipo que acepte ambas estructuras, por ejemplo `ListaEnlazada | TablaHash`.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda; la primera tiene siete valores de `n` con las dos curvas en los mismos ejes, y la segunda seis valores de `α`.
- Calcula factores de crecimiento de la lista con valores que coinciden con la gráfica publicada (por ejemplo, de 20.000 a 50.000 guías el tiempo pasa de cerca de 2.150 a cerca de 5.050 µs) y los compara con `Θ(n)`.
- Interpreta la gráfica del factor de carga y explica con prudencia el descenso en `α = 4`.

**Lo que puede mejorar (y cómo corregirlo):**
- Pide calcular cuánto se multiplicó el tiempo de cada estructura entre dos valores consecutivos de `n`, y para la tabla solo describe que "oscila" entre 0,4 y 1,1 µs.
  → *Cómo corregirlo:* tome dos valores consecutivos de `n` de su tabla y calcule también el cociente de los tiempos de la tabla; compárelo con el cociente de `n`.
- La explicación del salto entre 5.000 y 10.000 guías (efecto de caché) no está respaldada por ninguna medición suya.
  → *Cómo corregirlo:* preséntela como una posible causa, o repita esa medición varias veces y vea si el salto se mantiene.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura acordada (`lab3-estructuras-datos/` con los archivos y las dos gráficas) y entregó en `main`.
- El `README.md` tiene su nombre, las instrucciones de reproducción y las partes en orden; las imágenes se ven y cada parte práctica enlaza su código.
- Hay cuatro commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre completa y regenera las dos gráficas. Las estructuras responden igual y los tiempos muestran la misma forma que su informe.
