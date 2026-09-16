# Szukanie maksimum ręcznie (max_score = max(max_score, score)) - alternatywy zakomentowane wyżej.
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

# print(max(score for score in student_scores))

# print(max(student_scores))

# student_sorted1 = student_scores[::-1]
# print(student_sorted1)

# student_sorted2 = sorted(student_scores)
# print(student_sorted2)

max_score = 0

for score in student_scores:
    max_score = max(max_score, score)

print(max_score)
