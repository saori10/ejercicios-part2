word = input("Ingrese una palabra: ")
vowels = ["a", "e", "i", "o", "u"]

count_A = 0
count_E = 0
count_I = 0
count_O = 0
count_U = 0

for caracter in word:
    if caracter.lower() == vowels[0]:
        count_A += 1
    elif caracter.lower() == vowels[1]:
        count_E += 1
    elif caracter.lower() == vowels[2]:
        count_I += 1
    elif caracter.lower() == vowels[3]:
        count_O += 1
    elif caracter.lower() == vowels[4]:
        count_U += 1

print("Vocal A =", count_A ,"\nVocal E =", count_E,"\nVocal I =", count_I,"\nVocal O =", count_O,"\nVocal U =", count_U)