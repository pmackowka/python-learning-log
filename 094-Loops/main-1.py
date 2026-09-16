# Trzy sposoby iteracji - for po liście, while z licznikiem, sumowanie/średnia i max() przez generator.
owoce = ["jabłko", "banan", "gruszka"]

for owoc in owoce:
    print(owoc)

count = 0
while count < len(owoce):
    print(owoce[count])
    count += 1


student_scores = [
    78,
    65,
    89,
    86,
    55,
    91,
    64,
    89,
    81,
    94,
    76,
    87,
    79,
    85,
    76,
    61,
    68,
    82,
    88,
    93,
]
sum = 0
for score in student_scores:
    sum += score
average = sum / len(student_scores)
print(average)


print(max(score for score in student_scores))
