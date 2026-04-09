#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <unordered_map>

using namespace std;

bool check(string target) {
    set<char> open = {'(','{','['};
    unordered_map<char,char> p = {
        {')','('},
        {'}','{'},
        {']','['}
    };
    
    vector<char> stack;
    for(char& t: target) {
        if (open.count(t)) { // 여는괄호
            stack.push_back(t);
        } else { // 닫는괄호
            if (!stack.empty() && stack.back() == p[t]) { // 쌍이 일치함
                stack.pop_back();
            } else {
                return false;
            }
        }
    }
    if (!stack.empty()) return false;
    return true;
}

int solution(string s) {
    int answer = 0;
    
    for(int x=0;x<s.length();x++) {
        string tmp = string(s.begin()+x, s.end()) + string(s.begin(), s.begin()+x);
        if(check(tmp)) answer++;
    }
    
    return answer;
}