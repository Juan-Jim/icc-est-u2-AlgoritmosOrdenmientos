import matplotlib.pyplot as plt
import benchmarking as bm
from metodos_ordenamientos import Metodo_ordenamiento

class Show_results:
    
    def __init__(self):
        self.bench = bm.Benchmarking()
        self.mO = Metodo_ordenamiento()
    
    def results(self):
        tamanios = [5000, 10000, 30000, 50000, 100000]
        tam_max = max(tamanios)
        arreglo_final = self.bench.build_arreglo(tam_max)
        resultado = []
    
        for tam in tamanios:
            arregglo_base = self.bench.build_arreglo(tam)
            ##arreglo_pruebas = self.eh.build_arreglo(tam)

            metodos = {
                "Bubble Sort": self.mO.metodo_burbuja,
                "Burbuja mejorado": self.mO.sort_burbuja_mejorado_optimizado,
                "Selection Sort": self.mO.sort_seleccion,
                "Insertion sort": self.mO.sort_insertion,
                "Shell Sort": self.mO.sort_shell
            }

            for nombre, metodo_type in metodos.items():
                tiempo_final = self.bench.medir_tiempo(metodo_type, arregglo_base.copy())
                bench_resultados = (tam, nombre, tiempo_final)
                resultado.append(bench_resultados)

        # Imprimir resultados
        for tam, nombre, time in resultado:
            print(f"Tamaño del arreglo: {tam}, Nombre: {nombre}, Tiempo: {time:.6f} segundos")
    
        # Organizar datos para gráficos
        tiempos_by_metodo = {
            "Bubble Sort": [],
            "Burbuja mejorado": [],
            "Selection Sort": [],
            "Insertion sort": [],
            "Shell Sort": []
        }

        for tam, nombre, tiempo in resultado:
            tiempos_by_metodo[nombre].append(tiempo)

        fig, axs = plt.subplots(6, 1, figsize=(10, 25))

        # comparacion general
        for nombre, tiempos in tiempos_by_metodo.items():
            axs[0].plot(tamanios, tiempos, label=nombre, marker="o")
        axs[0].set_title("Comparación de todos los métodos")
        axs[0].set_xlabel("Tamaño del arreglo")
        axs[0].set_ylabel("Tiempo (segundos)")
        axs[0].legend()
        axs[0].grid(True)

        #bucle que muestra las graficas individuales
        for i, (nombre, tiempos) in enumerate(tiempos_by_metodo.items(), start=1):
            axs[i].plot(tamanios, tiempos, marker="o", color="blue")
            axs[i].set_title(f"Tiempo de ejecución: {nombre}")
            axs[i].set_xlabel("Tamaño del arreglo")
            axs[i].set_ylabel("Tiempo (segundos)")
            axs[i].grid(True)

        plt.tight_layout()
        plt.show()

