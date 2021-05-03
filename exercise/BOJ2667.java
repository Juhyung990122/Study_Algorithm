import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
/**
 * BOJ2667
 */
public class BOJ2667 {
    private static int[] dx = {-1,1,0,0};
    private static int[] dy = {0,0,-1,1};
    private static int[][] graph;
    private static int[][] visited;
    private static int n;
    static int cnt = 0;
    static ArrayList<Integer> a = new ArrayList<Integer>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        graph = new int[n][n];
        visited = new int[n][n];

        for (int i = 0; i < n; i++){
            String input = sc.next();
            for(int j = 0; j < n; j++){
                graph[i][j] = input.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if(graph[i][j] == 1 && visited[i][j] == 0){
                    cnt = 1;
                    visited[i][j] = 1;
                    solution(i,j);
                    a.add(cnt);
                }
            }
        }

        Collections.sort(a);
        System.out.println(a.size());
        for(int i : a){
            System.out.println(i);
        }
       
    }

    public static void solution(int col,int row){

        for (int i = 0; i < 4; i++){
            int moveY = col + dy[i];
            int moveX = row + dx[i];

            if(0 <= moveX && moveX < n && moveY < n && 0 <= moveY){
                if(graph[moveY][moveX] == 1 && visited[moveY][moveX] != 1 ){
                    cnt++;
                    visited[moveY][moveX] = 1;
                    solution(moveY,moveX);
                }
            }

        }
    }
}