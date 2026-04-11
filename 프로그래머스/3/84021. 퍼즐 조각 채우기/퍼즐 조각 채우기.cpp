#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

vector<pair<int,int>> normal(vector<pair<int,int>> v) {
    sort(v.begin(), v.end());
    int minx = 1e9, miny = 1e9;
    for (auto [x,y] : v) {
        minx = min(minx, x);
        miny = min(miny, y);
    }
    for(auto& [x,y]: v) {
        x -= minx;
        y -= miny;
    } 
    sort(v.begin(), v.end());
    return v;
}

vector<pair<int,int>> bfs(
    const vector<vector<int>>& graph, 
    int x,
    int y,
    int target, 
    vector<vector<bool>>& visited
) {
    int n = graph.size();
    int dirx[4] = {1,-1,0,0};
    int diry[4] = {0,0,1,-1};
    
    vector<pair<int,int>> points;
    points.push_back({x,y});
    
    queue<pair<int,int>> q;
    q.push({x,y});
    visited[x][y] = true;
    
    while (!q.empty()) {
        auto [a,b] = q.front();
        q.pop();
        
        for(int i=0;i<4;i++) {
            int dx = a + dirx[i];
            int dy = b + diry[i];
            if (0<=dx && dx<n && 0<=dy && dy<n) {
                if (graph[dx][dy] == target && !visited[dx][dy]) {
                    q.push({dx,dy});
                    visited[dx][dy] = true;
                    points.push_back({dx,dy});
                }
            }
        }
    }
    return points;
}

vector<pair<int,int>> rotate(vector<pair<int,int>> v) {
    vector<pair<int,int>> rotated;
    for(auto [x,y]: v) {
        rotated.push_back({y,-1 * x});
    }
    return (normal(rotated));
}

int solution(vector<vector<int>> game_board, vector<vector<int>> table) {
    int answer = 0;
    int n = game_board.size();
    
    vector<vector<pair<int,int>>> game;
    vector<vector<pair<int,int>>> puzzle;
    
    vector<vector<bool>>visited1(n, vector<bool>(n,false));
    vector<vector<bool>>visited2(n, vector<bool>(n,false));
    
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(game_board[i][j] == 0 && !visited1[i][j]) {
                game.push_back(normal(bfs(game_board, i, j, 0, visited1)));
            }
            if(table[i][j] == 1 && !visited2[i][j]) {
                puzzle.push_back(normal(bfs(table, i, j, 1, visited2)));
            }
        }
    }
    
    vector<bool> used(puzzle.size(), false);
    for(auto g: game) {
        for (int i = 0; i < puzzle.size(); i++) {
            if (used[i]) continue;
            if (g.size() != puzzle[i].size()) continue;
            for(int r=0;r<4;r++) {
                if(g == puzzle[i]) {
                    answer += puzzle[i].size();
                    used[i] = true;
                    break;
                }
                puzzle[i] = rotate(puzzle[i]);
            }
            if (used[i]) break;
        }
    }
    
    
    return answer;
}