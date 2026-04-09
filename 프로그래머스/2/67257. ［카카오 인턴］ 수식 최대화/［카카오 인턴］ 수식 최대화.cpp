#include <string>
#include <vector>

using namespace std;

long long solution(string expression) {
    long long answer = 0;
    
    vector<long long> numbers;
    vector<char> exp;
    string number = "";
    for(const auto& e: expression) {
        if(isdigit(e)) {
            number += e;
        } else {
            numbers.push_back(stoll(number));
            number.clear();
            exp.push_back(e);
        }
    }
    numbers.push_back(stoll(number));
    
    vector<vector<char>> orders = {
        {'+', '-', '*'},
        {'+', '*', '-'},
        {'-', '+', '*'},
        {'-', '*', '+'},
        {'*', '+', '-'},
        {'*', '-', '+'}
    };
    for(const auto& order: orders) {
        
        vector<long long> curNums = numbers;
        vector<char> curExps = exp;
        
        for(char op: order) {
            vector<long long> nextNums;
            vector<char> nextExps;

            nextNums.push_back(curNums[0]);
            for (int i = 0; i < curExps.size(); i++) {
                if (curExps[i] == op) {
                    long long a = nextNums.back(); // 현재 숫자
                    long long b = curNums[i + 1]; // 다음숫자
                    long long res;
                    
                    if (op == '+') res = a + b;
                    else if (op == '-') res = a - b;
                    else res = a * b;
                    
                    nextNums.back() = res;
                } else {
                    nextNums.push_back(curNums[i+1]);
                    nextExps.push_back(curExps[i]);
                }
            }
            curNums = nextNums;
            curExps = nextExps;
        }
        answer = max(answer, llabs(curNums[0]));
    }

    return answer;
}