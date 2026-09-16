# Jak main-2.py, plus dodatkowe input() o dopłatę za zdjęcie.
wzrost = 130
lat = 19
bilet = 0

if wzrost > 120:
    print("Jedziesz na rollercoasterze!")
    if lat <= 12:
        bilet = 40
        print(f"Płacisz {bilet} zł.")
    elif lat <= 18:
        bilet = 80
        print(f"Płacisz {bilet} zł.")
    else:
        bilet = 150
        print(f"Płacisz {bilet} zł.")

    czy_foto = input("Czy chcesz zdjęcie? (t/n): ")
    if czy_foto == "t":
        bilet += 50
        print(f"Za zdjęcie płacisz dodatkowo 3 zł. Razem: {bilet} zł.")
        print("Dziękujemy za zakup biletu.")
    else:
        print("Dziękujemy za zakup biletu.")

else:
    print("Za niski na rollercoaster.")

print("Koniec programu.")
