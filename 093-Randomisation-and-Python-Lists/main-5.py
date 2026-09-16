# random.seed(), random.choice(), losowy indeks przez randint() - wybór losowego przyjaciela z listy.
friends = ["Rolf", "Anne", "Charlie", "Jen", "Bob", "Adam", "Becky", "Harry"]

import random

random.seed(0)

# random.shuffle(friends)
# print(friends)

x = random.choice(friends)
print(x)

y = random.randint(0, len(friends) - 1)
print(friends[y])
