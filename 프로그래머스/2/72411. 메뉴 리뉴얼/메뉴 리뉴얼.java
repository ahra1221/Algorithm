import java.util.*;

class Solution {
    Map<String,Integer> m = new HashMap<>();
    
    public void dfs(String order, int course, int st, Set<Integer> s) {
        if(s.size() == course) {
            List<Integer> list = new ArrayList<>(s);
            Collections.sort(list);
            StringBuilder sb = new StringBuilder();
            for(int index: list) sb.append(order.charAt(index));
            String result = sb.toString();
            m.put(result, m.getOrDefault(result,0) + 1);
            return;
        }
        
        for(int i=st;i<order.length();i++) {
            if(!s.contains(i)) {
                s.add(i);
                dfs(order, course, i+1, s);
                s.remove(i);
            }
        }
        
    }
    public String[] solution(String[] orders, int[] course) {
        int idx = 0;
        for(String order: orders) {
            char[] arr = order.toCharArray();
            Arrays.sort(arr);
            String sortedOrder = new String(arr);
            for (int c : course) {
                dfs(sortedOrder, c, 0, new HashSet<>());
            }
        }
        
        List<String> answer = new ArrayList<>();
        for(int c: course) {
            int max = 0;
            for(Map.Entry<String,Integer> en: m.entrySet()) {
                if(en.getKey().length() == c && en.getValue() >= 2) {
                    max = Math.max(max, en.getValue());
                }
            }
            
            for(Map.Entry<String,Integer> en: m.entrySet()) {
                if(en.getKey().length() == c && en.getValue() == max) {
                    answer.add(en.getKey());
                }
            }
        }
        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }
}