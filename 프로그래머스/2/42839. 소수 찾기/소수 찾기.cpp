#include <string>
#include <vector>
#include <functional>
#include <set>
#include <iostream>

using namespace std;

int solution(string numbers) {
    int answer = 0;
    set<int> candidate;
    
    function<bool(int)> is_prime = [](int target) {
        if(target < 2) return false;
        for(int i=2;i*i<=target;i++) {
            if (target%i == 0) return false;
        }
        return true;
    };
    
    function<void(vector<int>)> backtracking = [&](vector<int> curr) {
        if (!curr.empty()) {
            string tmp = "";
            for (auto idx: curr) {
                tmp += numbers[idx];
            }
            candidate.insert(stoi(tmp));
        }
        
        for(int i=0;i<numbers.length();i++) {
            if (find(curr.begin(), curr.end(), i) == curr.end()) {
                curr.push_back(i);
                backtracking(curr);
                curr.pop_back();
            }
        }
    };
    backtracking(vector<int>());
    for(auto c: candidate) {
        if (is_prime(c)) {
            answer++;
        }
    }
    
    return answer;
}