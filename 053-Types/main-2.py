# a, b, c = (10,) * 3
a = b = c = 10
print(a, id(a), b, id(b), c, id(c))
a = 20
print(a, id(a), b, id(b), c, id(c))

# 10 4363872848 10 4363872848 10 4363872848
# 20 4363873168 10 4363872848 10 4363872848

print(20 * "-")
a = b = c = [1, 2, 3]
print(a, id(a), b, id(b), c, id(c))
# a.append(4)
a += [4]
print(a, id(a), b, id(b), c, id(c))
# [1, 2, 3] 4311350720 [1, 2, 3] 4311350720 [1, 2, 3] 4311350720
# [1, 2, 3, 4] 4311350720 [1, 2, 3, 4] 4311350720 [1, 2, 3, 4] 4311350720

print(20 * "-")
# chociaż mamy do czynienia z dwoma niezależnymi zmiennymi, to optymalizator pythona nadał im ten sam id
x = 10
y = 10
print(x, id(x), y, id(y))  # 10 4376848976 10 4376848976

print(20 * "-")
# identyfikatory nadal powinny być takie same, tzn. optymalizator poradził sobie z prostym działaniem + 1 - 1
x = x + 1 - 1
print(x, id(x), y, id(y))  # 10 4363020880 10 4363020880

print(20 * "-")
# identyfikatory powinny być różne, tzn. optymalizator nie rozpoznał, że zmienne mają nadal te same wartości
y = y + 1234567890 - 1234567890
print(x, id(x), y, id(y))  # 10 4332743248 10 4332743248
