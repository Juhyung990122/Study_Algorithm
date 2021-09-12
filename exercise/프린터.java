import javax.print.Doc;
import java.io.*;
import java.util.*;

public class 프린터 {
    public static void main(String[] args) throws IOException {
        System.out.println(solution(new int[]{2, 1, 3, 2},2));
    }

    public static int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Document> queue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++){
            queue.add(new Document(i,priorities[i]));
        }

        while(!queue.isEmpty()){
            boolean check = false;
            int first = queue.peek().priority;
            for(Document document : queue){
                if(document.priority > first){
                    check = true;
                }
            }

            if(check){
                queue.offer(queue.poll());
            }
            else{
                if(queue.poll().location == location){
                    answer = priorities.length - queue.size();
                }
            }
        }

        return answer;
    }

    static class Document{
        int location;
        int priority;
        Document(int location, int priority){
            this.location = location;
            this.priority = priority;
        }
    }
}