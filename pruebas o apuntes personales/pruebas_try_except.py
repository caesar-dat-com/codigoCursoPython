while (True):                                                               #un bucle nunca esta mal
    try:                                                                    #el try es para poner un porsiacaso 
        numero1 = float(input("ingresa un numero para realizar una suma"))    #una suma estandar 
        numero2 = float(input("ingresa otro numero para realizar la suma"))   #una suma estandar
        resultado = numero1 + numero2                                           
        print (f"el resultado de la suma es {resultado} ")                  #resutado de la suma
    except:                                                                 #esta es la excepcion                 
        print("metiste cualquier cosa animal, debias meter un numero")      #imprimimos el por siacaso
    else: 
        print("mira eres capaz de sumar, que orgullo ")
        break
    finally:
        print("hemos acabdo")