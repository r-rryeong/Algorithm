n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.

n은 1이상 8000000000 이하인 자연수입니다.

```python
# 1.
def solution(n):
    n = list(str(n))
    n.sort()
    result = []
    for i in range(len(n)-1, -1, -1):
        result.append(n[i])
    answer = int(''.join(result))
    return answer
```

