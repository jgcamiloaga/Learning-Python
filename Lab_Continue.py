word_without_vowels = ""

user_word = input("Ingresa palabra:")

user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        word_without_vowels = word_without_vowels + letter
        continue
    elif letter == "E":
        word_without_vowels = word_without_vowels + letter
        continue
    elif letter == "I":
        word_without_vowels = word_without_vowels + letter
        continue
    elif letter == "O":
        word_without_vowels = word_without_vowels + letter
        continue
    elif letter == "U":
        word_without_vowels = word_without_vowels + letter
        continue
    else:
        continue
print(word_without_vowels)
