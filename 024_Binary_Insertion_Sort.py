# Función para encontrar la posición usando búsqueda binaria
def binary_search(arr, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        # Encuentra la posición donde insertar el elemento
        pos = binary_search(arr, val, 0, i)
        # Desplaza los elementos y coloca el valor en su posición
        arr = arr[:pos] + [val] + arr[pos:i] + arr[i+1:]

# Ejemplo de uso
arr = [37, 23, 0, 17, 12, 72, 31]
binary_insertion_sort(arr)
print("Lista ordenada con Binary Insertion Sort:", arr)
