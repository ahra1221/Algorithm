import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        
        Stack<Integer> st = new Stack<>();
        for(int i=0;i<n;i++) {
            while(!st.isEmpty() && prices[st.peek()] > prices[i]) {
                int idx = st.pop();
                answer[idx] = i - idx;
            }
            st.push(i);
        }
        
        while(!st.isEmpty()) {
            int idx = st.pop();
            answer[idx] = n - 1 - idx;
        }
        
        return answer;
    }
}