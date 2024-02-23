fruits = {
    "Plátano" : 1.35,
    "Manzana" : 0.80,
    "Pera" : 0.85,
    "Naranja" : 0.70
}

fruit = input("Ingrese una fruta: ").title()
kg = float(input("¿Cuántos kg desea?: "))
fruit_kg = fruits[fruit] * kg

if fruit in fruits :
    print(kg, "kilos de", fruit, "valen", fruit_kg, "$")
else:
    print("Esa fruta no se encuentra")




