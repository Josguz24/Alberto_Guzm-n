def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True  # Indica si hubo intercambio en la pasada
    start = 0       # Inicio del recorrido
    end = n - 1     # Final del recorrido

    while swapped:
        swapped = False
        
        # Pasa de izquierda a derecha, moviendo el mayor elemento hacia el final
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Si no hubo intercambio, la lista ya está ordenada
        if not swapped:
            break

        # Actualiza el límite superior y pasa de derecha a izquierda
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Incrementa el inicio después de la pasada de derecha a izquierda
        start += 1

# Ejemplo de uso
arr = [5, 1, 4, 2, 8, 0, 2]
cocktail_shaker_sort(arr)
print("Lista ordenada con Cocktail Shaker Sort:", arr)
