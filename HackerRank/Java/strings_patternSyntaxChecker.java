// https://www.hackerrank.com/challenges/pattern-syntax-checker
// Difficulty: EASY

import java.util.Scanner;
import java.util.regex.*;

public class strings_patternSyntaxChecker
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while (testCases > 0) {
			String pattern = in.nextLine();
          	try {
                Pattern p = Pattern.compile(pattern);
                System.out.println("Valid");  
            } catch (PatternSyntaxException e) {
                System.out.println("Invalid");
            }
            testCases--;
		}
        in.close();
	}
}