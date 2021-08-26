package stackQueue;

import java.util.*;

public class 기능개발 {

    public static int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> qe = new LinkedList<>();
        List<Integer> answerList = new ArrayList<>();

        for(int i = 0 ; i < progresses.length ; i++){
            int requiredTime = (100-progresses[i])%speeds[i] == 0 ? (100-progresses[i])/speeds[i] : (100-progresses[i])/speeds[i] + 1 ;
            qe.add(requiredTime);
        }

        while(!qe.isEmpty()){
            int count = 1;
            int day = qe.poll();
            while(!qe.isEmpty() && qe.peek() <= day){
                count++;
                qe.poll();
            }
            answerList.add(count);
        }

        int[] answer = new int[answerList.size()];
        for(int i = 0 ; i < answerList.size(); i++){
            answer[i] = answerList.get(i);
        }


        return answer;
    }

    public static void main(String[] args) {
        int[] progesses = {93, 30, 55};
        int[] speeds = {1, 30, 5};

        for (int i : solution(progesses,speeds))
            System.out.printf(" " + i);
    }
}
