primitive_lottery = []

for i in range(3) :
    primitive_lottery.append(int(input("¿Cuáles son los números de la lotería primitiva?: ")))
primitive_lottery.sort()
print("Los números son " + str(primitive_lottery))