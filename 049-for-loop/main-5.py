# Pętla for - ciąg Fibonacciego, filtrowanie słów z literą "p", iteracja po słowniku,
# zliczanie wystąpień słów w tekście.
fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(fibonacciIterations):
    print("Step", i, "value", a3)
    a1 = a2
    a2 = a3
    a3 = a1 + a2

# Step 0 value 0
# Step 1 value 1
# Step 2 value 1
# Step 3 value 2
# Step 4 value 3
# Step 5 value 5
# Step 6 value 8
# Step 7 value 13
# Step 8 value 21
# Step 9 value 34
# Step 10 value 55
# Step 11 value 89
# Step 12 value 144
# Step 13 value 233
# Step 14 value 377
# Step 15 value 610
# Step 16 value 987
# Step 17 value 1597
# Step 18 value 2584
# Step 19 value 4181
print("-------------------------------------------------")

text = """
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn't do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it's an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can't.
"""
listOfWords = text.replace("\n", " ").split(" ")
for word in listOfWords:
    if word.lower().find("p") >= 0:
        print(word)

# Python
# production
# process
# scripting
# complex,
# computer
# graphic-intensive
# scripting,
# Python
# compared
# Perl,
# implement
# Python
# scripting
# Python
print("-----------------------------------------------")


dictionary = {"A": "80%-10%", "B": "60%-80%", "C": "50-60%", "D": "less than 50%"}
for word in dictionary:
    print(word, "-", dictionary[word])

# A - 80%-10%
# B - 60%-80%
# C - 50-60%
# D - less than 50

print("-----------------------------------------------")


wordDictionary = {}
for word in listOfWords:
    if word in wordDictionary:
        wordDictionary[word] = wordDictionary[word] + 1
    else:
        wordDictionary.setdefault(word, 1)

print(wordDictionary)

# {'': 2, 'Industrial': 2, 'Light': 2, '&': 2, 'Magic:': 1, 'In': 2, 'this': 2, 'case,': 1, 'you': 1, 'find': 1, 'Python': 4, 'used': 1, 'in': 4, 'the': 4, 'production': 1, 'process': 1, 'for': 1, 'scripting': 2, 'complex,': 1, 'computer': 1, 'graphic-intensive': 1, 'films.': 1, 'Originally,': 1, 'Magic': 1, 'relied': 1, 'on': 1, 'Unix': 1, 'shell': 1, 'scripting,': 1, 'but': 1, 'it': 1, 'was': 2, 'found': 1, 'that': 3, 'solution': 1, 'just': 1, "couldn't": 1, 'do': 1, 'job.': 1, 'compared': 1, 'to': 1, 'other': 2, 'languages,': 1, 'such': 2, 'as': 3, 'Tcl': 1, 'and': 2, 'Perl,': 1, 'chosen': 1, 'because': 1, "it's": 1, 'an': 1, 'easier-to-learn': 1, 'language': 2, 'organization': 1, 'can': 3, 'implement': 1, 'incrementally.': 1, 'addition,': 1, 'be': 1, 'embedded': 1, 'within': 1, 'a': 3, 'larger': 1, 'software': 1, 'system': 2, 'language,': 1, 'even': 1, 'if': 1, 'is': 1, 'written': 1, 'C/C++.': 1, 'It': 1, 'turns': 1, 'out': 1, 'successfully': 1, 'interact': 1, 'with': 1, 'these': 1, 'languages': 2, 'situations': 1, 'which': 1, 'some': 1, "can't.": 1}
