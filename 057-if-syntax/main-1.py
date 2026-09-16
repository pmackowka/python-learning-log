# Różne formy instrukcji warunkowej - if/elif/else, zagnieżdżony operator ternary, print() w ternary.
dayType = 3
weekend = 1
workday = 2
holiday = 3

if dayType == 1 or dayType == 2:
    pass
else:
    pass

print(20 * "-")
if dayType == 1:
    print("Weekend")
elif dayType == 2:
    print("Workday")
else:
    print("Holiday")

print(20 * "-")
print(
    "Weekend"
    if dayType == 1
    else "Workday"
    if dayType == 2
    else "Holiday"
    if dayType == 3
    else None
)

print(20 * "-")
light = "yellow"
print("GO") if light == "green" else print("HALT") if light == "red" else print("WAIT")
