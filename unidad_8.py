# Unidad 6 - Nivel Avanzado - TP Final
# Entrega Mariano Palacio

from tkinter import *
from temas.OpcionTemas import EleccionTema
from tkinter.messagebox import *
from modificarModal import *
from eliminarModal import *
from guardarModal import *
from decogral import *
from observador import *
from tkinter import ttk
import base_datos
import val


class Producto(Tema):

    def __init__(self, window):
        # Ventana principal
        self.observadorA = ConcreteObserverA(self)
        self.observadorB = ConcreteObserverB(self)
        self.observadorC = ConcreteObserverC(self)
        self.estado = None
        self.root = window
        self.root.title("Menú Seleccion")

        titulo = Label(self.root, text="Ingrese sus datos",
                       bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        titulo.grid(row=0, column=0, columnspan=4,
                    padx=1, pady=1, sticky=W + E)

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val = StringVar(), StringVar()
        w_ancho = 20

        self.tree = ttk.Treeview(height=10, columns=3)
        self.tree["columns"] = ("one", "three", "four")
        self.tree.grid(row=7, column=0, columnspan=3)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("one", text='Título', anchor=CENTER)
        self.tree.heading("three", text='Descripción', anchor=CENTER)
        self.tree.heading("four", text='Prueba', anchor=CENTER)
        # Boton Agregar Producto
        divisor = Label(self.root, text="Registros existentes en su base", bg="DarkOrchid3",
                        fg="thistle1", height=1, width=60).grid(row=6, columnspan=3, sticky=W + E)

        Button(self.root, text="Ayuda",
               command=lambda: self.Ayuda()).grid(row=5, column=1)
        Button(self.root, text='Guardar',
               command=lambda: self.pasarObjetoGuardar()).grid(row=11, column=0)
        Button(self.root, text='Eliminar',
               command=lambda: self.pasarObjetoEliminar()).grid(row=11, column=1)
        Button(self.root, text='Modificar',
               command=lambda: self.pasarObjetoModificar()).grid(row=11, column=2)

        # #####################################################
        # ################ TEMAS #############3#################
        # #####################################################3
        self.temas_opciones = Frame(
            self.root, bg="red", borderwidth=2, relief=RAISED)
        self.temas_opciones.grid(
            row=12, column=0, columnspan=4, padx=1, pady=1, sticky=W + E)

        ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        # Agrego variables de contorl para eleccion de tema
        self.tema_option = IntVar(value=0)

        Label(self.temas_opciones, borderwidth=4, relief=RAISED,
              text="Temas", bg="#222", fg="OrangeRed", ).pack(fill=X)
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(self.temas_opciones, text=str(opcion), indicatoron=1, value=int(
                opcion[-1]) - 1, variable=self.tema_option, bg="#222", fg="OrangeRed", command=self.bg_fg_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

    def setestado(self, value):
        self.estado = value
        self.notificar()

    def getestado(self):
        return self.estado

    def Ayuda(self,):
        showinfo('Ayuda', 'Para insertar un registro nuevo, dar click en el botón Guardar, los resultados almacenados previamente se visualizaran en pantalla.Para eliminar un registro, presione eliminar y seleccione el ID deseado')

    def pasarObjetoGuardar(self, ):
        # print(self)
        guardar(self)
        #self.observadorA.update()

    def pasarObjetoEliminar(self, ):
        # print(self)
        eliminar(self)

    def pasarObjetoModificar(self, ):
        # print(self)
        modificar(self)

    def bg_fg_option(self):
        self.temas_opciones["bg"] = EleccionTema(self.tema_option.get())
        self.root["bg"] = EleccionTema(self.tema_option.get())

    # #####################################################
    # ################ FIN DE TEMAS #######################
    # #####################################################

    # obteniendo información
    def mostrar(self, ):
        # limpieza de tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Agrego los resultados del alta
        resultado = base_datos.producto.select()
        for fila in resultado:
            self.tree.insert('', 0, text=fila.id, values=(
                fila.titulo, fila.descripcion, fila))

    def alta(self, ):
        cadena = self.a_val.get()  # obtenemos la cadena del campo de texto
        if val.validar(cadena) == "true":
            print("validado")

            datos = (self.a_val.get(), self.b_val.get())
            insertar = base_datos.producto()
            insertar.titulo = datos[0]
            insertar.descripcion = datos[1]
            insertar.save()
        else:
            showinfo('Verificar', 'Los datos ingresados no son compatibles.')
        self.mostrar()


if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    application.mostrar()
    window.mainloop()
