courses =["Matemáticas", "Física", "Química", "Historia", "Lengua"]
approved = []

for course in courses:
    note = int(input("¿Qué nota has sacado en " + course + "? "))
    if note >= 10:
        approved.append(course)
for course in approved:
    courses.remove(course)
print("Usted debe repetir: " + str(courses))