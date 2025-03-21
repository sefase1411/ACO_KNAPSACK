# ACO Knapsack Problem Solver

Este proyecto implementa un algoritmo de Optimización por Colonia de Hormigas (ACO) para resolver el problema de la mochila.

## Descripción
El problema de la mochila consiste en seleccionar un subconjunto de objetos con beneficios y pesos conocidos, de manera que el beneficio total se maximice sin superar la capacidad de la mochila.

El algoritmo ACO simula el comportamiento colectivo de hormigas para explorar soluciones, actualizando caminos mediante feromonas y heurísticas.

## Características
- Lectura dinámica de instancias desde archivos `.txt`.
- Visualización de la estructura de datos (capacidad, pesos, beneficios, y ratios).
- Construcción probabilística de soluciones usando parámetros:
  - Alpha (α): Influencia de las feromonas.
  - Beta (β): Influencia del beneficio/peso (heurística).
  - Rho (ρ): Tasa de evaporación.
  - Q: Intensidad de feromonas depositadas.
- Evaluación de soluciones con actualización global de feromonas.
- Registro de la mejor solución por iteración.

## Estructura del proyecto
```
ACO_KNAPSACK/
│
├─ p05_c.txt   # Capacidad
├─ p05_p.txt   # Beneficios
├─ p05_w.txt   # Pesos
├─ p05_s.txt   # Solución óptima (para validación)
├─ read.py     # Módulo para leer y mostrar las instancias
├─ AcoKnapsack.py  # Algoritmo ACO para el problema de la mochila
```

## Ejecución
1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/ACO_Knapsack.git
cd ACO_Knapsack
```

2. Instalar librerias.

3. Ejecutar el archivo principal:
```bash
python AcoKnapsack.py
```

4. Ingresar el nombre base de la instancia cuando se solicite (ejemplo: `p05`).

## Ejemplo de salida
```
Ingrese el nombre base de la instancia (ejemplo: p05): p05

=== Estructura de la instancia cargada ===
Capacidad de la mochila: 104
Cantidad de objetos: 8
...
Iteración 1: Nueva mejor solución con beneficio 900

Mejor solución encontrada:
Ítems seleccionados: [0, 2, 4, 3, 6, 7]
Beneficio total: 900
Peso total: 104 de capacidad 104
```

