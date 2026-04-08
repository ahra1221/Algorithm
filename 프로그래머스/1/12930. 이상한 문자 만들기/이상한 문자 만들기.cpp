#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s) {
    string answer = "";
    int idx = 0;
    for(auto x: s) {
        if (x == ' ') {
            idx = 0;
            answer += x;
            continue;
        }
        
        if (idx % 2 == 0) {
            answer += toupper(x);
        } else {
            answer += tolower(x);
        }
        idx++;
    }
    return answer;
}