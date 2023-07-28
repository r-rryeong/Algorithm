### k의 개수

```python
def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        if str(k) in list(str(n)):
            answer += list(str(n)).count(str(k))
    return answer
```

