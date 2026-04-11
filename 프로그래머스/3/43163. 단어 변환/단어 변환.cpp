#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

bool is_one_diff(string a, string b) {
    int diff = 0;
    for(int i=0;i<a.length();i++) {
        if (a[i] != b[i]) {
            if(diff > 1) return false;
            else diff++;
        } 
    }
    if (diff == 1) return true;
    else return false;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    int l = words[0].length();
    set<string> s(words.begin(), words.end());
    if (!s.count(target)) return answer;

    vector<bool> visited(words.size(), false);
    queue<pair<string,int>> q;
    q.push({begin,0});
    while(!q.empty()) {
        auto [cur_str, cur_dist] = q.front();
        q.pop();
        if(cur_str == target) {
            answer = cur_dist;
            break;
        }
        
        for(int i=0;i<words.size();i++) {
            if (!visited[i] && is_one_diff(words[i], cur_str)) {
                q.push({words[i],cur_dist+1});
                visited[i] = true;
            }
        }
    }

    
    return answer;
}