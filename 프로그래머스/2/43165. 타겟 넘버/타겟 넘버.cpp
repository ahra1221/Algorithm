#include <string>
#include <vector>
#include <functional>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    function<void(int,int)> dfs = [&](int idx, int total) {
        if (idx == numbers.size()) {
            if (total == target) {
                answer++;
            }
            return;
        }
        
        dfs(idx+1, total+numbers[idx]);
        dfs(idx+1, total-numbers[idx]);
    };
    dfs(0,0);
    return answer;
}