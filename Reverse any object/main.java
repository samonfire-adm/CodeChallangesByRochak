import java.util.Stack;

public class ReverseString {
    public static String reverseString(String inputString) {
        Stack<Character> stack = new Stack<>();
        for (char c : inputString.toCharArray()) {
            stack.push(c);
        }

        StringBuilder reversedString = new StringBuilder();
        while (!stack.isEmpty()) {
            reversedString.append(stack.pop());
        }

        return reversedString.toString();
    }
    public static void main(String[] args) {
        String inputString = "Hello, world!";
        String reversedString = reverseString(inputString);
        System.out.println("Original string: " + inputString);
        System.out.println("Reversed string: " + reversedString);
    }
}
