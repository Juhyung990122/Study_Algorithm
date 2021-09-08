import java.io.*;
import java.util.*;

public class 프린터 {
    public static void main(String[] args) throws IOException {
        System.out.println(solution(new int[]{2, 1, 3, 2},2));
    }

    public static int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Document> queue = new LinkedList<>();

        for( int i = 0; i < priorities.length; i++) {
            queue.offer(new Document(i,priorities[i]));
        }

        while(!queue.isEmpty()){
            boolean flag = false;
            int peek = queue.peek().priority;
            for(Document document : queue){
                //뺀거보다 더 높은게 있는지 검색한 뒤
                if(peek < document.priority){
                    //있으면 뺸건 뒤로 보낸다
                   flag = true;
                }
            }

                if(flag){
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