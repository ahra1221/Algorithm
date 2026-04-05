#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> array, int n) {
    int answer = 0;
    vector<pair<int,int>> v;
    for(auto a: array){
        v.push_back({a, abs(n-a)});
    }
    sort(v.begin(), v.end(), [](auto a, auto b){
        if (a.second == b.second) {
            return a.first < b.first;
        }
        return a.second < b.second;
    });
    return v[0].first;
}