#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> parent;

int find(int x)
{
    if (parent[x] == x)
        return x;
    return parent[x] = find(parent[x]);
}

bool unite(int a, int b)
{
    int pa = find(a);
    int pb = find(b);
    if (pa == pb)
        return false;
    parent[pb] = pa;
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, E;
    cin >> V >> E;

    vector<vector<int>> edges;

    for (int i = 0; i < E; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        edges.push_back({a, b, c});
    }

    sort(edges.begin(), edges.end(), [](vector<int> a, vector<int> b)
         { return a[2] < b[2]; });

    parent.resize(V + 1);
    for (int i = 1; i <= V; i++)
        parent[i] = i;

    int cnt = 0;
    int answer = 0;
    for (auto e : edges)
    {
        int st = e[0];
        int en = e[1];
        int cost = e[2];

        if (unite(st, en))
        {
            answer += cost;
            cnt++;
            if (cnt == V - 1)
                break;
        }
    }
    cout << answer;
    return 0;
}