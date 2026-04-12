#include<vector>
#include <queue>
#include <tuple>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    int n = maps.size();
    int m = maps[0].size();
    
    int dirx[4] = {1,-1,0,0};
    int diry[4] = {0,0,1,-1};
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    
    queue<tuple<int,int,int>> q;
    q.push({0,0,0});
    visited[0][0] = true;
    while(!q.empty()) {
        auto [curx,cury,curd] = q.front();
        q.pop();
        if (curx == n-1 && cury == m-1) {
            answer = curd + 1;
            break;
        }
        for(int i=0;i<4;i++) {
            int nextx = curx + dirx[i];
            int nexty = cury + diry[i];
            if(0<=nextx && nextx<n && 0<=nexty && nexty<m) {
                if(maps[nextx][nexty] > 0 && !visited[nextx][nexty]) {
                    q.push({nextx,nexty,curd+1});
                    visited[nextx][nexty] = true;
                }
            }
        }
    }
    
    return answer;
}