class fabrica:
    def __init__(self,tiempo,nombre,ruedas):            #https://www.udemy.com/course/aprende-el-lenguaje-de-programacion-python3-practicando/learn/lecture/17796762#announcements
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("se creo el auto", self.nombre)

    def __str__(self):
        return "{} ({})".format(self.nombre,self.tiempo)
#########################################################
class listado:
    autos = []

    def __init__(self,autos=[]):
        self.autos = autos

    def fabricar(self,x):
        self.autos.append(x)

    def visualizar(self):
        for x in self.autos:
            print(x)
#########################################################
a = fabrica(10,"alvaro",4)

l = listado([a])

l.visualizar()

l.fabricar(fabrica(25,"estudiantes",2))

l.visualizar()