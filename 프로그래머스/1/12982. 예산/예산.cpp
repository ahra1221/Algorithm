#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    sort(d.begin(), d.end());
    int total = 0;
    for (auto x: d) {
        total += x;
        if (total <= budget) {
            answer ++;
            continue;
        } else {
            return answer;
        }
    }
    return answer;
}