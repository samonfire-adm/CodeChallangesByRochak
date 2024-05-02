#include <iostream>
#include <stack>
#include <string>

std::string reverse_string(std::string input_string) {
    std::stack<char> char_stack;
    for (char c : input_string) {
        char_stack.push(c);
    }

    std::string reversed_string;
    while (!char_stack.empty()) {
        reversed_string += char_stack.top();
        char_stack.pop();
    }

    return reversed_string;
}

int main() {
    std::string input_string = "Hello, world!";
    std::string reversed_string = reverse_string(input_string);
    std::cout << "Original string: " << input_string << std::endl;
    std::cout << "Reversed string: " << reversed_string << std::endl;
    return 0;
}
