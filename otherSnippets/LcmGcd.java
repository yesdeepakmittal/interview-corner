public class LcmGcd {
    public static void main(String[] args) {
        int a = 16;
        int b = 28;

        int lcm = a*b/GCD(a,b);
        System.out.println(lcm);
    }
    static int GCD(int a, int b){
        if(a == 0){
            return b;
        } return GCD(b%a,a);
    }
}
