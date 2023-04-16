"""
Este es un programa simple que muestra la serie de
Fibonacci hasta un número dado
"""



def fibonacci(num):  #Creamos la función
    a,b=0,1          #Inicializamos la lista con 2 números
    fibonacci_lista=[0]  #Icluimos el 0 como punto de partida
    for i in range(num):
        if b>num: return fibonacci_lista   #Establecemos el límite
        else:
            fibonacci_lista.append(b)  #Añadimos el número correspondiente a la lista
            a,b=b,a+b                   #Reemplazamos los número scon los 2 siguientes 
        
 
resultado =fibonacci(34)    #Colocamos el número hasta donde obtendremos la serie
print(resultado)   #Imprimimos el resultado