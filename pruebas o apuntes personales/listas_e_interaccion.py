numeros = [1,2,3,4,9,6,7,8,9]#lista con error 
numeros[4] = 5               #ordenamos que aquel objeto en lugar 4 cambie a otro valor 
print (numeros)
numeros[4] = "catalina guerrero revelo" # no solo debe ser un numero o (int) tambien podemos meter un string
print (numeros)
numeros.append(10)          #append hace lo que dice su nombre agrega algo al final de la lista en este caso el numerop 10 
print (numeros)
numeros.append(10+1)        #tambien se puede interactuar con ello como el agregarle algo extra en este caso una suma 
print (numeros)
palabras = ["catalina","guerrero","revelo"] #lista de palabras
todo = [numeros,palabras]   #concatenacion de plabras y numeros
print (todo)                #mostramos todo
print (todo[0])             #mostramos solo numeros
print (todo[1])             #mostramos solo palabras
print (todo[0][0])          #mostramos solo el primer digito de numeros 
print (todo[1][0])          #mostramos solo el primer digito de palabras