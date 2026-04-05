#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    vector<int> width;
    vector<int> height;
    for(auto& s: sizes){
        int w = s[0];
        int h = s[1];
        width.push_back(max(w,h));
        height.push_back(min(w,h));
    }
    int max_w = *max_element(width.begin(), width.end());
    int max_h = *max_element(height.begin(), height.end());
    answer = max_w * max_h;
    return answer;
}