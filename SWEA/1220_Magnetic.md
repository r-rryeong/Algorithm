```python
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0   # 교착 상태 개수
    for j in range(N):
        m = 0
        for i in range(N):
            if arr[i][j] == 1:    # 열 방향으로 이동
                m = 1
            elif arr[i][j] == 2 and m == 1:   # m이 1이고 그 아래에서 2를 만나면(교착상태)
                cnt += 1
                m = 0    # m 초기화
    print(f'#{tc} {cnt}')
```

