from itertools import zip_longest

def split_into_runs(arr, run_size):
    """Divide la lista en sublistas o 'runs' de tamaño run_size."""
    return [arr[i:i + run_size] for i in range(0, len(arr), run_size)]

def merge_runs(run1, run2):
    """Mezcla dos 'runs' ordenados en una sola lista ordenada."""
    result = []
    i, j = 0, 0
    while i < len(run1) and j < len(run2):
        if run1[i] < run2[j]:
            result.append(run1[i])
            i += 1
        else:
            result.append(run2[j])
            j += 1
    # Añade los elementos restantes de ambas listas (si quedan)
    result.extend(run1[i:])
    result.extend(run2[j:])
    return result

def polyphase_merge_sort(arr, initial_run_size=2):
    """Simulación de Polyphase Merge Sort."""
    run_size = initial_run_size

    # Divide la lista original en 'runs' iniciales de tamaño run_size
    runs = split_into_runs(arr, run_size)
    runs = [sorted(run) for run in runs]  # Ordena cada 'run' individualmente

    # Proceso de mezcla en fases
    while len(runs) > 1:
        # Agrupa en pares de 'runs' para mezclar
        new_runs = []
        for run1, run2 in zip_longest(runs[::2], runs[1::2], fillvalue=[]):
            merged_run = merge_runs(run1, run2)  # Mezcla dos 'runs' en una sola lista ordenada
            new_runs.append(merged_run)
        
        runs = new_runs  # Actualiza los 'runs' para la siguiente fase de mezcla

    return runs[0] if runs else []

# Ejemplo de uso
arr = [34, 7, 23, 32, 5, 62]
print("Arreglo ordenado:", polyphase_merge_sort(arr))
