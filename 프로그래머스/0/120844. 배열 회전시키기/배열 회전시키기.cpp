#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> numbers, string direction) {
    vector<int> answer;
    if (direction == "right") {
        answer.push_back(numbers.back());
        for(int i=0;i<numbers.size()-1;i++) {
            answer.push_back(numbers[i]);
        }
    } else {
        for(int i=1;i<numbers.size();i++) {
            answer.push_back(numbers[i]);
        }
        answer.push_back(numbers.front());
    }
    return answer;
}