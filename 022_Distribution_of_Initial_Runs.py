def create_initial_runs(arr, run_size):
    # Crear una lista para almacenar las secuencias (runs) iniciales
    runs = []
    n = len(arr)
    
    # Recorrer el arreglo en segmentos de tamaño run_size
    for i in range(0, n, run_size):
        # Tomar un segmento del arreglo y ordenarlo para crear una secuencia
        run = sorted(arr[i:i + run_size])
        # Agregar la secuencia ordenada a la lista de runs
        runs.append(run)
    
    return runs

# Ejemplo de uso
arr = [3, 6, 2, 8, 5, 1, 9, 4, 7, 0]
run_size = 3
initial_runs = create_initial_runs(arr, run_size)
print(initial_runs)  # Salida esperada: [[2, 3, 6], [1, 5, 8], [0, 4, 7], [9]]
