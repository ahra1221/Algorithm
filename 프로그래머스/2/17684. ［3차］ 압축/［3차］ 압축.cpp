#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    
    unordered_map<string,int> dict;
    for(int i=1;i<27;i++) {
        dict[string(1, 'A' + (i - 1))] = i;
    }
    
    int idx = 27;
    string w = "";
    w += msg[0];
    for(int i=1;i<msg.length();i++) {
        if (dict.count(w + msg[i])) {
            w += msg[i];
            continue;
        } else {
            answer.push_back(dict[w]);
            dict[w + msg[i]] = idx;
            w = msg[i];
            idx ++;
        }
    }
    answer.push_back(dict[w]);
    
    return answer;
}