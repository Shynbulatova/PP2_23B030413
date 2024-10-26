package task1.c;

public class Daughter extends Parent {
    
    private String schoolName;

    public Daughter(String name, Enums.HairType hairType, Enums.EyeColor eyeColor, String schoolName) {
        super(name, hairType, eyeColor);
        this.schoolName = schoolName;
    }

    public String getSchoolName() {
        return schoolName;
    }

    @Override
    public boolean equals(Object o) {
        if (!super.equals(o)) return false; // Call superclass equals method
        if (!(o instanceof Daughter)) return false; // Check type for subclass
        Daughter daughter = (Daughter) o; // Cast to Daughter
        return schoolName.equals(daughter.schoolName); // Compare school names for equality
    }

    @Override
    public int hashCode() {
        int result = super.hashCode(); // Get superclass hash code
        result = 31 * result + schoolName.hashCode(); // Include school name in hash code calculation
        return result;
    }

    @Override
    public String toString() {
        return "Daughter{" +
                "schoolName='" + schoolName + '\'' +
                ", " + super.toString() +
                '}';
    }
 }