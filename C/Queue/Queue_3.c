#include<stdio.h>
#include<stdlib.h>

struct Circular_Queue
{
    int size;
    int front;
    int rear;
    int *arr;
};

void circular_enqueue(struct Circular_Queue *q, int value)
{
    if((q->rear + 1) % q->size == q->front)
    {
        printf("Queue is full\n");
        return;
    }

    q->rear = (q->rear + 1) % q->size;
    q->arr[q->rear] = value;

    printf("Enqueued element: %d\n", value);
}

void circular_dequeue(struct Circular_Queue *q)
{
    if(q->front == q->rear)
    {
        printf("Queue is empty\n");
        return;
    }

    q->front = (q->front + 1) % q->size;

    printf("Dequeued element: %d\n", q->arr[q->front]);
}

void circular_display(struct Circular_Queue *q)
{
    if(q->front == q->rear)
    {
        printf("Queue is empty\n");
        return;
    }

    printf("Queue elements: ");

    for(int i = (q->front + 1) % q->size;
        i != (q->rear + 1) % q->size;
        i = (i + 1) % q->size)
    {
        printf("%d ", q->arr[i]);
    }

    printf("\n");
}

int main()
{
    struct Circular_Queue *q = (struct Circular_Queue*)malloc(sizeof(struct Circular_Queue));

    printf("Enter size of queue: ");
    scanf("%d", &q->size);

    q->front = q->rear = 0;

    q->arr = (int*)malloc(q->size * sizeof(int));

    while(1)
    {
        int choice, value;

        printf("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                circular_enqueue(q, value);
                break;

            case 2:
                circular_dequeue(q);
                break;

            case 3:
                circular_display(q);
                break;

            case 4:
                free(q->arr);
                free(q);
                exit(0);

            default:
                printf("Invalid choice\n");
        }
    }
}