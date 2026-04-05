#include <string>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

string solution(string my_string) {
    string answer = "";
    unordered_set <char> s;
    for(auto str: my_string) {
        if (!s.count(str)) {
            answer += str;
            s.insert(str);
        }
    }
    return answer;
}