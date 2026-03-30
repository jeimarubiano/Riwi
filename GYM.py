edad = int(input("Ingresa tu edad"))
if edad <= 13:
    print("No puede ingresar")
elif edad > 13 < 17:
    print("Clase: Juvenil")
elif edad > 18 < 59:
    print("clase: general")
else:
    print("clase: senior")
