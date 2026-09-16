# Klasyfikacja BMI przez łańcuchowe porównanie (elif 18.5 <= bmi <= 24.9).
weight = 85
height = 1.85

bmi = weight / (height**2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 24.9:
    print("normal weight")
elif 25 <= bmi < 29.9:
    print("overweight")
else:
    print("obese")
