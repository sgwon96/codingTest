package stackQueue;

import java.util.*;

public class 프린터 {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        Arrays.stream(priorities).forEach(p->pq.offer(p));

        while(!pq.isEmpty()){
            for(int i = 0 ; i < priorities.length ; i++){
                if(pq.peek() == priorities[i]){
                    pq.poll();
                    answer++;
                    if(location == i)
                        return answer;
                }
            }

        }

        return answer;

    }
}
