import java.util.*;

class Solution {
    public String solution(String new_id) {
        StringBuilder sb = new StringBuilder();
        
        // 1
        new_id = new_id.toLowerCase();
        
        // 2
        Set<Character> s = new HashSet<>(Arrays.asList('-','_','.'));
        for(char x: new_id.toCharArray()) {
            if (Character.isLowerCase(x) || Character.isDigit(x) || s.contains(x)) sb.append(x);
        }
        new_id = sb.toString();
        
        // 3
        sb.setLength(0);
        for(char x: new_id.toCharArray()) {
            if(x == '.' && sb.length() > 0 && sb.charAt(sb.length() - 1) == '.') {
                continue;
            }
            sb.append(x);
        }
        new_id = sb.toString();
        
        //4
        if (new_id.length() > 0 && new_id.charAt(0) == '.') {
            new_id = new_id.substring(1);
        }

        if (new_id.length() > 0 && new_id.charAt(new_id.length()-1) == '.') {
            new_id = new_id.substring(0,new_id.length()-1);
        }
        
        //5
        if (new_id.length() == 0) new_id = "a";
        
        //6
        if (new_id.length() >= 16) new_id = new_id.substring(0,15);
        if (new_id.charAt(new_id.length()-1) == '.') new_id = new_id.substring(0,new_id.length()-1);
        
        //7
        if (new_id.length() <= 2) {
            char last = new_id.charAt(new_id.length()-1);
            while (new_id.length() < 3) new_id += last;
        }
        
        return new_id;
    }
}