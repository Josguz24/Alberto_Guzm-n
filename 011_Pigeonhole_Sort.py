def pigeonhole_sort(arr):
    if not arr:  # Caso de lista vacía
        return arr

    # Encuentra el valor mínimo y máximo para definir el rango de los huecos
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1  # Define el número de huecos necesarios

    # Crea huecos (pigeonholes) para almacenar los elementos
    holes = [[] for _ in range(size)]

    # Coloca cada elemento en su hueco correspondiente
    for num in arr:
        holes[num - min_val].append(num)

    # Recolecta los elementos ordenados desde los huecos
    sorted_arr = []
    for hole in holes:
        sorted_arr.extend(hole)

    return sorted_arr

# Ejemplo de uso
arr = [8, 3, 2, 7, 4, 6, 8]
print("Arreglo ordenado:", pigeonhole_sort(arr))
