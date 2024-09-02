// https://www.hackerrank.com/challenges/sha-256
// Difficulty: MEDIUM

import java.util.*;
import java.security.MessageDigest;

public class advanced_sha256 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String message = in.nextLine();
        
        try {            
            // Create the SHA-256 object 
            MessageDigest md = MessageDigest.getInstance("SHA-256");
                       
            // Compute the SHA-256 hash in bytes
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