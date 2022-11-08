class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

def aprovado(nom, nota):
    if (float(nota) >= 6):
        return True
    else:
        return False

a = Alumno(" ", " ")

a.nombre = input("Escribe tu nombre: ")

a.nota = input("Escribe tu nota: ")

if aprovado(a.nombre, a.nota):
    print(a.nombre, "aprovaste con una calificación de:", a.nota)
else:
    print(a.nombre, "reprovaste con una calificación de:", a.nota)


