#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> parent;

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

bool unite(int a, int b) {
    int parent_a = find(a);
    int parent_b = find(b);
    if (parent_a == parent_b) return false;
    parent[parent_b] = parent_a;
    return true;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    parent.resize(n);
    for(int i=0;i<n;i++) parent[i]=i;
    
    sort(costs.begin(), costs.end(), [](vector<int> a , vector<int> b){
        return a[2] < b[2];
    });
    
    int cnt = 1;
    for(auto c: costs) {
        int st = c[0];
        int en = c[1];
        int cost = c[2];
        
        if(unite(st, en)) {
            answer += cost;
            cnt++;
            if (cnt == n) break;
        }
    }
    return answer;
}