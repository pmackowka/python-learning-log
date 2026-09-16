# 1. Programowanie proceduralne
# Skupia się na podziale programu na funkcje i instrukcje wykonywane sekwencyjnie.

cake_01 = {
    "taste": "vanilia",
    "glaze": "chocolade",
    "text": "Happy Birthday",
    "weight": 0.7,
}

cake_02 = {
    "taste": "tee",
    "glaze": "lemon",
    "text": "Happy Python Coding",
    "weight": 1.3,
}


def show_cake_info(cake):
    print(
        '{} cake with {} glaze with text "{}" of {} kg'.format(
            cake["taste"], cake["glaze"], cake["text"], cake["weight"]
        )
    )


cakes = [cake_01, cake_02]

for cake in cakes:
    show_cake_info(cake)

# vanilia cake with chocolade glaze with text "Happy Birthday" of 0.7 kg
# tee cake with lemon glaze with text "Happy Python Coding" of 1.3 kg
