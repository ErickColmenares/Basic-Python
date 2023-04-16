"""
Este programa solicita nombres y edades de compañeros, los ordena de menor a mayor
donde el menor de ellos es asistente del profesor.
"""
# Función para ingresar al asistente y al profesor por la edad

def obtener_compañero(cantidad_de_compañeros):
    compañeros=[]   #Se crea la lista para rellenar con los datos 
    
    for i in range(cantidad_de_compañeros): #Con un ciclo se crea la lista
        nombre=input('Ingrese el nombre: ')
        edad=int(input('Ingrese edad: '))
        compañero=(nombre,edad)
        compañeros.append(compañero)
    
    compañeros.sort(key=lambda x:x[1])         #Se ordenan a los compañeros de menor a mayor
    
    asistente=compañeros[0][0]                #La persona más joven el asistente
    profesor=compañeros[-1][0]                #La persona más grande es el profesor
    
    return asistente,profesor

asistente,profesor=obtener_compañero(13)         #Se despliega el resultado en pantalla
print(f'El profesor es: {profesor} y el asistente: {asistente}')
    
    
