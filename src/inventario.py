from funciones import agregar_producto
opcion = 1
# Creamos un menú de opciones para el usuario


# Aqui definimos que el usuario ingrese una opcion y la vez que solo sea una opcion valida


while opcion != 0:
    print("\nInventario de Productos\n")
    print("Menu de opciones:\n")
    print("1. Agregar Productos")
    print("2. Ver Productos")
    print("3. Actualizar Producto Existente")
    print("4. Eliminar Producto")
    print("0. Salir")
    while True:
        try:
            opcion = int(input("\nIngrese una opción: "))
            break
        except ValueError:
                    print("Por favor ingrese un número")
             
    if opcion == 1:
            agregar_producto()
    print("Opcion invalida.")
