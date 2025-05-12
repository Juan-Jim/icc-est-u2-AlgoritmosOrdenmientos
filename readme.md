# Algoritmos de ordenamientos

 ## Datos
 
 - Estudiantes: Juan Jimenez, Cristopher Salinas
 - Materia: Estructura de Datos
 - Docente: Ing. Pablo Torres

## Descripcion del proyecto

    - En este proyecte realizaremos varias comparaciones sobre diferentes metodos ordenamientos con distintos tamaños de arreglos pra verificar cual es el mas optimo en situaciones de arreglos grandes o pequeños.

## Capturas de pantalla

A continuación se presentan las capturas de pantalla de la ejecución en consola:

![alt text](imagen23.png)

![alt text](image-1.png)

--- 

## Tabla de resultados

| Tamaño   | Bubble | Bubble Mejorado | Selección | Inserción | Shell |
|----------|--------|-----------------|-----------|-----------|-------|
| 5000     | 1.447  | 1.211           | 0.831     | 0.815     | 0.015 |
| 10000    | 4.701  | 6.048           | 4.864     | 4.745     | 0.062 |
| 30000    | 43.760 | 33.994          | 24.547    | 23.479    | 0.133 |
| 50000    | 95.808 | 89.624          | 75.267    | 110.483   | 0.420 |
| 100000   | 693.258| 534.441         | 1422.77   | 357.82    | 0.848 |

Resultado del tiempo demora en los diferentes arreglos

---

## Gráfica comparativa

![alt text](imagen21.png)

---

##  CONCLUCIONES CON TERMINOLOGIA DE NOTACION 

    - Los algoritmos Bubble Sort, Burbuja mejorado, Selection Sort e Insertion Sort presentan un crecimiento exponencial del tiempo conforme aumenta el tamaño del arreglo, lo que refleja su complejidad temporal cuadrática O(n²).

    - En contraste, Shell Sort mantiene un tiempo de ejecución consistentemente bajo, incluso con entradas de hasta 100,000 elementos, lo que demuestra un comportamiento mucho más eficiente, cercano a O(n log n) en promedio.

    - Bubble Sort toma más de 11 minutos (693 s) para ordenar 100,000 elementos, mientras que Shell Sort lo hace en menos de 1 segundo (0.85 s), lo que representa una diferencia de más de 800 veces en velocidad.

    - Insertion Sort supera incluso a Selection en ciertos casos pequeños, pero sufre mucho en tamaños grandes.

    - Burbuja mejorado es más rápido que Bubble clásico, especialmente con tamaños medianos (p. ej. en 30,000 elementos baja de 43.76 s a 33.99 s), pero sigue siendo impráctico para tamaños grandes.

    - Shell Sort es el único algoritmo probado que escala eficientemente. Su tiempo crece de 0.015 s (5,000) a solo 0.85 s (100,000), lo que sugiere que maneja grandes volúmenes con bajo costo computacional.

    - Para conjuntos de datos grandes, los algoritmos Shell Sort, Merge Sort o QuickSort deben ser preferidos sobre los métodos educativos como Bubble o Insertion, que solo son adecuados para fines didácticos o conjuntos muy pequeños.


