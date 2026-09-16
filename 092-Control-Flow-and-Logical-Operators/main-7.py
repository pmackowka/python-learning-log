# Gra tekstowa (choose your own adventure) - zagnieżdżone input()/if o rozgałęzionej fabule.
print("""Witaj na Wyspie Skarbów.
Twoim zadaniem jest znalezienie skarbu.
Jesteś na skrzyżowaniu. Dokąd chcesz iść?""")

kierunek = input('\tWpisz "lewo" lub "prawo"').strip().lower()

if kierunek == "lewo":
    print("Dotarłeś do jeziora. Na środku jeziora znajduje się wyspa.")
    akcja = (
        input('\tWpisz "czekaj", aby czekać na łódź, lub "płyń", aby przepłynąć')
        .strip()
        .lower()
    )
    if akcja == "czekaj":
        print("Docierasz na wyspę bez szwanku. Jest tam dom z 3 drzwiami.")
        drzwi = input('\tWpisz "czerwone", "niebieskie" lub "żółte"').strip().lower()
        if drzwi == "czerwone":
            print("Zostałeś spalony przez ogień. Koniec gry.")
        elif drzwi == "niebieskie":
            print("Zostałeś zjedzony przez bestie. Koniec gry.")
        elif drzwi == "żółte":
            print("Wygrywasz!")
        else:
            print("Koniec gry.")
    else:
        print("Zostałeś zaatakowany przez pstrągi. Koniec gry.")
else:
    print("Fall into a hole.\nKoniec gry.")

print("Koniec programu.")
