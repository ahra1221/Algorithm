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

    int answer = 0;
    vector<int> parent(100001, -1);
    parent[N] = N;

    queue<pair<int, int>> q;
    q.push({N, 0});
    while (!q.empty())
    {
        auto [now, dist] = q.front();
        q.pop();

        if (now == K)
        {
            answer = dist;
            break;
        }

        vector<int> v = {now - 1, now + 1, now * 2};
        for (auto next : v)
        {
            if (0 <= next && next < 100001 && parent[next] < 0)
            {
                q.push({next, dist + 1});
                parent[next] = now;
            }
        }
    }
    cout << answer << "\n";

    vector<int> ans;
    ans.push_back(K);
    int tmp = K;
    while (tmp != N)
    {
        ans.push_back(parent[tmp]);
        tmp = parent[tmp];
    }
    reverse(ans.begin(), ans.end());
    for (auto p : ans)
    {
        cout << p << " ";
    }

    return 0;
}