// https://www.hackerrank.com/challenges/tag-content-extractor
// Difficulty: MEDIUM

import java.util.*;
import java.util.regex.*;

public class strings_tagContentExtractor {
	public static void main(String[] args){
		
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while (testCases > 0){
			String line = in.nextLine();
			
          	String regex = "<([^<>]+)>([^<>]+)</\\1>";
            Pattern p = Pattern.compile(regex);
            Matcher m = p.matcher(line);
            
            if (m.find()) {
                System.out.println(m.group(2));
                while (m.find()) {
                    System.out.println(m.group(2));
                }
            } else {
                System.out.println("None");
            }
			
			testCases--;
		}
        in.close();
	}
}