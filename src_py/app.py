# Archivo principal main
import matplotlib.pyplot as plt
import benchmarking as bm
from metodos_ordenamientos import Metodo_ordenamiento

if __name__ == "__main__":
    arreglo_pruebas = [4, 6, 2, 8, 3]
    bench = bm.Benchmarking()
    mO = Metodo_ordenamiento()

    tamanios = [5000, 10000, 30000, 50000, 100000]
    resultado = []
    
    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        metodos = {
            "Bubble Sort": mO.metodo_burbuja,
            "Burbuja mejorado": mO.sort_burbuja_mejorado_optimizado,
            "Selection Sort": mO.sort_seleccion,
            "Insertion sort": mO.sort_insertion,
            "Shell Sort": mO.sort_shell
        }

        for nombre, metodo_type in metodos.items():
            tiempo_final = bench.medir_tiempo(metodo_type, arreglo_base)

            bench_resultados = (tam, nombre, tiempo_final)
            resultado.append(bench_resultados)


    for tam, nombre, time in resultado:
        print(f"Tamanio del arreglo: {tam} nombre: {nombre} Tiempo{time:.6f} segundos")


    tiempos_by_metodo = {
        "Bubble Sort": [],
        "Burbuja mejorado": [],
        "Selection Sort": [],
        "Insertion sort": [],
        "Shell Sort": []
    }

    for tam, nombre, tiempo in resultado:
        tiempos_by_metodo[nombre].append(tiempo)
        
    plt.figure(figsize=(10,6))

    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label = nombre, marker = "o")

    #agregar parametros

    plt.title("Comparacion de tiempo prar cada metodo")     
    plt.xlabel("Tamanio de los arreglos")
    plt.ylabel("Tiempo de ejecucion")

    plt.legend()
    plt.show()