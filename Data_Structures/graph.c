#include <stdio.h>

struct node {
    int V;
    
};


int main(){
    int graph[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) {
        printf("%d\n", graph[i]);
    }
    return 0;
}