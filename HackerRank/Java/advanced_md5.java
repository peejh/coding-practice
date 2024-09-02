// https://www.hackerrank.com/challenges/java-md5
// Difficulty: MEDIUM

import java.util.*;
import java.security.MessageDigest;

public class advanced_md5 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String message = in.nextLine();
        
        try {            
            // Create the MD5 object 
            MessageDigest md = MessageDigest.getInstance("MD5");
                       
            // Compute the MD5 hash in bytes
            byte[] digest = md.digest(message.getBytes());
            
            // Convert the byte array to a hexadecimal string
            StringBuffer hexString = new StringBuffer();            
            for (byte b : digest) {
                String hex = Integer.toHexString(0xFF & b);
                if (hex.length() == 1)
                    hexString.append("0");
                hexString.append(hex);
            }
            
            System.out.println(hexString.toString());         
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        in.close();
    }
}