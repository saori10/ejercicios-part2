word = input("Ingrese una palabra: ")
word_palindrome = word
word = list(word)
word_palindrome = list(word_palindrome)

word_palindrome.reverse()

if word_palindrome == word:
    print("Es palíndromo")
else:
    print("No es palíndromo")
