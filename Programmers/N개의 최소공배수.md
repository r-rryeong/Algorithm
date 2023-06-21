```python
def solution(arr):
    answer = 0
    m = 1
    for a in arr:
        m *= a
        
    for lcm in range(max(arr), m+1):
        i = 0
        while i != len(arr):
            if lcm%arr[i]!=0:
                break
            i += 1

        if i==len(arr):
            answer = lcm
            break

    return answer
```

