import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        String prev = phone_book[0];
        Integer len = prev.length();
        for(int i=1;i<phone_book.length;i++) {
            String cur = phone_book[i];
            if (cur.length() >= len && cur.substring(0,len).equals(prev)) return false;
            else {
                prev = phone_book[i];
                len = prev.length();
            }
        }
        return true;
    }
}