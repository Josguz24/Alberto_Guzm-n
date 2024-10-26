def merge_sort_in_place(arr, start, end):
    # Divide el arreglo recursivamente en mitades hasta llegar a subarreglos de un solo elemento
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort_in_place(arr, start, mid)  # Ordena la mitad izquierda
        merge_sort_in_place(arr, mid, end)    # Ordena la mitad derecha
        merge_in_place(arr, start, mid, end)  # Combina ambas mitades ordenadas

def merge_in_place(arr, start, mid, end):
    # Divide el arreglo en dos subarreglos temporales
    left = arr[start:mid]
    right = arr[mid:end]
    
    i = j = 0  # Índices para recorrer los subarreglos izquierdo y derecho
    k = start  # Índice para la posición en el arreglo original
    
    # Combina ambas mitades en orden ascendente en el arreglo original
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Si quedan elementos en el subarreglo izquierdo, agrégalos al arreglo original
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Si quedan elementos en el subarreglo derecho, agrégalos al arreglo original
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_in_place(arr, 0, len(arr))
print("Arreglo ordenado:", arr)
