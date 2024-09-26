from autos import *
from esperar import esperar_enter

def menu():

    while True:
        print("""
                    Menú de Opciones:
        ============================================
        1. Mostrar el auto más caro
        2. Mostrar la moto más barata
        3. Mostrar marcas que fabrican autos y motos
        4. Consultar los 3 valores al mismo tiempo
        5. Salir
        """)

        opcion = input("Elige una opción: ")
        while opcion not in ["1", "2", "3", "4", "5"]:
            print("Opción inválida. Por favor, intente nuevamente.")
            opcion = input("Elige una opción: ")

        if opcion == "1":
            marca_auto, precio_auto = auto_mas_caro(autos, precios_autos)
            print(f"El auto más caro es {marca_auto} con un precio de ${precio_auto}.")
        
        elif opcion == "2":
            marca_moto, precio_moto = moto_mas_barata(motos, precios_motos)
            print(f"La moto más barata es {marca_moto} con un precio de ${precio_moto}.")
        
        elif opcion == "3":
            comunes = marcas_autos_motos(autos, motos)
            if comunes:
                print(f"Las marcas que fabrican autos y motos son: {', '.join(comunes)}")
            else:
                print("No hay marcas que fabriquen tanto autos como motos.")
        
        elif opcion == "4":
            # Consultar los 3 valores al mismo tiempo
            marca_auto, precio_auto = auto_mas_caro(autos, precios_autos)
            marca_moto, precio_moto = moto_mas_barata(motos, precios_motos)
            comunes = marcas_autos_motos(autos, motos)

            print(f"El auto más caro es {marca_auto} con un precio de ${precio_auto}.")
            print(f"La moto más barata es {marca_moto} con un precio de ${precio_moto}.")
            if comunes:
                print(f"Las marcas que fabrican autos y motos son: {', '.join(comunes)}")
            else:
                print("No hay marcas que fabriquen tanto autos como motos.")
        
        elif opcion == "5":
            print("Gracias, por su preferencia.")
            break

        # Pausa antes de mostrar el menú nuevamente
        esperar_enter() 
        print("\n" + "=" * 60)
