#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = s.length();
    for(int i=1;i<=s.length() / 2;i++) {
        int len = 0;
        string prev = s.substr(0, i);
        int zip = 1;
        for(int idx=i;idx<s.length();idx+=i) {
            string tmp = s.substr(idx, i);
            if (prev != tmp) {
                // 계산
                if (zip > 1) {
                    len += to_string(zip).length();
                }
                len += prev.length();
                prev = tmp;
                zip = 1;
            } else {
                zip ++;
            }
        }
        if (zip > 1) {
            len += to_string(zip).length();
        }
        len += prev.length();
        answer = min(answer, len);
    }
    return answer;
}