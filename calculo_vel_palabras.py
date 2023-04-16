""""
Este programa simple calcula el tiempo en que tardarías en decir una palabra
"""

frase=input('Di una frase para calcular el tiempo en decirla:')  #El usuario ingresa la frase
palabras_separadas=frase.split(" ")                              #La frase se separa en palabras
cantidad_de_palabras=len(palabras_separadas)                     #Se obtiene la cantidad de palabras en la oración

if cantidad_de_palabras > 120:                                    #Si la cantidad de palabras excede las 120 solo se le informa que la oración es muy larga
    print('Espera, son muchas palabras')

print(f'dijiste {cantidad_de_palabras} palabras y tardarías {cantidad_de_palabras/2} segundos en decirlo')  #Se imprime el resultado en pantalla
print(f'Alguien que habla un 30% más lento lo diría {cantidad_de_palabras*100//2*1.3/100} segundos')

