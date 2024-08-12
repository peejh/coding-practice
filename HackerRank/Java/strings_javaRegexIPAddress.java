// https://www.hackerrank.com/challenges/java-regex
// Difficulty: MEDIUM

import java.util.Scanner;

class MyRegex {
    // 000 to 199 -> [01]?\\d{1,2}
    // 200 to 249 -> 2[0-4]\\d
    // 250 to 255 -> 25[0-5]
    String octet = "([01]?\\d{1,2}|25[0-5]|2[0-4]\\d)";
    String pattern = octet + "(\\." + octet + "){3}";
}

public class strings_javaRegexIPAddress {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }
        in.close();
    }    
}
