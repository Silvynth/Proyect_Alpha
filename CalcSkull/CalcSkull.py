#Calculadora de personajes de skullgirls
#librerias
import os

#Variable Bronces/plata/oro
B = 0
P = 0
O = 0

#Menu principal
def show_menu():
    print("Evolution skullgirls\n1. Plata\n2. Oro\n3. Diamante\n4. Salir")

def diamond():
    print("El costo a evolucionar sera 5 de de oro\el proceso de calculo es simple\nIntrodusca la cantidad de personajes de\nBronce\nPlata\nOro")
    input("Bronce: ")
    input("Plata: ")
    input("Oro: ")

def info():
    print("Helo world")

def clean_console():
    os.system('cls' if os.name == 'nt' else 'clear')


#Codigo a ejecucin primaria
def main():
    clean_console()
    while True:
        show_menu()
        opcion = input("Seleccionar opción:")

        if opcion == "1":
            diamond()
        elif opcion == "2":
            info()
        elif opcion == "3":
            break
        else:
            clean_console()
            print("Opcin invalida\nporfavor vuelva a digitar un digito Ej:\n1 / 2 / 3\n==================================================")
            
            
if __name__ == "__main__":
    main()