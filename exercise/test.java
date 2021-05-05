import java.io.*;

public class test {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        
        
        br.close();
        bw.flush();
        bw.close();
    }

    public static void solution(int col,int row){

    }
}
