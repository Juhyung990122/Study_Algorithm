package algorithm.exercise;

public class interview3 {
    public static void main(String [] args ){
        Integer s = solution(10);
        System.out.print(s);
    }

    private static Integer solution(int n){{
        int answer = 0;
        int[] dp = new int[n+1];
        for (int i = 1; i <= n; i++){
            dp[i] = i;
            for(int j = 1; j*j <= i; j++){
                dp[i] = Math.min(dp[i], dp[i-j*j] + 1);
            }
        }
        answer = dp[n];
        return answer;
    }}
}