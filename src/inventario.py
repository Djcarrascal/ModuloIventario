from funciones import *
opcion = 1

# Creamos un menú de opciones para el usuario y creamos un bucle. Tambien definimos que el usuario solo pueda ingresar opciones validas.
while opcion != 0:
    print("\nInventario de Productos\n")
    print("Menu de opciones:\n")
    print("1. Agregar Productos")
    print("2. Ver Inventario")
    print("3. Calcular estadísticas")
    print("4. Guardar inventario")
    print("5. Buscar producto")
    print("6. Actualizar producto")
    print("7. Eliminar producto")
    print("8. Cargar archivo CSV")
    print("0. Salir")
    while True:
        try:
            opcion = int(input("\nIngrese una opción: "))
            break
        except ValueError:
                    print("Por favor ingrese una opción válida")
             
    if opcion == 1:
            agregar_producto()
            mensaje_agradecimiento()

    elif opcion == 2:
          if not producto_nuevo:
                print("\nEl inventario está vacío.")
          else:
                print(producto_nuevo)
                
    elif opcion == 3:
            calcular_estadisticas()
            mensaje_agradecimiento()
      
    elif opcion == 4:
            guardar_inventario()
            print("\nInventario guardado exitosamente.\n")
            mensaje_agradecimiento()

    elif opcion == 5:
            nombre = input("\nIngrese el nombre del producto a buscar: ")
            producto = buscar_producto(nombre)
            if producto:
                print(f"\nProducto encontrado: {producto['nombre']}, cantidad: {producto['cantidad']}, precio unitario: {producto['precio']}, costo total: {producto['costo_total']}")
            else:
                print("\nProducto no encontrado.")

    elif opcion == 6:
            nombre = input("\nIngrese el nombre del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            precio = float(input("Ingrese el nuevo precio: "))
            actualizar_producto(nombre, cantidad, precio)

    elif opcion == 7:
            nombre = input("\nIngrese el nombre del producto a eliminar: ")
            eliminar_producto(nombre)
            
    elif opcion == 8:
            cargar_archivo_csv()
    else:
          mensaje_agradecimiento()
            
          
          
