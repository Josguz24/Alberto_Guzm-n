def hashing_sort(arr):
    # Encuentra el valor máximo y mínimo para definir el rango de las cubetas
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) // len(arr) + 1

    # Crea las cubetas
    buckets = [[] for _ in range(bucket_range)]

    # Distribuye los elementos en las cubetas
    for num in arr:
        index = (num - min_val) // len(arr)
        buckets[index].append(num)

    # Ordena cada cubeta individualmente y combina los resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Usa sorted() para simplificar

    return sorted_arr

# Ejemplo de uso
arr = [29, 25, 3, 49, 9, 37, 21, 43]
sorted_arr = hashing_sort(arr)
print("Lista ordenada con Hashing Sort:", sorted_arr)
