import random
import time
from metodos_ordenamientos import Metodo_ordenamiento


class Benchmarking:

    
    def __init__(self):
        print('Benchmarking instanciado')
    
    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio





    def metodo(self):
        self.mo = Metodo_ordenamiento()

        arreglo = self.build_arreglo(10000)

        tarea = lambda: self.mo.metodo_burbuja(arreglo)
        tarea2 = lambda: self.mo.sort_burbuja_mejorado_optimizado(arreglo)
        tarea3 = lambda: self.mo.sort_seleccion(arreglo)
        tarea4 = lambda: self.mo.sort_shell(arreglo)
        
        ##tiempoM = self.contar_con_current_time_milles(tarea)
        tiempoN = self.contar_con_nano_time(tarea)
        tiempoN2 = self.contar_con_nano_time(tarea2)
        tiempoN3 = self.contar_con_nano_time(tarea3)
        tiempo4 = self.contar_con_nano_time(tarea4)

        ##print(f'Tiempo con milisegundos: {tiempoM} \nTiempo en nanosegundos {tiempoN}')
        print(f'Tiempo en nanosegundos burbuja {tiempoN}')
        print(f'Tiempo en nanosegundos burbuja mejorado {tiempoN2}')
        print(f'Tiempo en nanosegundos seleccion {tiempoN3}')
        print(f'Tiempo en nano segundos shell {tiempo4}')

    def build_arreglo(self, tamano):
        arreglo =[]
        for i in range(tamano):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)


    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0
        

       