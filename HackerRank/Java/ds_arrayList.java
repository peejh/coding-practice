// https://www.hackerrank.com/challenges/java-arraylist
// Difficulty: EASY

import java.util.*;

public class ds_arrayList {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<List> arr = new ArrayList<List>();
        
        // Store the arrays in a list of lists
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int d = sc.nextInt();
            ArrayList<Integer> curr = new ArrayList<Integer>();
            for (int j = 0; j < d; j++) {
                curr.add(sc.nextInt());
            }
            arr.add(curr);
        }

        // Query the arrays
        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int x = sc.nextInt() - 1;
            int y = sc.nextInt() - 1;
            try {
                System.out.println(arr.get(x).get(y));
            } catch (IndexOutOfBoundsException e) {
                System.out.println("ERROR!");
            }
        }
        
        sc.close();
    }
}