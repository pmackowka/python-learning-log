# Pętla while - procent składany, suma cyfr liczby, zliczanie krótkich/długich słów w tekście.
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0
capital = initialCapital
while year < maxTimeYears:
    year += 1
    capital = round((1 + percent) * capital, 2)
    print("after this year:", year, "you will have:", capital)
print("the total revenue is", capital - initialCapital)

print("-------------------------------------------------------")


number = 20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber > 0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber // 10
print("the sum of digits of ", number, " is", sumOfDigits)

print("-------------------------------------------------------")


text = """
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
"""
listOfWords = text.replace("\n", " ").split(" ")
wordLength = 6
i = 0
shortWords = 0
longWords = 0
while i < len(listOfWords):
    if len(listOfWords[i]) > wordLength:
        longWords += 1
    else:
        shortWords += 1

    i += 1
print("Words shorter than ", wordLength, ":", shortWords)
print("Words longer than ", wordLength, ":", longWords)
