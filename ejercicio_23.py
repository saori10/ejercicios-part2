badge = input("Ingrese una divisa: ")

coins = {
    "Euro" : "€",
    "Dollar" : "$",
    "Yen" : "¥"
}

if badge.title() in coins:
    print("Su símbolo es:", coins[badge.title()])
else:
    print("Esa divisa no esta en el diccionario")
