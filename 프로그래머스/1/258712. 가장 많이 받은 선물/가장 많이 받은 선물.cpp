#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<string> friends, vector<string> gifts) {
    int answer = 0;
    unordered_map<string, int> total;
    
    unordered_map<string, unordered_map<string, int>> gift;
    unordered_map<string, int> giftnum;
    for(auto g: gifts) {
        stringstream ss(g);
        string a,b;
        ss >> a >> b;
        gift[a][b] += 1;
        giftnum[a] += 1;
        giftnum[b] -= 1;
    }
    
    for(int i=0;i<friends.size();i++) {
        for(int j=i+1;j<friends.size();j++) {
            string a = friends[i];
            string b = friends[j];
            int atob = gift[a][b];
            int btoa = gift[b][a];
            
            if (atob > btoa) total[a]++;
            else if (atob < btoa) total[b]++;
            else {
                int numa = giftnum[a];
                int numb = giftnum[b];
                if (numa > numb) total[a]++;
                else if (numa < numb) total[b]++;
            }
        }
    }
    
    for(auto [k,v]: total) {
        answer = max(answer,v);
    }
    
    return answer;
}