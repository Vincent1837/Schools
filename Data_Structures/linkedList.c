#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node* get_node (int data) {
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

void printList(struct node *nodePtr)
{
    printf("%d\n", nodePtr->data);
    if (nodePtr->next)
    {
        printList(nodePtr->next);
    }
}



int main (){
    struct node *headptr = get_node(3);
    headptr->next = get_node(5);
    headptr->next->next = get_node(6);

    printList(headptr);
}
