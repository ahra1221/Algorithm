import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        char[] c = s.toCharArray();
        Arrays.sort(c);
        return new StringBuilder().append(c).reverse().toString();
    }
}