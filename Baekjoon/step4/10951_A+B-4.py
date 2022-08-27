while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:     # error가 발생한 경우
        break    # while문을 빠져나간다