# Pętla for po liście stringów - parsowanie "Error:..."/"Warning:..." przez split(":").
data = [
    "Error:File cannot be open",
    "Error:No free space on disk",
    "Error:File missing",
    "Warning:Internet connection lost",
    "Error:Access denied",
]

for s in data:
    print(s.upper())

print("----------------")

for s in data:
    elements = s.split(":")
    print(elements[0].upper())
    print(elements[1])

print("----------------")

for s in data:
    elements = s.split(":")
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])
