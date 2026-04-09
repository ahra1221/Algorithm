#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cctype>

using namespace std;

struct FileInfo {
    string original;
    string head;
    int number;
    int index;
};

vector<string> solution(vector<string> files) {
    vector<string> answer;
    vector<FileInfo> parsed;
    
    for(int i=0;i<files.size();i++) {
        string f = files[i];
        string head = "";
        string number = "";
        
        int j = 0;
        
        while (j <= f.length() && !isdigit(f[j])) {
            head += f[j];
            j++;
        }
        
        while (j <= f.length() && isdigit(f[j])) {
            number += f[j];
            j++;
        }
        
        parsed.push_back({f, head, stoi(number), i});
    }
    
    sort(parsed.begin(), parsed.end(), [](FileInfo& a, FileInfo&b) {
        string headA = a.head;
        string headB = b.head;
        
        for(char& c: headA) c = tolower(c);
        for(char& c: headB) c = tolower(c);
        
        if (headA != headB) return headA < headB;
        if (a.number != b.number) return a.number < b.number;
        return a.index < b.index;
    });
    
    for(const auto& p: parsed) {
        answer.push_back(p.original);
    } 
    
    return answer;
}