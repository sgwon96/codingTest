package dp;

import java.util.*;

public class N으로표현 {

    public int solution(int N, int number) {
        int answer = -1;
        Set<Integer>[] setArr = new Set[9];

        int temp = N;
        for (int i = 1 ; i < 9 ; i++){
            setArr[i] = new HashSet<>();
            setArr[i].add(temp);
            temp += 10*N;
        }

        for (int i = 1 ; i < 9 ; i++){
            for (int j = 1 ; j <= i/2 ; j++){
                for (Integer a : setArr[j]){
                    for (Integer b : setArr[i-j]){
                        setArr[i].add(a+b);
                        setArr[i].add(a-b);
                        setArr[i].add(b-a);
                        setArr[i].add(a*b);
                        if (b != 0) setArr[i].add(a/b);
                        if (a != 0) setArr[i].add(b/a);
                    }
                }
            }
        }

        for(int i = 1; i < 9; i++) {
            if(setArr[i].contains(number)) {
                answer = i;
                break;
            }
        }

        return answer;
    }
}
