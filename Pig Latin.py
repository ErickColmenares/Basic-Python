'''
Es u lenguaje inventado que altera las palabras.
Las terminadas en vocal, se les agrega yay o ay 
Dependiendo de su terminación. 
'''
print('Ingresa un mensaje para traducirlo a "Pig Latin"')

msg=input()

vocales=('a','e','i','o','u')

pigLatin=[]

for palabra in msg.split():
    prefixNoLetras=''
    while len(palabra)>0 and not palabra[0].isalpha():
        prefixNoLetras+=palabra[0]
        palabra=palabra[1:]
    if len(palabra)==0:
        pigLatin.append(prefixNoLetras)
        continue
    sufijoNoLetras=''
    while not palabra[-1].isalpha():
        sufijoNoLetras+=palabra[-1]
        palabra=palabra[:-1]
    
    mayus=palabra.isupper()
    titulo=palabra.istitle()
    
    palabra=palabra.lower()
    
    prefixCons=''
    while len(palabra)>0 and not palabra[0] in vocales:
        prefixCons+=palabra[0]
        palabra=palabra[1:]
    
    if prefixCons!='':
        palabra+=prefixCons + 'ay'
    else:
        palabra+='yay'
    
    if mayus:
        palabra=palabra.upper()
    if titulo:
        palabra=palabra.title()
    
    pigLatin.append(prefixNoLetras+palabra+sufijoNoLetras)


print(' '. join(pigLatin))
