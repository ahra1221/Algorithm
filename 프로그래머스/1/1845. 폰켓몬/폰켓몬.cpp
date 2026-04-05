#include <vector>
#include <unordered_set>
using namespace std;

int solution(vector<int> nums)
{
    unordered_set<int> s(nums.begin(), nums.end());
    int answer = s.size();
    int l = nums.size() / 2;
    if (answer > l) {
        return l;
    }
    return answer;
}