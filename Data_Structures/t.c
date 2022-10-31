#include <stdio.h>

struct t
{
    int number;
    char character;
};

void scanStruct()
{
    struct t st;
    scanf("%d %c", &st.number, &st.character);
    printf("%d %c\n", st.number, st.character);
}

int main(){
    int flag = 3 == 3;
    printf("%d\n", flag);
}


