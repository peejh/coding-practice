// https://www.hackerrank.com/challenges/can-you-access
// Difficulty: MEDIUM

import java.io.*;
import java.security.*;

public class advanced_canYouAccess {

	public static void main(String[] args) throws Exception {
		DoNotTerminate.forbidExit();	

		try{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int num = Integer.parseInt(br.readLine().trim());
			Object o; // Must be used to hold the reference of the instance of the class Solution.Inner.Private
            Inner i = new Inner();
			o = i.new Private();
            Inner.Private ip = (Inner.Private) o;
            System.out.printf("%d is %s\n", num, ip.powerof2(num));
		    System.out.println("An instance of class: " + o.getClass().getCanonicalName() + " has been created");
		} catch (DoNotTerminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	}
	
    static class Inner {
		private class Private {
			private String powerof2(int num) {
				return ((num&num-1)==0) ? "power of 2" : "not a power of 2";
			}
		}
	}
}

class DoNotTerminate { //This class prevents exit(0)	 
    public static class ExitTrappedException extends SecurityException {
		private static final long serialVersionUID = 1L;
    }
 
    public static void forbidExit() {
        final SecurityManager securityManager = new SecurityManager() {
            @Override
            public void checkPermission(Permission permission) {
                if (permission.getName().contains("exitVM")) {
                    throw new ExitTrappedException();
                }
            }
        };
        System.setSecurityManager(securityManager);
    }
}	
	
