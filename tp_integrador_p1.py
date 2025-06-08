import time
import random

# Funciones de Ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Funciones de Busqueda
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda = 0 
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1



print("ALGORITMOS DE BÚSQUEDA Y ORDENAMIENTO")

# Ejemplo práctico con datos pequeños
print("\nDEMOSTRACIÓN CON DATOS DE EJEMPLO")

print("\nPrueba con poca cantidad de datos")

datos_ejemplo = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
print(f"Datos originales: {datos_ejemplo}")


# Demostrar ordenamiento
print("\nORDENAMIENTO:")

vector_bubble = datos_ejemplo.copy()

# Se empieza a medir el tiempo de ejecion del ordenamiento bubble sort
inicio_bubble = time.time() 
bubble_sort(vector_bubble)
fin_bubble = time.time()
# Fin a la toma del tiempo

print(f"Bubble Sort: {vector_bubble}")

vector_quick = datos_ejemplo.copy()

# Se empieza a medir el tiempo de ejecion del ordenamiento quick sort
inicio_quick = time.time()
vector_quick = quick_sort(vector_quick)
fin_quick = time.time()
# Fin a la toma del tiempo

print(f"Quick Sort:  {vector_quick}")

# Comparativa de tiempos de Ordenamiento
print("\n=====Comparativa de tiempo entre algoritmos de Ordenamiento=====")
print(f"Tiempo de Bubble Sort: {fin_bubble-inicio_bubble:.6f} segundos")
print(f"Tiempo de Quick Sort: {fin_quick-inicio_quick:.6f} segundos")


# Demostrar búsqueda
print("\nBÚSQUEDA (buscando el número 76):")
inicio_lineal = time.time()
posicion_lineal = busqueda_lineal(vector_quick, 76)
fin_lineal = time.time()

if posicion_lineal != -1:
    print(f"Búsqueda Lineal: Se encontró el valor buscado en la posición: {posicion_lineal}")
else:
    print("Búsqueda Lineal: No se encontró el valor buscado")

# El vector tiene que estar ordenado, usaremos uno de los ordenados que tenemos
inicio_binaria = time.time()
posicion_binaria = busqueda_binaria(vector_quick, 76)
fin_binaria = time.time()

if posicion_binaria != -1:
    print(f"Búsqueda Binaria: Se encotró el valor buscado en la posición {posicion_binaria}")
else:
    print("Búsqueda Binaria: No se encontró el valor buscado")

# Comparativa de tiempos de Busqueda
print("\n=====Comparativa de tiempo entre algoritmos de Busqueda=====")
print(f"Tiempo de Busqueda Lineal: {fin_lineal-inicio_lineal:.10f} segundos")
print(f"Tiempo de Busqueda Binaria: {fin_binaria-inicio_binaria:.10f} segundos")

cantidad_elementos = 20000
print(f"\n\n=====Prueba para {cantidad_elementos} elementos=====")
lista_larga = random.sample(range(1,10000000), cantidad_elementos)

valor_buscado = random.choice(lista_larga)


# Demostrar ordenamiento
print("\nORDENAMIENTO:")

vector2_bubble = lista_larga.copy()

# Se empieza a medir el tiempo de ejecion del ordenamiento bubble sort
inicio2_bubble = time.time() 
bubble_sort(vector2_bubble)
fin2_bubble = time.time()
# Fin a la toma del tiempo

vector2_quick = lista_larga.copy()

# Se empieza a medir el tiempo de ejecion del ordenamiento quick sort
inicio2_quick = time.time()
vector2_quick = quick_sort(vector2_quick)
fin2_quick = time.time()
# Fin a la toma del tiempo

print("Se decide no imprimir las listas ordenadas debido a la cantidad de datos")

# Comparativa de tiempos de Ordenamiento
print("\n=====Comparativa de tiempo entre algoritmos de Ordenamiento (con grandes datos)=====")
print(f"Tiempo de Bubble Sort: {fin2_bubble-inicio2_bubble:.6f} segundos")
print(f"Tiempo de Quick Sort: {fin2_quick-inicio2_quick:.6f} segundos")


# Demostrar búsqueda
print(f"\nBÚSQUEDA (buscando el número: {valor_buscado}):")
inicio2_lineal = time.time()
posicion2_lineal = busqueda_lineal(vector2_quick, valor_buscado)
fin2_lineal = time.time()

if posicion2_lineal != -1:
    print(f"Búsqueda Lineal: Se encontró el valor buscado en la posición: {posicion2_lineal}")
else:
    print("Búsqueda Lineal: No se encontró el valor buscado")

# El vector tiene que estar ordenado, usaremos uno de los ordenados que tenemos
inicio2_binaria = time.time()
posicion2_binaria = busqueda_binaria(vector2_quick, valor_buscado)
fin2_binaria = time.time()

if posicion2_binaria != -1:
    print(f"Búsqueda Binaria: Se encotró el valor buscado en la posición {posicion2_binaria}")
else:
    print("Búsqueda Binaria: No se encontró el valor buscado")

# Comparativa de tiempos de Busqueda
print("\n=====Comparativa de tiempo entre algoritmos de Busqueda=====")
print(f"Tiempo de Busqueda Lineal: {fin2_lineal-inicio2_lineal:.6f} segundos")
print(f"Tiempo de Busqueda Binaria: {fin2_binaria-inicio2_binaria:.6f} segundos")


# Conclusiones
print("\nCONCLUSIONES DEL ANÁLISIS")
print("-" * 40)
print("ORDENAMIENTO:")
print("Bubble Sort: O(n²) - Lento para grandes datasets, fácil de implementar")
print("Quick Sort: O(n log n) - Mucho más eficiente, algoritmo divide y vencerás")
print("\nBÚSQUEDA:")
print("Búsqueda Lineal: O(n) - Funciona en cualquier lista, pero lenta")
print("Búsqueda Binaria: O(log n) - Muy eficiente, pero requiere datos ordenados")
print("\n\n")
print(f"Quick Sort es ~{(fin2_bubble-inicio2_bubble)/(fin2_quick-inicio2_quick):.3f}x más rápido que Bubble Sort")
print(f"Búsqueda Binaria usa ~{(fin2_lineal-inicio2_lineal)/(fin2_binaria-inicio2_binaria):.3f}x mas rápida que Búsqueda Lineal")
print()