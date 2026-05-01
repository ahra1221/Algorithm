import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        
        int total = stages.length;
        Map<Integer,Integer> map = new HashMap<>(); 
        for(int s: stages) {
            map.put(s, map.getOrDefault(s,0)+1);
        }
        
        Map<Integer,Double> failure = new HashMap<>(); // index,failure
        for(int i=1;i<N+1;i++) {
            if(map.containsKey(i)) {
                failure.put(i, (double)map.get(i)/total);
                total -= map.get(i);
            } else {
                failure.put(i, 0.0);
            }
        }
        
        List<Map.Entry<Integer,Double>> entry = new ArrayList<>(failure.entrySet());
        entry.sort((a,b) -> {
            if(a.getValue()!=b.getValue()) {
                return Double.compare(b.getValue(),a.getValue());
            }
            return a.getKey() - b.getKey();
        });
        
        int idx = 0;
        for(Map.Entry<Integer,Double> en: entry) {
            answer[idx++] = en.getKey();
        }
        
        return answer;
    }
}