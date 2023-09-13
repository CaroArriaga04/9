import datetime
import re
from tabulate import tabulate

folio_actual = 0
class Nota:
    def __init__(self, cliente, fecha):
        global folio_actual
        folio_actual += 1
        self.folio = folio_actual
        self.fecha = fecha
        self.cliente = cliente
        self.servicios = []
        self.cancelada = False
    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
    def calcular_monto_total(self):
        total = sum(servicio.costo for servicio in self.servicios)
        return total
    
class Servicio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

notas = []

def registrar_nota():    
    hoy = datetime.date.today()
    while True:
        fecha = input("\nIngresa la fecha (dd/mm/aaaa): ")
        try:
            fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            if fecha <= hoy:
                break
            else:
                print("\n* LA FECHA NO PUEDE SER POSTERIOR A LA ACTUAL, INGRESE NUEVAMENTE *")
        except Exception:
            print("\n* FECHA NO INGRESADA O INVALIDA, INGRESE NUEVAMENTE *")
    while True:
      cliente = input("\nNombre del cliente: ")
      if cliente == "":
        print ("\n* INGRESE UN NOMBRE PARA EL REGISTRO DE LA NOTA *")
        continue
      elif not (bool(re.search('^[a-zA-Z]+$', cliente))):
        print ("\n* NOMBRE NO VALIDO, INGRESE NUEVAMENTE *")
        continue
      else:
        break
    nota = Nota(cliente,fecha)
    servicio_agregado = False
    while True:
        nombre_servicio = input("\nNombre del servicio requerido (f para finalizar)): ")
        if nombre_servicio.lower() == "f":
            if servicio_agregado:
                break
            else:
                print("\n* PARA FINALIZAR DEBE AGREGAR MINIMO UN SERVICIO *")
                continue
        elif nombre_servicio == "":
          print ("\n * INGRESE EL SERVICIO REQUERIDO * ")
          continue
        elif not (bool(re.search('^[a-zA-Z]+$', nombre_servicio))):
          print ("\n* SERVICIO NO VALIDO, INGRESE NUEVAMENTE *")
          continue
        while True:
            costo_servicio = input("\nCosto del servicio: ")
            if costo_servicio == "":
                print ("\n* NO SE PERIMTE LA OMICION DEL COSTO *")
                continue
            elif not (bool(re.match("^[0-9]+(\.[0-9]+)?$", costo_servicio))):
                print ("\n* COSTO NO VALIDO, INGRESE NUEVAMENTE *")
                continue
            costo_servicio = float(costo_servicio)
            if costo_servicio <= 0:
                print("\n* EL COSTO DEL SERVICIO DEBE SER MAYOR A 0, INGRESE NUEVAMENTE *")
                continue
            else:
                servicio = Servicio(nombre_servicio, costo_servicio)
                nota.agregar_servicio(servicio)
                servicio_agregado = True
                break
    notas.append(nota)
    monto_total = nota.calcular_monto_total()
    print("\n---------------NOTA-------------")
    print(f"Folio: {nota.folio}")
    print(f"Fecha: {nota.fecha}")
    print(f"Cliente: {nota.cliente}")
    print("--------------------------------")
    print("Servicio:")
    for servicio in nota.servicios:
        print(f"- {servicio.nombre}: ${servicio.costo:.2f}")
    print("--------------------------------")
    print(f"Total a pagar: ${monto_total:.2f}")


def consulta_por_periodo():
    while True:
        try:
            fecha_inicial = input("Ingresa la fecha inicial (dd/mm/aaaa): ")
            fecha_final = input("Ingresa la fecha final (dd/mm/aaaa): ")
            fecha_inicial = datetime.datetime.strptime(fecha_inicial, "%d/%m/%Y").date()
            fecha_final = datetime.datetime.strptime(fecha_final, "%d/%m/%Y").date()
        except Exception:
            print("Las fechas ingresadas deben estar en formato dd/mm/aaaa")
        else: 
            notas_no_canceladas = [n for n in notas if not n.cancelada]
            notas_por_periodo = [n for n in notas_no_canceladas if fecha_inicial <= datetime.datetime.strptime(n.fecha, "%d/%m/%Y").date() <= fecha_final]
            if notas_por_periodo:
                print("\n---------NOTAS POR PERIODO---------")
                informacion = [[n.folio, n.fecha, n.cliente] for n in notas_por_periodo]
                titulos = ["Folio", "Fecha", "Cliente"]
                print(tabulate(informacion, titulos, tablefmt="fancy_grid"))
            else:
                print("\n** No hay notas registradas en el periodo ingresado **")
            break

def consulta_por_folio():
    folio = input("Ingresa el folio de la nota solicitada: ")
    nota_encontrada = False
    for nota in notas:
        if nota.folio == folio and not nota.cancelada:
            monto_total = nota.calcular_monto_total()
            print("\n---------------NOTA-------------")
            print(f"Folio: {nota.folio}")
            print(f"Fecha: {nota.fecha}")
            print(f"Cliente: {nota.cliente}")
            print("--------------------------------")
            print("Servicio:")
            for servicio in nota.servicios:
                print(f"- {servicio.nombre}: ${servicio.costo:.2f}")
            print("--------------------------------")
            print(f"Total a pagar: ${monto_total:.2f}")
            nota_encontrada = True
    if not nota_encontrada:
        print("** El folio indicado no existe o corresponde a una nota cancelada **")

def cancelar_nota():
    while True:
        cancelado = input("Ingresa el folio de la nota a cancelar (o '0' para regresar al menú principal): ")
        if cancelado == '0':
            break
        nota_a_cancelar = None 
        for nota in notas:
            if nota.folio == cancelado:
                nota_a_cancelar = nota
                break
        if nota_a_cancelar:
            monto_total = nota_a_cancelar.calcular_monto_total()
            print("\n---------NOTA A CANCELAR--------")
            print(f"Folio: {nota_a_cancelar.folio}")
            print(f"Fecha: {nota_a_cancelar.fecha}")
            print(f"Cliente: {nota_a_cancelar.cliente}")
            print("--------------------------------")
            print("Servicio:")
            for servicio in nota_a_cancelar.servicios:
                print(f"- {servicio.nombre}: ${servicio.costo:.2f}")
                print("--------------------------------")
            print(f"Total a pagar: ${monto_total:.2f}")
            confirmacion = input("\n¿Estás seguro de que quieres cancelar esta nota? (Si/No): ")
            while True:
                if confirmacion.upper() in ["SI", "S"]:
                    print("\n*** NOTA CANCELADA ***")
                    nota_a_cancelar.cancelada = True
                    break
                elif confirmacion.upper() in ["NO", "N"]:
                    print("\n*** NOTA NO CANCELADA ***")
                    break
                else:
                    print("La respuesta ingresada debe ser 'Si' o 'No'.")
                    confirmacion = input("\n¿Estás seguro de que quieres cancelar esta nota? (Si/No): ")
        else:
            print("\n** La nota ingresada no se encuentra en el sistema **")

def recuperar_nota():
    while True:
        recuperar = input("Ingresa el folio de la nota a recuperar (o '0' para regresar al menú principal): ")
        if recuperar == '0':
            break
        nota_recuperada = None 
        for nota in notas:
            if nota.folio == recuperar:
                nota_recuperada = nota
                break
        if nota_recuperada:
            print("\n---------NOTA RECUPERADA--------")
            print(f"Folio: {nota_recuperada.folio}")
            print(f"Fecha: {nota_recuperada.fecha}")
            print(f"Cliente: {nota_recuperada.cliente}")
            print("--------------------------------")
            print("Servicio:")
            for servicio in nota_recuperada.servicios:
                print(f"- {servicio.nombre}: ${servicio.costo:.2f}")
                print("--------------------------------")
        else:
            print("\n** La nota ingresada no se encuentra en el sistema **")


print("\n---------------TALLER MECANICO--------------")
print("   BIENVENIDO A NUESTRO SISTEMA DE NOTAS    ")
print("--------------------------------------------")

while True:
    print("\nMENU")
    print("1. Registrar nota")
    print("2. Consultas y Reportes")
    print("3. Cancelar nota")
    print("4. Recuperar nota")
    print("5. Salir del sistema")

    opcion = input("Elige una opcion: ")
    if opcion == "":
        print("\n* OPCION OMITIDA, INGRESE UNA OPCION *")
        continue

    if opcion == "1":
        while True:
            confirmar = input("\n¿Estas seguro de realizar un registro (Sí/No)?: ")
            if confirmar == "":
                print("\n* RESPUESTA OMITIDA, INGRESE RESPUESTA *")
                continue
            elif confirmar.upper() in ("N", "NO"):
                break
            elif confirmar.upper() in ("S", "SI"):
                print("\nDe acuerdo.")
                registrar_nota()
                break

    elif opcion == "2":
        confirmar = input("¿Estas seguro de que quieres realizar una consulta (Solamente Sí/No)?: ")
        if confirmar.upper() in ("S", "SI"):
            print("De acuerdo.")
            while True:
                print("\n----CONSULTAS Y REPORTES----")
                print("1. Consulta por periodo\n2. Consulta por folio\n3. Regresar al menu principal ")
                sub_opcion = input("Elige una opcion: ")
                if sub_opcion == "1":
                    consulta_por_periodo()
                elif sub_opcion == "2":
                    consulta_por_folio()
                elif sub_opcion == "3":
                    print("***OK***")
                    break
                else:
                    print("\n** Opcion no valida, ingrese nuevamente **")

    elif opcion == "3":
        confirmar = input("¿Estas seguro de que quieres cancelar una nota (Solamente Sí/No)?: ")
        if confirmar.upper() in ("S", "SI"):
            print("De acuerdo.")
            cancelar_nota()

    elif opcion == "4":
        confirmar = input("¿Estas seguro de que quieres recuperar una nota (Solamente Sí/No)?: ")
        if confirmar.upper() in ("S", "SI"):
            print("De acuerdo.")
            recuperar_nota()

    elif opcion == "5":
        salida = input("¿Deseas salir del programa (Solamente Sí/No)?: ")
        if salida.upper() in ("S", "SI"):
            print("De acuerdo. Saliendo del programa...")
            break
        elif salida.upper() in ("N", "NO"):
            print("***No se saldrá del programa, se le regresará al menú principal.***")
        else:
            print("En esta respuesta solo se acepta Sí o No")

    else:
        print("\n* OPCION NO VALIDA, INGRESE NUEVAMENTE *")
        continue
