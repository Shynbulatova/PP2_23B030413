package task1.c;
import task1.c.Enums;

public class Parent {
    private String name;
    private Enums.HairType hairType;
    private Enums.EyeColor eyeColor;

    public Parent(String name, Enums.HairType hairType, Enums.EyeColor eyeColor) {
        this.name = name;
        this.hairType = hairType;
        this.eyeColor = eyeColor;
    }

    // Getters
    public String getName() {
        return name;
    }

    public Enums.HairType getHairType() {
        return hairType;
    }

    public Enums.EyeColor getEyeColor() {
        return eyeColor;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true; // Check for reference equality
        if (!(o instanceof Parent)) return false; // Check type
        Parent parent = (Parent) o; // Cast to Parent
        return name.equals(parent.name) &&
               hairType == parent.hairType &&
               eyeColor == parent.eyeColor; // Compare attributes
    }

    @Override
    public int hashCode() {
        int result = name.hashCode();
        result = 31 * result + hairType.hashCode();
        result = 31 * result + eyeColor.hashCode(); // Generate hash code based on attributes
        return result;
    }

   @Override
   public String toString() {
       return "Parent{" +
               "name='" + name + '\'' +
               ", hairType=" + hairType +
               ", eyeColor=" + eyeColor +
               '}';
   }
}