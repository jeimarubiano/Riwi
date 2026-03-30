#tkinter es la librería que estoy usando y as tk convierte como en un apodo la llamada en vez de poner tkinter completo solo pongo tk (as lo convierte en eso.)
from funciones import *
import tkinter as tk



#ventana es una variable creada por mi y lo pongo = tk.Tk porque eso crea una ventana vacia pero no la abré
ventana = tk.Tk()
#el .title lo encapsulo ("Calculadora") es para ponerle el nombre en la esquina a la ventana que cree con tk.Tk()
ventana.title("Calculadora")
#resizable tiene 2 parametros y funcionan con true: permite cambiarle tamaño y false: no permite hacerlo. (izquierda: es de ancho) (derecha: es de altura)
ventana.resizable(False, False)
#geometry la utilizo para poner fijo un tamaño a la ventana y pongo false false a resizable para que no puedan modificar el tamaño.
ventana.geometry("371x400")
etiqueta = tk.Label(ventana, text="--AA--")
etiqueta.grid(row=6,column=3)
#btn (es boton pero es una variable creada por mi para identificar quue es boton.)
#tk (libreria) y utilizo button para convertir mi variable en boton.
#ventana: mostrar btn en ventana, text: Nombre que muestra, width: Tamaño del largo, height: tamaño de alto, command: lo que hará el boton al presionar
#lambda: es una funcion que sirve para que la funcion que creaste se le pueda poner parametros sin eso la funcion se lanza enseguida sin esperar el CLICK y no funciona.
btn_2D = tk.Button(ventana, text= "2D", width=12, height=3, command=lambda:saludar)
btn_3D = tk.Button(ventana, text= "3D", width=12, height=3, command=lambda:saludar)
btn_CUADRADO = tk.Button(ventana, text= "Cuadrado", width=8, height=1, command=lambda: saludar("jeimar"))
btn_RECTANGULO = tk.Button(ventana, text= "Rectangulo", width=8, height=1, command=lambda:saludar)
btn_CIRCULO = tk.Button(ventana, text= "Circulo", width=8, height=1, command=lambda:saludar)
btn_ROMBO = tk.Button(ventana, text= "Rombo", width=8, height=1, command=lambda:saludar)
btn_TRIANGULO_RECTANGULO = tk.Button(ventana, text= "T. rectangulo", width=8, height=1, command=lambda:saludar)
btn_CUBO = tk.Button(ventana, text= "Cubo",width=8,height=1, command=lambda:saludar)
btn_ESFERA = tk.Button(ventana, text= "Esfera", command=lambda:saludar)
btn_CILINDRO = tk.Button(ventana, text= "Cilindro", command=lambda:saludar)
btn_CONO = tk.Button(ventana, text= "Cono", command=lambda:saludar)
btn_0 = tk.Button(ventana, text= "0", width=4, height=1, command=lambda:cambiar_numero("0"))
btn_1 = tk.Button(ventana, text= "1", width=4, height=1, command=lambda:cambiar_numero("1"))
btn_2 = tk.Button(ventana, text= "2", width=4, height=1, command=lambda:cambiar_numero("2"))
btn_3 = tk.Button(ventana, text= "3", width=4, height=1, command=lambda:cambiar_numero("3"))
btn_4 = tk.Button(ventana, text= "4", width=4, height=1, command=lambda:cambiar_numero("4"))
btn_5 = tk.Button(ventana, text= "5", width=4, height=1, command=lambda:cambiar_numero("5"))
btn_6 = tk.Button(ventana, text= "6", width=4, height=1, command=lambda:cambiar_numero("6"))
btn_7 = tk.Button(ventana, text= "7", width=4, height=1, command=lambda:cambiar_numero("7"))
btn_8 = tk.Button(ventana, text= "8", width=4, height=1, command=lambda:cambiar_numero("8"))
btn_9 = tk.Button(ventana, text= "9", width=4, height=1, command=lambda:cambiar_numero("9"))

#esto es la posicion de los botones creados
#.grid indica que: row: fila que quieres poner el boton (solo puede estar en filas creedas o siguientes ej: solo tienes 1 fila y creas una y pones en fila 30 se vera como si estuviera en fila 2
#column: indica la columna de la fila en la que va ambas empiezan desde 0 hasta donde quieran poner depende de los botones.
#columnspan: son las columnas que ocupara el boton, sticky dice hacia donde estirarse en este caso es e= derecha w= izquierda (faltaría n y s puedes poner hasta las 4 y se estiraria en todas las direcciones)
#padx separador de botones, es la distancia que se encuentra un boton en X (derecha e izquierda)
#pady separador de botones, es la distancia que se encuentra un boton en Y (arriba y abajo)
btn_2D.grid(row=1,column=0,columnspan=2, sticky="ew", padx=1, pady=1)
btn_3D.grid(row=1,column=2,columnspan=2, sticky="ew", padx=1, pady=1)
btn_CUADRADO.grid(row=3,column=0,columnspan=1, sticky="ew", padx=1, pady=1)
btn_RECTANGULO.grid(row=3,column=1,columnspan=1, sticky="ew", padx=1, pady=1)
btn_CIRCULO.grid(row=3,column=2,columnspan=1, sticky="ew", padx=1, pady=1)
btn_ROMBO.grid(row=3,column=3,columnspan=1, sticky="ew", padx=1, pady=1)

btn_TRIANGULO_RECTANGULO.grid(row=4,column=0,columnspan=1, sticky="ew", padx=1, pady=1)
btn_CUBO.grid(row=4,column=1,columnspan=1, sticky="ew", padx=1, pady=1)
btn_ESFERA.grid(row=4,column=2,columnspan=1, sticky="ew", padx=1, pady=1)
btn_CILINDRO.grid(row=4,column=3,columnspan=1, sticky="ew", padx=1, pady=1)
btn_CONO.grid(row=6,column=0)
btn_0.grid(row=8,column=1)
btn_1.grid(row=7,column=0)
btn_2.grid(row=7,column=1)
btn_3.grid(row=7,column=2)
btn_4.grid(row=6,column=0)
btn_5.grid(row=6,column=1)
btn_6.grid(row=6,column=2)
btn_7.grid(row=5,column=0)
btn_8.grid(row=5,column=1)
btn_9.grid(row=5,column=2)

#Valor_pantalla es una variable creada por mi, tk libreria, y stringvar() una clase de tk que sirve para un texto mirarlo todo el tiempo.
valor_pantalla = tk.StringVar()
#Este es el metodo de StringVar() el metodo set sirve para cambiarle el valor a StringVar y como puse "0" StringVar se convertira en valor Str 0
valor_pantalla.set("0")
#Pantalla otra variable creada por mi, uso Entry para que muestre valor y en sus parametros digo Ventana para que lo muestre en la ventana, 
#textvariable: conecta mi variable de valor_pantalla con Entry, es lo que mostrara en la pantalla de lo que el valor de Stringvar cambie en el .set(0)
#justify "right" es para ponerlo pegado a la derecha, si pusiera center me centra el texto o si pongo left me lo pega a la izquierda
#font: es la fuente de texto que voy a usar en este caso Arial con tamaño 24
#state: "readonly" es para que nadie puede escribir solo leer, existe "normal" que es para que escriba y "disable" para no escribir ni copiar.

pantalla = tk.Entry(ventana, textvariable=valor_pantalla ,justify="right", font=("Arial", 24), state="readonly")
#Esto es lo mismo de arriba, la posiciones etc.
pantalla.grid(row=0,column=0,columnspan=4, sticky="ew", padx=4, pady=4)

#funciones
#1
def cambiar_numero(numero):
    valor_actual = valor_pantalla.get()
    if valor_actual == "0":
        valor_pantalla.set(numero)
    else:
        valor_pantalla.set(valor_actual + numero)

#Esto es como un proceso de evento, todo lo que se encuentre detras de el lo procesa, si no estuviera de ultimo no se mostrara nada al estar de ultimo lee todo lo que este detras.
ventana.mainloop()