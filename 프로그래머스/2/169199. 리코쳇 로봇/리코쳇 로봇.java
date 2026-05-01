import java.util.*;

class Solution {
    public int solution(String[] board) {
        int r = board.length, c = board[0].length();
        
        int[] start = new int[2];
        int[] end = new int[2];
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if (board[i].charAt(j) == 'R') start = new int[]{i,j};
                else if (board[i].charAt(j) == 'G') end = new int[]{i,j};
            }
        }
        
        int[] dirx = {1,-1,0,0};
        int[] diry = {0,0,1,-1};
        boolean[][] visited = new boolean[r][c];
        
        Queue<int[]> q = new ArrayDeque<>(); // x,y,count
        q.add(new int[]{start[0],start[1], 0});
        visited[start[0]][start[1]] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y= cur[1];
            if (x == end[0] && y == end[1]) {
                return cur[2];
            }
            
            for(int i=0;i<4;i++) {
                int nx = x, ny = y;
                while(0<=nx && nx<r && 0<=ny && ny<c && board[nx].charAt(ny) != 'D') {
                    nx += dirx[i];
                    ny += diry[i];
                }
                nx -= dirx[i];
                ny -= diry[i];
                if (!visited[nx][ny]){
                    q.add(new int[]{nx,ny,cur[2]+1});
                    visited[nx][ny] = true;
                }
            }
        }
        
        return -1;
    }
}