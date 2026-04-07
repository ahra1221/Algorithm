#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    sort(rocks.begin(), rocks.end());
    
    int left = 0;
    int right = distance;
    while (left <= right) {
        int mid = (left + right) / 2;
        
        int prev = 0;
        int removed = 0;
        for(auto r: rocks) {
            if (r - prev < mid) {
                removed++; 
            } else {
                prev = r;
            }
        }
        
        if (distance - prev < mid) {
            removed++;
        }
        
        if (removed > n) {
            right = mid - 1;
        } else {
            left = mid + 1;
            answer = mid;
        }
    }
    return answer;
}