package dp;

public class 도둑질 {

    public int solution(int[] money) {
        int[][] pick = new int[2][money.length];

        pick[0][0] = money[0];  // 첫번째 집을 훔치는 경우
        pick[0][1] = money[0];
        pick[1][0] = 0;         // 첫번째 집을 훔치지 않는 경우
        pick[1][1] = money[1];

        for(int i=2; i<money.length; i++) {
            pick[0][i] = Math.max(pick[0][i-2] + money[i], pick[0][i-1]);
            pick[1][i] = Math.max(pick[1][i-2] + money[i], pick[1][i-1]);
        }

        return Math.max(pick[0][pick[0].length-2], pick[1][pick[1].length-1]);
    }
}
