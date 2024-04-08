#include <iostream>
using namespace std;
void cococola(int n) {
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "CocoCola" << endl;
        } else if (i % 3 == 0) {
            cout << "Coca" << endl;
        } else if (i % 5 == 0) {
            cout << "Cola" << endl;
        } else {
            cout << i << endl;
        }
    }
}

int main() {
    cococola(15);
    return 0;
}
