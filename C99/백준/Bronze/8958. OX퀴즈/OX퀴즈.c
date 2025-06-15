#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    char str[100];
    for (int i = 0; i < T; i++) {
        scanf("%s", str);

        int score = 0, streak = 0;
        for (int j = 0; str[j] != '\0'; j++) {
            if (str[j] == 'O') {
                streak++;
                score += streak;
            } else {
                streak = 0;
            }
        }

        printf("%d\n", score);
    }

    return 0;
}
