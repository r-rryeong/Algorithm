T = int(input())

for x in range(1, T+1):
    A, B = map(int,input().split())
    C = A + B
    print("Case #%s: %s + %s = %s"%(x, A, B, C))