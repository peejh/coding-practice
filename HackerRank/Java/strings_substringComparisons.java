// https://www.hackerrank.com/challenges/java-string-compare
// Difficulty: EASY

import java.util.Scanner;

public class strings_substringComparisons {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        
        for (int i = k+1; i <= s.length(); i++) {
            String curr = s.substring(i-k, i);
            if (curr.compareTo(smallest) < 0)
                smallest = curr;
            else if (curr.compareTo(largest) > 0)
                largest = curr;
        }
        
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}