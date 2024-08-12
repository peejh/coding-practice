// https://www.hackerrank.com/challenges/java-priority-queue
// Difficulty: MEDIUM

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.PriorityQueue;

class Student implements Comparable<Student> {
    int id;
    double cgpa;
    String name;
    
    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }
    
    public int getID() {
        return this.id;
    }
    
    public String getName() {
        return this.name;
    }
    
    public double getCGPA() {
        return this.cgpa;
    }
    
    @Override
    public int compareTo(Student other) {
        if (this.getCGPA() != other.getCGPA())
            return Double.compare(other.getCGPA(), this.getCGPA());
        else if (!this.getName().equals(other.getName()))           
            return this.getName().compareTo(other.getName());
        return Integer.compare(this.getID(), other.getID());
    }
}

class Priorities {
    PriorityQueue<Student> pq;
    
    public Priorities() {
        this.pq = new PriorityQueue<Student>();
    }
    
    public List<Student> getStudents(List<String> events) {       
        for (String event : events) {
            String[] args = event.split(" ");
            String op = args[0];
            
            switch (op) {
                case "ENTER":
                    String name = args[1];
                    double cgpa = Double.parseDouble(args[2]);
                    int id = Integer.parseInt(args[3]);
                    Student s = new Student(id, name, cgpa);
                    pq.add(s);
                    break;
                case "SERVED":
                    pq.poll();
                    break;
            }
        }

        List<Student> res = new ArrayList<Student>();
        while (pq.size() > 0) {
            res.add(pq.poll());
        }
        
        return res;
    }
}

public class ds_priorityQueue {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();
    
    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());    
        List<String> events = new ArrayList<>();
        
        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }
        
        List<Student> students = priorities.getStudents(events);
        
        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}