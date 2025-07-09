from collections import deque
from traceback import print_exception


class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
    def ver_cliente(self):
        print(f"Nombre: {self.nombre}, motivo de consulta: {self.motivo_consulta}")

pacientes_espera = deque()
opcion = 0
while opcion != "4":
    print("==MENÚ DE RECEPCIÓN==")
    print("1.Registrar paciente")
    print("2.Atender paciente")
    print("3.Mostrar pacientes en espera")
    print("4.Salir")
    try:
        opcion = input("\nSeleccione una opción: ")
        match opcion:
            case "1":
                print("Ingrese datos del paciente:")
                nombre = input("Nombre: ")
                motivo = input("Motivo de consulta: ")
                registrar_paciente = Paciente(nombre, motivo)
                pacientes_espera.append(registrar_paciente)
                print("Paciente registrado con éxito")
            case "2":
                if pacientes_espera:
                    print(f"El siguiente en ser atendido es {pacientes_espera[0]}")
                    input("Precione ENTER para continuar")
                    print(f"{pacientes_espera.popleft().nombre} Ha sido atendido")
                else:
                    print("No hay pacientes registrados")
            case "3":
                if pacientes_espera:
                    print("Pacientes en espera:")
                    for i in pacientes_espera:
                        i.ver_paciente()
                else:
                    print("No hay pacientes registrados")
            case "4":
                print("Tenga buen día, hasta pronto!")
            case __:
                print(f"La opción {opcion} no está disponible")
    except ValueError:
        print("ERROR: Dato ingresado no válido")