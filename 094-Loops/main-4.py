# student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 81, 94, 76, 87, 79, 85, 76, 61, 68, 82, 88, 93]

# max_score = 0
# for score in student_scores:
# 	if score > max_score:
# 		max_score = score

# print(max_score)

# sum = 0
# for i in range(1, 101):
# 	sum += i

# print(sum)

for x in range(1, 101):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
