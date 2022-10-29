#include <stdio.h>
#include <stdlib.h>
int main(){
    char strBuffer[100];
    printf("Enter string: ");
    scanf("%100s", strBuffer);
    printf("%s\n", strBuffer);
    return 0;
}
