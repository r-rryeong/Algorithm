```java
class Solution {
    public int[] solution(int n, int[] numlist) {
        int[] arr = new int[numlist.length];
        int idx = 0;
        for (int i=0; i<numlist.length; i++) {
            if (numlist[i]%n == 0) {
                arr[idx] = numlist[i];
                idx++;
            }
        }
        
        int[] answer = new int[idx];
        for (int i=0; i < idx; i++) {
            answer[i] = arr[i];
        }
        
        return answer;
    }
}
```

```java
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> arr = new ArrayList<>();
        
        for (int i=0; i<numlist.length; i++) {
            if (numlist[i]%n == 0) 
                arr.add(numlist[i]);
        }
        int[] answer = arr.stream().mapToInt(x -> x).toArray();
        return answer;
    }
}
```

