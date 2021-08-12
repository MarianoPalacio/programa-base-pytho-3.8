from tkinter import *
from tkinter.messagebox import *
from modificar import *
#from decogral import *
from observador import *
import base_datos
import val



def show(variables, popupModificar):
    popupModificar.destroy()
    imprimir(variables)
    print(type(variables))

#@deco_modificar
def modifica(variables, popupModificar, elobjeto):
    popupModificar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    try:
        id = base_datos.producto.get(base_datos.producto.id == lista[0])
        if (val.validar(variable.get())) == "true":
            print("validado")
            actualizar = base_datos.producto.update(
                titulo=lista[1], descripcion=lista[2]).where(base_datos.producto.id == lista[0])
            actualizar.execute()
            elobjeto.observadorC.update()
            elobjeto.mostrar()
        else:
            showinfo('No Validado',
                     'ingrese datos, campo vacío o datos no válidos')
    except:
        showinfo('Error', 'Debe seleccionar un Id valido')


def modificar(objeto):
    popupModificar = Toplevel()
    vars_modificar = CrearFormModificar(popupModificar, campos)
    print(vars_modificar)
    Button(popupModificar, text='modificar', command=(
        lambda: modifica(vars_modificar, popupModificar, objeto))).pack()

    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()
