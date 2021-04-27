package algorithm.exercise;

public class interview2 {
    public static void main(String [] args ){
        int[][] m ={{5, -1, 4}, {6, 3, -1}, {2, -1, 1}};
        String[] st = {"go", "go", "right", "go", "right", "go", "left", "go"};
        Integer s = Solution(m, 1, 0, st);
        System.out.print(s);
    }

    private static Integer Solution(int[][] office, int r, int c, String[] move) {
        {
            int answer = 0;
            int see = 1;
            int[] now = {r,c};
            for(int i = 0; i < move.length; i++){
                int move_x = 0;
                int move_y = 0;
                switch(move[i]){
                    case "go" :
                    //북
                        if(see == 1){
                            move_y = now[0] - 1;
                            move_x = now[1];
                            break;
                        }
                        //서
                        else if(see ==2){
                            move_y = now[0];
                            move_x = now[1] -1;
                            break;
                        }
                        //남
                        else if(see == 3){
                            move_y = now[0] + 1;
                            move_x = now[1];
                            break;
                        }
                        //동
                        else{
                            move_y = now[0];
                            move_x = now[1] + 1;
                            break;
                        }
                    case "left":
                        if(see == 4){
                            see = 1;
                            break;
                        }
                        see += 1; 
                        break; 
                    case "right":
                        if(see == 1){
                            see = 4;
                            break;
                        }
                        see -= 1;
                        break;
                    
                }
                if(move[i] == "go"){
                    if((0 <= move_y && move_x < move.length) && (0 <= move_x && move_x < move.length)){
                        if(office[move_y][move_x] != -1){
                            answer += office[move_y][move_x];
                            office[move_y][move_x] = 0;
                            for(int idx = 0; idx < 2; idx++){
                                if(idx == 0){
                                    now[idx] = move_y;
                                    continue;
                                }
                                else{
                                    now[idx] = move_x;
                                }
                            }
                        }
                    }
                }
            }
            return answer;
        }
    }
}
