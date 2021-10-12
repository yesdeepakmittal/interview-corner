import java.util.*;
   
   public class Main{
   
   public static void main(String[] args) {
     List<Integer> values = new ArrayList<Integer>();
     Scanner sc = new Scanner(System.in);
     int n = sc.nextInt();
     while(n>0){values.add(n%10);
         n = n/10;
     }for (int i = 0;i<values.size();i++) System.out.println(values.get(i));
    }
   }