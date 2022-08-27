n = int(input())
for i in range(n):
    new_wd = ''
    num, word = input().split()
    for j in word:
        new_wd += j * int(num)
    print(new_wd)