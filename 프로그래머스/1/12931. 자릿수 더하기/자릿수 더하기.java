import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        char[] arr = String.valueOf(n).toCharArray();
        for (int i=0;i<arr.length;i++) {
            answer += arr[i] - '0';
        }
        return answer;
    }
}