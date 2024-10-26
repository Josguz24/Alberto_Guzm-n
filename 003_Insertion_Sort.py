def insertion_sort(arr):
    # Recorre cada elemento en la lista, empezando por el segundo
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual a insertar en la posición correcta
        j = i - 1
        # Mueve los elementos de arr[0...i-1] que son mayores que "key" hacia la derecha
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Coloca "key" en su lugar correcto
        arr[j + 1] = key

# Ejemplo de uso
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Lista ordenada:", arr)
