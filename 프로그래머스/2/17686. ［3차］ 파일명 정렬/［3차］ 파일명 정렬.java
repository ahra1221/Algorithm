import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        String[] answer = new String[files.length];
        
        List<String[]> list = new ArrayList<>(); // name, head,number,index
        for(int i=0;i<files.length;i++) {
            String name = files[i];
            
            String head = "", number = "";
            boolean watch = false;
            for(char c: name.toCharArray()) {
                if (Character.isDigit(c)) {
                    if(number.equals("")) watch = true;
                    number += c;
                }
                else {
                    if (!watch) head += c;
                    else break;
                }
            }
            list.add(new String[]{name, head.toLowerCase(),number, String.valueOf(i)});
        }
        
        list.sort((a,b) -> {
            if (!a[1].equals(b[1])) { // head
                return a[1].compareTo(b[1]);
            }
            int na = Integer.parseInt(a[2]);
            int nb = Integer.parseInt(b[2]);
            if (na != nb) return na-nb;
            
            return Integer.parseInt(a[3]) - Integer.parseInt(b[3]);
         });
        
        
        int idx = 0;
        for(String[] l: list) {
            answer[idx++] = l[0];
        }
        
        return answer;
    }
}