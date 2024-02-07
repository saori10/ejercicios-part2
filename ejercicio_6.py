user_name = input("¿Cuál es tu nombre? ")
user_gender = input("¿Cuál es tu género (M - F)? ")

#print(user_name[0])

first_str = user_name[0]

# otra forma : name_woman_1 = ["a", "b", "c"]

if first_str.lower() in "abcefghijkl" and user_gender.upper() == "F":
    print("Está en el grupo A")
elif first_str.lower() in "nopqrstuvwxyz" and user_gender.upper() == "F":
    print("Está en el grupo B")

if first_str.lower() in "opqrstuvwxyz" and user_gender.upper() == "M":
    print("Está en el grupo A")
elif first_str.lower() in "abcdefghijklm" and user_gender.upper() == "M":
    print("Está en el grupo B")