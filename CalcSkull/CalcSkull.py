class Recursos:
    def __init__(self):
        self.bronces = 0  # Bronces
        self.platas = 0   # Platas
        self.oros = 0     # Oros
        self.diamantes = 0  # Diamantes

    def convertir_bronces_a_platas(self, bronces):
        platas_obtenidas = bronces // 4
        self.platas += platas_obtenidas
        return platas_obtenidas

    def convertir_platas_a_oros(self, platas):
        oros_obtenidos = platas // 5
        self.oros += oros_obtenidos
        return oros_obtenidos

    def convertir_oros_a_diamantes(self, oros):
        diamantes_obtenidos = oros // 6
        self.diamantes += diamantes_obtenidos
        return diamantes_obtenidos

    def mostrar_recursos(self):
        print(f"Recursos actuales:\nBronces: {self.bronces}, Platas: {self.platas}, Oros: {self.oros}, Diamantes: {self.diamantes}")


def mostrar_menu():
    print("\n----- Menú -----")
    print("1. Bronce -> Plata")
    print("2. Plata -> Oro")
    print("3. Oro -> Diamante")
    print("4. Mostrar recursos actuales")
    print("5. Salir")


def main():
    recursos = Recursos()

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1-5): "))

            if opcion == 1:
                bronces_a_evolucionar = int(input("Ingresa el número de bronces a convertir a platas: "))
                if bronces_a_evolucion <= recursos.bronces:
                    recursos.bronces -= bronces_a_evolucion
                    platas_obtenidas = recursos.convertir_bronces_a_platas(bronces_a_evolucion)
                    print(f"Se han obtenido {platas_obtenidas} platas.")
                else:
                    print("No tienes suficientes bronces.")

            elif opcion == 2:
                platas_a_evolucionar = int(input("Ingresa el número de platas a convertir a oros: "))
                if platas_a_evolucionar <= recursos.platas:
                    recursos.platas -= platas_a_evolucionar
                    oros_obtenidos = recursos.convertir_platas_a_oros(platas_a_evolucionar)
                    print(f"Se han obtenido {oros_obtenidos} oros.")
                else:
                    print("No tienes suficientes platas.")

            elif opcion == 3:
                oros_a_evolucionar = int(input("Ingresa el número de oros a convertir a diamantes: "))
                if oros_a_evolucionar <= recursos.oros:
                    recursos.oros -= oros_a_evolucionar
                    diamantes_obtenidos = recursos.convertir_oros_a_diamantes(oros_a_evolucionar)
                    print(f"Se han obtenido {diamantes_obtenidos} diamantes.")
                else:
                    print("No tienes suficientes oros.")

            elif opcion == 4:
                recursos.mostrar_recursos()
                
            elif opcion == 5:
                print("Saliendo del programa...")
                break
                
            else:
                print("Opción no válida. Por favor, selecciona una opción correcta.")
                
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
