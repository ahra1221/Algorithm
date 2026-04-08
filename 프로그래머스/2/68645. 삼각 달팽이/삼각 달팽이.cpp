#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    int dirx[3] = {1,0,-1};
    int diry[3] = {0,1,-1};
    
    int target = 0;
    for(int i=1;i<=n;i++) target += i;
    
    vector<vector<int>> v(n, vector<int>(n,0));
    
    int num = 1;
    int x = 0;
    int y = 0;
    int dir = 0;
    while (num <= target) {
        v[x][y] = num;
        
        // 다음 좌표 계산
        int nx = x + dirx[dir];
        int ny = y + diry[dir];
        
        if (nx < 0 || nx >= n || ny < 0 || ny >= n || v[nx][ny] != 0) {
            dir = (dir + 1) % 3;
            nx = x + dirx[dir];
            ny = y + diry[dir];
        }
        
        x = nx;
        y = ny;
        num ++;
    }
    
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if (v[i][j] > 0) answer.push_back(v[i][j]);
        }
    }
    
    return answer;
}