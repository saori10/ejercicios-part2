basket = {}
stall = True



while stall:
    article = input("Introduce un artículo: ")
    price = float(input("Ingrese el precio del articulo: "))
    basket[article] = price
    stall = input("¿Desea agregar más artículos?: ").lower() == "si"

total_price = 0
print("La lista de compra es la siguiente:")
for article, price in basket.items():
    print(article, "\t", price)
    total_price += price
print("El coste total es:", total_price)
    
        



    