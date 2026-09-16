# Pętla while - numeracja wierszy, tabliczka kwadratów/sześcianów, potęgi 2, trójkąt z "x".
firstRow = 1
lastRow = 5

currentRow = firstRow

while currentRow <= lastRow:
    print("Row number", currentRow)
    currentRow += 1

# Row number 1
# Row number 2
# Row number 3
# Row number 4
# Row number 5
print("#################")

start = 1
end = 5

number = start

while number <= end:
    print(number, number * number, number * number * number)
    number += 1

# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125
print("#################")

start = 0
end = 5

x = start
while x <= end:
    print(x, 2**x)
    x += 1

# 0 1
# 1 2
# 2 4
# 3 8
# 4 16
# 5 32
print("#################")

start = 1
end = 10
number = start

while number <= end:
    print(number * "x")
    number += 1

# x
# xx
# xxx
# xxxx
# xxxxx
# xxxxxx
# xxxxxxx
# xxxxxxxx
# xxxxxxxxx
# xxxxxxxxxx
