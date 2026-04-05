#include <numeric>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        vector<int> curr;

        function<void(int)> backtracking = [&](int st) {
            if (curr.size() == 2) {
                int sum = 0;
                for (auto idx: curr) {
                    sum += nums[idx];
                }
                if (sum == target) {
                    answer = curr;
                    return;
                }
                return;
            }

            for(int i = st; i<nums.size(); i++) {
                curr.push_back(i);
                backtracking(i+1);
                curr.pop_back();
            }
        };
        backtracking(0);
        return answer;
    };
};