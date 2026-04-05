#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> score(3,0);
    vector<vector<int>> choice {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };
    for(int i=0;i<answers.size(); i++) {
        int ans = answers[i];
        for(int j=0;j<choice.size();j++) {
            int idx = i % choice[j].size();
            if (ans == choice[j][idx]) {
                score[j]++;
            }
        }
    }
    int max_score = *max_element(score.begin(), score.end());
    for(int i=0;i<3;i++) {
        if (score[i] == max_score) {
            answer.push_back(i+1);
        }
    }
    return answer;
}