import java.util.*;

class Solution {
    Set<Integer> set = new HashSet<>();
    boolean[] visited;
    
    public boolean isPrime(int n) {
        if(n<2) return false;
        for(int i=2;i*i<=n;i++) {
            if(n%i == 0) return false;
        }
        return true;
    }
    
    public void dfs(String numbers, String cur) {
        if(!cur.equals("") && isPrime(Integer.parseInt(cur))) {
            set.add(Integer.parseInt(cur));
        }
        
        for(int i=0;i<numbers.length();i++) {
            if (!visited[i]) {
                visited[i] = true;
                cur += numbers.charAt(i);
                dfs(numbers,cur);
                cur = cur.substring(0,cur.length()-1);
                visited[i] = false;
            }
        }
    }
    
    public int solution(String numbers) {
        visited = new boolean[numbers.length()];
        dfs(numbers,"");
        return set.size();
    }
}