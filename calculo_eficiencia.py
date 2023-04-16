
"""
En este programa se calculará la diferencia en tiempo de viaje entre un
un autobús a la cd de Oaxaca saliendo de Qro contra el viaje directo
en avión utilizando sentencias de nivel básico en python
"""



autobuses_min=int(input('Ingresa la duración minima de trayectoria que hace el autobús: '))           #Se ingresa el valor en horas de la duració minima del viaje
autobuses_max=int(input('Ingresa la duración máxima de trayectoria que hace el autobús: '))           #Se ingresa el valor en horas de la duració máxima del viaje
autobuses_promedio= int(input('Ingresa la duración promedio de trayectoria que hace el autobús: '))   #Se ingresa el valor promedio de la duració del viaje
viaje_avion=int(input('Ingresa la duración de trayectoria que se hace en avión: '))                   #El usuario ingresa las horas de viaje en avión


diferencia_con_minimo= 100-viaje_avion/autobuses_min*100                      #Se calcula el porcentaje de duración entre el viaje en avión y el autobus más rápido
diferencia_con_maximo= 100-viaje_avion*1000//autobuses_max/10                 #Se calcula el porcentaje de duración entre el viaje en avión y el autobus más lento
diferencia_con_promedio=100-viaje_avion/autobuses_promedio*100                #Se calcula el porcentaje de duración entre el viaje en avión y el autobus promedio

print('-----------------------')
print('El viaje en avión dura:')  #Se despliegan los datos en pantalla
print(f'- un {diferencia_con_minimo}% menos que el autobús más rápido')
print(f'- un {diferencia_con_maximo}% menos que el autobús más lento')
print(f'- un {diferencia_con_promedio}% menos que el autobús promedio')
print('----------------')

