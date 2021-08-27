package heap;

import java.util.*;

public class 더맵게 {

    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Arrays.stream(scoville).forEach(s -> pq.offer(s));

        while(true){
            if(pq.peek() >= K)
                return answer;
            answer++;
            int firstScoville = pq.poll();

            if(pq.isEmpty())
                return -1;

            int secondScoville = pq.poll();
            int newScoville = firstScoville + 2*secondScoville;
            pq.offer(newScoville);
        }


    }
}
