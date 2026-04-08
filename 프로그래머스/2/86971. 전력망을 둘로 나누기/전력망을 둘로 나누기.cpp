#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <functional>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    unordered_map<int, vector<int>> graph;
    unordered_map<int, vector<int>> temp;
    for(auto w: wires) {
        int v1 = w[0];
        int v2 = w[1];
        graph[v1].push_back(v2);
        temp[v1].push_back(v2);
        graph[v2].push_back(v1);
    }
    
    function <int(int, int)> bfs = [&](int st, int pass) {
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(st);
        visited[st] = true;
        int cnt = 0;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            for(auto next: graph[cur]) {
                if (next == pass) continue;
                if (!visited[next]) {
                    q.push(next);
                    visited[next] = true;
                    cnt ++;
                }
            }
        }
        return cnt;
    };
    
    for(int i =1;i<=n;i++) {
        for(auto j: temp[i]) {
            int dist = abs(bfs(i,j) - bfs(j,i));
            answer = min(answer,dist);
        }
    }
        
    return answer;
}