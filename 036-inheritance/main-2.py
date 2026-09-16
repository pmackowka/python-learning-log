# Dziedziczenie i nadpisywanie metody - Gawron dziedziczy po Zwierze i nadpisuje daj_glos.
class Zwierze:
    def przedstaw_sie(self):
        print("Jestem jakimś zwierzęciem.")

    def daj_glos(self):
        print("Nie wiem czym jestem i jaki dźwięk wydaję.")


class Gawron(Zwierze):
    def daj_glos(self):
        print("Kraaa kraaa!")


g = Gawron()
g.przedstaw_sie()
# Jestem jakimś zwierzeciem.

g.daj_glos()
# Kraaa kraaa!
