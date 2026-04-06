#include <vector>
#include <functional>
#include <queue>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    vector<vector<bool>> visited(m, vector<bool>(m,false));
    int dirx[4] = {-1,1,0,0};
    int diry[4] = {0,0,-1,1};
    
    function <int(int,int)> bfs = [&](int x, int y) {
        queue<pair<int,int>> q;
        q.push({x,y});
        visited[x][y] = true;
        int color = picture[x][y];
        int size = 1;
        
        while (!q.empty()) {
            auto [cur_x, cur_y] = q.front();
            q.pop();
            
            for(int i=0;i<4;i++) {
                int next_x = cur_x + dirx[i];
                int next_y = cur_y + diry[i];
                if (0<=next_x && next_x<m && 0<=next_y && next_y<n) {
                    if (picture[next_x][next_y] == color && !visited[next_x][next_y]) {
                        q.push({next_x, next_y});
                        visited[next_x][next_y] = true;
                        size ++;
                    }
                }
            }
        }
        return size;
    };
    
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++) {
            if (picture[i][j] > 0 && !visited[i][j]) {
                int s = bfs(i,j);
                max_size_of_one_area = max(max_size_of_one_area, s);
                number_of_area++;
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}