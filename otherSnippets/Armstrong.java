import java.util.*;
public class Armstrong {
    public static void main(String[] args) {
        int start = 100;
        int end = 999;
        List<Integer> list = new ArrayList<Integer>();
        for (int i = start; i <= end; i++) {
            if(isArmstrong(i)){
                list.add(i);
            }
        }            System.out.println(list);


    }

    static boolean isArmstrong(int i) {
        int sum = 0;
        int temp;
        int num = i;
        while(i>0){
            temp = i%10;
            i /= 10;
            sum += Math.pow(temp,3);
        }
        return sum == num;
    }
}
