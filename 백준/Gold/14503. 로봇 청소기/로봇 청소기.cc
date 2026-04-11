#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    int r, c, d;
    cin >> r >> c >> d;

    vector<vector<int>> room(N, vector<int>(M));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> room[i][j];
        }
    }

    int ans = 0;
    unordered_map<int, vector<pair<int, int>>> directions = {
        // 상 하 좌 우
        {0, {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}}, // 북
        {1, {{0, 1}, {0, -1}, {-1, 0}, {1, 0}}}, // 동
        {2, {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}}, // 남
        {3, {{0, -1}, {0, 1}, {1, 0}, {-1, 0}}}  // 서
    };

    int nx = r, ny = c;
    int nd = d;
    while (true)
    {
        if (room[nx][ny] == 0)
        {
            room[nx][ny] = -1; // 청소
            ans++;
        }
        bool has_room = false;
        for (auto [dx, dy] : directions[nd])
        {
            int nextx = nx + dx, nexty = ny + dy;
            if (0 <= nextx && nextx < N && 0 <= nexty && nexty < M)
            {
                if (room[nextx][nexty] == 0)
                {
                    has_room = true;
                    break;
                }
            }
        }
        if (!has_room)
        {
            int backx = nx + directions[nd][1].first;
            int backy = ny + directions[nd][1].second;
            if (0 <= backx && backx < N && 0 <= backy && backy < M && room[backx][backy] != 1)
            {
                nx = backx;
                ny = backy;
            }
            else
                break;
        }
        else
        {
            nd = (nd + 3) % 4; // 회전
            int frontx = nx + directions[nd][0].first;
            int fronty = ny + directions[nd][0].second;
            if (room[frontx][fronty] == 0)
            {
                nx = frontx;
                ny = fronty;
            }
        }
    }

    cout << ans;
    return 0;
}