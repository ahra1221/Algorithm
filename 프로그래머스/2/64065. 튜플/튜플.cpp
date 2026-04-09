#include <string>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>
#include <unordered_set>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    vector<vector<int>> v;
    vector<int> tmp;
    bool flag = false;
    string num = "";
    
    for(int i=1;i<s.length()-1;i++) {
        if (s[i] == '{') {
            flag = true;
            continue;
        }
        if (isdigit(s[i])) {
            num += s[i];
        }
        if (s[i] == ',' && flag) {
            if (!num.empty()) {
                tmp.push_back(stoi(num));
                num = "";   
            }
            continue;
        }
        if (s[i] == '}') {
            flag = false;
            if (!num.empty()) {
                tmp.push_back(stoi(num));
                num = ""; 
            }
            v.push_back(tmp);
            tmp.clear();
            continue;
        }
        if (s[i] == ',' && flag) {
            tmp.push_back(stoi(num));
            num = "";
        }
    }
    
    sort(v.begin(), v.end(), [](vector<int> a, vector<int> b){
        return a.size() < b.size();
    });
    
    
    unordered_set<int> set;
    for(auto a:v) {
        for(auto b: a) {
            if (!set.count(b)) {
                set.insert(b);
                answer.push_back(b);
                break;
            }
        }
    }
    
    return answer;
}