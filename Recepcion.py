class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
    def ver_cliente(self):
        print(f"Nombre: {self.nombre}, motivo de consulta: {self.motivo_consulta}")

opcion = 0
while opcion != "4":
    print("==MENÚ DE RECEPCIÓN==")
    print("1.Registrar paciente")
    print("2.Atender paciente")
    print("3.Mostrar pacientes en espera")
    print("4.Salir")
    try:
        opcion = input("\nSeleccione una opción: ")

    except ValueError:
        print("ERROR: Dato ingresado no válido")