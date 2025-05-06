## Creen una clase MetodosOrdenamientos

class Metodo_ordenamiento:

    def metodo_burbuja(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
    
    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            condicion = False
            
            for j in range(i + 1, n-i-1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                    condicion = True
            
            if not condicion:
                break
        
        return arreglo

    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_idx]:
                    min_idx = j
            if min_idx != i:
                arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        return arreglo
    
    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo