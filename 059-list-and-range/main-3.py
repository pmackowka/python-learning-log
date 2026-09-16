# Wyciąganie tekstu w nawiasie - przez re.findall oraz ręcznie przez index()/slice.
import re

# Tekst źródłowy
text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."

result = " ".join(re.findall(r"\((.*?)\)", text))
print(result)

print(20 * "-")
definition = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. "

print(definition.index("(") + 1)  # 12
print(definition.index(")"))  # 68

print(definition[definition.index("(") + 1 : definition.index(")")])
