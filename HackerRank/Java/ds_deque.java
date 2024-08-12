// https://www.hackerrank.com/challenges/java-dequeue
// Difficulty: MEDIUM

import java.util.*;
public class ds_deque {

    public static void main(String[] args) {
        // This solution uses a Map to track what is currently in the Deque

        Scanner in = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<Integer>();
        Map<Integer, Integer> freqs = new HashMap<Integer, Integer>();
        int maxUniques = Integer.MIN_VALUE;

        int n = in.nextInt(); // size of array
        int m = in.nextInt(); // size of contiguous elements
        
        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            deque.add(num);
            int freq = freqs.containsKey(num) ? freqs.get(num) + 1 : 1;
            freqs.put(num, freq);

            // Perform the following logic once we have `m` amount in deque
            if (deque.size() == m) {
                // The count of keys in the Map is equal to the count of unique
                // numbers currently in the deque
                maxUniques = Math.max(maxUniques, freqs.keySet().size());
                // Adjust the frequency count in the Map for the number being
                // removed from the deque
                int first = deque.remove(); // Remove the first element of the Deque
                int newFreq = freqs.get(first) - 1;
                // If the frequency count for a number in the Map reaches 0, remove its
                // key entry from the Map
                if (newFreq == 0)
                    freqs.remove(first);
                else
                    freqs.put(first, newFreq);
            }     
        }
        
        System.out.println(maxUniques);
        in.close();
    }

    public static void main2(String[] args) {
        // This solution uses a Set to keep track of the unique numbers that
        // are currently in the Deque

        Scanner in = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<Integer>();
        HashSet<Integer> set = new HashSet<>();
        int maxUniques = Integer.MIN_VALUE;
    
        int n = in.nextInt(); // size of array
        int m = in.nextInt(); // size of contiguous elements
    
        for (int i = 0; i < n; i++) {
            int num = in.nextInt();    
            deque.add(num);
            set.add(num);
            
            // Perform the following logic once we have `m` amount in deque
            if (deque.size() == m) {
                // The size of the Set represents the amount of unique
                // numbers in the deque
                maxUniques = Math.max(maxUniques, set.size());  
                // Remove the first element of the Deque
                int first = (int) deque.remove();
                
                // If there are no duplicates of the removed number in the
                // Deque, remove it also from the set list
                // NOTE: This is probably a runtime bottleneck as the
                // `contains` method runs in O(n) time
                if (!deque.contains(first))
                    set.remove(first);
            }
        }

        System.out.println(maxUniques);
        in.close();
    }    
}



