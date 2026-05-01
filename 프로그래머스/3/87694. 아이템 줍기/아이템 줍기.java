import java.util.*;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        
        int[][] map = new int[102][102];
        for(int[] rec: rectangle) {
            int x1 = rec[0]*2, y1 = rec[1]*2;
            int x2 = rec[2]*2, y2 = rec[3]*2;
            
            for (int x = x1; x <= x2; x++) {
                for (int y = y1; y <= y2; y++) {
                    if(map[x][y] != 2) map[x][y] = 1;
                }
            }
            
            //내부
            for (int x = x1 + 1; x < x2; x++) {
                for (int y = y1 + 1; y < y2; y++) {
                    map[x][y] = 2;
                }
            }
        }
        
        int[] dirx = {-1,1,0,0};
        int[] diry = {0,0,-1,1};
        boolean[][] visited = new boolean[102][102];
        
        Queue<int[]> q = new ArrayDeque<>(); // x,y,distance
        q.add(new int[]{characterX*2, characterY*2,0});
        visited[characterX*2][characterY*2] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1], dist = cur[2];
            if(x == itemX*2 && y == itemY*2) {
                return dist / 2;
            }
            
            for(int i=0;i<4;i++) {
                int nx = x+dirx[i], ny = y+diry[i];
                if (0 <= nx && nx < 102 && 0 <= ny && ny < 102 && !visited[nx][ny] && map[nx][ny] == 1) {
                    q.add(new int[]{nx,ny,dist+1});
                    visited[nx][ny] = true;
                }
            }
            
        }
        
        return answer;
    }
}