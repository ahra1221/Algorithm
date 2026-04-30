import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> st = new Stack<>();
        for(Integer a: arr) {
            if (st.empty() || st.peek() != a) st.push(a);
            else continue;
        }
        
        int[] answer = new int[st.size()];
        for(int i=0;i<answer.length;i++) {
            answer[i] = st.get(i);
        }
        
        
        return answer;
    }
}