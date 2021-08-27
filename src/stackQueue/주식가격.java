package stackQueue;

import java.util.*;

public class 주식가격 {
    public int[] solution(int[] prices) {
        Stack<Integer> priceRaise = new Stack<>();
        int[] answer = new int[prices.length];

        for(int i = 0 ; i < prices.length ; i++){
            while(!priceRaise.isEmpty() && prices[i] < prices[priceRaise.peek()]){
                int pushTime = priceRaise.pop();
                answer[pushTime] = i - pushTime;
            }
            priceRaise.push(i);
        }

        while (!priceRaise.isEmpty()) {
            int pushTime = priceRaise.pop();
            answer[pushTime] = prices.length - pushTime - 1;
        }

        return answer;
    }
}
