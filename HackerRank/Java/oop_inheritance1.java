// https://www.hackerrank.com/challenges/java-inheritance-1
// Difficulty: EASY

class Animal {
	void walk() {
		System.out.println("I am walking");
	}
}

class Bird extends Animal {
	void fly() {
		System.out.println("I am flying");
	}
    
    void sing() {
        System.out.println("I am singing");
    }
}

public class oop_inheritance1 {

   public static void main(String args[]) {

	  Bird bird = new Bird();
	  bird.walk();
	  bird.fly();
      bird.sing();
	
   }

}