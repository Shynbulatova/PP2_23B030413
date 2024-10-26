package task1.c;

import java.util.HashSet;

public class Test {

   public static void main(String[] args) {
       HashSet<Parent> familySet = new HashSet<>(); 

       Daughter daughter1 = new Daughter("Mereke", Enums.HairType.STRAIGHT, Enums.EyeColor.BROWN, "SH.UALIKHANOV");
       Daughter daughter2 = new Daughter("Aida", Enums.HairType.STRAIGHT, Enums.EyeColor.BROWN, "SH.UALIKHANOV"); 

       familySet.add(daughter1);
       familySet.add(daughter2); 

       System.out.println("Number of family members in set: " + familySet.size()); 

       for (Parent member : familySet) {
           System.out.println(member); 
       }
   }
}