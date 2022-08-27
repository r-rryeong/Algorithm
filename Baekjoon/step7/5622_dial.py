dial = [
    'ABC', 'DEF', 'GHI', 'JKL',
    'MNO', 'PQRS', 'TUV', 'WXYZ',
    ]
word = input()
call = []
for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            call += [dial.index(j)+2]
time_c = 0
for x in call:
    time_c += x+1
print(time_c)