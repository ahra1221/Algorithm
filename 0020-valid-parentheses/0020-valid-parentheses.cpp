class Solution {
public:
    bool isValid(string s) {
        vector<char> v;
        unordered_set<char> open = {'(', '{', '['};
        unordered_map<char, char> m = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        for(auto x: s) {
            if (open.count(x)) {
                v.push_back(x);
            } else {
                if (v.empty() || v.back() != m[x]) {
                    return false;
                } else {
                    v.pop_back();
                }
            }
        }
        return v.empty();
    }
};