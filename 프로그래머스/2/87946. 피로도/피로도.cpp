#include <string>
#include <vector>
#include <functional>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    function<void(int, set<int>)> backtracking = [&](int tired, set<int> curr) {
        answer = max(answer, (int)curr.size());
        
        for(int i=0;i<dungeons.size();i++) {
            int a = dungeons[i][0];
            int b = dungeons[i][1];
            if (tired >= a && !curr.count(i)) {
                curr.insert(i);
                backtracking(tired-b, curr);
                curr.erase(i);
            }
        }
    };
    
    backtracking(k, set<int>());
    
    return answer;
}