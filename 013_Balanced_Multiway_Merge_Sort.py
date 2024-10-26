import heapq

def split_into_runs(arr, run_size):
    """Divide el arreglo en sublistas ordenadas de tamaño run_size."""
    # Divide 'arr' en sublistas de tamaño 'run_size' y las ordena individualmente
    runs = [sorted(arr[i:i + run_size]) for i in range(0, len(arr), run_size)]
    return runs

def multiway_merge(runs):
    """Realiza una mezcla de múltiples 'runs' en un solo arreglo ordenado."""
    min_heap = []
    sorted_result = []
    
    # Inicializa el heap con el primer elemento de cada 'run'
    for i, run in enumerate(runs):
        if run:  # Verifica que el 'run' no esté vacío
            heapq.heappush(min_heap, (run[0], i, 0))  # (valor, índice del run, índice en el run)

    # Mezcla balanceada de todos los 'runs'
    while min_heap:
        val, run_idx, elem_idx = heapq.heappop(min_heap)  # Extrae el elemento mínimo actual
        sorted_result.append(val)
        
        # Si el 'run' tiene más elementos, agrega el siguiente al heap
        if elem_idx + 1 < len(runs[run_idx]):
            next_val = runs[run_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, run_idx, elem_idx + 1))
    
    return sorted_result

def balanced_multiway_merge_sort(arr, run_size):
    """Simulación de Balanced Multiway Merge Sort."""
    # Genera 'runs' iniciales de tamaño run_size
    runs = split_into_runs(arr, run_size)
    
    # Realiza una mezcla multi-camino en todas las fases hasta obtener un arreglo ordenado completo
    sorted_arr = multiway_merge(runs)
    return sorted_arr

# Ejemplo de uso
arr = [34, 7, 23, 32, 5, 62, 32, 12, 45, 18, 93, 21]
run_size = 3
print("Arreglo ordenado:", balanced_multiway_merge_sort(arr, run_size))
