import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class 사탕게임 {
    public static void main(String[] args) throws IOException {
        int[] sc = {1,2,3,9,10,12};
        System.out.println(solution(sc,7));
    }

    public static int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 0; i<scoville.length; i++){
            heap.add(scoville[i]);
        }

        while(heap.peek() < K){
            if(heap.size() < 2){
                return -1;
            }

            int first = heap.poll();
            int second = heap.poll();

            int sumScoville = first + (second * 2);
            heap.add(sumScoville);
            answer += 1;

        }

        return answer;
    }
}
