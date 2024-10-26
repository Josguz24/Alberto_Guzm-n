def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n  # Arreglo de salida
    count = [0] * 10  # Arreglo de conteo para los dígitos (0-9)

    # Cuenta ocurrencias en el dígito actual (exp representa la posición del dígito)
    for i in arr:
        index = i // exp  # Encuentra el dígito en la posición actual
        count[index % 10] += 1  # Incrementa el conteo para este dígito

    # Acumula los conteos para obtener las posiciones correctas en el arreglo de salida
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construye el arreglo de salida en orden inverso para mantener la estabilidad
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]  # Coloca el elemento en su posición
        count[index % 10] -= 1  # Decrementa el conteo
        i -= 1

    # Copia el arreglo de salida de vuelta en arr
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Encuentra el valor máximo para conocer el número de dígitos
    max_val = max(arr)
    exp = 1  # Inicializa la posición del dígito (unidades, decenas, centenas, etc.)
    
    # Aplica counting_sort_exp para cada dígito, comenzando desde las unidades
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10  # Mueve a la siguiente posición del dígito

# Ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Lista ordenada:", arr)


