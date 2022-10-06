#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct stack
{
    int maxSize;
    int top;
    char *items;
};

struct stack* newStack (int capacity)
{
    struct stack *pt = (struct stack*)malloc(sizeof(struct stack));
    pt->maxSize = capacity;
    pt->top = -1;
    pt->items = (char*)malloc(sizeof(int) * capacity);

    return pt;
}

int size (struct stack *pt)
{
    return pt->top + 1;
}

int isFull (struct stack *pt)
{
    return pt->top == pt->maxSize - 1;  
}

int isEmpty (struct stack *pt)
{
    return pt->top == -1;
}

void push (struct stack *pt, char c)
{
    if (isFull(pt))
    {
        printf("Overflow\nProgram Terminated\n");
        exit(EXIT_FAILURE);
    }
    // printf("Inserting %.2f\n", f);
    pt->items[++pt->top] = c;
}

char peek (struct stack *pt)
{
    if (!isEmpty(pt))
    {
        return pt->items[pt->top];
    } else
    {
        exit(EXIT_FAILURE);
    }
}

char pop (struct stack *pt)
{
    if (isEmpty(pt))
    {
        printf("Underflow\nProgram Terminated\n");
        exit(EXIT_FAILURE);
    }
    // printf("Removing %.2f\n", peek(pt));
    return pt->items[pt->top--];
}

int main(){
    struct stack *pt = newStack(50);
    char infixStr[50];
    scanf("%s", infixStr);
    int length = (int)strlen(infixStr);

    // Reverse the string
    char reversedStr[length];
    char prefixStr[length];
    for (int i = 0; i < length; i++) {
        reversedStr[i] = infixStr[length - i - 1];
    }
    for (int i = 0; i < length; i++) {
        infixStr[i] = reversedStr[i];
    }


    return 0;
}
