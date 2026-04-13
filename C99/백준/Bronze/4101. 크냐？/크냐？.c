#include <stdio.h>

int main(void)
{
    int a, b;
    while (scanf("%d %d", &a, &b) != EOF) {
        if (a == 0 && b == 0)
            break;
        else if (a > b)
            printf("Yes\n");
        else
            printf("No\n");
    }
    return 0;
}

// 대소문자 조심 좀 합시다