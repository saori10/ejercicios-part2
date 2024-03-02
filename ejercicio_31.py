bills = {}
charged = 0
not_charged = 0
answer = " "

while answer != "T":
    if answer == "N":
        clue = input("Ingrese el numero de factura: ")
        value = float(input("Ingrese el coste de la factura: "))
        bills[clue] = value
        not_charged += value
    if answer == "P":
        clue = input("Ingrese el numero de factura: ")
        value = bills.pop(clue, 0)
        charged += value
        not_charged -= value
    print("Se ha cobrado:", charged)
    print("Queda pendiente de cobro:", not_charged)
    answer = input("¿Desea añadir(N), pagar una existente factura(P) o terminar(T)?: ").upper()




            

