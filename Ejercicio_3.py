#Escribir una función que calcule el área de un círculo y 
# otra que calcule el volumen de un cilindro usando la primera función.

def valor_de_pi():
    return 3.1415

pi = valor_de_pi()

def areacirculo(radio):
    
    area = pi * radio**2

def volumencilindro(radio,altura):
    volumen = areacirculo(radio) * altura 
    return volumen 

def main ():
    print (areacirculo(10))
    print (volumencilindro(3,10))

if __name__ == '__main__':
    main()
    


    