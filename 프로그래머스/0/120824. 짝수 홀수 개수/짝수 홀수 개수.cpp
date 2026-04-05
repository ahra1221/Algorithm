#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer(2,0);
    for(auto x: num_list) {
        if (x % 2 == 0) {
            answer[0] += 1;
        } else {
            answer[1] += 1;
        }
    }
    return answer;
}