#include <string>
#include <vector>
#include <functional>
#include <iostream>

using namespace std;

int solution(string word) {
    int answer = 0;
    int count = 0;
    char w[5] = {'A', 'E', 'I', 'O', 'U'};
    
    function<void(string&)> dfs = [&](string& s) {
        if (s.length() > 5 || answer != 0) return;

        if (!s.empty()) {
            count++;
            if (s == word) {
                answer = count;
                return;
            }
        }

        for (int i = 0; i < 5; i++) {
            s.push_back(w[i]);
            dfs(s);
            s.pop_back();
        }
    };
    
    string s = "";
    dfs(s);
        
    return answer;
}