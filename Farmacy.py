class Medicine:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display(self):
        print(f"Nombre: {self.name}, Precio: {self.price}, cantidad: {self.quantity}")
def Medicines():
    allow = False
    medicines = []
    try:
        name = input("Ingrese el nombre de la medicina: ")
        price = int(input("Ingrese el precio de la medicina"))
        if price <= 0:
            print("El precio ingresado no es valido")
        else:
            quantity = int(input("Ingrese cúantas unidades de esta medicina va a ingresar"))
            if quantity <= 0:
                print("La cantidad ingresada no es valida")
            else:
                medicine = Medicine(name, price, quantity)
                return medicine
    except(ValueError):
        print("No se a ingresado el tipo de valor correcto")
def MenuMed():
    print("Menu")
    print("1.Ingresar nuevas medicinas")
    print("2.Entregar medicamento")
    print("3.Ver las medicinas en bodega")
    print("4.salir")
allow = False
medicines = []
try:
    while allow == False:
        MenuMed()
        opt = int(input("seleccione una opcion: "))
        match opt:
            case 1:
                medicine = Medicines()
                medicines.append(medicine)
            case 2:
                print("Entregar")
            case 3:
                for medicine in medicines:
                    medicine.display()
            case 4:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("La opcion ingresada no es valida")
except(ValueError):
    print("No se a ingresado el tipo de valor correcto")