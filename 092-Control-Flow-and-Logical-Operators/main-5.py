# Kalkulator ceny pizzy - input() rozmiaru i dodatków, quit() przy błędnym rozmiarze.
bill = 0

size = input("Enter the size of the pizza (S, M, L): ").strip().upper()

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid input. Please try again.")
    quit()

pepperoni = input("Do you want pepperoni? Y or N: ").strip().upper()

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()

if extra_cheese == "Y":
    bill += 1

print(f"Total bill: ${bill}")
print("Thank you for your order. Enjoy your pizza!")
print("End of the program.")
