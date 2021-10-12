package dsa;
import java.util.*;
public class numberCount {

	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int n = sc.nextInt();
	    int i = 0;
	    List<Integer> values = new ArrayList<Integer>();
	    while(n>0){
	    	values.add(n%10);
        n = (int)n/10;
        i = i+1;
	}//System.out.println(values);
	    for (int j = values.size()-1; j>=0; j--) System.out.println(values.get(j));

}}
