// https://www.hackerrank.com/challenges/phone-book
// Difficulty: EASY

import java.util.*;

class ds_phoneBook {
	public static void main(String []argh) {
		Scanner in = new Scanner(System.in);
        
        // Store the phone directory data
        HashMap<String, Integer> dir = new HashMap<String, Integer>();
		int n = Integer.parseInt(in.nextLine());
		for(int i = 0; i < n; i++) {
			String name = in.nextLine();
			int phone = Integer.parseInt(in.nextLine());
            dir.put(name, phone);
		}
        
        // Query the phone directory
		while (in.hasNext()) {
			String queryName = in.nextLine();
            Integer queryPhone = dir.get(queryName);
            if (queryPhone != null) {
                System.out.printf("%s=%d\n", queryName, queryPhone);
            } else {
                System.out.println("Not found");
            }
		}
        
        in.close();
	}
}