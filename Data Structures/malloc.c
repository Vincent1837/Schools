#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *pt = (int*)malloc(10);
    pt[0] = 5;
    pt[1] = 2;
    printf("%d %d\n", pt[0], pt[1]);
    printf("memory address: %p\n", pt);
    return 0;
}
