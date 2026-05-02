import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int s :scoville) pq.offer(s);
        
        while(pq.peek() < K && pq.size() >= 2) {
            int a = pq.poll();
            int b = pq.poll();
            int mix = a + 2*b;
            pq.offer(mix);
            answer++;
        }
        return pq.peek() >= K ? answer : -1;
    }
}