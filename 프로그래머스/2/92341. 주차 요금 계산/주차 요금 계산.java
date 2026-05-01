import java.util.*;

class Solution {
    public int calTime(String inTime, String outTime) {
        String[] in = inTime.split(":");
        String[] out = outTime.split(":");
        int inH = Integer.parseInt(in[0]), inM = Integer.parseInt(in[1]);
        int outH = Integer.parseInt(out[0]), outM = Integer.parseInt(out[1]);
        return (outH-inH) * 60 + (outM-inM);
    }
    
    public int calFee(int[] fees, int time) {
        int totalFee = fees[1];
        
        if (time > fees[0]) {
            int exceed = (time - fees[0] + fees[2] - 1) / fees[2];
            totalFee += exceed * fees[3];
        }
        return totalFee;
    }
    
    public int[] solution(int[] fees, String[] records) {
        List<int[]> fee = new ArrayList<>();
        Map<String, Integer> cumulative = new HashMap<>();
        Map<String,String> inTime = new HashMap<>();
        
        for(String record: records) {
            String[] r = record.split(" ");
            String carNumber = r[1];
            if (r[2].equals("IN")) {
                inTime.put(carNumber, r[0]);
            } else {
                int time = calTime(inTime.get(carNumber),r[0]);
                inTime.remove(carNumber);
                cumulative.put(carNumber, cumulative.getOrDefault(carNumber,0) + time);
            }
        }
        
        // 출차 없는 차량 처리
        if (inTime.size() > 0) {
            for(Map.Entry<String,String> in: inTime.entrySet()) {
                int t = calTime(in.getValue(), "23:59");
                String number = in.getKey();
                cumulative.put(number, cumulative.getOrDefault(number,0) + t);
            }
        }
        
        for(Map.Entry<String,Integer> c: cumulative.entrySet()) {
            fee.add(new int[]{Integer.parseInt(c.getKey()), calFee(fees, c.getValue())});
        }
        fee.sort((a,b) -> {
            return a[0] - b[0];
        });
        
        int[] answer = new int[fee.size()];
        int idx = 0;
        for(int[] x: fee) answer[idx++] = x[1];
        
        return answer;
    }
}