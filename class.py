import math
print("i am a calculator||||For square root type [square root] without big brackets")
a = int(input("First number?/Square root yr number"))
b = int(input("second number?"))
c = input(str("operation?"))

if c == "+":
    print(a+b)

if c == "-":
    print(a-b)

if c == "*":
    print(a*b)

if c == "/":
    print(a/b)

if c == "square root":
    d = math.sqrt(a)
    print(d)
