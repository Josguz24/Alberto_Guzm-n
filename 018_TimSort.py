MIN_RUN = 32

def insertion_sort(arr, left, right):
    """Ordena un sub-arreglo usando Insertion Sort."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    """Combina dos sub-arreglos ordenados en uno solo ordenado."""
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    # Combina los elementos de ambas mitades en orden ascendente
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Agrega los elementos restantes de la mitad izquierda
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Agrega los elementos restantes de la mitad derecha
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    """Ordena un arreglo usando el algoritmo TimSort."""
    n = len(arr)
    
    # Ordena cada "run" usando Insertion Sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Combina los "runs" ordenados usando Merge Sort
    size = MIN_RUN
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

# Ejemplo de uso
arr = [5, 21, 7, 23, 19, 10, 1, 3, 2, 8, 6, 4, 12, 15]
tim_sort(arr)
print("Arreglo ordenado:", arr)
