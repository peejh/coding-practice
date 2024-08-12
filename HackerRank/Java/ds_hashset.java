// https://www.hackerrank.com/challenges/java-hashset
// Difficulty: EASY

import java.util.*;

public class ds_hashset {

 public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];
        
        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
        
        HashSet<String> names = new HashSet<String>();
        for (int i = 0; i < t; i++) {
            names.add(pair_left[i] + ' ' + pair_right[i]);
            System.out.println(names.size());
        }
        
        s.close();
   }
}