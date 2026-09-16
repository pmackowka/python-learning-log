# Zapis inputu do pliku bez żadnej obsługi błędów (punkt wyjścia dla main-4/5/6).
line = input("Enter accepted price: ")
filepath = input("Enter filename : ")

file = open(filepath, "w+")
file.write(line)
file.close()
