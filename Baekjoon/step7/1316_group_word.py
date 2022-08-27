N = int(input())

group = N
for n in range(N):
    word = input()
    for i in range(len(word)-1):
        if word.index(word[i]) > word.index(word[i+1]):    # word의 인덱스 비교를 통해 이미 나왔던 문자를 찾음
            group -= 1    # 이미 나왔던 문자가 발견되면 단어의 개수에서 1 차감
            break
print(group)

