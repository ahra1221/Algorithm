import java.util.*;

class Node {
    String s;
    int count;
    
    Node(String s, int count) {
        this.s = s;
        this.count = count;
    }
}

class Solution {
    public boolean checkOneDiff(String word1, String word2) {
        int len = word1.length();
        char[] w1 = word1.toCharArray();
        char[] w2 = word2.toCharArray();
        
        int diff = 0;
        for(int i=0;i<len;i++) {
            if (w1[i] != w2[i]) diff++;
        }
        return diff == 1 ? true : false;
    }
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        boolean[] visited = new boolean[words.length];
        Queue<Node> q = new ArrayDeque<>();
        q.add(new Node(begin, 0)); // word,count
        
        while(!q.isEmpty()) {
            Node cur = q.poll();
            if (cur.s.equals(target)) {
                answer = cur.count;
                break;
            }
            
            for(int i=0;i<words.length;i++) {
                String word = words[i];
                if(checkOneDiff(cur.s, word) && !visited[i]) {
                    q.add(new Node(word,cur.count+1));
                    visited[i] = true;
                }
            }
        }
        
        return answer;
    }
}