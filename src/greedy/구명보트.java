package greedy;

import java.util.*;

public class 구명보트 {

    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        for (; i < j; j--) {
            if (people[i] + people[j] <= limit)
                i++;
        }
        return people.length - i;
    }
}
