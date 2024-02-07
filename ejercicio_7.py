user_income = float(input("¿Cuál es su renta anual? "))

if user_income < 10000 :
    print("El tipo impositivo que le corresponde es del 5%")
elif user_income >= 10000 and user_income <= 20000 :
    print("El tipo impositivo que le corresponde es del 15%")
elif user_income >= 20000 and user_income <= 35000 :
    print("El tipo impositivo que le corresponde es del 20%")
elif user_income >= 35000 and user_income <= 60000 :
    print("El tipo impositivo que le corresponde es del 30%")
else:
    print("El tipo impositivo que le corresponde es del 45%")