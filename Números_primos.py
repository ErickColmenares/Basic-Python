"""
Este programa regresa una lista de números primos de acuerdo a un valor mínimo 
"""

def es_primo(num):  #Se crea la función que determina si es primo
    
    for i in range(2,num-1):   #Se recorre este rango de números
        if num%i==0: return False  #Si es divisible entre algún otro número no es primo
    return True


def primos_hasta(num): #La función crea la lista de números primos
    primos=[]
    for i in range(3,num+1):
        resultado = es_primo(i)  #Llamamos a la función que verifica si es primo
        if resultado == True: primos.append(i)  #Si lo es, se agrega a la lista
    return primos


resultado = primos_hasta(98)    
print(resultado)   #Se despliegan los datos en pantalla