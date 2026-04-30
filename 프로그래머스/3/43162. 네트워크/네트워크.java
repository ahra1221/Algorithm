import java.util.*;

class Solution {
    public void bfs(int x, int n, Map<Integer,List<Integer>> map, boolean[] v) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(x);
        v[x] = true;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for(int l: map.getOrDefault(cur, new ArrayList<>())) {
                if (!v[l]) {
                    q.add(l);
                    v[l] = true;
                }
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        Map<Integer,List<Integer>> map = new HashMap<>();
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                if (i!=j && computers[i][j] == 1) {
                    map.computeIfAbsent(i, k->new ArrayList<>()).add(j);
                }
            }
        }
        
        boolean[] visited = new boolean[n];
        for(int i=0;i<n;i++) {
            if(!visited[i]) {
                bfs(i,n,map,visited);
                answer++;
            }
        }
        
        return answer;
    }
}