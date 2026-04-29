class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(char c: s.toCharArray()) {
            int code = (int)c;
            if (c==' ') answer += c;
            else if (Character.isUpperCase(c)) {
                answer += (char)((c - 'A' + n) % 26 + 'A');
            }
            else {
                answer += (char)((c - 'a' + n) % 26 + 'a');
            }
        }
        return answer;
    }
}