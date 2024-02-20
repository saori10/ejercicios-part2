prices = [50, 75, 46, 22, 80, 65, 8]

min_price = prices[0]
max_price = prices[0]


for price in prices:
    if price < min_price:
        min_price = price
    if price > max_price:
        max_price = price

print("El precio menor es:", min_price,"\nEl precio mayor es:", max_price)
        