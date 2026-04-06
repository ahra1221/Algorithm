#include<vector>
#include<queue>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int n = maps.size();
    int m = maps[0].size();
    
    vector<vector<int>> dist(n, vector<int>(m,-1));
    int dirx[4] = {-1,1,0,0};
    int diry[4] = {0,0,-1,1};
    
    // bfs
    queue<pair<int,int>> q;
    q.push({0,0});
    dist[0][0] = 1;
    
    while (!q.empty()) {
        auto [x,y] = q.front();
        q.pop();
        
        for(int i=0; i<4; i++) {
            int nx = x + dirx[i];
            int ny = y + diry[i];
            if (0<=nx && nx<n && 0<=ny && ny<m) {
                if (maps[nx][ny] == 1 && dist[nx][ny] < 0) {
                    dist[nx][ny] = dist[x][y] + 1;
                    q.push({nx,ny});
                }
            }
        }
    }
    
    return dist[n-1][m-1];
}