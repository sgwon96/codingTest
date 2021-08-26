package hash;

import java.util.*;

public class 전화번호목록 {

    public static boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>();
        Arrays.stream(phone_book).forEach(s -> set.add(s));

        for(String str : phone_book){
            for(int i = 1; i < str.length(); i++){
                if(set.contains(str.substring(0, i))){
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String[] phoneBook = {"123","456","789"};
        System.out.println(solution(phoneBook));
    }
}
