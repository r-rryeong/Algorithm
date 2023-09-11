```java
class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        int[] check=new int[after.length()];
        //방문 체크 배열 생성
        for (int i=0;i<check.length;i++) {
            check[i] = 0;
        }
        //before와 after 탐색
        String[] b_lst = before.split("");
        String[] a_lst = after.split("");
        for (int i=0;i<after.length();i++) {
            for (int j=0;j<before.length();j++) {
                if (a_lst[i].equals(b_lst[j])) {
                    if (check[j]==0) {
                        check[j] = 1;
                        break;
                    }
                }
            } 
        }
        //after를 만들 수 있는지 체크
        int total=0;
        for (int c:check) {
            total += c;
        }
        if (total == check.length) {
            answer = 1;
        }
        
        return answer;
    }
}
```

```java
class Solution {
    public int solution(String before, String after) {
        int answer = 1;
        for (int i=0;i<after.length();i++) {
            String ss=String.valueOf(after.charAt(i));
            
            if (before.contains(ss)) {
                before = before.replaceFirst(ss,"");  //처음 만나는 문자만 치환
            } else return 0;
        }
        
        return answer;
    }
}
```

