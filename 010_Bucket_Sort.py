def bucket_sort(arr):
    # Encuentra el valor máximo para determinar el número de cubetas
    max_value = max(arr)
    bucket_count = len(arr)  # Define el número de cubetas igual al tamaño del arreglo
    buckets = [[] for _ in range(bucket_count)]  # Crea cubetas vacías

    # Distribuye los elementos en sus cubetas correspondientes
    for num in arr:
        index = int(bucket_count * num / (max_value + 1))  # Calcula la cubeta para cada número
        buckets[index].append(num)  # Agrega el número a su cubeta

    # Ordena cada cubeta individualmente y luego las combina
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # Ordena y añade cada cubeta a la lista final

    return sorted_array

# Ejemplo de uso
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Lista ordenada con Bucket Sort:", sorted_arr)
