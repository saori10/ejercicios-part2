customer_reviews = float(input("¿Cuál es tu puntuación? "))

if customer_reviews == 0.0:
    money = customer_reviews * 2400
    print("Tu nivel de rendimiento es Inaceptable, por lo tanto recibirás", money,"€")
elif customer_reviews == 0.4:
    money = customer_reviews * 2400
    print("Tu nivel de rendimiento es Aceptable, por lo tanto recibirás", money,"€")
elif customer_reviews >= 0.6:
    money = customer_reviews * 2400
    print("Tu nivel de rendimiento es Meteorito, por lo tanto recibirás", money,"€")
else:
    print("Ese nivel de puntuación no existe")