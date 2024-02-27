translations = {}

words = input("Ingrese palabras en español con su traduccion en ingles (palabra:traduccion) separadas por comas: ")
for i in words.split(","):
    word, value = i.split(":")
    translations[word] = value

phrase = input("Ingrese una frase en español: ")
for i in phrase.split():
    if i in translations:
        print(translations[i], end= " ")
    else:
        print(i, end= " ")