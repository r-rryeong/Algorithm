a = int(input())
b = int(input())

x1 = a * (b%10)
x2 = a * ((b%100)//10)
x3 = a * (b//100)
x4 = a * b

print(x1)
print(x2)
print(x3)
print(x4)