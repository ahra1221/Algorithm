#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer(id_list.size(), 0);
    
    unordered_map<string, int> report_count;
    unordered_map<string, set<string>> dict;
    vector<string> reported;
    
    for(auto r: report) {
        stringstream ss(r);
        string a,b;
        ss >> a >> b;
        if (!dict[a].count(b)) report_count[b]++;
        dict[a].insert(b);
    }
    
    for(auto [key,val]: report_count) {
        if (val >= k) reported.push_back(key);
    }
    
    for(int i=0;i<id_list.size();i++) {
        set<string> report_set = dict[id_list[i]];
        for (auto r: reported) {
            if (report_set.count(r)) answer[i]++;
        }
    }
    
    return answer;
}