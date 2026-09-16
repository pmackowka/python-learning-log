# Pętla for + range - rysowanie siatki/trójkąta ze znaków, z warunkiem co drugi wiersz.
string_A = "+---+---+---+---+"
string_B = "|   |   |   |   |"

for i in range(10):
    print(string_A)

print()

for i in range(9):
    if i % 2 == 0:
        print(string_A)
    else:
        print(string_B)

print()

for i in range(1, 10):
    print("x" * i)

print()

for i in range(1, 10):
    if i % 2 == 0:
        print("x" * i)
    else:
        print("o" * i)
