def heapify(arr, n, i):
    # Inicializa el elemento más grande como el nodo raíz
    largest = i
    left = 2 * i + 1     # Índice del hijo izquierdo
    right = 2 * i + 2    # Índice del hijo derecho

    # Si el hijo izquierdo existe y es mayor que la raíz actual
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho existe y es mayor que el elemento más grande actual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el elemento más grande no es la raíz, intercambia y aplica heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambia elementos
        heapify(arr, n, largest)  # Aplica heapify al nuevo subárbol

def heap_sort(arr):
    n = len(arr)

    # Construye el heap, reorganizando el arreglo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrae cada elemento del heap, uno por uno, y aplica heapify
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mueve el elemento raíz al final
        heapify(arr, i, 0)  # Aplica heapify al sub-arreglo reducido

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Lista ordenada:", arr)
