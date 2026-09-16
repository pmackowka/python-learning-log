# Jak main-4.py, z dodanym konkretnym except FileNotFoundError przed bare except.
line = input("Enter accepted price: ")
filepath = input("Enter filename : ")

try:
    file = open(filepath, "w+")
    file.write(line)
    file.close()
except FileNotFoundError as e:
    print("Error opening file", filepath, e)
except:
    print("SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN")

# Enter accepted price: 10 PLN
# Enter filename :
# Error opening file  [Errno 2] No such file or directory: ''
