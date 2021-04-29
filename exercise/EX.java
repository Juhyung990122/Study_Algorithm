
import java.math.BigInteger;

public class EX{
    public static void main(String [] args ){
        String s = Solution("1234","5678");
        System.out.print(s);
    }

    private static String Solution(String a, String b) {
        String answer = "6912";
        BigInteger aINT = new BigInteger(a);
        BigInteger bINT = new BigInteger(b);
        BigInteger sum = aINT.add(bINT);
        answer = (String)sum.toString();
        return answer;

    }
}