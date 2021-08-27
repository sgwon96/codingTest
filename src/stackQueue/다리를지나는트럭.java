package stackQueue;

import java.util.*;

public class 다리를지나는트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        int allWeight = 0;
        int time = 0;

        for(int i : truck_weights){
            while(true){
\                if(q.isEmpty()){
                    q.offer(i);
                    allWeight += i;
                    time++;
                    break;
\                }else if(q.size() == bridge_length){
                    allWeight -= q.poll();
                }else
                if(weight >= allWeight + i){
                    q.offer(i);
                    allWeight += i;
                    time++;
                    break;
                }else{
                    q.offer(0);
                    time++;
                }
            }
        }
    }
    answer += time + bridge_length;

        return answer;
}
}
