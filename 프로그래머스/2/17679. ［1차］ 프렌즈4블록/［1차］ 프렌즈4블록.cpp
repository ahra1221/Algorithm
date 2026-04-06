#include <string>
#include <vector>
#include <set>
#include <functional>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    set<pair<int,int>> erase_set;
    
    function<bool(vector<vector<char>>&)> check4 = [&](vector<vector<char>>& b) {
        int dx[3] = {0, 1, 1};
        int dy[3] = {1, 0, 1};
        bool found = false;
        
        for(int i=0;i<m-1;i++) {
            for(int j=0;j<n-1;j++) {
                if (b[i][j] == ' ') continue;
                
                char target = b[i][j];
                bool flag = true;
                
                for (int d = 0; d < 3; d++) {
                    if (b[i + dx[d]][j + dy[d]] != target) {
                        flag = false;
                        break;
                    }
                }
                
                if (flag) {
                    found = true;
                    erase_set.insert({i, j});
                    for (int d = 0; d < 3; d++) {
                        erase_set.insert({i + dx[d], j + dy[d]});
                    }
                }
            }
        }
        return found;
    };
    
    function<void(vector<vector<char>>&)> erase = [&](vector<vector<char>>& b) {
        for(auto [x,y]: erase_set) {
            b[x][y] = ' ';
            answer++;
        }
    };
    
    function<void(vector<vector<char>>&)> down = [&](vector<vector<char>>& b) {
        for(int col=0;col<n;col++) {
            int write = m-1;
            for(int row=m-1;row>=0;row--) {
                if(b[row][col] != ' ') {
                    b[write][col] = b[row][col];
                    if (write != row) {
                        b[row][col] = ' ';
                    }
                    write--;
                }
            }
            
            for(int row = write; row >=0; row--) {
                b[row][col] = ' ';
            }
        }
    };
    
    vector<vector<char>> tmp(m, vector<char>(n));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            tmp[i][j] = board[i][j];
        }
    }
    
    while(true) {
        erase_set.clear();
        
        bool found = check4(tmp);
        if (!found) break;
        
        erase(tmp);
        down(tmp);
    }
    
    return answer;
}