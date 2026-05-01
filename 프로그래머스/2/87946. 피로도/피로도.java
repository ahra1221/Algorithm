import java.util.*;

class Solution {
    
    int answer = -1;
    
    public void backtracking(int[][] dungeons, List<Integer> cur, int left) {
        answer = Math.max(answer, cur.size());
        for(int i=0;i<dungeons.length;i++) {
            int need = dungeons[i][0];
            int use = dungeons[i][1];
            if(need <= left && !cur.contains(i)) {
                cur.add(i);
                backtracking(dungeons,cur,left-use);
                cur.remove(cur.size()-1);
            }
        }
    }
    
    public int solution(int k, int[][] dungeons) {
       backtracking(dungeons, new ArrayList<>(), k);
       return answer;
    }
}