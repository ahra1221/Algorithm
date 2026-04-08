#include <string>
#include <vector>
#include <functional>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    
    function <string(int)> solve = [&](int num) {
        string s = "";
        while (num>0) {
            s = to_string(num%2) + s;
            num /= 2;
        }
        s = string(n - s.length(), '0') + s;
        return s;
    };
    
    for(int i=0;i<n;i++) {
        string tmp = "";
        string a1 = solve(arr1[i]);
        string a2 = solve(arr2[i]);
        
        for(int j=0;j<n;j++) {
            if (a1[j] == '1' || a2[j] == '1') {
                tmp += "#";
            } else {
                tmp += " ";
            }
        }
        answer.push_back(tmp);
    }
    return answer;
}