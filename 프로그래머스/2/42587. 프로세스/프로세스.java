import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        
        Deque<int[]> dq = new ArrayDeque<>();
        for(int i=0;i<priorities.length; i++) {
            dq.addLast(new int[]{i, priorities[i]}); // index, priority
        }
        
        while (!dq.isEmpty()) {
            int max = 0;
            for (int[] job : dq) max = Math.max(max, job[1]);
            
            int[] cur = dq.pollFirst();
            if (cur[1] < max) {
                dq.addLast(cur);
            } else {
                if (cur[0] == location) break;
                else answer ++;
                
            }
        }
        
        return answer;
    }
}