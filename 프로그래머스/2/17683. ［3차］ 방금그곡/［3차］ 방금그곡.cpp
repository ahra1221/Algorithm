#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

int cal_time(string time1, string time2) {
    stringstream ss1(time1), ss2(time2);
    string tmp;
    vector<int> v1, v2;
    while(getline(ss1,tmp,':')) v1.push_back(stoi(tmp));
    while(getline(ss2,tmp,':')) v2.push_back(stoi(tmp));
    
    return (v2[0] - v1[0]) * 60 + (v2[1] - v1[1]);
}

string convert(string s) {
    string res = "";
    for(int i=0;i<s.length();i++) {
        if (i < s.length()-1 && s[i+1] == '#') {
            if (s[i] == 'C') res += 'c';
            else if (s[i] == 'D') res += 'd';
            else if (s[i] == 'F') res += 'f';
            else if (s[i] == 'G') res += 'g';
            else if (s[i] == 'A') res += 'a';
            i++;
        } else {
            res += s[i];
        }
    }
    return res;
}
 
string solution(string m, vector<string> musicinfos) {
    string answer = "(None)";
    m = convert(m);
    
    vector<pair<string,int>> candidate;
    
    for(string music: musicinfos) {
        stringstream ss(music);
        string word;
        vector<string> v;
        while(getline(ss, word,',')) v.push_back(word);
        
        int time = cal_time(v[0], v[1]);
        string title = v[2];
        string melody = convert(v[3]);
        
        string play = "";
        for(int i=0;i<time;i++) {
            play += melody[i % melody.size()];
        }
        
        if(play.find(m) != string::npos) {
            candidate.push_back({title,time});
        }
    }
    
    if (!candidate.empty()) {
        stable_sort(candidate.begin(), candidate.end(), [](pair<string,int> a, pair<string,int> b) {
            return a.second > b.second;
        });   
        answer = candidate[0].first;
    }
    
    return answer;
}