package greedy;

import java.util.*;

public class 조이스틱 {

    public int solution(String name) {
        int answer = 0;
        int len = name.length();
        int min = len-1;
        for(int i = 0 ; i < len ; i++){
            char target = name.charAt(i);
            if(target != 'A'){
                answer += Math.min(target-'A','Z'- target + 1);
                int next = i+1;
                while(next < len && name.charAt(next) == 'A') next++;
                min = Math.min(min, (i * 2) + len - next);
            }
        }
        answer += min;
        return answer;
    }
}
