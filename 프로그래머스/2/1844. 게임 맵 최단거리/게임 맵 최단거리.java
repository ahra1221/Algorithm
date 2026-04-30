import java.util.*;

class Solution {
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        int n = maps.length, m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0,0,1});
        visited[0][0] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1], d = cur[2];
            
            if (x==n-1 && y==m-1) {
                answer = d;
                break;
            }
            
            for(int i=0;i<4;i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (0<=nx && nx<n && 0<=ny && ny<m && !visited[nx][ny] && maps[nx][ny] == 1) {
                    q.add(new int[]{nx,ny,d+1});
                    visited[nx][ny] = true;
                }
            }
        }
        return answer == 0 ? -1 : answer;
    }
}