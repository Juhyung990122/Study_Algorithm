
import java.util.Arrays;
import java.util.Scanner;

public class BOJ3190 {
    private static int[] dx = {-1,1,0,0};
    private static int[] dy = {0,0,-1,1};
    private static int n,k,l;
    private static int[][] graph;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        graph = new int[n][n];
        graph[0][0] = -1;
        int[] now = {0,0};
        int snake = 1;

        k = sc.nextInt();
        for(int i = 0; i < k; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            graph[x][y] = 1;
        }

        l = sc.nextInt();
        int[][] move = new int[l][2];
        for(int i = 0; i < l; i++){
            move[i][0] = sc.nextInt();
            move[i][1] = sc.next().charAt(0);
        }
        
        //벽에 부딪힐떄 종료
        while(true){
            
        }

    }
}
