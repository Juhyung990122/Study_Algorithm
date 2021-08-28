import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class K번째수{

    public static void main(String[] args) throws IOException {
        System.out.println(Arrays.toString(solution(new int[]{1, 5, 2, 6, 3, 7, 4},new int[][]{{2, 5, 3}, {4, 4, 1},{1, 7, 3}})));
    }

    public static int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        List<int[]> commandsToList = Arrays.stream(commands).collect(Collectors.toList());
        List<Integer> arrayToList = Arrays.stream(array).boxed().collect(Collectors.toList());
//        System.out.println(arrayToList);
//        System.out.println(Arrays.deepToString(commandsToList.toArray()));
        for(int[] i : commandsToList){
                List<Integer> sliceList = arrayToList.subList(i[0]-1, i[1]);
                List<Integer> sortedList   = sliceList.stream().sorted().collect(Collectors.toList());
                answer.add(sortedList.get(i[2]-1));
        }

        int[] returnAnswer = new int[answer.size()];
        for(int i = 0; i <  answer.size(); i++){
            returnAnswer[i] = answer.get(i);
        }
        return returnAnswer;
    }

}
