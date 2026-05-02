import java.util.*;

class Solution {
    Set<Integer> s = new HashSet<>();
    public void dfs(int[] numbers, Set<Integer> cur) {
        if (cur.size() == 2) {
            int sum = 0;
            for(int x: cur) sum+= numbers[x];
            s.add(sum);
            return;
        }
        
        for(int i=0;i<numbers.length;i++) {
            if(!cur.contains(i)) {
                cur.add(i);
                dfs(numbers,cur);
                cur.remove(i);
            }
        }
        
    }
    public int[] solution(int[] numbers) {
        dfs(numbers, new HashSet<>());
        
        int[] answer = new int[s.size()];
        int idx = 0;
        for(int x: s) answer[idx++] = x;
        Arrays.sort(answer);
        return answer;
    }
}