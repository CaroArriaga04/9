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
            notas_por_periodo = [n for n in notas if fecha_inicial <= datetime.datetime.strptime(n.fecha, "%d/%m/%Y").date() <= fecha_final]
            if notas_por_periodo:
                print("\n---------NOTAS POR PERIODO---------")
                informacion = [[n.folio, n.fecha, n.cliente] for n in notas_por_periodo]
                titulos = ["Folio", "Fecha", "Cliente"]
                print(tabulate(informacion, titulos, tablefmt="fancy_grid"))
            else:
                print("No hay notas registradas en el periodo ingresado")
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
    nota_a_cancelar = None 
    cancelado = input("Ingresa el folio de la nota a cancelar: ")
    for nota in notas:
        if nota.folio == cancelado:
            nota_a_cancelar = nota
            break
        else:
            print("\n** La nota ingresada no se encuentra en el sistema **")
            break
    if nota_a_cancelar:
        monto_total = nota.calcular_monto_total()
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
        confirmacion = input("\n¿Estas seguro de que quieres cancelar esta nota?: ")
        while True:
            if confirmacion.upper() == "SI" or confirmacion.upper() == "S" or confirmacion.upper() == "Y":
                print ("\n*** NOTA CANCELADA ***")
                nota_a_cancelar.cancelada = True
                break
            if confirmacion.upper() == "NO" or confirmacion.upper() == "N":
                print ("\n*** NOTA NO CANCELADA ***")
                break
            else:
                print ("La respuesta ingresada debe ser Si o No.")
                continue

def recuperar_nota():
    nota_a_cancelar = {
        "001": {"titulo": "Nota 1", "contenido": "Contenido de la nota 1"},
        "002": {"titulo": "Nota 2", "contenido": "Contenido de la nota 2"},
        "003": {"titulo": "Nota 3", "contenido": "Contenido de la nota 3"},
    }
    print("Notas canceladas:")
    print("{:<5} {:<10}".format("Folio", "Título"))
    for folio, nota in nota_a_cancelar.items():
        print("{:<5} {:<10}".format(folio, nota["titulo"]))
    
    folio_a_recuperar = input("Ingresa el folio de la nota a recuperar (No para salir)")
    if (folio_a_recuperar.lower() == "no"):
        print("No se realizará ninguna recuperación.")
    else:
        if folio_a_recuperar in nota_a_cancelar:
            nota = nota_a_cancelar[folio_a_recuperar]
            print("\nDetalle de la nota:")
            print("Título:", nota["titulo"])
            print("Contenido:", nota["contenido"])
            confirmacion = input("¿Desea recuperar esta nota? (Sí/No): ")
            if confirmacion.lower() == "si":
                del nota_a_cancelar[folio_a_recuperar]
                print("La nota ha sido recuperada con éxito.")
            else:
                print("La nota no ha sido recuperada.")
        else:
            print("El folio proporcionado no corresponde a una nota cancelada.")

def main():
    registrar_nota()
    consulta_por_periodo()
    consulta_por_folio()
    cancelar_nota()
    recuperar_nota()

if __name__ == "__main__":
    main()
