class Solution {
    public String solution(int n) {
        String answer = "";
        int share = n;
        int remainder = 0;
        
        while(share > 0){
            remainder = share % 3;
            share = share / 3;
            
            if(remainder == 0){
                answer = "4" + answer;
                share = share - 1;
            }
            else if(remainder == 1){
                answer = "1" + answer;
            }
            else {
                answer = "2" + answer;
            }
        }
        return answer;
    }
}