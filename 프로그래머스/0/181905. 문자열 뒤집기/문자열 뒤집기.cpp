#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string my_string, int s, int e) {
    string answer = "";
    answer += my_string.substr(0,s);
    for(int i=e; i>=s; i--){
        answer += my_string[i];
    }
    answer += my_string.substr(e+1,my_string.length()-e);
    return answer;
}