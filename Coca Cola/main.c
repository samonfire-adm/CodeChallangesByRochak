#include <stdio.h>

void cococola(int n) {
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            printf("CocoCola\n");
        } else if (i % 3 == 0) {
            printf("Coca\n");
        } else if (i % 5 == 0) {
            printf("Cola\n");
        } else {
            printf("%d\n", i);
        }
    }
}

int main() {
    cococola(15);
    return 0;
}
