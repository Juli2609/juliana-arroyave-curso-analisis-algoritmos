# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Juliana Arroyave Arango · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `ef877e7`

Excelente trabajo, Juliana: entrega completa, ordenada y con análisis apoyado en sus propios datos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **97 / 100** |
| **Nota (0–5)** | **4.85** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre n = 50 y n = 100, con su tabla, y explica por qué no gana desde el inicio (el costo fijo de las llamadas recursivas pesa más con pocos datos).
- Compara con el máximo de un arreglo: combinar cuesta O(1), la recurrencia da Θ(n) y dividir no aporta nada.
- Recomienda divide y vencerás y estima el tiempo a 1.000.000 de registros (unas 20 horas contra unos 11 segundos), declarándolo como estimación y explicando sus supuestos.

**Lo que puede mejorar:**
- Para la estimación, apoyarse en varios tamaños y no solo en n = 8000 haría la calibración más confiable.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término y la resuelve con el método maestro (caso 2, comparando `n^(log₂2) = n` con `f(n)`).
- Justifica el `Θ(n²)` de la fuerza bruta contando los n(n+1)/2 pares.

**Lo que puede mejorar:**
- Podría decir explícitamente que en el caso 2 se cumple `f(n) = Θ(n^(log_b a))`, como cierre de la verificación.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones están completas, con `type hints` y docstrings, y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- `pruebas.py` cubre todos los casos pedidos y 30 listas aleatorias; ninguna función modifica la lista recibida.

**Lo que puede mejorar:**
- En `medicion.py`, la función `medir` no tiene `type hints` en sus parámetros.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con ocho tamaños.
- Calcula el factor al duplicar n (3.84 para fuerza bruta y 2.11 para divide y vencerás entre 4000 y 8000) y lo contrasta con lo teórico; las cifras coinciden con la gráfica publicada.
- Reconoce y explica el salto atípico de 5.20.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas exacta, informe en el orden pedido, enlaces al código en cada parte, gráfica visible, instrucciones de reproducción y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones coinciden en listas aleatorias y `medicion.py` corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Agregue `type hints` a todos los parámetros, incluidos los de funciones auxiliares.
- Revise que cada función tenga docstring con Args y Returns y dos líneas en blanco entre funciones.
- Calibre las estimaciones con más de un tamaño medido.
