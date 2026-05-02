class Solution {
    public long solution(int n, int[] times) {
        long max = 0;
        for(int t: times) max = Math.max(max,t);
        long left = 1, right = max * n;
        long answer = right;
        
        while (left <= right) {
            long mid = (left+right) / 2;
            
            long count = 0;
            for(int time: times) {
                count += mid / time;
            }
            
            if(count >= n) {
                answer = mid;
                right = mid-1;
            } else {
                left = mid+1;
            }
        }
        return answer;
    }
}