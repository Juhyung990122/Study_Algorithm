import java.io.*;
import java.util.Scanner;

public class template {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        int[] arr = { in.nextInt(), in.nextInt(), in.nextInt(),
                in.nextInt(), in.nextInt(), in.nextInt(),
                in.nextInt(), in.nextInt(), in.nextInt() };
        in.close();
        System.out.println(solution(arr));

    }

    public static int solution(int[] arr){
        int max = 0;
        for(int value : arr){
            if(value > max){
                max = value;
            }
        }
        return max;
    }
}