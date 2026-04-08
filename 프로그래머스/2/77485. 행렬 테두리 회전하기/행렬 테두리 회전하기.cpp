#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    int dir = 0; // 0 right, 1 down, 2 left, 3 up
    vector<pair<int,int>> dirs = {
        {0,1},
        {1,0},
        {0,-1},
        {-1,0}
    };
    vector<vector<int>> v(rows, vector<int>(columns));
    int num = 1;
    for(int i = 0; i < rows; i++) {
        for (int j=0; j<columns;j++) {
            v[i][j] = num++;
        }
    }
    
    for (auto& q : queries) {
        int x1 = q[0];
        int y1 = q[1];
        int x2 = q[2];
        int y2 = q[3];
        
        vector<pair<int,int>> border;
        int nx = x1;
        int ny = y1;
        
        // right
        while (ny < y2) {
            border.push_back({nx,ny});
            ny ++;
        }
        
        // down
        while (nx < x2) {
            border.push_back({nx,ny});
            nx++;
        }
        
        // left
        while (ny > y1) {
            border.push_back({nx,ny});
            ny--;
        }
        
        // up
        while (nx > x1) {
            border.push_back({nx,ny});
            nx--;
        }
        
        int x = border[0].first;
        int y = border[0].second;
        int tmp = v[x-1][y-1];
        int min_num = tmp;
        
        for(int i=1;i<border.size();i++) {
           auto [nextx,nexty] = border[i];
           int next = v[nextx-1][nexty-1];
           v[nextx-1][nexty-1] = tmp;
           tmp = next;
           min_num = min(min_num, tmp);
        }
        v[x-1][y-1] = tmp;
        
        answer.push_back(min_num);
    }
    return answer;
}