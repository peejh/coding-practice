import java.util.*;

class Student {
	private int id;
	private String fname;
	private double cgpa;

	public Student(int id, String fname, double cgpa) {
		super();
		this.id = id;
		this.fname = fname;
		this.cgpa = cgpa;
	}

	public int getId() {
		return id;
	}

	public String getFname() {
		return fname;
	}

	public double getCgpa() {
		return cgpa;
	}

}

class StudentSorter implements Comparator<Student> {
    public int compare(Student a, Student b) {
        if (a.getCgpa() > b.getCgpa()) {
            return -1;
        } else if (a.getCgpa() == b.getCgpa()) {
            return a.getFname().compareTo(b.getFname());
        }
        return 1;
    }
}

public class ds_sort
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		
		List<Student> studentList = new ArrayList<Student>();
		while(testCases>0){
			int id = in.nextInt();
			String fname = in.next();
			double cgpa = in.nextDouble();
			
			Student st = new Student(id, fname, cgpa);
			studentList.add(st);
			
			testCases--;
		}
        StudentSorter studentSorter = new StudentSorter();
        Student[] studentArr = new Student[studentList.size()];
        studentList.toArray(studentArr);
        Arrays.sort(studentArr, studentSorter);
      	for(Student st: studentArr){
			System.out.println(st.getFname());
		}
	}
}

