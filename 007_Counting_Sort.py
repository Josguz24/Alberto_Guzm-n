def counting_sort(arr):
    # Encuentra el valor máximo en la lista para determinar el tamaño del arreglo de conteo
    max_val = max(arr)
    count = [0] * (max_val + 1)  # Crea una lista de conteo de tamaño max_val + 1

    # Cuenta la ocurrencia de cada elemento en la lista
    for num in arr:
        count[num] += 1

    # Reconstruye la lista ordenada usando el arreglo de conteo
    index = 0
    for num, freq in enumerate(count):  # num representa el valor, freq su frecuencia
        for _ in range(freq):
            arr[index] = num
            index += 1

# Ejemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Lista ordenada:", arr)
