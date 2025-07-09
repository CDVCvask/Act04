class Medicine:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
def Medicines():
    allow = False
    medicines = []
    try:
        while allow == False:
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
                    medicines.append(medicine)
    except(ValueError):
        print("No se a ingresado el tipo de valor correcto")