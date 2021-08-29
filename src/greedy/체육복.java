package greedy;

import java.util.*;



public class 체육복 {

    public int solution(int n, int[] lost, int[] reserve) {
        int result = n - lost.length;

        HashSet<Integer> reserveSet = new HashSet<Integer>();

        for (int reserveNum : reserve){
            reserveSet.add(reserveNum);
        }

        // 내껀 내가 빌려
        for (int i = 0 ; i < lost.length ; i++){
            if (reserveSet.contains(lost[i])){
                reserveSet.remove(lost[i]);
                result++;
                lost[i] = -1;
            }
        }

        // 다른 사람꺼 빌려
        for (int i = 0 ; i < lost.length ; i++){
            if (reserveSet.contains(lost[i]-1)){
                reserveSet.remove(lost[i]-1);
                result++;
                lost[i] = -1;
            } else if (reserveSet.contains(lost[i]+1)){
                reserveSet.remove(lost[i]+1);
                result++;
                lost[i] = -1;
            }
        }

        return result;

    }
}
