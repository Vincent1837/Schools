#include <stdio.h>
#include <stdlib.h>
int main(){
    double arr[2] = {11.0, 23.0};
    printf("Element \t Value \t Address \n");
    int i;
    for (i = 0; i < 2; i++) 
    {
        printf("arr[%d]\t\t %.2lf \t %p \n", i, arr[i], arr+i);
    }
    printf("i \t\t %d \n", i);
    printf("arr \t\t\t\t %p \n", arr);
    printf("arr+1 \t\t\t\t %p \n", (arr+1));
    printf("arr+2 \t\t\t\t %p \n", (arr+i));
    return 0;

}
