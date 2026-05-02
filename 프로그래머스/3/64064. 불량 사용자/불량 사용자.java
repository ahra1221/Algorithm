import java.util.*;

class Solution {
    List<List<String>> list = new ArrayList<>();
    Set<String> set = new HashSet<>();
    
    public boolean checkEqual(String u, String b) {
        if (u.length() != b.length()) return false;
        int len = u.length();
        for(int i=0;i<len;i++) {
            if(b.charAt(i) == '*') continue;
            else if(u.charAt(i) != b.charAt(i)) return false;
        }
        return true;
    }
    
    public void dfs(int st, Set<String> s) {
        if(st == list.size()) {
            List<String> tmp = new ArrayList<>(s);
            Collections.sort(tmp);
            String result = String.join(",", tmp);
            set.add(result);
            return;
        }
        
        for(String can: list.get(st)) {
            if(!s.contains(can)) {
                s.add(can);
                dfs(st+1,s);
                s.remove(can);
            }
        }
    }
    
    public int solution(String[] user_id, String[] banned_id) {
        
        for(String ban: banned_id) {
            List<String> candidate = new ArrayList<>();
            for(String user: user_id) {
                if (checkEqual(user,ban)) candidate.add(user);
            }
            list.add(candidate);
        }
        dfs(0,new HashSet<>());
        int answer = set.size();
        return answer;
    }
}