def flash_sort(arr):
    """Ordena una lista usando el algoritmo Flash Sort."""
    n = len(arr)
    if n <= 1:
        return arr

    # Paso 1: Encuentra el valor mínimo y máximo en el arreglo
    min_val = min(arr)
    max_val = max(arr)
    
    if min_val == max_val:
        return arr  # Si todos los elementos son iguales, el arreglo ya está ordenado
    
    # Paso 2: Inicializa las clases
    m = int(0.43 * n)  # Número de clases (aproximadamente el 43% del tamaño del arreglo)
    classes = [0] * m  # Inicializa la lista de clases con ceros
    
    # Paso 3: Clasifica los elementos en clases
    scale = (m - 1) / (max_val - min_val)
    for num in arr:
        class_index = int(scale * (num - min_val))
        classes[class_index] += 1  # Cuenta los elementos para cada clase
    
    # Convertimos las frecuencias en posiciones acumuladas
    for i in range(1, m):
        classes[i] += classes[i - 1]
    
    # Paso 4: Coloca los elementos en sus posiciones finales dentro de cada clase
    i = 0
    count = 0
    while count < n:
        class_index = int(scale * (arr[i] - min_val))
        while i >= classes[class_index]:  # Encuentra el próximo elemento sin ordenar
            i += 1
            class_index = int(scale * (arr[i] - min_val))
        
        # Coloca el elemento en la posición correcta
        flash_val = arr[i]
        while i != classes[class_index]:
            class_index = int(scale * (flash_val - min_val))
            target_index = classes[class_index] - 1
            arr[target_index], flash_val = flash_val, arr[target_index]
            classes[class_index] -= 1
            count += 1
    
    # Paso 5: Ordena cada clase con Insertion Sort
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso
arr = [3, 6, 4, 1, 9, 8, 2, 5, 7]
flash_sort(arr)
print("Arreglo ordenado:", arr)
