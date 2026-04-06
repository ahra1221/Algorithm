#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    
    set<int> lost_set(lost.begin(), lost.end());
    set<int> reserve_set(reserve.begin(), reserve.end());
    vector<int> remove;
    
    for(auto lost: lost_set) {
        if (reserve_set.count(lost)) {
            remove.push_back(lost);
        }
    }
    
    for(auto r: remove) {
        lost_set.erase(r);
        reserve_set.erase(r);
    }
    
    int answer = n - lost_set.size();
    
    for(auto x: lost_set) {
        if (reserve_set.count(x-1)) {
            reserve_set.erase(x-1);
            answer++;
        } else if (reserve_set.count(x+1)) {
            reserve_set.erase(x+1);
            answer++;
        }
    }
    
    return answer;
}