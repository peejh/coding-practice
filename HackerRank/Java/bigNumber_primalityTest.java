// https://www.hackerrank.com/challenges/java-primality-test
// Difficulty: EASY

import java.io.*;
import java.math.BigInteger;

public class bigNumber_primalityTest {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        BigInteger n = new BigInteger(bufferedReader.readLine());
        boolean isPrime = n.isProbablePrime(100);
        System.out.println((isPrime) ? "prime" : "not prime");

        bufferedReader.close();
    }
}