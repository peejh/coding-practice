// https://www.hackerrank.com/challenges/java-1d-array
// Difficulty: EASY

import java.util.*;

public class ds_1dArrayPart2 {

    public static boolean canWin(int leap, int[] game) {
        return canWinHelper(leap, game, 0);
    }
    
    public static boolean canWinHelper(int leap, int[] game, int i) {
        // Base cases
        if (i >= game.length)
            return true;
        else if (i < 0 || game[i] != 0)
            return false;
        
        // Tag current index as non-zero, i.e. as "visited"
        game[i] = 1;
        
        // Invoke recursion to next three choices
        return canWinHelper(leap, game, i-1) ||
            canWinHelper(leap, game, i+1) ||
            canWinHelper(leap, game, i+leap);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
