#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *prev;
    struct node *next;
};

struct node *front = NULL;
struct node *rear = NULL;

/* Enqueue at Rear */
void enqueue_rear(int value)
{
    struct node *newnode;

    newnode = (struct node*)malloc(sizeof(struct node));

    newnode->data = value;
    newnode->prev = NULL;
    newnode->next = NULL;

    if(front == NULL)
    {
        front = rear = newnode;
    }
    else
    {
        rear->next = newnode;
        newnode->prev = rear;
        rear = newnode;
    }

    printf("%d inserted at rear\n", value);
}

/* Dequeue from Rear */
void dequeue_rear()
{
    struct node *temp;

    if(rear == NULL)
    {
        printf("Queue is Empty\n");
        return;
    }

    temp = rear;

    if(front == rear)
    {
        front = rear = NULL;
    }
    else
    {
        rear = rear->prev;
        rear->next = NULL;
    }

    printf("%d deleted from rear\n", temp->data);
    free(temp);
}

/* Dequeue from Front */
void dequeue_front()
{
    struct node *temp;

    if(front == NULL)
    {
        printf("Queue is Empty\n");
        return;
    }

    temp = front;

    if(front == rear)
    {
        front = rear = NULL;
    }
    else
    {
        front = front->next;
        front->prev = NULL;
    }

    printf("%d deleted from front\n", temp->data);
    free(temp);
}

/* Display Queue */
void display()
{
    struct node *temp;

    if(front == NULL)
    {
        printf("Queue is Empty\n");
        return;
    }

    temp = front;

    printf("Queue Elements: ");

    while(temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    printf("\n");
}

int main()
{
    int choice, value;

    while(1)
    {
        printf("\n--- Input Restricted Deque Menu ---\n");
        printf("1. Enqueue Rear\n");
        printf("2. Dequeue Rear\n");
        printf("3. Dequeue Front\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                enqueue_rear(value);
                break;

            case 2:
                dequeue_rear();
                break;

            case 3:
                dequeue_front();
                break;

            case 4:
                display();
                break;

            case 5:
                exit(0);

            default:
                printf("Invalid Choice\n");
        }
    }

    return 0;
}