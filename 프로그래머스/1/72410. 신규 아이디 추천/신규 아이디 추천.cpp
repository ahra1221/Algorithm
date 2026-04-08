#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cctype>

using namespace std;

string solution(string new_id) {
    string answer = "";
    transform(new_id.begin(), new_id.end(), new_id.begin(), ::tolower); // 1
    
    for(auto x: new_id) { // 2
        if (isalnum(x) || x == '-' || x == '_' || x == '.') {
            answer += x;
        } else continue;
    }
    
    char prev = answer[0];
    string tmp = "";
    tmp += prev;
    for (int i=1; i<answer.length();i++) {
        if (answer[i] == '.') {
            if (prev == '.') {
                continue;
            } else {
                tmp += answer[i];
                prev = '.';
            }
        } else {
            tmp += answer[i];
            prev = ' ';
        }
    }
    answer = tmp; // 3
    
    if (answer.front() == '.') {
        answer.erase(0,1);
    }
    if (answer.back() == '.') {
        answer.erase(answer.length()-1,1);
    } // 4
    
    if (answer.empty()) answer = 'a'; // 5
    if (answer.length() >= 16) {
        answer.erase(15, answer.length()-15);
    }
    if (answer.back() == '.') {
        answer.erase(answer.length()-1,1);
    } // 6
    if (answer.length() <= 2) {
        char last = answer.back();
        while (answer.length() < 3) {
            answer += last;
        }
    }
    
    return answer;
}