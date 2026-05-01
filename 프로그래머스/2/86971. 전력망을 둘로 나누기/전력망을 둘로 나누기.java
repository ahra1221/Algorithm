import java.util.*;

class Solution {
    Map<Integer,List<Integer>> wire = new HashMap<>();
    
    public int bfs(int i, int a, int b) {
        Queue<Integer> q = new ArrayDeque<>();
        boolean[] visited = new boolean[wire.size()+1];
        q.add(i);
        visited[i] = true;
        int count = 1;
        
        while(!q.isEmpty()) {
            int cur = q.poll();
            for(int x: wire.get(cur)) {
                if(cur == a && x == b) continue;
                if(cur == b && x == a) continue;
                if(!visited[x]) {
                    q.add(x);
                    visited[x] = true;
                    count++;
                }
            }
        }
        return count;
    }
    public int solution(int n, int[][] wires) {
        for(int[] w: wires) {
            wire.computeIfAbsent(w[0],k->new ArrayList<>()).add(w[1]);
            wire.computeIfAbsent(w[1],k->new ArrayList<>()).add(w[0]);
        }
        
        int answer = wire.size();
        for(int[] w: wires) {
            int a = w[0], b = w[1];
            int cnt = bfs(a,a,b);
            int diff = Math.abs(n-cnt-cnt);
            answer = Math.min(answer,diff);
        }
        
        return answer;
    }
}