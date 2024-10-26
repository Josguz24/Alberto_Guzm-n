def enumeration_sort(arr):
    n = len(arr)
    sorted_arr = [None] * n

    # Para cada elemento en arr, cuenta cuántos elementos son menores
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] < arr[i] or (arr[j] == arr[i] and j < i):
                count += 1
        # Coloca el elemento en su posición de acuerdo al conteo
        sorted_arr[count] = arr[i]

    return sorted_arr

# Ejemplo de uso
arr = [4, 3, 2, 1, 0]
sorted_arr = enumeration_sort(arr)
print("Lista ordenada con Algoritmos de Enumeración:", sorted_arr)
