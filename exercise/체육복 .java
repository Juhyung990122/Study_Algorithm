import java.util.Arrays;  

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);
        int answer = n;
        for (int i = 0; i < lost.length; i++){  
            boolean rent = false;
            int j = 0;
            while(rent == false){
                if(j == reserve.length){
                    break;
                }
                else if(lost[i] == reserve[j]){
                    reserve[j] = -1;
                    rent = true;
                }
                else if(lost[i] == reserve[j]+1){
                    reserve[j] = -1;
                    rent = true;
                } 
                else if(lost[i] == reserve[j]-1){
                    reserve[j] = -1;
                    rent = true;
                }
                else{
                    j++;
                }
            }
            if(rent == false){
                    answer--;
                }
        }
        return answer;
    }
}