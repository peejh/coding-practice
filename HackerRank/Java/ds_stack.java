// https://www.hackerrank.com/challenges/java-stack
// Difficulty: MEDIUM

import java.util.*;

class ds_stack {
	
	public static void main(String []argh)
	{
		Scanner in = new Scanner(System.in);
        
        // Map closing brackets to its opening counterparts
        HashMap<Character, Character> close = new HashMap<Character, Character>();
        close.put(')', '(');
        close.put('}', '{');
        close.put(']', '[');
		
        // Scan and process each input line
		while (in.hasNextLine()) {
			String line = in.nextLine();
            Stack<Character> stack = new Stack<Character>();
            boolean isBalanced = true;
            
            for (int i = 0; i < line.length() && isBalanced; i++) {
                char curr = line.charAt(i);
                if (close.containsKey(curr) && !stack.empty()) {
                    // If the current character is a closing bracket,
                    // check whether the top of the stack is the matching
                    // opening bracket
                    char top = stack.pop();
                    char open = close.get(curr);
                    isBalanced = top == open;
                } else {
                    // Push to stack if opening bracket
                    stack.push(curr);
                }
            }
            
            System.out.println(isBalanced && stack.empty());
		}
		
        in.close();
	}

    public static void main2(String[] args) {
        Scanner in = new Scanner(System.in);
        Map<String, String> openClose = Map.of(
            "{", "}",
            "[", "]",
            "(", ")");
    
        while (in.hasNext()) {
            Stack<String> stack = new Stack<>();
            boolean isBalanced = true;
        
            for (String curr : in.nextLine().split("")) {
                if (openClose.containsKey(curr)) {
                    stack.push(curr);
                } else if (!stack.empty() && openClose.containsValue(curr)) {
                    String open = stack.pop();
                    isBalanced = openClose.get(open).equals(curr);
                } else {
                    isBalanced = false;
                    break;
                }
            }

            System.out.println(isBalanced && stack.empty());
        }
        in.close();    
    }
}



