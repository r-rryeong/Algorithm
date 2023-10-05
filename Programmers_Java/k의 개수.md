```java
class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String str_k=String.valueOf(k);
        for (int n=i;n<=j;n++) {
            String num=String.valueOf(n);
            if(num.contains(str_k)) {
                String[] arr_n=num.split("");
                for (String aa : arr_n) {
                    if(aa.equals(str_k)) answer++;
                }
            }
        }
        
        return answer;
    }
}
```

```java
class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        
        for(int n=i; n<=j; n++) {
            String[] number = String.valueOf(n).split("");
            
            for(int idx=0;idx<number.length;idx++){
                int tmp = Integer.parseInt(number[idx]);
                if(tmp == k) answer++;
            }
        }
        return answer;
    }
}
```

