#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

void printList(struct node *nodePtr)
{
    printf("%d\n", nodePtr->data);
    if (nodePtr->next)
    {
        printList(nodePtr->next);
    }
}

void push(struct node *nodePtr);
{
    struct node *current = nodePtr;
    while ()
}

int main (){
    struct node headPtr, headNode;
    headPtr = &headNode;
    struct node *secondNode;
    headNode.data = 1;
    headNode.next = secondNode;
    secondNode->data = 2;
    secondNode->next = NULL;
    printList(headPtr);
    return 0;
}
