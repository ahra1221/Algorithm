import java.util.*;

class Solution {
    public int[] solution(int n) {
        int target = 0;
        for(int i=1;i<=n;i++) target += i;
        
        int[] dirx = {1,0,-1};
        int[] diry = {0,1,-1};
        int[][] snail = new int[n][n];
        
        int num = 1;
        int d = 0;
        int x = 0, y = 0;
        while(num <= target) {
            snail[x][y] = num;
            
            int nx = x+dirx[d], ny = y+diry[d];
            if(nx<0 || nx>=n || ny<0 || ny>=n || snail[nx][ny] != 0) {
                d = (d+1) % 3;
                nx = x+dirx[d];
                ny = y+diry[d];
            }
            x = nx;
            y = ny;
            num++;
        }
        int[] answer = new int[target];
        int idx = 0;
        for(int[] s: snail) {
            for(int a: s) {
                if (a > 0) answer[idx++] = a;
            }
        }
        
        return answer;
    }
}