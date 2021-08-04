print ("ingresa un numero menor a 9")                                           #se pide un numero menor a 9
numero = float(input())                                                         #se guarda este numero como un float osea (0.0)
while numero <= 9:                                                              #e inicia un bucle super bestial
    numero += 1.0                                                               #se le suma 1.0 a nuestro valor hasta que llegue a cumplir el valor superior a 9 y se rompa este bucle
    if (numero == 6):   #esta parte es un (y si llega a seis pasa a lo siguiente)
        print (f"a interar se ha dicho van = {numero}")                             #se imprime cada cambio que posee nuestra variable integrada
else:                                                                           #ya no se cumple el bucle entonces salimos con else
    print (f" hemos terminado de interar \n ahora el digito vale {numero}")     #imprimimos el valor de salida que ha resultado ser 10.0 (recordemos que estamos trabajando con floats)
################################################################################################################################################################
print ("es momento de sacar un valor en un solo bucle introdece un numero que sera multiplicado por 2 y si su resultado es menor a 100 te lo diremos ")
multiplicacion = int(input())
while multiplicacion <=100:
    multiplicacion * 2
    print (f"tu multiplicacion posee un valor inferior o igual a 100 este es el resultado {multiplicacion}")
    break    