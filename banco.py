saldo = float(0)
opcion = "0"

while opcion != "4":
    print("\n--- MENU ---")
    print("1: saldo = ", saldo)
    print("2: Depositar")
    print("3: Retirar")
    print("4: Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("Tu saldo es", saldo)

    elif opcion == "2":
        try:
            monto = input("Cuanto quieres depositar? ").replace(",", ".")
            monto = float(monto)
            if float(monto) > 0:
                saldo = saldo + float(monto)
                print("Deposito exitoso, ahora tu saldo es", saldo)
            else:
                print("El monto a depositar es incorrecto")
        except ValueError:
            print("Incorrecto")

    elif opcion == "3":
        try:
            monto = input("¿Cuánto quieres Retirar? ").replace(",", ".")
            monto = float(monto)
            if monto > saldo:
                print("No tienes suficiente saldo")
            elif monto <= 0:
                print("El monto debe ser mayor que 0")
            else:
                saldo = saldo - monto
                print("Envío exitoso, tu saldo actual es ", saldo)
        except ValueError:
            print("Incorrecto")

    elif opcion == "4":
        print("Has salido exitosamente")

    else:
        print("Opción no válida")

