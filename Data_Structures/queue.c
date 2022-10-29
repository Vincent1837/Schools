#include <stdio.h>
#include <stdlib.h>

struct Queue {
    int front, rear, size;
    unsigned capacity;
    int* array;
};

struct Queue* creatQueue (unsigned capacity) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->capacity = capacity;
	queue->front = queue->size = 0;
    queue->rear = queue->size - 1;
    queue->array = (int*)malloc(queue->capacity * sizeof(int));

    return queue;
}

int isEmpty (struct Queue* queue) {
    return queue->size == 0;
}
    
int isFull (struct Queue* queue) {
    return queue->size == queue->capacity;
}

int size (struct Queue* queue) {
    return queue->size;
}

int front (struct Queue* queue) {
    return queue->array[queue->front];
}

int rear (struct Queue* queue) {
    return queue->array[queue->rear];
}

void enqueue (struct Queue* queue, int n) {
    if (isFull(queue)) {
        printf("Overflow!!!! Program terminated.\n");
        exit(EXIT_FAILURE);
    } else {
        queue->array[++queue->rear] = n;
        queue->size++;
    }
}

int dequeue (struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Underflow!!!! Program terminated.\n");
        exit(EXIT_FAILURE);
    } else {
        return queue->array[queue->front++];
        queue->size--;
    }
}

void printQueue (struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("queue is empty!");
        return;
    } else {
        printf("Queue: [");
        for (int i = queue->front; i < queue->size; i++) {
            printf(" %d ", queue->array[i]);
        }
        printf("]\n");
    }
}

int main() {

    struct Queue* queue = creatQueue(100);

    enqueue(queue, 5);
    enqueue(queue, 6);
    enqueue(queue, 9);
    enqueue(queue, 13);

    dequeue(queue);
    dequeue(queue);

    printQueue(queue);


    return 0;
}
