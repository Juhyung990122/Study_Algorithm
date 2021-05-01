import java.util.Arrays;
import java.util.Scanner;

/**
 * BOJ2667
 */
public class BOJ2667 {

    private static int[][] graph;
    private static int n;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        graph = new int[n][n];
        for (int i = 0; i < n; i++){
            String input = sc.next();
            for(int j = 0; j < i; j++){
                graph[i][j] = input.charAt(j) - '0';
            }
        }

        System.out.println(Arrays.deepToString(graph));

    }
}