import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class 직업군추천하기 {
    public static void main(String[] args) throws IOException {
        System.out.println(solution(new String[]{"SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"},
                new String[]{"PYTHON", "C++", "SQL"},
        new int[]{7, 5, 5}));
    }
    public static String solution(String[] table, String[] languages, int[] preference) {
        HashMap<String,String[]> tableToMap = new HashMap<>();
        for(int i = 0; i < table.length; i++){
            StringTokenizer st = new StringTokenizer(table[i]);
            String job = st.nextToken();
            tableToMap.put(job,new String[5]);

            for(int j = 0; j<5; j++){
                tableToMap.get(job)[j] = st.nextToken();
            }
        }

        HashMap<String,Integer> preferList = new HashMap<>();
        for(int i = 0; i < languages.length; i++){
            preferList.put(languages[i],preference[i]);
        }

        String[] list = {"CONTENTS", "GAME", "HARDWARE", "PORTAL", "SI"};

        String answer = "";
        Integer pre_sum = -1;
        for(int i = 0; i < preferList.size();i++){
            Integer sum = 0;
            String[] jobs = tableToMap.get(list[i]);

            for(int j = 0; j < jobs.length ; j++){
                if(preferList.containsKey(jobs[j])){
                    sum += (5-j) * preferList.get(jobs[j]);
                }
            }
            if(sum > pre_sum){
                pre_sum = sum;
                answer = list[i];
            }

        }

        return answer;
    }

}
