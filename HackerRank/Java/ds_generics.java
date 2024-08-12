// https://www.hackerrank.com/challenges/java-generics
// Difficulty: EASY

import java.lang.reflect.Method;

class Printer
{
   public <T> void printArray(T[] arr) {
       for (T item : arr) {
           System.out.println(item);
       }
   }
}

// NOTE: This part is given
public class ds_generics {
    public static void main( String args[] ) {
        Printer myPrinter = new Printer();
        Integer[] intArray = { 1, 2, 3 };
        String[] stringArray = {"Hello", "World"};
        myPrinter.printArray(intArray);
        myPrinter.printArray(stringArray);
        int count = 0;

        for (Method method : Printer.class.getDeclaredMethods()) {
            String name = method.getName();

            if(name.equals("printArray"))
                count++;
        }

        if (count > 1)
            System.out.println("Method overloading is not allowed!");
    }
}