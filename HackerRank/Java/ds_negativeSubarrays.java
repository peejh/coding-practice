// https://www.hackerrank.com/challenges/java-negative-subarray
// Difficulty: EASY

import java.util.*;

public class ds_negativeSubarrays {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();      
        int[] a = new int[n];
                
        // Read and store array
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        
        sc.close();
        
        // Sum subarrays of `a` and count negative sums
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += a[j];
                if (sum < 0)
                    count++;
            }
        }
        
        System.out.println(count);
    }
}
