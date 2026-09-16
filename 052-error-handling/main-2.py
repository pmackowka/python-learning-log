# Ten sam plik co main-1.py, ale z bare except zastąpionym konkretnymi wyjątkami
# (ValueError, IndexError) - pokazuje różnicę względem generycznej obsługi błędów.
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

        except ValueError:
            print(
                "Problem with conversion. Check whether the amount is correct. Line: %s"
                % line
            )

        except IndexError:
            print(
                "Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: %s"
                % line
            )

        except:
            print("General error: %s" % sys.exc_info()[0])

print("Processing finished")

# Order from drugstore "Pharma A", item " Vitamin C", amount 100
# Order from drugstore "Drugstore XYZ", item "Penicilin", amount 20
# Order from drugstore "Drugstore ABC", item "Aspirin", amount 60
# Order from drugstore "Pharma X", item "Montelukast", amount 10
# Problem with conversion. Check whether the amount is correct. Line: Pharma at grocery,Amoxicillin,?
# Order from drugstore "Pharmacy 123", item "Cephalexin", amount 100
# Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: Pharmacy 123,Prednisolone Sodium Phosphate
# Order from drugstore "Pharma X", item "Nystatin", amount 45
# Processing finished
