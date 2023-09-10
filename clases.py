import datetime
import uuid
from tabulate import tabulate

class Nota:
    def __init__(self, cliente):
        self.folio = str(uuid.uuid4())[:5]
        self.fecha = datetime.date.today().strftime("%d/%m/%Y")
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
    cliente = input("Nombre del cliente: ")
    nota = Nota(cliente)
    while True:
        nombre_servicio = input("Nombre del servicio requerido (f para finalizar)): ")
        if nombre_servicio.lower() == "f":
            break
        costo_servicio = float(input("Costo del servicio: "))
        while costo_servicio <= 0:
            print("El costo debe ser mayor que 0.")
            costo_servicio = float(input("Ingrese el costo del servicio: "))
        servicio = Servicio(nombre_servicio, costo_servicio)
        nota.agregar_servicio(servicio)
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

def generar_folio():
    if not hasattr(generar_folio, "contador"):
        generar_folio.contador = 1
    folio = generar_folio.contador
    generar_folio.contador += 1
    return str(folio)

notas = []

class Nota:
    def __init__(self, folio, fecha, cliente, servicios):
        self.folio = folio
        self.fecha = fecha
        self.cliente = cliente
        self.servicios = servicios
        self.cancelada = False

    def calcular_monto_total(self):
        total = sum(servicio.costo for servicio in self.servicios)
        return total

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
while True:
    print("\n--- Menú ---")
    print("1. Cancelar Nota")
    print("2. Recuperar Nota")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        cancelar_nota()
    elif opcion == '2':
        recuperar_nota()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

from tabulate import tabulate

# Función para generar folios únicos y consecutivos
def generar_folio():
    if not hasattr(generar_folio, "contador"):
        generar_folio.contador = 1
    folio = generar_folio.contador
    generar_folio.contador += 1
    return str(folio)

# Lista para almacenar las notas
notas = []

class Nota:
    def __init__(self, folio, fecha, cliente, servicios):
        self.folio = folio
        self.fecha = fecha
        self.cliente = cliente
        self.servicios = servicios
        self.cancelada = False

    def calcular_monto_total(self):
        total = sum(servicio.costo for servicio in self.servicios)
        return total

# Función para cancelar una nota
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
                if confirmacion.lower() in ["si", "s"]:
                    print("\n*** NOTA CANCELADA ***")
                    nota_a_cancelar.cancelada = True
                    break
                elif confirmacion.lower() in ["no", "n"]:
                    print("\n*** NOTA NO CANCELADA ***")
                    break
                else:
                    print("La respuesta ingresada debe ser 'Si' o 'No'.")
                    confirmacion = input("\n¿Estás seguro de que quieres cancelar esta nota? (Si/No): ")
        else:
            print("\n** La nota ingresada no se encuentra en el sistema **")

def recuperar_nota():
    notas_canceladas = [nota for nota in notas if nota.cancelada]
    if notas_canceladas:
        print("\n---------NOTAS CANCELADAS---------")
        informacion = [[n.folio, n.fecha, n.cliente] for n in notas_canceladas]
        titulos = ["Folio", "Fecha", "Cliente"]
        print(tabulate(informacion, headers=titulos, tablefmt="fancy_grid"))
    while True:
        folio_a_recuperar = input("Ingresa el folio de la nota a recuperar (o 'No' para salir): ")
        if folio_a_recuperar.lower() == "no":
            break
        
        nota_a_recuperar = None
        for nota in notas_canceladas:
            if nota.folio == folio_a_recuperar:
                nota_a_recuperar = nota
                break
        
        if nota_a_recuperar:
            monto_total = nota_a_recuperar.calcular_monto_total()
            print("\n---------------NOTA-------------")
            print(f"Folio: {nota_a_recuperar.folio}")
            print(f"Fecha: {nota_a_recuperar.fecha}")
            print(f"Cliente: {nota_a_recuperar.cliente}")
            print("--------------------------------")
            print("Servicio:")
            for servicio in nota_a_recuperar.servicios:
                print(f"- {servicio.nombre}: ${servicio.costo:.2f}")
                print("--------------------------------")
            print(f"Total a pagar: ${monto_total:.2f}")
            confirmacion = input("\n¿Desea recuperar esta nota? (Si/No): ")
            if confirmacion.lower() == "si":
                nota_a_recuperar.cancelada = False
                print("** La nota ha sido recuperada con éxito **")
            else:
                print("La nota no ha sido recuperada.")
        else:
            print("\nEl folio proporcionado no corresponde a una nota cancelada.")

while True:
    print("\n--- Menú ---")
    print("1. Cancelar Nota")
    print("2. Recuperar Nota")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        cancelar_nota()
    elif opcion == '2':
        recuperar_nota()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")



print("---------------TALLER MECANICO--------------")
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
    if opcion == "1":
        registrar_nota()
    elif opcion == "2":
        while True:
            print("\n----CONSULTAS Y REPORTES----")
            print("1.Consulta por periodo\n2.Consulta por folio\n3.Regresar al menu principal ")
            opcion = input("Elige una opcion: ")
            if opcion == "1":
                consulta_por_periodo()
            elif opcion == "2":
                consulta_por_folio()
            elif opcion == "3":
                break
            else:
                print("\n** Opcion no valida, ingrese nuevamente **")
    elif opcion == "3":
        cancelar_nota()
    elif opcion == "4":
        recuperar_nota()
    elif opcion == "5":
        if input("Deseas salir del programa: ").upper() in ("S", "SI"):
            break

