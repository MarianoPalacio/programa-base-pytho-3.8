#Unidad 6 - Nivel Avanzado - TP Final

def deco_insertar (f):
    def envoltura(*args):
        print('Nuevo registro guardado.')
        f(*args)
    return envoltura


def deco_eliminar(f):
    def envoltura(*args):
        print('Registro borrado.')
        f(*args)
    return envoltura


def deco_modificar(f):
    def envoltura(*args):
        print('Registro actualizado')
        f(*args)
    return envoltura
