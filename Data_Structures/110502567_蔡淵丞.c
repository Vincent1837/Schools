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
    return temp;
}

struct node *insert (struct node *node, int data) {
    if (node == NULL) {
        return getNode(data);
    }

    if (data < node->data) {
        node->left = insert(node->left, data);
    } else {
        node->right = insert(node->right, data);
    }
    return node;
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
        
        int input = 0;
        scanf("%d", &input);
        if (input == -1) {
            break;
        }

        for (int i = 0; i < input; i++) {
            int data;
            scanf("%d", &data);
            tree = insert(tree, data);
        }
        insert(tree, 5);
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