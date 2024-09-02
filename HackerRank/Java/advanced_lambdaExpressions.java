// https://www.hackerrank.com/challenges/java-lambda-expressions
// Difficulty: MEDIUM

import java.io.*;
import java.util.*;

interface PerformOperation {
    boolean check(int a);
}

class MyMath {
    public static boolean checker(PerformOperation p, int num) {
        return p.check(num);
    }
    public PerformOperation isOdd() {
        return num -> num % 2 != 0;
    }
    public PerformOperation isPrime() {
        return num -> {
            if (num <= 1) return false;
            int sqrt = (int) Math.sqrt(num);
            for (int i = 2; i <= sqrt; i++) {
                if (num % i == 0) return false;
            }
            return true;
        };
    }
    public PerformOperation isPalindrome() {
        return num -> {
            char[] digits = String.valueOf(num).toCharArray();
            int left = 0;
            int right = digits.length - 1;
            while (left < right) {
                if (digits[left] != digits[right])
                    return false;
                left++;
                right--;
            }
            return true;
        };
    }
}

public class advanced_lambdaExpressions {

    public static void main(String[] args) throws IOException {
        MyMath ob = new MyMath();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        PerformOperation op;
        boolean ret = false;
        String ans = null;
        
        while (T-- > 0) {
            String s = br.readLine().trim();
            StringTokenizer st = new StringTokenizer(s);
            int ch = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            if (ch == 1) {
                op = ob.isOdd();
                ret = ob.checker(op, num);
                ans = (ret) ? "ODD" : "EVEN";
            } else if (ch == 2) {
                op = ob.isPrime();
                ret = ob.checker(op, num);
                ans = (ret) ? "PRIME" : "COMPOSITE";
            } else if (ch == 3) {
                op = ob.isPalindrome();
                ret = ob.checker(op, num);
                ans = (ret) ? "PALINDROME" : "NOT PALINDROME";
            }

            System.out.println(ans);
        }
    }

}