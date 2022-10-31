#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 5

struct customers
{
    char code;
    int count;
};

struct Queue
{
    int front, rear, size;
    unsigned capacity;
    struct customers *array;
};

struct Queue *creatQueue(unsigned capacity)
{
    struct Queue *queue = (struct Queue *)malloc(sizeof(struct Queue));

    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = -1;
    queue->array = (struct customers *)malloc(queue->capacity * sizeof(struct customers));

    return queue;
}

int isEmpty(struct Queue *queue)
{
    return queue->size == 0;
}

int isFull(struct Queue *queue)
{
    return queue->size == queue->capacity;
}

int size(struct Queue *queue)
{
    return queue->size;
}

void enqueue(struct Queue *queue, struct customers *customer)
{
    //check code confrontation
    int flag = 0;
    for (int i = queue->front; i <= queue->rear; i++)
    {
        if (queue->array[i].code == customer->code)
        {
            flag = 1;
        }
    }

    if (!isFull(queue) && !flag)
    {
        queue->rear = (queue->rear + 1) % 5;
        queue->array[queue->rear] = *customer;
        queue->size++;
    }
}

void dequeue(struct Queue *queue)
{
    if (!isEmpty(queue))
    {
        queue->array[queue->front];
        queue->front = (queue->front + 1) % 5;
        queue->size--;
    }
}

int main()
{
    struct Queue *queue = creatQueue(MAX_SIZE);

    int input;
    while (1)
    {
        scanf("%d", &input);
        if (input == -1)
        {
            break;
        }
        else if (input == 1)
        {
            struct customers customer;
            scanf(" %c %d", &customer.code, &customer.count);
            enqueue(queue, &customer);
        }
        else if (input == 2)
        {
            int headCount = 0;
            for (int i = queue->front; i <= queue->rear; i++)
            {
                headCount += queue->array[i].count;
            }
            printf("%d\n", headCount);
        }
        else if (input == 3)
        {
            printf("%c\n", queue->array[queue->front].code);
        }
        else if (input == 4)
        {
            dequeue(queue);
        }
        else
        {
            printf("error\n");
        }
    }
}
