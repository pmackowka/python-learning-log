# Zagnieżdżony if/elif/else - cena biletu na rollercoaster wg wieku (pod warunkiem wzrostu).
wzrost = 130
lat = 16
bilet = True


if wzrost > 120:
    print("Jedziesz na rollercoasterze!")
    if lat <= 12:
        print("Płacisz 5 zł.")
    elif lat <= 18:
        print("Płacisz 7 zł.")
    else:
        print("Płacisz 10")
else:
    print("Za niski na rollercoaster.")
