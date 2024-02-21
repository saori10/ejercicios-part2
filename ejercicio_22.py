numbers = input("Ingrese una muestra de números separados por comas: ")
half = 0
typicla_medium = 0

addition = 0
sum_squares = 0

shows_numbers = []
for number in numbers.split(","):
    shows_numbers.append(int(number))
#print(shows_numbers)

for number in shows_numbers:
    addition += number
half = addition / len(shows_numbers)
#print(half)
    
for number in shows_numbers:
    sum_squares += (number - half) ** 2
typicla_medium = (sum_squares / len(shows_numbers)) ** 0.5
#print(typicla_medium)

print("La media de esos números es:", half)
print("Y la desviación típica es:", typicla_medium)








