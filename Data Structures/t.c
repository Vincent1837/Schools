#include <stdio.h>

bool isZero (int number) {
    return number == 0;
}

int main()
{
    bool a = isZero(2);
    bool b = isZero(0);
    printf("%b, %b", a, b);
    return 0;
}


