// https://www.hackerrank.com/challenges/java-list
// Difficulty: EASY

import java.util.*;
import java.util.stream.IntStream;

public class ds_list {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        // Store the array
        int n = in.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            arr.add(in.nextInt());
        }
        
        // Query the array
        int q = in.nextInt();
        for (int i = 0; i < q; i++) {
            String command = in.next();
            if (command.equals("Insert")) {
                int idx = in.nextInt();
                int item = in.nextInt();
                arr.add(idx, item);
            } else if (command.equals("Delete")) {
                int idx = in.nextInt();
                arr.remove(idx);
            }
        }
        
        // Display final state of the array
        for (Integer num : arr) {
            System.out.printf("%d ", num);
        }
        
        in.close();
    }

    public static void main2(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());
        List<String> arr = new ArrayList<String>(Arrays.asList(in.nextLine().split(" ")));
        int q = Integer.parseInt(in.nextLine());

        IntStream.range(0, q).forEach(value -> {
            String command = in.nextLine();

            if (command.equals("Insert")) {
                String[] items = in.nextLine().split(" ");
                arr.add(Integer.parseInt(items[0]), items[1]);
            } else if (command.equals("Delete")) {
                int idx = Integer.parseInt(in.nextLine());
                arr.remove(idx);
            }
        });

        System.out.print(String.join(" ", arr));
    }    
}