#Calculadora matematica v0.00.1

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#variables De momento no hay
Menu = 3
v1 = 0
v2 = 1

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Menu
print("CalcSlv v0.00.1\nFunciones disponibles\n1.- Sumas\n2.- Restas\n3.- Salir")
Menu = input("Ingrese funcion a usar: ")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Resultado
while True:
    if Menu == '1':
        v1 = int(input("Ingrese primer digito: "))
        v2 = int(input("Ingrese segundo digito: "))
        Rs = v1+v2
        print(Rs)

    elif Menu == '2':
        v1 = int(input("Ingrese primer digito: "))
        v2 = int(input("Ingrese segundo digito: "))
        Rs = v1-v2
        print(Rs)

    elif  Menu == '3':
        break

    else:
        print("Porfavor vuelva a seleccionar una opcion valida")
        break
        
