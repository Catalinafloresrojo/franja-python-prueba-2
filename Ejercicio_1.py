#Escribir un programa que contenga una función que reciba una lista de palabras
# y devuelva la más larga.  Imprimir por pantalla la palabra resultante.

def palabra_mas_larga(resultado):
    palabra_mas_grande = len(resultado[0])
    palabra_a_mostrar = resultado[0]

    for palabra in resultado:
        if palabra_mas_grande <= len(palabra):
            palabra_a_mostrar = palabra 
            palabra_mas_grande = len(palabra)
        else: 
            palabra_a_mostrar = palabra_a_mostrar
            
    print (palabra_a_mostrar)