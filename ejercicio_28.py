data_person = {}
stall = 0  


while True:
    key = input("Introduzca un dato: ")
    value = input(key + ": ")
    data_person[key] = value
    print(data_person)
    stall = input("¿Desea seguir?: ")
    if stall.lower() == "si":
        True
    else:
        break

