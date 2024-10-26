def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False  # Indica si la lista está ordenada

    # Repite hasta que la lista esté completamente ordenada
    while not is_sorted:
        is_sorted = True
        
        # Ordena los elementos en posiciones impares
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:  # Intercambia si el elemento actual es mayor que el siguiente
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False  # Aún no está ordenada

        # Ordena los elementos en posiciones pares
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:  # Intercambia si el elemento actual es mayor que el siguiente
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False  # Aún no está ordenada

# Ejemplo de uso
arr = [34, 2, 10, -9]
odd_even_sort(arr)
print("Lista ordenada con Odd-Even Sort:", arr)
