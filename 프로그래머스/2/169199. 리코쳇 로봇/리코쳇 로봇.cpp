#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <tuple>

using namespace std;

int solution(vector<string> board) {
    int answer = 0;
    int n = board.size();
    int m = board[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    
    function<pair<int,int>()> find_start = [&]() {
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++){
                if (board[i][j] == 'R') {
                    return pair<int,int>(i,j);
                }
            }
        }
        return pair<int,int>(-1, -1);
    };
    
    function<int(int,int)> bfs = [&](int x, int y) {
        queue<tuple<int,int,int>> q;
        q.push({x,y,0});
        visited[x][y] = true;
        
        while (!q.empty()) {
            auto [curx,cury,curc] = q.front();
            q.pop();
            
            if (board[curx][cury] == 'G') {
                return curc;
            }
            
            // 상
            int i = curx;
            while (i-1>=0 && board[i-1][cury] != 'D') i--;
            if (!visited[i][cury]) {
                q.push({i,cury,curc+1});
                visited[i][cury] = true;
            }
            
            // 하
            i = curx;
            while (i+1<n && board[i+1][cury] != 'D') i++;
            if (!visited[i][cury]) {
                q.push({i,cury,curc+1});
                visited[i][cury] = true;
            }
            
            // 좌
            int j = cury;
            while (j-1>=0 && board[curx][j-1] != 'D') j--;
            if (!visited[curx][j]) {
                q.push({curx,j,curc+1});
                visited[curx][j] = true;
            }
            
            // 우
            j = cury;
            while (j+1<m && board[curx][j+1] != 'D') j++;
            if (!visited[curx][j]) {
                q.push({curx,j,curc+1});
                visited[curx][j] = true;
            }
        }
        return -1;
    };
    
    auto [startx,starty] = find_start();
    answer = bfs(startx,starty);
    return answer;
}