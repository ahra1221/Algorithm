#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cmath>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    unordered_map<int, pair<int,int>> keypad = {
        {1, {3,0}},
        {2, {3,1}},
        {3, {3,2}},
        {4, {2,0}},
        {5, {2,1}},
        {6, {2,2}},
        {7, {1,0}},
        {8, {1,1}},
        {9, {1,2}},
        {0, {0,1}}
    };
    unordered_set<int> left_key = {1,4,7};
    unordered_set<int> right_key = {3,6,9};
    pair<int,int> left = {0,0};
    pair<int,int> right = {0,2};
    
    for(auto n: numbers) {
        if (left_key.count(n)) {
            left = keypad[n];
            answer += "L";
        } else if (right_key.count(n)) {
            right = keypad[n];
            answer += "R";
        } else {
            auto [nl,nr] = keypad[n];
            int left_dist = abs(nl-left.first) + abs(nr-left.second);
            int right_dist = abs(nl-right.first) + abs(nr-right.second);
            if (left_dist > right_dist) {
                right = keypad[n];
                answer += "R";
            } else if (left_dist < right_dist) {
                left = keypad[n];
                answer += "L";
            } else {
                if (hand == "left") {
                    left = keypad[n];
                    answer += "L";
                } else {
                    right = keypad[n];
                    answer += "R";
                }
            }
        }
    }
    
    return answer;
}