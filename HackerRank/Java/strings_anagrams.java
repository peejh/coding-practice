// https://www.hackerrank.com/challenges/java-anagrams
// Difficulty: EASY

import java.util.Scanner;

public class strings_anagrams {

    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length())
            return false;
        
        char[] A = a.toLowerCase().toCharArray();
        char[] B = b.toLowerCase().toCharArray();
        
        java.util.Arrays.sort(A);
        java.util.Arrays.sort(B);
        
        return java.util.Arrays.equals(A, B);
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}