def bitonic_sort(arr, up=True):
    """Ordena una lista usando el algoritmo Bitonic Sort."""
    if len(arr) <= 1:
        return arr
    
    # Divide el arreglo en dos mitades
    mid = len(arr) // 2
    first_half = bitonic_sort(arr[:mid], up=True)   # Ordena en bitonic creciente
    second_half = bitonic_sort(arr[mid:], up=False) # Ordena en bitonic decreciente
    
    # Combina ambas mitades en una secuencia bitónica
    return bitonic_merge(first_half + second_half, up)

def bitonic_merge(arr, up):
    """Combina una secuencia bitónica en una secuencia ordenada."""
    if len(arr) <= 1:
        return arr
    
    # Realiza comparaciones y swaps para ordenar la secuencia
    bitonic_compare(arr, up)
    mid = len(arr) // 2
    first_half = bitonic_merge(arr[:mid], up)
    second_half = bitonic_merge(arr[mid:], up)
    
    return first_half + second_half

def bitonic_compare(arr, up):
    """Realiza comparaciones en la secuencia para crear el orden bitónico."""
    dist = len(arr) // 2
    for i in range(dist):
        # Compara y, si es necesario, intercambia para cumplir con el orden bitónico
        if (arr[i] > arr[i + dist]) == up:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]

# Ejemplo de uso
arr = [3, 7, 4, 8, 6, 2, 1, 5]
print("Arreglo ordenado:", bitonic_sort(arr, up=True))
