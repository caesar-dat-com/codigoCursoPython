print ("ingresa un numero entre 5 y 15")    #pedimos al usuario introducir un valor numerico 
x = float(input())                          #convertimos el valor introducido en un float 

if x >= 5 and x <= 15:                        #usamos el if para decir si el numero introducido es mayor a 5 y menor que 15 
    print(f"el numero esta dentro del margen entre 5 y 15 \n el numero introducido es: { x }")      #se imprimira el texto positivo si cumple con las respectivas reglas 
else:                                                                                               #simepre poner los 2 puntos , SIMEPRE
    print(f"el numero no esta dentro del margen entre 5 y 15 \n el numero introducido es: { x }")   #se imprimira el texto negativo si NO cumple con las respectivas reglas 
############################################################################################################################################################################
print ("introduce el nombre de alguien al que ame este programador: ") #se pide que se ingrese una palabra y gracias a el str la guardamos como tal 
nombre = str(input())

if nombre == "catalina" or nombre == "juan carlos bodoque" or nombre == "azuka" :   #usamos el if para decir si lo digitado es compatible con lo que buscamos 
    print (f"exacto este programador adora mucho a3 {nombre}")                                          #se imprime el texto positivo 
else:                                                                                                   #simepre poner los 2 puntos , SIMEPRE
    print (f"lastima al parecer no conces lo suficiente a este programador \n dijitaste {nombre} ")     #se imprime el tecxto negativo 