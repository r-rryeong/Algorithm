A, B, C = map(int, input().split())

a= int((A+B)%C)
b= int(((A%C)+(B%C))%C)
c= int((A*B)%C)
d= int(((A%C)*(B%C))%C)

print(a)
print(b)
print(c)
print(d)