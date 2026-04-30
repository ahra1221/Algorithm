import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        int total = 0;
        int time = 0;
        int idx = 0;
        Queue<Integer> bridge = new LinkedList<>();
        while (idx < truck_weights.length || total > 0) {
            time++;
            
            if(bridge.size() == bridge_length) {
                total -= bridge.poll();
            }
            
            if (idx<truck_weights.length && total + truck_weights[idx] <= weight) {
                bridge.add(truck_weights[idx]);
                total += truck_weights[idx];
                idx++;
            } else {
                bridge.add(0);
            }
        }
        
        return time;
    }
}