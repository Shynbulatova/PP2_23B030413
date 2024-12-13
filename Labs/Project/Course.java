package Project;

public class Course {
	private String courseID;
	private String courseName;
	private int credits;
	private CourseType courseType;
	private List<Student> students;
	
	public Course(String coureID, String courseName, int credits, CourseType courseType) {
		this.courseID=courseID;
		this.courseName=courseName;
		this.credits=credits;
		this.courseType=courseType;
		this.students=new ArrayList<>();
	}
	
	public String getCourseID() {
		return courseID;
	}
	public String getCourseName() {
		return courseName;
	}
	public int getCredits() {
		return credits;
	}
	public CourseType getCourseType() {
		return courseType;
	}
	
	@Override
	public String toString() {
		return "Course{"+
	           "courseID="+courseID+'\''+
	           ", courseName='" + courseName+'\''+
	           ", credits="+credits +
	           ", courseType"+courseType+
	           '}';
				
	}

}
