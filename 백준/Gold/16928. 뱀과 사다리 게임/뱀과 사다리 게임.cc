#include <iostream>
#include <vector>
#include <functional>
#include <queue>
#include <set>
#include <unordered_map>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    unordered_map<int, int> ladder(N);
    unordered_map<int, int> snake(M);
    set<int> ladder_st;
    set<int> snake_st;

    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        ladder[a] = b;
        ladder_st.insert(a);
    }

    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        snake[a] = b;
        snake_st.insert(a);
    }

    int answer = 0;
    vector<int> visited(101, false);

    queue<pair<int, int>> q;
    q.push({1, 0});
    visited[1] = true;
    while (!q.empty())
    {
        int curp = q.front().first;
        int curt = q.front().second;
        q.pop();
        if (curp == 100)
        {
            answer = curt;
            break;
        }
        for (int i = 1; i <= 6; i++)
        {
            int next = curp + i;
            if (next > 100)
                break;
            if (ladder_st.count(next))
                next = ladder[next];
            else if (snake_st.count(next))
                next = snake[next];

            if (!visited[next])
            {
                q.push({next, curt + 1});
                visited[next] = true;
            }
        }
    }
    cout << answer;
    return 0;
}