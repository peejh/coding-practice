// https://www.hackerrank.com/challenges/java-bigdecimal
// Difficulty: MEDIUM

import java.math.BigDecimal;
import java.util.*;

class bigNumber_bigDecimal {
    public static void main(String []args) {
        // Input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String []s = new String[n + 2];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next();
        }
        sc.close();

        // `sort` method where a sublist can be specified is used
        // because the String array `s` has 2 extra indexes with
        // null values
        Arrays.sort(s, 0, n, new Comparator<String>() {
            @Override
            public int compare(String x, String y) {            
                BigDecimal bigX = new BigDecimal(x);
                BigDecimal bigY = new BigDecimal(y);
                return bigY.compareTo(bigX);
            }
        });

        // Output
        for (int i = 0; i < n; i++) {
            System.out.println(s[i]);
        }
    }
}