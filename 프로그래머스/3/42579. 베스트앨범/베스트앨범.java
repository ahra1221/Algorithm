import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> arr = new ArrayList<>();
        int n = genres.length;
        
        Map<String, Integer> total = new HashMap<>();
        Map<String, Map<Integer, Integer>> detail = new HashMap<>();
        
        for(int i=0;i<n;i++) {
            String genre = genres[i];
            total.put(genre, total.getOrDefault(genre, 0) + plays[i]);
            detail.computeIfAbsent(genre, k -> new HashMap()).put(i,plays[i]);
        }
        
        List<Map.Entry<String,Integer>> totalentry = new ArrayList<>(total.entrySet());
        totalentry.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));
        
        for(Map.Entry<String,Integer> t: totalentry) {
            String type = t.getKey();
            List<Map.Entry<Integer, Integer>> detailentry = new ArrayList<>(detail.get(type).entrySet());
            detailentry.sort((a,b) -> {
                if (!a.getValue().equals(b.getValue())) {
                    return b.getValue() - a.getValue();
                }
                return a.getKey() - b.getKey();
            });
            
            int cnt = 0;
            for(Map.Entry<Integer,Integer> d: detailentry) {
                arr.add(d.getKey());
                cnt ++;
                if (cnt == 2) break;
            }
        }
        
        int[] answer = new int[arr.size()];
        for(int i=0;i<arr.size();i++) {
            answer[i] = arr.get(i);
        }
        return answer;
    }
}