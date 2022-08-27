s = input()
alpha = [
    'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]
for i in alpha:
    for j in s:
        if j == i:
            print(s.index(i))
            break
    else:
        print(-1)