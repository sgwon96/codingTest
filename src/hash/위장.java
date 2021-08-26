package hash;

import java.util.*;

public class 위장 {

    public static int solution(String[][] clothes) {

        int answer = 1;

        HashMap<String, Integer> hm = new HashMap<>();
        Arrays.stream(clothes).forEach(c -> hm.put(c[1], hm.getOrDefault(c[1], 0)+1));

        // 안입는 경우를 포함해서 종류+1 을 전부 곱해서 경우의 수 구하기
        for (String key : hm.keySet()) {
            answer *= hm.get(key)+1;
        }

        // 모든 종류의 옷을 안입는 경우의 수 하나 빼기
        answer--;

        return answer;
    }

    public static void main(String[] args) {
        String[][] clothes = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"},{"green_turban", "headgear"}};
        System.out.println(solution(clothes));
    }

}
