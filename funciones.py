import tkinter as tk

#1: dev es la palabra reservada para definir funciones
#2: saludar (en este caso) es el nombre de la variable (puede ser lo que quieras y hacer lo que tu lo pongas a hacer.)
#3: () todo lo que este dentro de los parentesis es los parametros que pones para cuando llamas la funcion ejemplo:  saludar(Jeimar) en consola sale"Hola, ¿como estas? Jeimar"
#4 todo lo que va despues de los : y la sangría es lo que hará la funcion, ya sea desde lo más sencillo o lo más.
def saludar(nombre):
    print(f"Hola, ¿como estas? {nombre}")
def elegir (op1,op2,op3,op4,op5):
    print(f"1: {op1}")
    print(f"2: {op2}")
    print(f"3: {op3}")
    print(f"4: {op4}")
    print(f"5: {op5}")
def elevar (numero1,numero2):
    return numero1 ** numero2
def menu_opciones(*opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}:{opcion}")



    

