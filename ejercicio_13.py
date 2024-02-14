subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
grades = []

for subject in subjects:
    note = input("¿Qué nota sacaste en " + subject + "? ")
    grades.append(note)
for x in range(len(subjects)):
    print("En " + subjects[x] + " has sacado " + grades[x])
    

  

