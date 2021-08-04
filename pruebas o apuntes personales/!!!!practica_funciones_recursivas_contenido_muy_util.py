def atras (segundos ):                             #generando una una funcion llamada atras que posee segundos
    segundos -=1                                   #sele dictamina a segundo el restar -1 todo el tiempo a el valor que posee
    if segundos >= 0:                              #si segundos es mayor o igual a 0 
        print(segundos)                            #imprimir segundos mientras sea mayor o igual a 0
        atras(segundos)                            #ahora guardamos la el valor de segundos en atras para ir restando
    else:                                          #si no se cumple lo anterior
        print("termino de cuaenta atras")          #imprimimos que ha termiando todo el proceso de cuenta

print(atras(10))                                   #le damos segundos a atras

e = int("15")
print(e)

conversor_binario = bin(12)
print(conversor_binario)

conversor_hexadecimal = hex(15)
print(conversor_hexadecimal)

conversor_positivo = abs(-10)
print(conversor_positivo)

redondeador = round(5.5)
print(redondeador)

contador_de_cadena = len("catalina")
print(contador_de_cadena)

print(help())#la ayuda nunca es mala