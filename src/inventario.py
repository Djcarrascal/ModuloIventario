from funciones import *
opcion = 1

# Creamos un menú de opciones para el usuario y creamos un bucle. Tambien definimos que el usuario solo pueda ingresar opciones validas.
while opcion != 0:
    print("\nInventario de Productos\n")
    print("Menu de opciones:\n")
    print("1. Agregar Productos")
    print("2. Ver Productos")
    print("3. Calcular estadísticas")
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
    
    else:
          mensaje_agradecimiento()
            
          
          
