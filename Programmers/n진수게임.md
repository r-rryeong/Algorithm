- n진수 → 10진수: int(string, base)

  ```python
  print(int('111', 2))  #7
  print(int('222', 3))  #26
  print(int('333', 4))  #63
  print(int('FFF', 16))  #4095
  ```

- 10진수 → n진수

  ```python
  def convert(num, base):
      temp = '0123456789ABCDEF'
      q, r = divmod(num, base)
      
      if q == 0:
          return temp[r]
      else:
          return convert(q, base) + temp[r]
  ```

  

### 💡풀이

```python
# n진수로 변환하자
def convert(num, base):
    temp = '0123456789ABCDEF'
    q, r = divmod(num, base)   # num은 int형

    if q == 0:   # 몫이 0이면 더 나눌 필요없음
        return temp[r]   # 나머지 반환
    else:        # 몫이 0이 아니면 재귀호출하면서 문자열 추가
        return convert(q, base) + temp[r]


def solution(n, t, m, p):
    answer = ''   # 튜브가 말할 문자만 담을 변수
    test = ''     # n진수로 변환한 숫자를 담을 빈문자열

    # 0부터 mt-1까지의 숫자를 n진수로 변환해서 test에 저장
    for i in range(m * t):
        test += convert(i, n)

    # 말해야 하는 숫자 만큼 반복
    while len(answer) < t:
        # 튜브의 순번에서 말해야할 숫자를 answer에 저장
        answer += test[p - 1]
        p += m

    return answer
```

