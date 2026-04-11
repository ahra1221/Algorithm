#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool check_dist(vector<vector<char>> g, int x, int y) {
    // right, down
    vector<pair<int,int>> one_dist = {{0,1},{1,0}};
    for(int i=0;i<2;i++) {
        int dx = x+one_dist[i].first;
        int dy = y+one_dist[i].second;
        if(0<=dx && dx<5 && 0<=dy && dy<5) {
            if(g[dx][dy] == 'P') return false;
        }
    }
    
    // two
    vector<pair<int,int>> two_dist = {{0,2},{2,0}};
    for(int i=0;i<2;i++) {
        int dx = x+two_dist[i].first;
        int dy = y+two_dist[i].second;
        if(0<=dx && dx<5 && 0<=dy && dy<5) {
            int prevx = x+one_dist[i].first;
            int prevy = y+one_dist[i].second;
            if(g[dx][dy] == 'P' && g[prevx][prevy] != 'X') return false;
        }
    }
    
    // cross
    vector<pair<int,int>> cross_dist = {{1,1},{1,-1}};
    for(int i=0;i<2;i++) {
        int dx = x+cross_dist[i].first;
        int dy = y+cross_dist[i].second;
        if(0<=dx && dx<5 && 0<=dy && dy<5) {
            if (g[dx][dy] == 'P') {
                if(g[x][dy] == 'X' && g[dx][y] == 'X') continue;
                else return false;
            }
        }
    }
    return true;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    int dirx[6] = {0, 1, 0, 2, 1, 1};
    int diry[6] = {1, 0, 2, 0, 1, -1};
    
    for(int i=0;i<5;i++) {
        vector<vector<char>> v;
        for(int j=0;j<5;j++) {
            string p = places[i][j];
            vector<char> tmp(p.begin(), p.end());
            v.push_back(tmp);
        }
        bool flag = true;
        for(int x=0;x<5;x++) {
            for(int y=0;y<5;y++) {
                if (v[x][y] == 'P') {
                    if (!check_dist(v, x, y)) {
                        flag = false;
                        break;
                    }
                }
            }
            if (!flag) break;
        }
        answer.push_back(flag);
    }
    
    return answer;
}