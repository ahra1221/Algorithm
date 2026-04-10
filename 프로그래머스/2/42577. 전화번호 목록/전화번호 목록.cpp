#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
    
    for(int i=1;i<phone_book.size();i++) {
        string s = phone_book[i];
        string prefix = phone_book[i-1];
        if(s.substr(0, prefix.length()) == prefix) {
            return false;
        }
    }
    return answer;
}