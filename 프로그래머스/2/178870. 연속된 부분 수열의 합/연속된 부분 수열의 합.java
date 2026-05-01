class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        int minlen = Integer.MAX_VALUE;
        
        int left = 0, right = 0, sum = 0;
        while(right < sequence.length){
            sum += sequence[right];
            
            while (sum > k) {
                sum -= sequence[left++];
            }
            if(sum == k) {
                int len = right - left;
                if (minlen > len) {
                    minlen = len;
                    answer[0] = left;
                    answer[1] = right;
                }
            }
            right++;
        }
        return answer;
    }
}