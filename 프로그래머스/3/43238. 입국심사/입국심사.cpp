#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end(), greater<>());
    
    long long left = 1;
    long long right = (long long)times[0] * n;
    
    while (left <= right) {
        long long mid = (left + right) / 2;
        long long total = 0;
        for (auto t: times) {
            total += mid / t;
            if (total >= n) break;
        }
        if (total >= n) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return answer;
}