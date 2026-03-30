#DICCIONARIO DONDE SE GUARDARAN LOS PRODUCTOS, VAORES Y CANTIDAD.
inventario = {}
#VARIABLE PARA SALIR DEL BUCLE
Salir = False
#BUCLE PRINCIPAL
while Salir == False:
#COSTO TOTAL PARA QUE SE ACTUALICE SIEMPRE EN LA OPCION 2
    costo_total = 0
    for datos in inventario.values(): 
        costo_total += (datos["precio"] * datos["cantidad"])
#MENU DE OPCIONES
    print("Bienvenido a inventario de Jeimar")
    print()
    print("1: Registrar un producto")
    print(f"2: ver inventario --- [${costo_total} USD]")
    print("3: Salir")
# VARIABLE OPCION VACIA Y BUCLE PARA ELEGIR OPCION CORRECTAMENTE SI SE ESCRIBE UN TEXTO EL EXCEPT MANDA UN PRINT Y DEVUELVE OPCION A VACIA.
    opcion = None
    while opcion is None:
        try:
            opcion = int(input("Elige una opcion: ").strip())
        except ValueError:
            print("=" * 20 , "No puedes ingresar texto", "=" * 20)
            opcion = None
# SI LA OPCION ES 1, SOLICITA LOS DATOS DE LOS PRODUCTOS.            
    if opcion == 1:
        nombre = input("Ingresa el nombre del producto: ").strip().lower()
        precio = None
        while precio is None:
            try:
                precio = float(input(f"Ingresa el precio de {nombre}: ").strip())
            except ValueError:
                print("=" * 20, "El precio debe ser numeros", "=" * 20)
                precio = None
        cantidad = None
        while cantidad is None: 
            try:           
                cantidad = int(input(f"Ingresa la cantidad de {nombre}: ").strip())
            except ValueError:
                print("=" * 20, "la cantidad debe ser numeros", "=" * 20)
                cantidad = None
# SI EL NOMBRE SE ENCUENTRA EN EL DICCIONARIO, DICE QUE YA EXISTE SI NO ENTONCES LO GUARDA LOS DATOS SOLICITADOS.
        if nombre in inventario:
            print("Ya existe este producto")
        else:
            inventario[nombre] = {
                "precio":precio,
                "cantidad":cantidad}
#SI OPCIONES 2, MUESTRA EN CONSOLA DE MEJOR MANERA LO QUE EXISTE EN EL INVENTARIO, UTILIZANDO FOR PARA RECORRER EL DICCIONARIO.
    if opcion == 2:
        print(f"\nEn tu Inventario Tienes:\n")
        for nombre, datos in inventario.items():
            total_producto = datos["cantidad"] * datos["precio"]
            print(f"Producto: {nombre} | Precio: {datos['precio']}$ | Cantidad: {datos['cantidad']} | Total: ${total_producto}")
# SI OPCION ES 3 ENTONCES SE SALE DE BUCLE.
    if opcion == 3:     
        Salir = True
# SI NO SE ELIGE NINGUNA DE LAS OPCIONES ANTERIORES CUALQUIER OTRO NUMERO MUESTRA EN CONSOLA EL MENSAJE.       
    else:
        print("Solo tienes 3 opciones, esta opcion no es validad")

#ESTE INVENTARIO TIENE 3 OPCIONES DONDE LA OPCION 1 SIRVE PARA REGISTRAR LOS ARTICULOS CON PRECIO Y CANTIDAD, SE PUEDE REGISTRAR TODOS LOS QUE QUIERAN
#PERO NO SE PUEDE REPETIR LOS MISMO NOMBRE O MANDA UN MENSAJE QUE YA ESE ARTICULO EXISTE Y CON LA OPCION 2 MUESTRA TODOS LOS PRODUCTOS REGISTRADOS CON SU VALOR Y CANTIDAD.