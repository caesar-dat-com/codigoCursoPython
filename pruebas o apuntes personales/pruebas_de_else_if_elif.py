print ("que edad posee catalina en fecha de creacion de este archivo?") #se imprime una pregunta SERIA
catalina = int(input())                                                 #se almacena el valor ingresado como un int para manejarlo como un numero entero
if catalina == 20:                                                      #se compara el valor ingresado con el valor estipulado 
    print(f"exacto catalina posee {catalina} años")                     #se imprime esto si el valor es igual a 20
else:                                                                   #siempre los 2 puntos, SIEMPRE
    print(f"lo has errado catalina no posee {catalina} años")           #se imprime esto si el valor no es igual a 20 
#####################################################################################################################
print ("cual es el color favorito de cata? ")                                                   #se imprime otra pregunta SERIA
color = str(input())                                                                            #se almacena el valor ingresado como un str para manejarlo como un texto 
if color == "ROSADO" or color == "NEGRO":                                                       #se compara (color) para ver si es ROSADO o NEGRO
    print(f"exactisimo el color favorito de catalina es {color}")                               #se imprime si lo ingresado cumple con alguno de los 2 puntos
elif color == "tu cola":                                                                        #si no se cumple el primer if se seguira esta regla de (tu cola)
    print(f"para fiera que te pasa acabas de poner {color} en donde deberias poner un color")   #se imprime si lo ingresado cumple con el valor ingresado
else:                                                                                           #si no se cumple nada pasamos a el else 
    print(f"lo lamento a cata no le gusta el {color}")                                          #imprimimos mensaje de no cumplimiento con los requirimientos
    
