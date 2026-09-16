# Pętla for/else - break przerywa pętlę i pomija blok else (czyszczenie listy przy "abort").
words_list = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "papaya",
    "pear",
    "abort",
    "plum",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "watermelon",
    "apricot",
    "blueberry",
    "cantaloupe",
    "dragonfruit",
    "grapefruit",
    "jackfruit",
    "kumquat",
    "lime",
    "melon",
]


wordsAppend = []

for word in words_list:
    print("Dodawanie kolejnego elementu", word)
    wordsAppend.append(word)

    if word == "abort":
        print('Przerwanie pętli, bo trafiłem na "abort"')
        wordsAppend.clear()
        break

else:
    print(wordsAppend)
