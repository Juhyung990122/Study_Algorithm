import java.util.Scanner;


public class BOJ9095 {

    static int dp[] = new int[11];
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for(int i = 0; i < t; i++){
            int n = sc.nextInt();
            dp[0] = 1;
            dp[1] = 2;
            dp[2] = 4;

            for(int j = 3; j < n; j++){
                dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
            }
            System.out.println(dp[n-1]);
        }
        sc.close();
       
    }
}

