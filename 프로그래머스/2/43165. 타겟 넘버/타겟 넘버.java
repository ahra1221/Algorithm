class Solution {
    
    public int backtracking(int[] numbers, int target, int i, int cur) {
        if (i == numbers.length) {
            if (cur == target) return 1;
            return 0;
        }
        
        int plus = backtracking(numbers, target, i+1, cur+numbers[i]);
        int minus = backtracking(numbers, target, i+1, cur-numbers[i]);
        return plus+minus;
    }
    
    public int solution(int[] numbers, int target) {
        return backtracking(numbers,target,0,0);
    }
}