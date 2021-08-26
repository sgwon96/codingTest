package hash;

import java.util.*;

public class 베스트앨범 {

    public static int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();

        // 장르:재생횟수 순으로 해시맵 만들어서 넣기
        HashMap<String, Integer> hm = new HashMap<>();
        for (int i = 0 ; i < genres.length ; i++)
            hm.put(genres[i], hm.getOrDefault(genres[i], 0) + plays[i]);

        // 장르를 재생횟수를 기준으로 정렬
        List<String> keySetList = new ArrayList<>(hm.keySet());
        Collections.sort(keySetList, (o1, o2) -> (hm.get(o2).compareTo(hm.get(o1))));

        // 재생횟수가 많은 장르부터 인덱스:재생횟수로 해시맵 만들어 넣기
        for(String genre : keySetList){
            HashMap<Integer, Integer> playList = new HashMap<>();

            for(int i = 0 ; i < genres.length ; i++){
                if(genre.equals(genres[i]))
                    playList.put(i,plays[i]);
            }

            List<Integer> keySetPlayList = new ArrayList<>(playList.keySet());
            Collections.sort(keySetPlayList, (o1, o2) -> (playList.get(o2).compareTo(playList.get(o1))));

            // 재생횟수가 가장 많은 노래 한개는 정답에 무조건 넣기
            answer.add(keySetPlayList.get(0));

            // 노래가 두개 이상이면 두번째 노래까지 정답에 넣기
            if(keySetPlayList.size() > 1){
                answer.add(keySetPlayList.get(1));
            }
        }


        int[] answers = new int[answer.size()];
        for(int i = 0 ; i < answers.length ; i++)
            answers[i] = answer.get(i);

        return answers;
    }

    public static void main(String[] args) {
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};

        for (int i : solution(genres,plays))
            System.out.printf(" " + i);

    }

}
