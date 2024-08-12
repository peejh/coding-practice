// https://www.hackerrank.com/challenges/java-exception-handling-try-catch
// Difficulty: EASY

import java.util.*;

public class exceptionHandling_tryCatch {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        try {
            int x = in.nextInt();
            int y = in.nextInt();
            System.out.println(x / y);
        } catch (InputMismatchException ime) {
            System.out.println(ime.getClass().getName());
        } catch (ArithmeticException ae) {
            System.out.println(ae);
        }
        in.close();
    }
}