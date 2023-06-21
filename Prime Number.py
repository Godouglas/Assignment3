from math import ceil, sqrt
Num = int(input("Enter number: "))
while Num < 1:
    print("Number should be positive")
    Num = int(input("Enter number: "))
for i in range(2, ceil(sqrt(Num))):
    if Num % i == 0:
        print(Num,"is not a prime")
        break
else:
    print(Num, "is a prime number")

