import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int count = 0;
        int time = 0;
        int idx = 0;
        int total = 0;
        
        Arrays.sort(jobs, (a,b) -> a[0]-b[0]);
        while(count < jobs.length) {
            while (idx < jobs.length && jobs[idx][0] <= time) {
                int request = jobs[idx][0], duration = jobs[idx][1];
                pq.offer(new int[]{duration,request});
                idx++;
            }
            if (!pq.isEmpty()) {
                int[] cur = pq.poll();
                int duration = cur[0], request = cur[1];
                time += duration;
                total += time - request;
                count++;
            } else {
                time = jobs[idx][0];
            }
        }
        int answer = total / jobs.length;
        return answer;
    }
}