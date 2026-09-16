# Przetwarzanie pliku CSV z zamówieniami - błędne linie są przechwytywane (bare except),
# a typ błędu wypisywany przez sys.exc_info(). Poniższy string to podgląd zawartości orders.csv.
"""Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10
Pharma at grocery,Amoxicillin,?
Pharmacy 123,Cephalexin,100
Pharmacy 123,Prednisolone Sodium Phosphate
Pharma X,Nystatin,45"""

import sys
from pathlib import Path

file_path = Path(__file__).parent / "orders.csv"


with open(file_path, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        order = line.split(",")

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print(
                'Order from drugstore "%s", item "%s", amount %d'
                % (pharmacy_name, item, amount)
            )
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])

print("Processing finished")

# Order from drugstore "Pharma A", item " Vitamin C", amount 100
# Order from drugstore "Drugstore XYZ", item "Penicilin", amount 20
# Order from drugstore "Drugstore ABC", item "Aspirin", amount 60
# Order from drugstore "Pharma X", item "Montelukast", amount 10
# Problem with line Pharma at grocery,Amoxicillin,?
# <class 'ValueError'>
# Order from drugstore "Pharmacy 123", item "Cephalexin", amount 100
# Problem with line Pharmacy 123,Prednisolone Sodium Phosphate
# <class 'IndexError'>
# Order from drugstore "Pharma X", item "Nystatin", amount 45
# Processing finished
