import java.util.*;
  
  public class Main{
  
  public static void main(String[] args) {
      Scanner scn = new Scanner(System.in);
  
      int t = scn.nextInt();
      int[] arr = new int[t];
      for (int i = 0; i < t; i++){
          arr[i]  = scn.nextInt();
      }
      
      for(int i = 0; i<t; i++){
          if (isPrime(arr[i])) System.out.println("prime");
          else System.out.println("not prime");
      }
   }
   
   static boolean isPrime(int n){
       for(int i = 2; i<=Math.sqrt(n);i++){
           if (n%i == 0) return false;
       } return true;
   }
  }