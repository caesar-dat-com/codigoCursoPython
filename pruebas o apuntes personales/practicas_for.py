lista = [1,2,3,4,5,6,7,8,9]     #generamos una lista de numeros enteros usando [] y espaciando con comillas para delimitar su ubicacion
indice = 0                      #generamos un indice el cual posee un valor de cero 
for recorrer in lista:          #pasa por cada digito dentro de lista 
    lista[indice] *= 10         #me multiplica los numeros de la lista x 10 
    indice += 1                 #le da un valor superior a indice y lo renueva
print(lista)                    #me imprime los nuevoos valores de lista
