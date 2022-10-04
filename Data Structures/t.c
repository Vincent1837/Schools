#include <stdio.h>

int main()
{
    int input, h, m, s;
    printf("please enter seconds : ");
    scanf("%d", &input);
    h = input / 3600;
    m = (input % 3600) / 60;
    s = (input % 3600) % 60;
    printf("Answer : %dh %dm %ds", h, m, s);
    return 0;
}
