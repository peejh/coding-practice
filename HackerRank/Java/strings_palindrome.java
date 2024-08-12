// https://www.hackerrank.com/challenges/java-string-reverse
// Difficulty: EASY

import java.util.*;

public class strings_palindrome {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        sc.close();
        
        int l = 0; // left pointer
        int r = A.length() - 1; // right pointer
        boolean isPalindrome = true;
        
        while (l < r) {
            if (A.charAt(l) != A.charAt(r)) {
                isPalindrome = false;
                break;
            }

            l++;
            r--;
        }
        
        System.out.println((isPalindrome) ? "Yes" : "No");
    }
}