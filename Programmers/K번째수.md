### K번째수

```python
from collections import deque

def solution(array, commands):
    commands = deque(commands)   # deque로 변환
    answer = []

    while commands:
        i, j, k = commands.popleft()
        slice_lst = array[i-1:j]    # 슬라이싱 후 정렬
        slice_lst.sort()
        answer.append(slice_lst[k-1])   # k번째 원소
        
    return answer
```

