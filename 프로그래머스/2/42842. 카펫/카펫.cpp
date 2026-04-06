#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    vector<pair<int,int>> candidate;
    for(int i=1;i<=int(sqrt(double(yellow)));i++) {
        if (yellow % i == 0) {
            candidate.push_back({i, yellow / i});
        }
    }
    for (auto [c1,c2]: candidate) {
        int need = 2 * c1 + 2 * c2 + 4;
        if (need == brown) {
            answer = {c1+2,c2+2};
        }
    }
    sort(answer.begin(), answer.end(), greater<>());
    return answer;
}