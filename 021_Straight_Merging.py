def straight_merge(arr1, arr2):
    # Inicializar punteros para arr1 y arr2
    i, j = 0, 0
    merged = []

    # Recorrer ambas listas y agregar el elemento más pequeño a merged
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Si quedan elementos en arr1, agregarlos a merged
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Si quedan elementos en arr2, agregarlos a merged
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Ejemplo de uso (comentado para evitar ejecución):
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = straight_merge(arr1, arr2)
print(result) # Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8]
