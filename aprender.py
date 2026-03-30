hija = {
    "Nombre":"Ariana",
    "Edad":"1",
    "estatura":80}
#Variables para agregar los valores del diccionario.
nombre = hija["Nombre"]
edad = hija["Edad"]
estatura = hija["estatura"]
#Agrega una clave:valor al diccionario.
hija["Cabello"] = "Ondulado"
Cabello = hija["Cabello"]
#Itera sobre el diccionario de hija.
for caracteristicas in hija.items():
    print(caracteristicas)

print(f"\nNombre: {nombre}\nEdad: {edad}\nEstatura: {estatura}\nCabello: {Cabello}")
print("=" * 80)
Selecciones = {
    "Colombia":{
        "Jugador1":{
            "nombre":"Jeimar",
            "Dorsal":10,
            "Posicion":"Delantero",
            "Goles":50},

        "jugador2":{
            "nombre":"Jennifer",
            "Dorsal":7,
            "Posicion":"Arquera",
            "Goles":50},
        
        "jugador3":{
            "nombre":"Ariana",
            "Dorsal":1,
            "Posicion":"Defensa",
            "Goles":9}}}


Selecciones["Colombia"]["Jugador1"].update({"Goles":99,"Posicion":"Extremo"})
Elimina_goles = Selecciones["Colombia"]["Jugador1"].pop("Goles")
print(f"Goles eliminados: {Elimina_goles}")
for seleccion, jugadores in Selecciones["Colombia"].items():
    if jugadores["Dorsal"] == 10:
        print(jugadores)
        print(len(jugadores))