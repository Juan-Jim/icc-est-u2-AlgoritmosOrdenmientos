# Archivo principal main
import benchmarking as bm
##from benchmarking import Benchmarking
from metodos_ordenamientos import Metodo_ordenamiento

if __name__ == "__main__":
    mO = Metodo_ordenamiento

    tamanos = list[int]
    max_tamano = 50000
    
    self.arreglo_base: list[int] = []
    self.algoritmos: metodos[str, Callable] = {
        "Bubble Sort": mO.metodo_burbuja,
        "Burbuja mejorado": mO.sort_burbuja_mejorado_optimizado,
        "Selection Sort": mO.sort_seleccion,
        "Shell Sort": mO.sort_shell
    }
