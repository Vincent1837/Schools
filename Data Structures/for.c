#include <stdio.h>
#include <stdlib.h>
int main(){
    int nums[] = {1, 3, 6, 9};
    for (int i : nums)
    {
        printf("%d", i);
    }
    return 0;
}
