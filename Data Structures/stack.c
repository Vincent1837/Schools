#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct stack {
    int maxSize;
    int top;
    char *items;
};

struct stack* newStack (int capacity) {
    struct stack *pt = (struct stack*)malloc(sizeof(struct stack));
    pt->maxSize = capacity;
    pt->top = -1;
    pt->items = (char*)malloc(sizeof(int) * capacity);

    return pt;
}

int size (struct stack *pt) {
    return pt->top + 1;
}

int isFull (struct stack *pt) {
    return pt->top == pt->maxSize - 1;  
}

int isEmpty (struct stack *pt) {
    return pt->top == -1;
}

void push (struct stack *pt, char c) {
    if (isFull(pt)) {
        printf("Overflow\nProgram Terminated\n");
        exit(EXIT_FAILURE);
    }
    pt->items[++pt->top] = c;
}

char peek (struct stack *pt) {
    if (!isEmpty(pt)) {
        return pt->items[pt->top];
    } else {
        exit(EXIT_FAILURE);
    }
}

char pop (struct stack *pt) {
    if (isEmpty(pt)) {
        printf("Underflow\nProgram Terminated\n");
        exit(EXIT_FAILURE);
    }
    return pt->items[pt->top--];
}

int getPriority (char c) {
    if (c == '+' || c == '-') {
        return 1;
    } else if (c == '*' || c == '/') {
        return 2;
    }
    return 0;
}

int main() {

    struct stack *operatorStack = newStack(50);
    push(operatorStack, 'b'); // bottom of the stack
    char infixStr[50];
    scanf("%s", infixStr);
    int length = (int)strlen(infixStr);
    struct stack *prefixStack = newStack(50);
    char prefixStr[length];
    push(prefixStack, '\0');

    // Reverse the string
    char reversedStr[length];
    for (int i = 0; i < length; i++) {
        reversedStr[i] = infixStr[length - i - 1];
    }
    for (int i = 0; i < length; i++) {
        infixStr[i] = reversedStr[i];
    }
    
    // infix to postfix
    for (int i = 0; i < length; i++) {
        if (infixStr[i] >= '0' && infixStr[i] <= '9') {
            push(prefixStack, infixStr[i]);
        } else {
            while (getPriority(infixStr[i]) < getPriority(peek(operatorStack))) {
                push(prefixStack, pop(operatorStack));
            }
            push(operatorStack, infixStr[i]);
        }
    }


    while (!isEmpty(operatorStack)) {
        push(prefixStack, pop(operatorStack));
	if (size(operatorStack) == 1) {
    	pop(operatorStack); // pop('b')
	}
    }

    // prefixStack -> prefixStr
    int loopCount = 0;
    while (!isEmpty(prefixStack)) {
	prefixStr[loopCount++] = pop(prefixStack);
    }

    printf("%s\n", prefixStr);

    return 0;
}
