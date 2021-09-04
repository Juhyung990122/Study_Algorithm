import java.io.*;

public class 셀프넘버 {
    public static void main(String[] args) throws IOException {
        solution();
    }

    public static void solution(){
        boolean[] check = new boolean[10001];
        for(int i = 1; i < 10001; ++i){
            int checkNum = getDn(i);
            //false가 기본값이므로 셀프넘버 아닌걸 true로 체크
            if(checkNum <= 10000){
                check[checkNum] = true;
            }
        }
        for(int i = 1; i < check.length; ++i){
            if(!check[i]){
                System.out.println(i);
            }
        }
    }

    public static int getDn(int n){
        int dn = n;
        while(n > 0){
            dn += n % 10;
            n /= 10;
        }
        return dn;
    }
}
