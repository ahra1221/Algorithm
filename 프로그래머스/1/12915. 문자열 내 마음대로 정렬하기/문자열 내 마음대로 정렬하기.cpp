#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    sort(strings.begin(), strings.end(), [n](string a, string b){
        if (a[n] == b[n]) {
            return a < b;
        }
        return a[n] < b[n];
    });
    for(auto s: strings) {
        answer.push_back(s);
    }
    return answer;
}