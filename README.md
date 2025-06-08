# Algoritmos de Búsqueda y Ordenamiento
## Trabajo Práctico Integrador - Programación I

### **Información del Proyecto**
- **Materia:** Programación I
- **Carrera:** Tecnicatura Universitaria en Programación
- **Modalidad:** A Distancia
- **Fecha de Entrega:** Junio 2025

---
## **Equipo de Desarrollo**

**Integrantes:**
- Lara Malena Pérez Hernández – larahernandez.edu@gmail.com
- Kevin Antonio Pelaez Dioses – pelaezkevin@hotmail.com

**Profesor:** Nicolás Quirós
**Tutora:** Carla Bustos
**Institución:** UTN - Universidad Tecnológica Nacional

---

##  **Objetivo del Proyecto**

Este trabajo presenta una investigación práctica y aplicada sobre algoritmos fundamentales de búsqueda y ordenamiento en Python, comparando su eficiencia y analizando su comportamiento con diferentes volúmenes de datos.

### **Algoritmos Implementados:**
- **Ordenamiento:** Bubble Sort vs Quick Sort
- **Búsqueda:** Búsqueda Lineal vs Búsqueda Binaria

---

## **Cómo Ejecutar el Programa**

### **Prerequisitos:**
- Python 3.6 o superior
- No requiere librerías externas

### **Ejecución:**
```bash
# Clonar o descargar el repositorio
git clone [URL_DEL_REPOSITORIO]

# Navegar al directorio
cd algoritmos-busqueda-ordenamiento

# Ejecutar el programa principal
python tp_integrador_p1.py
```

---

## **Funcionalidades del Programa**

### **1. Demostración con Datos Pequeños**
- Lista de ejemplo: `[64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]`
- Comparación visual de resultados
- Medición de tiempos de ejecución

### **2. Análisis con Grandes Volúmenes de Datos**
- Prueba con 20,000 elementos aleatorios
- Comparación de rendimiento escalable
- Cálculo de ratios de eficiencia

### **3. Algoritmos de Ordenamiento**

#### **Bubble Sort**
- **Complejidad:** O(n²)
- **Tipo:** Ordenamiento in-place (en el propio vector)
- **Ventajas:** Simple de implementar
- **Desventajas:** Ineficiente para grandes datasets

#### **Quick Sort**
- **Complejidad:** O(n log n) promedio
- **Tipo:** Divide y vencerás
- **Ventajas:** Muy eficiente en la práctica
- **Desventajas:** Puede degradarse a O(n²) en peor caso

### **4. Algoritmos de Búsqueda**

#### **Búsqueda Lineal**
- **Complejidad:** O(n)
- **Ventajas:** Funciona en cualquier lista
- **Desventajas:** Muy lenta para grandes volúmenes

#### **Búsqueda Binaria**
- **Complejidad:** O(log n)
- **Ventajas:** Extremadamente eficiente
- **Desventajas:** Requiere lista previamente ordenada

---

## **Resultados Esperados**

### **Rendimiento con 20,000 elementos:**
| Algoritmo | Tiempo Aproximado | Eficiencia |
|-----------|------------------|------------|
| Bubble Sort | ~15-30 segundos | Baja |
| Quick Sort | ~0.01-0.05 segundos | Alta |
| Búsqueda Lineal | ~0.001 segundos | Media |
| Búsqueda Binaria | ~0.0001 segundos | Muy Alta |

### **Ratios de Mejora:**
- Quick Sort es **~500-1000x más rápido** que Bubble Sort
- Búsqueda Binaria es **~10-100x más rápida** que Búsqueda Lineal

---

## **Análisis de Código**

### **Funciones Principales:**

```python
def bubble_sort(arr):          # Ordenamiento burbuja
def quick_sort(arr):           # Ordenamiento rápido
def busqueda_lineal(lista, objetivo):    # Búsqueda secuencial
def busqueda_binaria(lista, objetivo):   # Búsqueda dicotómica
```

