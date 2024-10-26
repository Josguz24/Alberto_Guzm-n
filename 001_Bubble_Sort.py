def bubble_sort(arr):
    # Recorre todos los elementos de la lista
    for i in range(len(arr)):
        # Cada pasada coloca el elemento mayor al final, así que el rango se reduce
        for j in range(0, len(arr) - i - 1):
            # Si el elemento actual es mayor que el siguiente, se intercambian
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Lista ordenada:", arr)
