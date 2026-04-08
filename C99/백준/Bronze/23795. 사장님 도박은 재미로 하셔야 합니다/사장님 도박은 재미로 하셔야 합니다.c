#include <stdio.h>

int main(void) {
    int M, sum = 0;
    while (1) {
        scanf("%d", &M);
        if (M == -1) {
            printf("%d\n", sum);
            break;
        }
        sum += M;
    }
}