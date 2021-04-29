public class interview1{
    public static void main(String [] args ){
        Integer s = Solution(50);
        System.out.print(s);
    }

    private static Integer Solution(int n) {
            int answer = 0;
            // 약수의 갯수가 홀수인 수들(제곱수)
            for(int i = 1; i <= n; i++){
                if(i * i <= n){
                    answer += 1;
                }
            }
            
            return answer;
    }

}