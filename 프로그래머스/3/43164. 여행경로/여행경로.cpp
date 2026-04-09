#include <string>
#include <vector>
#include <functional>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer = {"ICN"};
    unordered_map<string,vector<pair<string, bool>>> m;
    for(auto t: tickets) {
        string a = t[0];
        string b = t[1];
        m[a].push_back({b, false});
    } // icn : sfo,false
    
    for(auto& [key, val]: m) {
        sort(val.begin(), val.end(), [](auto a, auto b) {
            return a.first < b.first;
        });
    }
    
    bool found = false;
    
    function<void(string)> dfs = [&](string curr) {
        if (found) return;
        if (answer.size() == tickets.size() + 1) {
            found = true;
            return;
        }
        for(auto& next: m[curr]) {
            if(!next.second) {
                next.second = true;
                answer.push_back(next.first);

                dfs(next.first);
                if (found) return;

                next.second = false;
                answer.pop_back();
            }
        }
    };
    
    
    dfs("ICN");
    
    return answer;
}