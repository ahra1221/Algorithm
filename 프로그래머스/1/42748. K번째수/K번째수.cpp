#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int c=0;c<commands.size();c++) {
        int i = commands[c][0];
        int j = commands[c][1];
        int k = commands[c][2];
        
        vector<int> tmp(array.begin()+i-1, array.begin()+j);
        sort(tmp.begin(), tmp.end());
        answer.push_back(tmp[k-1]);
    }
    return answer;
}