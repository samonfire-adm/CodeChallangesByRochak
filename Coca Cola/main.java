public class Main {
    public static void cococola(int n) {
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("CocoCola");
            } else if (i % 3 == 0) {
                System.out.println("Coca");
            } else if (i % 5 == 0) {
                System.out.println("Cola");
            } else {
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        cococola(15);
    }
}
