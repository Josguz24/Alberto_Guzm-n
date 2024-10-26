def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializa el intervalo (gap)

    # Reduce el intervalo y realiza insertion sort en los elementos separados por gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Desplaza los elementos que están fuera de orden
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce el intervalo para la próxima iteración

# Ejemplo de uso
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Lista ordenada con ShellSort:", arr)
