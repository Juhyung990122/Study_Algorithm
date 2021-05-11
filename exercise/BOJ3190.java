
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;



public class BOJ3190 {
    private static int[] dx = {0,1,0,-1};
    private static int[] dy = {1,0,-1,0};
    private static int n,k,l;
    private static int[][] graph;
    private static List<int[]> snake;

    public static void main(String[] args) {
        snake = new LinkedList<>();
        snake.add(new int[]{0,0});

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        graph = new int[n][n];
        graph[0][0] = -1;
        
        k = sc.nextInt();
        for(int i = 0; i < k; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            graph[x-1][y-1] = 1;
        }

        l = sc.nextInt();
        int[][] dir = new int[l][2];
        for(int i = 0; i < l; i++){
            dir[i][0] = sc.nextInt();
            char temp = sc.next().charAt(0);
            dir[i][1] = (temp == 'L') ? -1 : 1;
        }
        
        int time = solution(0,0,0,dir);
        System.out.println(time);
        sc.close();
    }

    private static int solution(int curX, int curY, int currentDir, int[][] dir){
        int time = 0;
        int turn = 0;

        while(true){
            time++ ;
            int nextX = curX + dx[currentDir];
            int nextY = curY + dy[currentDir];

            if (isFinish(nextX, nextY)) break;

            //사과가 있으면
            if (graph[nextX][nextY] == 2){
                System.out.println("Apple O");
                snake.add(new int[]{nextX,nextY});
                //printArray(snake);
            } 
            else{
                System.out.println("Apple X");
                snake.add(new int[]{nextX,nextY});
                snake.remove(0);
                //printArray(snake);
            }

            curX = nextX;
            curY = nextY;
            
            if (turn < l){
                if (time == dir[turn][0]){
                    currentDir = nextDir(currentDir,dir[turn][1]);
                    turn++;
                }
            }
        }
        return time;
    }

    private static int nextDir(int current, int dir){
        int next = (current + dir) % 4;
        if(next == -1) next = 3;
        return next;
    }

    private static boolean isFinish(int x, int y){
        if (x == -1 || x == n || y == -1 || y == n){
            return true;
        }
        for (int i = 0; i < snake.size(); i++){
            int[] s = snake.get(i);
            if(s[0] == x && s[1] == y){
                return true;
            }
        }
        return false;
    }


}
