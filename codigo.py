class nota:
    def __init__(self, folio, fecha, cliente, monto_pagar, servicio_realizado):
        self.folio = folio
        self.fecha = fecha
        self.cliente = cliente
        self.monto_pagar = monto_pagar
        self.servicio_realizado = servicio_realizado
    
    def registrar_nota():
        pass

    def consultas_reportes():
        print("Menu de opciones")
        opcion = input("Elige una opcion \n1.Consulta por periodo\n2.Consulta por folio\n")
        if opcion == 1:
            pass

    def cancelar_nota():
        pass

    def recuperar_nota():
        pass
print("*** TALLER MECANICO ***")
print("*** BIENVENIDO A NUESTRO SISTEMA DE NOTAS ***")

while True:
    print("MENU")
    print("1. Registrar nota")
    print("2. Consultas y Reportes")
    print("3. Cancelar nota")
    print("4. Recuperar nota")
    print("5. Salir del sistema")

    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        break


    