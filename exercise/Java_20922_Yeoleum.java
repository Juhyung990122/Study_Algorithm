

import static java.lang.Math.max;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Java_20922_Yeoleum {
    private static BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int answer = 0;
        st = new StringTokenizer(r.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] nums = new int[n];
        st = new StringTokenizer(r.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for (int start = 0; start < n; start++) {
            int[] count = new int[100001];
            int end = start;
            while (end + 1 <= n && count[nums[end]] < k) {
                count[nums[end]]++;
                end++;
            }
            answer = max(answer, end - start);
        }
        System.out.println(answer);
    }
}
