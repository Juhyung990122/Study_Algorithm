import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Java_12789_Yeoleum {

    private static final BufferedReader r = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(r.readLine());
        Queue<Integer> waiting = new LinkedList<>();
        for (int i = 1; i < n + 1; i++) {
            waiting.offer(i);
        }
        Stack<Integer> newWaitingLine = new Stack<>();

        int out = 0;
        while (true) {
            Integer now;
            if (newWaitingLine.isEmpty() || waiting.peek() > newWaitingLine.peek()) {
                now = waiting.poll();
            } else {
                now = newWaitingLine.pop();
            }

            if (out + 1 == now) {
                out += 1;
                if (waiting.isEmpty() && newWaitingLine.isEmpty()) {
                    System.out.println("Nice");
                    break;
                }
                continue;
            }

            if (newWaitingLine.isEmpty() || newWaitingLine.peek() > now) {
                newWaitingLine.push(now);
            } else {
                System.out.println("Sad");
                return;
            }

        }

    }
}

//    int out = 0;
//    while (true) {
//            Integer now;
//            if (newWaitingLine.isEmpty() && !waiting.isEmpty()) {
//                now = waiting.poll();
//            } else {
//                now = Math.min(waiting.poll(), newWaitingLine.peek());
//            }
//
//            if (out + 1 == now) {
//                if (!newWaitingLine.isEmpty() && newWaitingLine.peek() == now) {
//                    newWaitingLine.pop();
//                }
//
//                if (!waiting.isEmpty() && waiting.get(0) == now) {
//                    waiting.remove(0);
//                }
//
//                out += 1;
//                System.out.println(now);
//
//                if (waiting.isEmpty() && newWaitingLine.isEmpty()) {
//                    System.out.println("Nice");
//                    return;
//                }
//                continue;
//            }
//            if (newWaitingLine.isEmpty() || newWaitingLine.peek() > now) {
//                newWaitingLine.push(now);
//            } else {
//                System.out.println("Sad");
//                return;
//            }
//        }
//    }
