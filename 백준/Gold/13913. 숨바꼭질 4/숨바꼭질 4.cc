#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    queue<pair<int, int>> q;
    vector<int> parent(100001, -1);

    q.push({N, 0});
    parent[N] = N;
    while (!q.empty())
    {
        int now = q.front().first;
        int dist = q.front().second;
        q.pop();
        if (now == K)
        {
            cout << dist << "\n";
            break;
        }

        vector<int> route = {now - 1, now + 1, now * 2};
        for (int i = 0; i < 3; i++)
        {
            int next = route[i];
            if (next < 0 || next > 100000)
                continue;
            if (parent[next] < 0)
            {
                q.push({next, dist + 1});
                parent[next] = now;
            }
        }
    }

    vector<int> path;
    int cur = K;
    while (cur != N)
    {
        path.push_back(cur);
        cur = parent[cur];
    }
    path.push_back(N);
    reverse(path.begin(), path.end());

    for (auto p : path)
    {
        cout << p << " ";
    }
    return 0;
}