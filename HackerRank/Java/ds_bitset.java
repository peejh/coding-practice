// https://www.hackerrank.com/challenges/java-bitset
// Difficulty: EASY

import java.util.*;

public class ds_bitset {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        in.nextLine();
        
        BitSet b1 = new BitSet(n);
        BitSet b2 = new BitSet(n);
        
        for (int i = 0; i < m; i++) {
            List<String> line = new ArrayList<String>(Arrays.asList(in.nextLine().split(" ")));
            String op = line.get(0);
            int which = Integer.parseInt(line.get(1));
            int index = Integer.parseInt(line.get(2));           
            BitSet b, other;
            
            if (which == 1) {
                b = b1;
                other = b2;
            } else {
                b = b2;
                other = b1;
            }
            
            switch (op) {
                case "AND":
                    b.and(other);
                    break;
                case "OR":
                    b.or(other);
                    break;
                case "XOR":
                    b.xor(other);
                    break;
                case "FLIP":
                    b.flip(index);
                    break;
                case "SET":
                    b.set(index);
                    break;
            }
            
            System.out.printf("%d %d\n", b1.cardinality(), b2.cardinality());
        }
        
        in.close();
    }
}