package dsa;
import java.util.*;

public class fibonacci{
	  
	  public static void main(String[] args) {
	      Scanner sc = new Scanner(System.in);
	      int a = 0;int b =1; 
	      int n = sc.nextInt();
	      if(n == 1) System.out.println(a);
	      else if(n==2) System.out.println(b);
	      else
	      {System.out.println(a);
	      System.out.println(b);
	          for(int i = 2;i<n;i++)
	          {int temp = b;
	              b = a+b;
	              System.out.println(b);
	              a = temp;
	          }
	      }
	   }}
