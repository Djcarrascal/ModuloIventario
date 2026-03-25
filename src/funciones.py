producto_nuevo = []

#Esta funcion permite agregar un producto digitando solo valores válidos y en caso del ingreso de algo no permitido el programa solicita nuevamente la información.
def agregar_producto():

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
            precio = float(input("\nIngrese el precio del producto: "))
            if not precio:
                    print("\nNo puede dejar el precio vacío, por favor ingrese el precio")
                    continue
            break
        except ValueError:
            print("\nSolo de pueden ingresar numeros")

#Aquí creé el diccionario que permitirá almacenar los prodcutos que digite el usuario.
    producto = {
               "nombre":nombre,
               "precio":precio,
               "cantidad": cantidad,
               "costo_total" : precio*cantidad
        }

    producto_nuevo.append(producto)



    print(f"\nProducto ingresado: {nombre}, cantidad: {cantidad}, precio unitario: {precio} y el costo total ingresado es de: {precio*cantidad}")

#En esta funcion tomé datos de la funcion (agregar_producto) para hacer el cálculo de los totales de cantidad y precio solicitados sumando item por item.
def calcular_estadisticas():
        total_cantidad = sum(item["cantidad"]for item in producto_nuevo)
        total_costo = sum(item["costo_total"]for item in producto_nuevo)
        print(f"\nSu inventario tiene {total_cantidad} productos, con un valor total de ${total_costo} USD")

#Creé una funcion de mensaje para que solamente llamarla depues de finalizar cada opcion elegida del menu principal
def mensaje_agradecimiento():
        print("\nGracias por usar el módulo de inventario")

def guardar_inventario():
        nombre_archivo = "Inventary.csv"
        with open(nombre_archivo, "w") as archivo:
            for producto in producto_nuevo:
                archivo.write(f"{producto['nombre']}, {producto['cantidad']}, {producto['precio']}, {producto['costo_total']}\n")
                print("\nProducto guardado en inventario.txt")

def buscar_producto(nombre):
        for producto in producto_nuevo:
            if producto["nombre"] == nombre:
                return producto
        return None

def actualizar_producto(nombre, cantidad, precio):
        for producto in producto_nuevo:
            if producto["nombre"] == nombre:
                producto["cantidad"] = cantidad
                producto["precio"] = precio
                producto["costo_total"] = cantidad * precio
                print(f"\nProducto actualizado: {nombre}, cantidad: {cantidad}, precio unitario: {precio} y el costo total actualizado es de: {cantidad * precio}")
                return
        print("\nProducto no encontrado para actualizar.")

def eliminar_producto(nombre):
        for producto in producto_nuevo:
            if producto["nombre"] == nombre:
                producto_nuevo.remove(producto)
                print(f"\nProducto eliminado: {nombre}")
                return
        print("\nProducto no encontrado para eliminar.")