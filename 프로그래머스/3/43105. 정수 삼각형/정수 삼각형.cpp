#include <string>
#include <vector>
#include <functional>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int d = triangle.back().size();
    int dirx[2] = {-1,-1};
    int diry[2] = {0,-1};
    
    vector<vector<int>> dp(d, vector<int>(d,-1));
    dp[0][0] = triangle[0][0];
    dp[1][0] = dp[0][0] + triangle[1][0];
    dp[1][1] = dp[0][0] + triangle[1][1];
    
    int x = 2;
    while (x < d) {
        for(int y=0;y<=x;y++) {
            int now = triangle[x][y];
            int prev_max = 0;
            for(int d=0;d<2;d++) {
                int prevx = x + dirx[d];
                int prevy = y + diry[d];
                if(0<=prevy && prevy < x) {
                    prev_max = max(prev_max, dp[prevx][prevy]);
                } 
            }
            dp[x][y] = now + prev_max;
        }
        x++;
    }
    
    int answer = *max_element(dp.back().begin(), dp.back().end());
    return answer;
}