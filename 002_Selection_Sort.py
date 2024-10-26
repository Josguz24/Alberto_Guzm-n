def selection_sort(arr):
    # Recorre todos los elementos de la lista
    for i in range(len(arr)):
        # Supone que el primer elemento no ordenado es el mínimo
        min_index = i
        # Recorre el resto de la lista para encontrar el índice del elemento mínimo
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambia el elemento mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Lista ordenada:", arr)
