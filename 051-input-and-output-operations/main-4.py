# Wczytywanie i walidacja wierszy pliku CSV z zamówieniami (bez modułu csv, na samym split).
# Poniższy string to podgląd zawartości orders.csv.
"""Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10"""

from pathlib import Path

file_path = Path(__file__).parent / "orders.csv"


with open(file_path, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        order = line.split(",")

        if len(order) == 3:
            print(
                'Order from drugstore "%s", item "%s", amount %s'
                % (order[0], order[1], order[2])
            )
        else:
            print("Line %s malformed!!!" % line)

print("Processing finished")

# Order from drugstore "Pharma A", item " Vitamin C", amount 100
# Line Drugstore XYZ,Penicilin, 20, pills malformed!!!
# Order from drugstore "Drugstore ABC", item "Aspirin", amount 60
# Order from drugstore "Pharma X", item "Montelukast", amount 10
# Processing finished
