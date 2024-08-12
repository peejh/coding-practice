// https://www.hackerrank.com/challenges/java-string-tokens
// Difficulty: EASY

import java.util.*;

public class strings_stringTokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();
        scan.close();    
        
        if (s.length() > 0) {
            String[] tokens = s.split("[ !,\\?\\._'@]+");        
            System.out.println(tokens.length);
            for (String tok : tokens) {
                System.out.println(tok);
            }            
        } else {
            System.out.println(0);
        }
    }
}