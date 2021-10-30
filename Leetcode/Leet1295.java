public class Leet1295 {
    public static void main(String[] args) {
        int[] arr = {12,345,2,6,7896};
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if(checkEven(arr[i]) == true){
                count++;
            }
        }
        System.out.println(count);
    }

    static boolean checkEven(int i) {
        int count = 0;
        while(i > 0){
            count++;
            i /= 10;
        }
        return count%2 == 0;
    }
}
