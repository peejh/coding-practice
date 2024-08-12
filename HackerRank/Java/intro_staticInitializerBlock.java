// https://www.hackerrank.com/challenges/java-static-initializer-block
// Difficulty: EASY

import java.util.*;

public class intro_staticInitializerBlock {

    private static int B;
    private static int H;
    
    private static void init(int x, int y) throws Exception {
        if (x <= 0 || y <= 0)
            throw new Exception("Breadth and height must be positive");
        
        B = x;
        H = y;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int b = scan.nextInt();
        int h = scan.nextInt();
        scan.close();

        try {
            init(b, h);
            System.out.println(intro_staticInitializerBlock.B * intro_staticInitializerBlock.H);
        } catch(Exception e) {
            System.out.println(e.toString());
        }
    }
    
}