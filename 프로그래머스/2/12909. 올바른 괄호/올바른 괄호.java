import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> st = new Stack<>();
        for(char ss: s.toCharArray()) {
            if (ss == ')') {
                if (!st.isEmpty() && st.peek() == '(') st.pop();
                else st.push(ss);
            }
            else st.push(ss);
        }

        return st.isEmpty() ? true : false;
    }
}