from collections import deque                   #la cola es una funcioen que no posee muchos usos por ende se debe llamar        
colas = deque                                   #le ponemos un nombre a esto para el ejemplo 
colas                                           #llamamos a colas
print(type(colas))                              #imprimimos a cola con un type para saber que tipo de funcion es 
colas = deque(["catalina","arepas","pocoyo"])   #confirmamos el tipo de variable que manejamos y lo rellenamos con una lista
print(colas)                                    #imprimimos la lista para visualizar lo que haremos         
colas.pop()                                     #elminamos la primera parte de la cola lo que seria el contrario a pilas
print(colas)                                    #visualisamos 
colas.popleft()
print(colas)
