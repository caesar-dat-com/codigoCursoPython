class encapsulamiento:
    __privado_atri = "soy un  atributo que no vas a poder acceder desde afuera de la clase"

    def __privado_met(self):
        print("soy un metodo que no vas a poder acceder desde afuera de la clase")

    def publico_atri(self):
        return self.__privado_atri

    def public_met(self):
        return self.__privado_met()    

e = encapsulamiento()

#e.__privado_atri()

#e.__privado_met()

e.publico_atri()

e.public_met()