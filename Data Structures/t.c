#include <stdio.h>


int main(){
    int input;
    while (scanf("%d", &input)) {
	if (input == -1) {
	    return -1;
	} else {
	    printf("%d\n", input);
	}
    }
    return 0;
}


