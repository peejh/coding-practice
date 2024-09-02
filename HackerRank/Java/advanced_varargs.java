// https://www.hackerrank.com/challenges/simple-addition-varargs
// Difficulty: EASY

import java.io.*;
import java.lang.reflect.*;
import java.util.*;

class Add {
    
    void add(int... args) {
        int n = args.length;
        int sum = args[0];
        System.out.print(args[0]);
        for (int i = 1; i < n; i++) {
            sum += args[i];
            System.out.printf("+%d", args[i]);
        }            
        System.out.printf("=%d\n", sum);
    }
    
}

public class advanced_varargs {

    public static void main(String[] args) {
       try{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
            int n2 = Integer.parseInt(br.readLine());
			int n1 = Integer.parseInt(br.readLine());
			int n3 = Integer.parseInt(br.readLine());
			int n4 = Integer.parseInt(br.readLine());
			int n5 = Integer.parseInt(br.readLine());
			int n6 = Integer.parseInt(br.readLine());
			
            Add ob = new Add();
			ob.add(n1,n2);
			ob.add(n1,n2,n3);
			ob.add(n1,n2,n3,n4,n5);	
			ob.add(n1,n2,n3,n4,n5,n6);
			
            Method[] methods = Add.class.getDeclaredMethods();
			Set<String> set = new HashSet<>();
			boolean overload = false;

			for (int i = 0; i < methods.length; i++) {
				if(set.contains(methods[i].getName())) {
					overload=true;
					break;
				}
				set.add(methods[i].getName());			
			}

			if (overload) {
				throw new Exception("Overloading not allowed");
			}

            br.close();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
		
}