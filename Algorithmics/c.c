#include <stdio.h>
#include <stdlib.h>
#include <types.h>
#include <wait.h>
#include <unistd.h>

int main(){
    int status;
    printf("A");
    if (fork() != 0) {
        waitpid(-1, &status, 0);
        printf("B");
    } else {
        printf("C");
    }
    printf("D");
    return 0;
}

