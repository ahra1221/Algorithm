import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> closet = new HashMap<>();
        for(String[] info: clothes) {
            String type = info[1];
            closet.put(type, closet.getOrDefault(type,0)+1);
        }
        
        for(int count: closet.values()) {
            answer *= (count + 1);
        }
        return answer-1;
    }
}