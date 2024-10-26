def quick_sort(arr):
    # Si la lista tiene un elemento o está vacía, ya está ordenada
    if len(arr) <= 1:
        return arr
    else:
        # Selecciona el pivote (aquí usamos el último elemento de la lista)
        pivot = arr[-1]
        
        # Divide los elementos en dos listas: izquierda y derecha
        left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores o iguales al pivote
        right = [x for x in arr[:-1] if x > pivot]  # Elementos mayores al pivote

        # Llama recursivamente a quick_sort en las particiones y las combina
        return quick_sort(left) + [pivot] + quick_sort(right)

# Ejemplo de uso
arr = [10, 7, 8, 9, 1, 5]
arr = quick_sort(arr)
print("Lista ordenada:", arr)
