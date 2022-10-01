#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int size;
    int top;
    int *items;
};

struct stack* newStack (int capacity)
{
    struct stack *pt = (struct stack*)malloc(sizeof(struct stack));
    pt->size = capacity;
    pt->top = -1;
    pt->items = (int*)malloc(sizeof(int) * capacity);

    return pt;
}

int size (struct stack *pt)
{
    return pt->top + 1;
}



int main(){
    
    return 0;
}
