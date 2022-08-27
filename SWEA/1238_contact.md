```python
# 1.

def bfs(s):
    while q:
        cn = q.pop(0)   # 현재 정점
        for nn in range(1, max_num+1):   # 다음 방문할 정점 탐색
            if table[cn][nn]==1 and visit[nn]==0:   # 현재 정점에서 연락 가능하고 아직 방문하지 않았다면 이동
                q.append(nn)    # 큐에 다음 정점 추가
                visit[nn] = 1   # 방문 표시
                contact[nn] = contact[cn] + 1    # 방문 순서 표시

for tc in range(1, 11):
    L, start = map(int, input().split())       # 입력받는 데이터의 길이, 시작점
    fromto = list(map(int, input().split()))   # 주어진 데이터(from, to)

    max_num = max(fromto)    # 사람들 중 가장 큰 번호
    table = [[0]*(max_num+1) for _ in range(max_num+1)]   # from, to를 나타내는 표
    for i in range(L//2):     # 주어진 데이터에 접근
        r = fromto[i*2]       # 행은 데이터 쌍 중에 첫번째 번호
        c = fromto[i*2+1]     # 열은 데이터 쌍 중에 두번째 번호
        table[r][c] = 1       # 연락할 수 있음을 표시

    q = [start]                 # 큐에 시작점을 넣어준다
    visit = [0]*(max_num+1)     # 방문표시를 할 리스트
    visit[start] = 1            # 시작점 방문 표시
    contact = [0]*(max_num+1)   # 연락 순서를 표시해줄 리스트
    bfs(start)  # 시작점부터 연락 시작

    last_c = max(contact)   # 리스트 중 가장 큰 수의 인덱스가 마지막으로 연락받은 사람들 번호
    res = 0     # 마지막으로 연락받은 사람들 중 가장 큰 값을 저장할 변수(결과값)
    for i in range(1, max_num+1):   # 1번부터 마지막 번호까지 접근
        if contact[i]==last_c:      # 마지막으로 연락받은 사람들인 경우
            if i > res:             # 번호와 현재 가장 큰 번호 비교
                res = i             # 크다면 결과값 갱신

    print(f'#{tc}', res)
```

