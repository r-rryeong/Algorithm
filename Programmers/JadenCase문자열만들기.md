```python
def solution(s):
    answer = ''
    string = s.split(' ')    # 문장을 단어 형태로 나눠서 list에 담는다
    
    for i in range(len(string)):    # 단어를 돌면서 첫 문자를 대문자로 변경
        # 숫자는 upper해도 그대로 숫자
        # [0] 런타임 에러 → [:1]
        string[i] = string[i][:1].upper() + string[i][1:].lower()
        
    answer = ' '.join(string)    # 다시 문장으로 합치기
    return answer
```

```python
def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if i==0:
            answer += s[i].upper()
            continue
        
        if s[i-1] == ' ' and s[i].isalpha():
            answer += s[i].upper()
        else:
            answer += s[i].lower()
            
    return answer
```

