class Solution {
    public String solution(String phone_number) {
        StringBuilder sb = new StringBuilder();
        int hide = phone_number.length() - 4;
        for(int i=0;i<hide;i++) {
            sb.append('*');
        }
        sb.append(phone_number.substring(phone_number.length() - 4));
        return sb.toString();
    }
}