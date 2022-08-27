n = int(input())
for i in range(n):
    result = input()
    score = 0
    total = 0
    for j in result:
        if j == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)

