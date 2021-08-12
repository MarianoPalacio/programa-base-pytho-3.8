from tkinter import *
from guardar import *
from base_datos import *
#from decogral import *
from observador import *


def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)

#@deco_insertar
def guarda(variables, popupGuardar, elobjeto):
    popupGuardar.destroy()

    lista = []
    for variable in variables:
        lista.append(variable.get())

    product = producto()
    product.titulo = lista[0]
    product.descripcion = lista[1]
    product.save()
    elobjeto.observadorA.update()
    elobjeto.mostrar()


def guardar(objeto):
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)

    Button(popupGuardar, text='guardar', command=(lambda: guarda(vars_guardar, popupGuardar, objeto))).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
