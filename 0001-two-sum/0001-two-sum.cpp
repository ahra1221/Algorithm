class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        unordered_map<int, int> m;
        for(int i = 0; i<nums.size();i++) {
            m[nums[i]] = i;
        }
        for(int i = 0; i<nums.size();i++) {
            int need = target - nums[i];
            if(m.count(need) && m[need] != i) {
                answer.push_back(m[need]);
                answer.push_back(i);
                break;
            }
        }
        return answer;
    };
};