import shelve


# ##################################################################
# Defino base de datos
# ##################################################################
with shelve.open("OpcionTemas") as db:
    db["tema1"] = "#222"
    db["tema2"] = "blue"
    db["tema3"] = "OrangeRed"

# ##################################################################
# Defino comando para modificar propiedades de los temas
# ##################################################################

def EleccionTema (variable):
    with shelve.open("OpcionTemas") as db:
        if variable == 0:
            variable = "tema1"
        elif variable == 1:
            variable = "tema2"
        elif variable == 2:
            variable = "tema3"
        TemaSeleccionado = db[variable]
        return TemaSeleccionado



