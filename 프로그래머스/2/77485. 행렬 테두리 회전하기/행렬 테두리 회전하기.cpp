#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    
    vector<vector<int>> graph(rows, vector<int>(columns,0));
    int num = 1;
    for(int i=0;i<rows;i++) {
        for(int j=0;j<columns;j++) {
            graph[i][j] = num++;
        }
    }
    
    for(auto q: queries) {
        int x1 = q[0]-1, y1 = q[1]-1;
        int x2 = q[2]-1, y2 = q[3]-1;
        
        int nx = x1, ny = y1;
        int min_val = graph[x2][y2];
        int prev = graph[nx][ny];
        // right
        while(ny <= y2) {
            if (ny == y2) break;
            min_val = min(min_val, prev);
            int next = graph[x1][ny+1];
            graph[x1][ny+1] = prev;
            prev = next;
            ny++;
        }
        
        // down
        while(nx <= x2) {
            if (nx == x2) break;
            min_val = min(min_val, prev);
            int next = graph[nx+1][y2];
            graph[nx+1][y2] = prev;
            prev = next;
            nx++;
        }
        
        // left
        while(ny >= y1) {
            if (ny == y1) break;
            min_val = min(min_val, prev);
            int next = graph[x2][ny-1];
            graph[x2][ny-1] = prev;
            prev = next;
            ny--;
        }
        
        // up
        while(nx >= x1) {
            if(nx==x1) break;
            min_val = min(min_val, prev);
            int next = graph[nx-1][y1];
            graph[nx-1][y1] = prev;
            prev = next;
            nx--;
        }
        answer.push_back(min_val);
    }
    return answer;
}