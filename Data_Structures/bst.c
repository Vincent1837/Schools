#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left, *right;
};

struct node *getNode (int data) {
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = data;
    temp->left = temp->right = NULL;
    printf("%d",data);
    return temp;
}

void insert (struct node *node, int data) {
    if (node == NULL) {
        node = getNode(data);
    printf("test\n");
    return;
    }

    if (data < node->data) {
        insert(node->left, data);
    } else {
        insert(node->right, data);
    }

}

void inorder (struct node *node) {
    if (node != NULL) {
        inorder(node->left);
        printf("%d ", node->data);
        inorder(node->right);
    }
}

void preorder (struct node *node) {
    if (node != NULL) {
        printf("%d ", node->data);
        preorder(node->left);
        preorder(node->right);
    }
}

void postorder (struct node *node) {
    if (node != NULL) {
        postorder(node->left);
        postorder(node->right);
        printf("%d ", node->data);
    }
}

int main () {
    while (1) {
        struct node *tree = NULL; // construct the tree
        
        insert(tree, 3);

    printf("data65555555\n");
        insert(tree, 4);
        insert(tree, 7);
        insert(tree, 2);

        /* int input = 0;
        scanf("%d", &input);
        if (input == -1) {
            break;
        }

        for (int i = 0; i < input; i++) {
            int data;
            scanf("%d", &data);
            insert(tree, data);
        } */

        printf("Preorder: ");
        preorder(tree);
        printf("\n");
        printf("Inorder: ");
        inorder(tree);
        printf("\n");
        printf("Postorder: ");
        postorder(tree);
        printf("\n");
    }

    return 0;
}