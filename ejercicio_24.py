name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
address = input("Ingrese su dirección: ")
phone = input("Ingrese su teléfono: ")

user = {
    "Nombre" : name,
    "Edad" : age,
    "Direccion" : address,
    "Telefono" : phone
}

print(user["Nombre"], "tiene", user["Edad"], ", vive en", user["Direccion"], "y su número de teléfono es", user["Telefono"])