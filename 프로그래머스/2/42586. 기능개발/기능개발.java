import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> arr = new ArrayList<>();
        int n = speeds.length;
        Stack<Integer> st = new Stack<>();
        
        for(int i=0;i<n;i++) {
            int p = 100 - progresses[i], s = speeds[i];
            int work = (p + s - 1) / s;
            
            if(st.isEmpty() || st.firstElement() >= work) st.push(work);
            else {
                arr.add(st.size());
                st.clear();
                st.push(work);
            }
        }
        arr.add(st.size());
        
        int[] answer = new int[arr.size()];
        for(int i=0;i<arr.size();i++) {
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}