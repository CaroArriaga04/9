import datetime

class Nota:
    def __init__(self, folio, fecha, cliente, monto_a_pagar):
        self.folio = folio
        self.fecha = fecha
        self.cliente = cliente
        self.monto_a_pagar = monto_a_pagar
    
def registrar_nota():
    import uuid
    import datetime

def main():
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

class Servicio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

class Nota:
    def __init__(self, cliente):
        self.folio = str(uuid.uuid4())[:5]
        self.fecha = datetime.date.today() 
        self.cliente = cliente
        self.servicios = []
    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
    def calcular_monto_total(self):
        total = sum(servicio.costo for servicio in self.servicios)
        return total

if __name__ == "__main__":
    main()

def consulta_por_periodo():
    fecha_inicial = input("Ingresa la fecha inicial (dd/mm(yyyy): ")
    fecha_inicial = datetime.datetime.strptime(fecha_inicial, "%d/%m/%Y").date()

    fecha_final = input("Ingresa la fecha final (dd/mm/yyyy): ")
    fecha_final = datetime.datetime.strptime(fecha_final, "%d/%m/%Y").date()

    notas = []
    for nota in notas:
        if fecha_final <= nota.fecha <= fecha_final:
            notas.append(nota)
    
    # Imprimir notas en un reporte tabular

def consulta_por_folio():
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
        print("Submenu Consultas y reportes")
        opcion = input("Elige una opcion \n1.Consulta por periodo\n2.Consulta por folio")
        if opcion == 1:
            consulta_por_periodo()
        elif opcion == 2:
            pass
        else:
            print("Opcion no valida")
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        break


    
