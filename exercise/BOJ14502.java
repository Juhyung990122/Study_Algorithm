import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.LinkedList;
import java.util.Queue;




public class BOJ14502 {
    private static int x,y,answer;
    private static int[][] graph;
    private static int[] dx = {-1,1,0,0};
    private static int[] dy = {0,0,-1,1};
    public static void main(String[] args) throws IOException {
        //// 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        x = Integer.parseInt(input[0]);
        y = Integer.parseInt(input[1]);
        graph = new int[y][x];
        
        for (int i = 0; i < y; i++){
            input = br.readLine().split(" ");
            for(int j = 0; j < x; j++){
                graph[i][j] = Integer.parseInt(input[j]);  
            }
        }
       //// 
        bfs(x,y,graph);

        ///답출력
        answer = 0;
        for (int i = 0; i < y; i++){
            for(int j = 0; j < x; j++){
                if(graph[i][j] == 0){
                    System.out.println(-1);
                    return;
                }
                answer = Math.max(answer, graph[i][j]);
            }
        }
        System.out.println(answer-1);
    }

    public static void bfs(int x, int y, int[][] graph) {
        Queue<Node> queue = new LinkedList<Node>();

        for(int i = 0; i < y; i++){
            for(int j = 0; j < x; j++){
                if(graph[i][j] == 1){
                    queue.add(new Node(j,i));
                }
            }
        }

        while(!queue.isEmpty()){
            Node now = queue.poll();
            for(int i = 0; i < 4; i++){
                int moveX = now.x + dx[i];
                int moveY = now.y + dy[i];

                if(0 <= moveX && moveX < x && 0 <= moveY && moveY < y ){
                    if(graph[moveY][moveX] == 0){
                        graph[moveY][moveX] = graph[now.y][now.x] + 1;
                        queue.add(new Node(moveX,moveY));
                    }
                }
            }
        }
    }
}

class Node{
    int x;
    int y;

    Node(int x, int y){
        this.x = x;
        this.y = y;
    }
}