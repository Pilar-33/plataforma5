def esperar_enter():
    while True:
        entrada = input("\nPresiona Enter para continuar...")
        if entrada == "":  # Solo si se presiona Enter, sigue adelante
            break
        else:
            print("Por favor, presiona solo la tecla Enter para continuar.")
