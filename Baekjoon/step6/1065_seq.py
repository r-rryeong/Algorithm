N = int(input())

cnt = 0
for n in range(1, N+1):
    seq_lst = list(map(int, str(n)))
    if n < 100:
        cnt += 1
    elif seq_lst[0]-seq_lst[1] == seq_lst[1]-seq_lst[2]:
        cnt += 1

print(cnt)