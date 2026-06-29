#include<stdio.h>
#include<stdlib.h>

struct queue{
    int size;
    int front;
    int rear;
    int *arr;
};
void enqueue(struct queue *q, int value)
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

void dequeue(struct queue *q)
{
    if(q->front == q->rear)
    {
        printf("Queue is empty\n");
        return;
    }
    else{
    q->front++;
    int a = q->arr[q->front];
    }
    printf("Dequeued element: %d\n", q->arr[q->front]);
}

int isEmpty(struct queue *q)
{
    return q->front == q->rear;
}

int isFull(struct queue *q)
{
    return (q->rear + 1) % q->size == q->front;
}

void display(struct queue *q)
{
    if(q->front == q->rear)
    {
        printf("Queue is empty\n");
        return;
    }
    int i = (q->front + 1) % q->size;
    while(i != (q->rear + 1) % q->size)
    {
        printf("%d ", q->arr[i]);
        i = (i + 1) % q->size;
    }
    printf("\n");
}

int main(){
    struct queue *q;
    q = (struct queue*)malloc(sizeof(struct queue));
    q->size = 100;
    q->front = q->rear = 0;
    q->arr = (int*)malloc(q->size*sizeof(int));
    while(1)
    {
        int choice, value;
        printf("1. Enqueue\n2. Dequeue\n3. Display\n4. isEmpty\n5. isFull\n6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1:
                printf("Enter the value to enqueue: ");
                scanf("%d", &value);
                enqueue(q, value);
                break;
            case 2:
                dequeue(q);
                break;
            case 3:
                display(q);
                break;
            case 4:
                if(isEmpty(q))
                    printf("Queue is empty\n");
                else
                    printf("Queue is not empty\n");
                break;
            case 5:
                if(isFull(q))
                    printf("Queue is full\n");
                else
                    printf("Queue is not full\n");
                break;
            case 6:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
}