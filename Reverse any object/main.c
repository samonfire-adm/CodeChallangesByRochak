#include <stdio.h>
#include <string.h>

void reverse_string(char* input_string) {
    int length = strlen(input_string);
    char stack[length];
    int top = -1;

    for (int i = 0; i < length; i++) {
        stack[++top] = input_string[i];
    }

    for (int i = 0; i < length; i++) {
        input_string[i] = stack[top--];
    }
}

int main() {
    char input_string[] = "Hello, world!";
    reverse_string(input_string);
    printf("Reversed string: %s\n", input_string);
    return 0;
}
