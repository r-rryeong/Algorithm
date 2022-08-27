```python
def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    for i in range(len(citations), -1, -1):   # 논문별 인용 횟수 10,000회 이하
        cnt = 0    # i회 이상 인용된 논문 개수
        for j in citations:  # 인용 횟수 check
            if j >= i:
                cnt += 1
            if cnt == i:
                return i      # 최댓값 return

    return answer
```

