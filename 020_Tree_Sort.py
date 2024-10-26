# Definimos la clase para el nodo del árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Función para insertar un valor en el árbol binario
def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# Función para realizar un recorrido in-order y obtener los elementos en orden
def in_order_traversal(root, sorted_list):
    if root is not None:
        in_order_traversal(root.left, sorted_list)
        sorted_list.append(root.value)
        in_order_traversal(root.right, sorted_list)

# Función principal de Tree Sort
def tree_sort(arr):
    if not arr:
        return []

    # Crear el árbol binario e insertar los elementos
    root = TreeNode(arr[0])
    for value in arr[1:]:
        insert(root, value)

    # Realizar el recorrido in-order para obtener la lista ordenada
    sorted_list = []
    in_order_traversal(root, sorted_list)
    return sorted_list

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = tree_sort(arr)
print("Lista ordenada con Tree Sort:", sorted_arr)
