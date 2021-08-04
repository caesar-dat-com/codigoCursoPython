print ("esto esun repaso rapido")                                       #imprimimmos un titulo amigable
usuario = str(input("cula es tu nombre?"))                              #hacemos una variable para guardar un input
print (f"hola {usuario}")                                               #imprimimos la variable registrada
yes = str(input("presiona (y)"))                                        #pedimos una variable en str para luego compararla y entrar en un bucle
while yes == "y":                                                       #compramos la variable y entramos a el bucle 
    listas = []                                                         #hacemos uan variable con una uncion de lista
    print ("se bienbenido a introducir 5 valores numericos")            #pedimos  5 variables
    for i in range(5):                                                  #le decimos que repita esto 5 veces 
        listas.append(float(input("introduce un numero porfavor: ")))   #se introduce y se agrega a la lista cada valor
        print(f" numeros introducidos {listas}")                        #imprimimos el conteo que poseemos
    break                                                               #salimos del while y terminamos el codigo