// https://www.hackerrank.com/challenges/java-biginteger
// Difficulty: EASY

import java.util.*;
import java.math.BigInteger;

public class bigNumber_bigInteger {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger a = new BigInteger(in.nextLine());
        BigInteger b = new BigInteger(in.nextLine());
        System.out.println(a.add(b));
        System.out.println(a.multiply(b));
        in.close();
    }
    
}