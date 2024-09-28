package Labs;
//5
import java.util.Vector;

public class DragonLaunch {

    public enum Gender {
        BOY, GIRL
    }

    public static class Person {
        private Gender gender;

        public Person(Gender gender) {
            this.gender = gender;
        }

        public Gender getGender() {
            return gender;
        }

        @Override
        public String toString() {
            return gender.toString();
        }
    }

    private Vector<Person> line;

    public DragonLaunch() {
        line = new Vector<>();
    }

    public void kidnap(Person p) {
        line.add(p);
    }

    public boolean willDragonEatOrNot() {
        while (line.size() > 1) {
            if (line.firstElement().getGender() != line.lastElement().getGender()) {
                line.remove(0);
                line.remove(line.size() - 1);
            } else {
                return true; 
            }
        }
        return false; 
    }

    public static void main(String[] args) {
        DragonLaunch launch = new DragonLaunch();
        launch.kidnap(new Person(Gender.BOY));
        launch.kidnap(new Person(Gender.GIRL));
        launch.kidnap(new Person(Gender.BOY));
        launch.kidnap(new Person(Gender.GIRL));

        if (launch.willDragonEatOrNot()) {
            System.out.println("Dragon will eat!");
        } else {
            System.out.println("No one will be eaten.");
        }
    }
}

