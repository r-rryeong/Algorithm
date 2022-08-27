```python
def BubbleSort(x):                           # 버블 정렬 구현
    for i in range(len(x)-1, 0, -1):         # 정렬될 구간의 끝 인덱스부터 접근
        for j in range(0, i):                # j는 0부터 i까지
            if x[j] > x[j+1]:                # x의 j번째 요소가 오른쪽 요소보다 더 크면
                x[j], x[j+1] = x[j+1], x[j]  # 자리바꿈
    return x

T = 10
for tc in range(1, T+1):
    dump = int(input())                     # 덤프 횟수
    high = list(map(int, input().split()))  # 각 상자의 높이 리스트

    box = BubbleSort(high)      # high를 정렬
    for cnt in range(dump):     # 덤프 횟수만큼 실행
        box[-1] -= 1            # 가장 높은 상자에서 1을 차감하고
        box[0] += 1             # 가장 낮은 상자에 1 누적
        box = BubbleSort(high)  # 리스트 다시 정렬

    print(f'#{tc} {box[-1] - box[0]}')
```