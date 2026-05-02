import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        int left = 0, right = distance;
        Arrays.sort(rocks);
        while (left <= right) {
            int mid = (left+right) / 2;
            
            int remove = 0;
            int prev = 0;
            for(int rock: rocks) {
                int dist = rock - prev;
                if (dist < mid) {
                    remove++;
                } else {
                    prev = rock;
                }
            }
            if (distance - prev < mid) remove++;
            if(remove > n) {
                right = mid-1;
            } else {
                answer = mid;
                left = mid +1;
            }
        }
        return answer;
    }
}