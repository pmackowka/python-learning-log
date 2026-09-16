# To samo co main-1.py, ale pętlą while zamiast for.
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

i = 0
while i < len(words_list):
    print("Dodawanie kolejnego elementu", words_list[i])
    wordsAppend.append(words_list[i])

    if words_list[i] == "abort":
        print('Przerwanie pętli, bo trafiłem na "abort"')
        wordsAppend.clear()
        break

    i += 1

else:
    print(wordsAppend)
