# Escriba un programa que pida dos palabras y diga si riman o no. 
# Si coinciden las últimas tres letras tiene que decir que riman. 
# Si coinciden sólo las últimas dos tiene que decir que riman un poco.
#  Y si no coinciden, decir que no riman.
#  Validar que las palabras tengan al menos tres letras. Nota: Utilizar slices

palabra1 = input("ingrese su primera: ")
palabra2 = input("ingrese su segunda palabra: ")

riman1= print (palabra1 [-3:])
riman2= print(palabra2[-3:])
riman_un_poco1 = print(palabra1 [-2:])
riman_un_poco2 = print(palabra2[-2:])

if riman1 == riman2: 
    print("las 2 palabras riman")

elif riman_un_poco1 == riman_un_poco2:
    print("las palabras solo riman un poco")

else: 
    print("las palabras no riman ")

