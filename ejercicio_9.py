user_age = int(input("¿Cuál es su edad? "))

if user_age < 4:
    print("Usted entra gratis")
elif user_age >= 4 and user_age <= 18:
    print("Usted pagará 5€")
else:
    print("Usted pagará 10€")