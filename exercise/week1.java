class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long total = 0;
        
        for(int i = 1;i <= count;i++){
            total = total + (price * i);
        }
        
        answer = total - money;
        if(answer > 0){
            return answer;
        }
        else{
            return 0;
        }
        
    }
}