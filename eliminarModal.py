# Unidad 6 - Nivel Avanzado - TP Final
from tkinter import *
from tkinter.messagebox import *
from eliminar import *
#from decogral import *
from observador import *
import base_datos


def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)

#@deco_eliminar
def elimina(variables, popupEliminar, elobjeto):
    popupEliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())

    try:
        registro = base_datos.producto.get(base_datos.producto.id == lista[0])
        registro.delete_instance()
        elobjeto.observadorB.update()
        elobjeto.mostrar()
        showinfo("Borrar", "Registro {} borrado exitosamente".format(registro))
    except:
        showinfo('Error', 'Debe seleccionar un Id valido')


def eliminar(objeto):
    popupEliminar = Toplevel()
    vars_eliminar = CrearFormEliminar(popupEliminar, campos)

    Button(popupEliminar, text='Eliminar', command=(
        lambda: elimina(vars_eliminar, popupEliminar, objeto))).pack()

    popupEliminar.grab_set()
    popupEliminar.focus_set()
    popupEliminar.wait_window()
