import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;



public class BOJ1463 {
    private static int n;
    private static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        n = Integer.parseInt(br.readLine());
        dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 1;

        for(int i = 4; i <= n; i++){
            dp[i] = dp[i-1] + 1;
            if(i % 3 == 0){
                dp[i] = Math.min(dp[i], dp[i/3]+1);
            }
            if( i % 2 == 0){
                dp[i] = Math.min(dp[i],dp[i/2]+1);
            }
            
        }
        
        bw.write(dp[n] + "\n");

        br.close();
        bw.flush();
        bw.close();

    }
}
