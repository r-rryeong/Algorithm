N = int(input())
for i in range(N):
    sum_g = 0
    students = list(map(int, input().split()))
    num = students[0]
    grade = students[1:]
    for g in grade:
        sum_g += g
    result = sum_g / num
    
    temp = 0
    for s in grade:
        if s > result:
            temp += 1
    result_a = temp/num*100
    print(f'{result_a:.3f}%')