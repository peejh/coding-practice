// https://www.hackerrank.com/challenges/java-strings-introduction
// Difficulty: EASY

import java.util.*;

public class strings_intro {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        sc.close();
        
        System.out.println(A.length() + B.length());
        System.out.println((A.compareTo(B) > 0) ? "Yes" : "No");
        
        A = Character.toUpperCase(A.charAt(0)) + A.substring(1);
        B = Character.toUpperCase(B.charAt(0)) + B.substring(1);
        
        System.out.printf("%s %s\n", A, B);
        
    }
}