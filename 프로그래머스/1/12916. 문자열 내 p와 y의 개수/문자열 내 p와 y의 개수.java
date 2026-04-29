class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        
        int pCount = 0, yCount = 0;
        for(int i=0;i<s.length();i++) {
            char c = s.charAt(i);
            if (c=='p') pCount++;
            else if (c=='y') yCount++;
        }
        
        return (pCount == yCount);
    }
}