user_age = int(input("¿Cuál es tu edad? "))
user_income = float(input("¿Cuáles son tus ingresos mensuales? "))
if user_age >= 16 and user_income >= 1000 :
    print("Usted tiene que tributar")
else:
    print("No cumple con los requisitos para tributar")