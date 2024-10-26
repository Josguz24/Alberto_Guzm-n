import heapq

def replacement_selection_sort(arr, memory_size):
    """
    Simulación de Replacement Selection Sort.
    
    Parámetros:
    arr (list): La lista de datos a ordenar (simula datos externos).
    memory_size (int): Tamaño de la memoria disponible (simula el tamaño del buffer).
    
    Retorna:
    list: Lista de "runs" ordenados.
    """
    # Inicializa una lista para almacenar los runs resultantes
    runs = []
    
    # Carga una porción de los datos en la memoria/buffer y la convierte en un min-heap
    buffer = arr[:memory_size]
    heapq.heapify(buffer)
    
    # El resto de los datos se almacena en una lista de "remaining" (datos pendientes)
    remaining = arr[memory_size:]
    
    # Generar runs
    while buffer:
        current_run = []
        
        # Extraer el menor elemento en cada iteración para formar el run
        while buffer:
            # Extraer el elemento mínimo del heap
            smallest = heapq.heappop(buffer)
            current_run.append(smallest)
            
            # Si hay datos pendientes, reemplaza el mínimo con un nuevo valor si es mayor o igual
            if remaining:
                next_item = remaining.pop(0)
                if next_item >= smallest:
                    heapq.heappush(buffer, next_item)
                else:
                    # Si el siguiente elemento no es mayor, lo devuelve a remaining para el siguiente run
                    remaining.insert(0, next_item)
                    break
        
        # Añadir el run actual a la lista de runs ordenados
        runs.append(current_run)
        
        # Volver a llenar el buffer hasta el tamaño de memoria disponible
        while len(buffer) < memory_size and remaining:
            heapq.heappush(buffer, remaining.pop(0))

    return runs

# Ejemplo de uso
arr = [34, 7, 23, 32, 5, 62, 32, 12, 45, 18, 93, 21]
memory_size = 4
runs = replacement_selection_sort(arr, memory_size)
print("Runs ordenados:", runs)
