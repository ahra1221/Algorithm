#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string,int> m;
    for(auto p: participant) {
        m[p]++;
    }
    for(auto c: completion) {
        m[c]--;
    }
    vector<pair<string,int>> v(m.begin(), m.end());
    sort(v.begin(), v.end(),[](auto a, auto b){
        return a.second > b.second;
    });
    return v[0].first;
}