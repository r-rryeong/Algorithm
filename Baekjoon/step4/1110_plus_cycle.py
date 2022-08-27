N = int(input())
result = N
cyc = 0

while True:
    a = result // 10
    b = result % 10
    c = (a + b) % 10
    result = (b * 10) + c

    cyc += 1
    if (result == N):
        break

print(cyc)
