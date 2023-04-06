#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


/* int max (int a, int b) {
    return (a > b) ? a : b;
}

int min(int a, int b) {
    return (a < b) ? a : b;
} */

void add(char* a, char* b, char* result) {
    int carry = 0;
    int len_a = strlen(a);
    int len_b = strlen(b);
    int len_result = max(len_a, len_b);

    for (int i = 0; i < len_result; i++) {
        int num_a = i < len_a ? a[len_a - 1 - i] - '0' : 0;
        int num_b = i < len_b ? b[len_b - 1 - i] - '0' : 0;
        int sum = num_a + num_b + carry;
        result[len_result - 1 - i] = (sum % 10) + '0';
        carry = sum / 10;
    }

    if (carry != 0) {
        result[0] = carry + '0';
    }
}

void subtract(char* a, char* b, char* result) {
    int borrow = 0;
    int len_a = strlen(a);
    int len_b = strlen(b);
    int len_result = max(len_a, len_b);

    for (int i = 0; i < len_result; i++) {
        int num_a = i < len_a ? a[len_a - 1 - i] - '0' : 0;
        int num_b = i < len_b ? b[len_b - 1 - i] - '0' : 0;
        int diff = num_a - num_b - borrow;
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        result[len_result - 1 - i] = diff + '0';
    }

    // Remove leading zeros from the result
    int i = 0;
    while (result[i] == '0' && i < len_result - 1) {
        i++;
    }
    memmove(result, result + i, len_result - i + 1);
}

void karatsuba(char* x, char* y, char* result) {
    int len_x = strlen(x);
    int len_y = strlen(y);

    // If either of the input numbers is zero, the result is zero
    if (len_x == 0 || len_y == 0) {
        result[0] = '0';
        result[1] = '\0';
        return;
    }

    // If either of the input numbers is one digit long, use the normal multiplication algorithm
    if (len_x == 1 || len_y == 1) {
        int a = atoi(x);
        int b = atoi(y);
        int prod = a * b;
        sprintf(result, "%d", prod);
        return;
    }

    // Split x and y into two parts
    int mid_x = len_x / 2;
    int mid_y = len_y / 2;

    char* a = (char*)malloc(mid_x + 1);
    char* b = (char*)malloc(len_x - mid_x + 1);
    char* c = (char*)malloc(mid_y + 1);
    char* d = (char*)malloc(len_y - mid_y + 1);

}

int main () {
    char result[100];
    karatsuba("78927263", "82736487", result);
    return 0;
}