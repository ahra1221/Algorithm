#include <string>
#include <vector>
#include <functional>
#include <queue>
#include <unordered_map>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    unordered_map<int, vector<int>> graph;
    for(int i=0;i<n;i++) {
        for(int j=i+1;j<n;j++) {
            if (i == j) continue;
            else if (computers[i][j] == 1) {
                graph[i].push_back(j);
                graph[j].push_back(i);
            }
        }
    }
    
    vector<bool> visited(n,false);
    function <void(int)> bfs = [&](int node) {
        queue<int> q;
        q.push(node);
        visited[node] = true;
        while (!q.empty()) {
            int cur_node = q.front();
            q.pop();
            for(auto x: graph[cur_node]) {
                if (!visited[x]) {
                    q.push(x);
                    visited[x] = true;
                }
            }
        }
    };
    
    for(int i=0;i<n;i++) {
        if (!visited[i]) {
            bfs(i);
            answer++;
        }
    }
    
    return answer;
}