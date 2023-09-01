import clases

print("*** TALLER MECANICO ***")
print("*** BIENVENIDO A NUESTRO SISTEMA DE NOTAS ***")

while True:
    print("\nMENU")
    print("1. Registrar nota")
    print("2. Consultas y Reportes")
    print("3. Cancelar nota")
    print("4. Recuperar nota")
    print("5. Salir del sistema")

    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        clases.registrar_nota()
    elif opcion == 2:
        print("\n** CONSULTAS Y REPORTES **")
        print("1.Consulta por periodo\n2.Consulta por folio ")
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            clases.consulta_por_periodo()
        elif opcion == "2":
            clases.consulta_por_folio()
        else:
            print("Opcion no valida")
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        if input("Deseas salir del programa: ").upper() in ("S", "SI"):
            break


    
