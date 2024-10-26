def counting_sort(arr):
    # Encuentra el valor máximo en la lista para definir el rango del conteo
    max_val = max(arr)
    # Crea una lista para contar cada valor en el rango de 0 hasta el valor máximo
    count = [0] * (max_val + 1)

    # Cuenta la ocurrencia de cada número en la lista original
    for num in arr:
        count[num] += 1

    # Reconstruye la lista ordenada con los valores contados
    index = 0
    for num, freq in enumerate(count):
        for _ in range(freq):  # Para cada frecuencia de número, agrégalo en orden
            arr[index] = num
            index += 1

# Ejemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Lista ordenada con Counting Sort:", arr)
