subjects = {
    "Matemática" : 6,
    "Física" : 4,
    "Química" : 5
}

total_credits =  0

for subject, credits in subjects.items():
    print(subject, "tiene", credits, "creditos")
    total_credits += credits
print("El número total de créditos es", total_credits)