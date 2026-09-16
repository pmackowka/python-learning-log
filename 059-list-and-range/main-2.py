"""LAB - range, list, slice
Budujesz moduł generujący wykresy. Chcesz samodzielnie wpływać na to, jakie kolory będą wykorzystane na wykresie. Definiujesz na początku listę kolorów:

["red", "orange", "green", "violet", "blue", "yellow"]

Czasami na wykresie będą prezentowane tylko 3 kategorie i wtedy chcesz wykorzystać tylko 3 pierwsze kolory, innym razem wykres ma mieć 5 kategorii i potrzebujesz listę 5 kolorów.

Napisz funkcję, która przyjmuje dwa argumenty: listę kolorów i liczbę n. Funkcja ma zwracać nową kopię listy kolorów o długości n korzystając z przekazanej listy argumentów, np,:
gdy potrzebny jest jeden kolor zostanie zwrócone ["red"]
gdy potrzebn są dwa kolory zostanie zwrócone ["red",' "orange"] itd.

Napisz pętlę, która wygeneruje wszystkie listy kolorów znajdujących się na wejściowej liście. Pętla powinna radzić sobie z wyświetleniem wszystkich zestawów, nawet jeżeli do początkowej listy zostanie kiedyś dodany następny kolor (nie korzystaj z wpisywania na stałe wartości liczbowej).

Napis też można "kroić". Wytnij z poniższego tekstu pochodzącego z https://nonsa.pl/wiki/Korporacja (dawniej nonsensopedia.pl) fragment tłumaczący pochodzenie słowa "Korporacja" - fragment znajduje się w nawiasach (same nawiasy pomiń):

Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."""

# Lista kolorów
colors = ["red", "orange", "green", "violet", "blue", "yellow"]


def generate_colors(color_list, n):
    # Tworzymy kopię listy kolorów, ale ograniczoną do liczby n
    return color_list[:n]


# Generowanie i wyświetlanie list dla różnych wartości n
for i in range(
    1, len(colors) + 1
):  # Pętla będzie się kręcić od 1 do długości listy kolorów
    print(generate_colors(colors, i))

# ['red']
# ['red', 'orange']
# ['red', 'orange', 'green']
# ['red', 'orange', 'green', 'violet']
# ['red', 'orange', 'green', 'violet', 'blue']
# ['red', 'orange', 'green', 'violet', 'blue', 'yellow']

print(20 * "-")


def get_list_of_colors(colors, n):
    return colors[:n]


colors = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(1, len(colors) + 1):
    print(get_list_of_colors(colors, i))
