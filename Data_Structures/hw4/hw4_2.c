#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void bubble_sort(int array[], int size) {
    int temp;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - 1; j++) {
        if (array[j] > array[j + 1]) {
            temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
        }
        }
    }
}

int partition(int array[], int low, int high) {
    int pivot = array[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (array[j] <= pivot) {
        i++;
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        }
    }
    int temp = array[i + 1];
    array[i + 1] = array[high];
    array[high] = temp;
    return i + 1;
}

void quick_sort(int array[], int low, int high) {
    if (low < high) {
        int pivot = partition(array, low, high);
        quick_sort(array, low, pivot - 1);
        quick_sort(array, pivot + 1, high);
    }
}


int main() {

    while (1) {
        int array_size;
        scanf("%d", &array_size);
        if (array_size == -1) {
            return 0;
        }

        int array[array_size];
        for (int i = 0; i < array_size; i++) {
            scanf("%d", &array[i]);
        }

        clock_t start, end;

        start = clock();
        bubble_sort(array, array_size);
        end = clock();
        double bubble_sort_time = (double)(end - start) / CLOCKS_PER_SEC;

        start = clock();
        quick_sort(array, 0, array_size - 1);
        end = clock();
        double quick_sort_time = (double)(end - start) / CLOCKS_PER_SEC;


        for (int i = 0; i < array_size; i++) {
            printf("%d ", array[i]);
        }
        printf("\n");
        printf("bubble sort : %f sec\n", bubble_sort_time);
        printf("quick sort : %f sec\n", quick_sort_time);

    }

    return 0;
    }
