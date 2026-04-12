#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    
    vector<vector<int>> graph(rows, vector<int>(columns));
    int num = 0;
    for(int i=0;i<rows;i++) {
        for(int j=0;j<columns;j++) {
            graph[i][j] = ++num;
        }
    }
    
    for(auto q: queries) {
        int x1 = q[0]-1, y1 = q[1]-1, x2 = q[2]-1, y2 = q[3]-1;
        int nx = x1, ny = y1;
        int prev = graph[nx][ny];
        int minval = rows * columns;
        
        // right
        while(ny+1 <= y2) {
            minval = min(prev, minval);
            int next = graph[nx][ny+1];
            graph[nx][ny+1] = prev;
            prev = next;
            ny++;
        }
        
        // down
        while(nx+1 <= x2) {
            minval = min(prev, minval);
            int next = graph[nx+1][ny];
            graph[nx+1][ny] = prev;
            prev = next;
            nx++;
        }
        
        // left
        while(ny-1 >= y1) {
            minval = min(prev, minval);
            int next = graph[nx][ny-1];
            graph[nx][ny-1] = prev;
            prev = next;
            ny--;
        }
        
        // up
        while(nx-1 >= x1) {
            minval = min(prev, minval);
            int next = graph[nx-1][ny];
            graph[nx-1][ny] = prev;
            prev = next;
            nx--;
        }
        answer.push_back(minval);
    }
    
    
    return answer;
}