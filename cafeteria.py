cafe = 4000
te = 3500
jugo = 5000
c_cafe = 0
c_te = 0
c_jugo = 0
cliente = input("Ingresa un nombre: ")
while True:
    print("================================================")
    print("Bienvenid@ a cafetería Rubiano señor(a): ", cliente)
    print("A continuacion, le muestro los precios disponible de la cafetería:")
    print("1: CAFÉ $5000")
    print("2: TÉ $3500")
    print("3: JUGO $5000") 
    print("4: PAGAR") 

    print("================================================")
    quiere = int(input("Ingrese el numero de la bebida que desea: "))

    if quiere == 1:
        c_cafe += 1
    elif quiere == 2:
        c_te +=1
    elif quiere == 3:
        c_jugo += 1
    elif quiere == 4:
        print("Muchas gracias por su compra")
        break
    
    total = (cafe * c_cafe) + (te * c_te) + (jugo * c_jugo)
    print("================================================")
    print("Bebidas elegidas para su compra:")
    print("CAFÉ:",c_cafe,"|", "TE:",c_te,"|","JUGO", c_jugo) 
    print("================================================")
    print ("Señor(a)", cliente, "Su total a pagar es: ", total)




