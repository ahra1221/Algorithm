import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int n = nums.length;
        Set<Integer> s = new HashSet<>();
        for(int num: nums) {
            s.add(num);
        }
        if (s.size() >= n / 2) return n / 2;
        else return s.size();
    }
}