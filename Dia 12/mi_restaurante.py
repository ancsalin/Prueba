from cProfile import label
from tkinter import *

#Iniciar tkinder
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

#evitar maximizar
aplicacion.resizable(0, 0)

#Titulo de la ventana
aplicacion.title(" Mi Restaurante- Sistema de facturacion")

# Color de fondo
aplicacion.config(bg='blueViolet')

#Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4', font=('Dosis', 50), bg='blueViolet',
                        width=27)

etiqueta_titulo.grid(row=0, column=0)

#Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#Panel comida
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT,
                           fg='blueViolet')
panel_comidas.pack(side=LEFT)

#Panel Bebida
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT,
                           fg='blueViolet')
panel_bebidas.pack(side=LEFT)

#Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT,
                           fg='blueViolet')
panel_postres.pack(side=LEFT)

#Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#Panel botonos
panel_botonos = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botonos.pack()

#Listas de productos
listas_comida = ['Pizza', 'Hamburguesa', 'Tacos', 'Sandwich', 'Papa aborrajado']
listas_bebidas = ['agua', 'Te', 'Gaseosa', 'Jugos naturales', 'Jugos en leche']
listas_postres = ['Helado', 'Ensalada de frutas', 'Cholados', 'Shampus', 'Pastel']

#generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in listas_comida:

    #Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)

    #Crear cuadros de entrada

    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1, width=6, state=DISABLED,
                                     textvariable=texto_comida[contador])


    cuadros_comida[contador].grid(row=contador, column=1)


    contador += 1

#generar items Bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in listas_bebidas:

    # Crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         variable=variables_bebida[contador],
                         offvalue=0)


    bebida.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebida[contador])

    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1

# generar items Postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in listas_postres:


    # Crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador])

    postres.grid(row=contador, column=0, sticky=W)
    # Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1, width=6, state=DISABLED,
                                     textvariable=texto_postres[contador])

    cuadros_postres[contador].grid(row=contador, column=1)


    contador += 1




#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#Etiquetas de costos y campos de entrada comida
etiqueta_costos_comida = Label(panel_costos,
                               text='Costo Comida',
                               font=('Dosis', 12, 'bold'),
                               bg='blueViolet',
                               fg='white')
etiqueta_costos_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1)


#Etiquetas de costos y campos de entrada Bebida
etiqueta_costos_bebida = Label(panel_costos,
                               text='Costo Bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='blueViolet',
                               fg='white')
etiqueta_costos_bebida.grid(row=0, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1)



#Etiquetas de costos y campos de entrada Postres
etiqueta_costos_postres = Label(panel_costos,
                               text='Costo Postres',
                               font=('Dosis', 12, 'bold'),
                               bg='blueViolet',
                               fg='white')
etiqueta_costos_postres.grid(row=0, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,column=1)

#evitar que la pantalla se cierre
aplicacion.mainloop()
