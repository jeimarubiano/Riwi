repetir = 0
while repetir < 2:
    vainilla = 0
    chocolate = 0
    fresa = 0

    while vainilla + chocolate + fresa <= 4:
        print("______________________________________________________")
        print(" 1: vainilla", "\n", "2: chocolate", "\n", "3: fresa")
        print("______________________________________________________")
        try:
                helados = int(input("Para hacer tu pedido ingresa un numero del 1 al 3 para elegir el sabor: "))
        except:
             print("Valor no valido.")
        if helados == 1:
             vainilla += 1
        elif helados == 2:
             chocolate += 1
        elif helados == 3:
             fresa += 1
        print("Pedido actual: ","\n", "vainilla: ", vainilla,"\n", "chocolate", chocolate,"\n", "fresa", fresa)

    print("muchas gracias por elegirnos, disfrute de su pedido vuelva pronto.")
    print("quieres hacer un nuevo pedido?")
    print("1: Si")
    print("2: No")
    repetir = int(input(""))
    
    if repetir == 1:
        repetir = 1
    else:
        repetir = 2