#include <string>
#include <vector>
#include <deque>
#include <iostream>
#include <utility>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> rc, vector<string> operations) {
    int r = rc.size();
    int c = rc[0].size();
    
    vector<vector<int>> answer(r, vector<int>(c,0));
    deque<int> left, right;
    deque<deque<int>> mid;
    
    for(int i=0;i<r;i++) {
        left.push_back(rc[i][0]);
        right.push_back(rc[i][c-1]);
        
        deque<int> tmp;
        for(int j=1;j<c-1;j++) {
            tmp.push_back(rc[i][j]);
        }
        mid.push_back(tmp);
    }
    
    for(auto op: operations) {
        if (op == "ShiftRow") {
            left.push_front(left.back());
            left.pop_back();
            mid.push_front(std::move(mid.back()));
            mid.pop_back();
            right.push_front(right.back());
            right.pop_back();
        } else { // Rotate
            if(c > 2) {
                mid.front().push_front(left.front());
                left.pop_front();

                right.push_front(mid.front().back());
                mid.front().pop_back();

                mid.back().push_back(right.back());
                right.pop_back();

                left.push_back(mid.back().front());
                mid.back().pop_front();                
            } else {
                right.push_front(left.front());
                left.pop_front();
                
                left.push_back(right.back());
                right.pop_back();
            }
        }
    }
    
    for(int i=0;i<r;i++) {
        answer[i][0] = left[i];
        answer[i][c-1] = right[i];
        
        for(int j=1;j<c-1;j++) {
            answer[i][j] = mid[i][j-1];
        }
    }
    return answer;
}