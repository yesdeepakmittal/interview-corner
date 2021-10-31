public class DigitLength{
    public static void main(String[] args) {
        int num = 34567;
        
        System.out.println("Length using method1 is "+ method1(num));
        System.out.println("Length using method2 is "+ method2(num));
        System.out.println("Length using method3 is "+ method3(num));
        System.out.println("Length using method4 is "+ method4(num));
    }

    static int method1(int num){
        int len = (int)Math.log10(num) + 1;
        return len;
    }

    static int method2(int num){
        String a = "";
        String temp = a + num;
        int len = temp.length();
        return len;
    }

    static int method3(int num){
        int len = String.valueOf(num).length();
        return len;
    }

    static int method4(int num){
        int len = 0;
        while(num > 0){
            num /= 10;
            len++;
        }
        return len;
    }
}