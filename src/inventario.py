# Creamos un menú de opciones para el usuario
print("\nInventario de Productos\n")

print("Menu de opciones:\n")
print("1. Agregar Productos")
print("2. Ver Productos")
print("3. Actualizar Producto Existente")
print("4. Eliminar Producto")
print("0. Salir")

opcion = input("\nIngrese una opcion: ")
if opcion == "1":

# Solicitamos los datos requeridos y colocamos condiciones para que los datos ingresados sean validos para el sistema
        while True:
                try:
                        nombre = str(input("\nIngrese el nombre del producto: "))
        
                        if not nombre:
                                print("\nNo puede dejar el nombre vacío, por favor ingrese el nombre")
                                continue
                        elif not nombre.isalpha():
                                print("\nERROR - Solo se pueden ingresar letras")
                                continue
                        break
                except:
                        nombre = input("\nIngrese el nombre del producto: ")
                        continue

        while True:
                try:
                        cantidad = int(input("\nIngrese la cantidad: "))
                        if not cantidad:
                                print("\nNo puede dejar el nombre vacío, por favor ingrese la cantidad ")
                        break
                except ValueError:
                        print("\nSolo de pueden ingresar numeros")                

        while True:
                try:
                        precio = int(input("\nIngrese el precio del producto: "))
                        if not precio:
                                print("\nNo puede dejar el precio vacío, por favor ingrese el precio")
                                continue
                        break
                except ValueError:
                        print("\nSolo de pueden ingresar numeros")

costo_total = precio * cantidad
print(f"\nProducto ingresado: {nombre}, cantidad: {cantidad}, precio unitario: {precio} y el costo total ingresado es de: {costo_total}")

