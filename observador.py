# Unidad 6 - Nivel Avanzado - TP Final
#Se toma ejemplo PDF
class Tema:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def modificar(self):
        for observador in self.observadores:
            observador.update()


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observadorA = obj
        self.observadorA.agregar(self)

    def update(self):
        print("Actualizado Concreto A")
        self.estado = self.observadorA.getestado()
        print("Alta Ok")


class ConcreteObserverB(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.agregar(self)

    def update(self):
        print("Actualizado Concreto B")
        self.estado = self.observadorB.getestado()
        print("Baja")


class ConcreteObserverC(Observador):
    def __init__(self, obj):
        self.observadorC = obj
        self.observadorC.agregar(self)

    def update(self):
        print("Actualizado Concreto C")
        self.estado = self.observadorC.getestado()
        print("Registro modificado")
