// https://www.hackerrank.com/challenges/java-singleton
// Difficulty: EASY

class Singleton{
    public String str;
    
    private Singleton() {}
    
    static Singleton getSingleInstance() {
        return new Singleton();
    }
}

public class advanced_singleton {
    public static void main(String[] args) {
        ;
    }
}