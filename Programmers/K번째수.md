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

```python
def solution(array, commands):
    answer = []
    N = len(commands)
    for n in range(N):
        i, j, k = commands[n][0]-1, commands[n][1]-1, commands[n][2]-1
        arr = sorted(array[i:j+1])
        answer.append(arr[k])
        
    return answer
```

