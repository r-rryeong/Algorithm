```python
def calc(X, Y):
    num = set()
    for x in X:
        for y in Y:
            num.add(x+y)
            num.add(x-y)
            num.add(x*y)
            if y != 0:
                num.add(x//y)
    return num

def solution(N, number):
    answer = -1
    d = dict()
    d[1] = {N}
    if number == N:
        return 1

    for i in range(2, 9):
        n = 1
        temp = {}
        while n < i:
            temp.update(calc(d[n], d[i-n]))
            n += 1

        if number in temp:
            answer = i
            break

        d[i] = temp

    return answer
```

