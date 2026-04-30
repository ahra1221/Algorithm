import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        int h = triangle.length;
        
        int[][] dp = new int[h][h];
        dp[0][0] = triangle[0][0];
        
        int height = 2;
        while (height <= h) {
            for(int i=0;i<height;i++) {
                if (i == 0) { // 첫번째값
                    dp[height-1][i] = triangle[height-1][i] + dp[height-2][i];
                } else if (i == height-1) { // 끝값
                    dp[height-1][i] = triangle[height-1][i] + dp[height-2][i-1];
                } else { // 중간값
                    dp[height-1][i] = triangle[height-1][i] + Math.max(dp[height-2][i-1], dp[height-2][i]);
                }
            }
            height++;
        }
        
        int answer = 0;
        for(int x: dp[h-1]) {
            answer = Math.max(answer, x);
        }
        
        return answer;
    }
}