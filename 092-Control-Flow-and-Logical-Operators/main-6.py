# Jak main-4.py, plus dodatkowy próg wiekowy ze zniżką (45-55 lat za darmo).
wzrost = 130
lat = 46
bilet = 0

if wzrost > 120:
    print("Jedziesz na rollercoasterze!")
    if lat <= 12:
        bilet = 40
        print(f"Płacisz {bilet} zł.")
    elif lat <= 18:
        bilet = 80
        print(f"Płacisz {bilet} zł.")
    # elif lat >= 45 and lat <= 55:
    elif 45 <= lat <= 55:
        bilet = 0
        print(f"Płacisz {bilet} zł.")
        # quit()
        # exit()
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
