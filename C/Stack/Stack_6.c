#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *top = NULL;

void push(int value)
{
    struct node *newnode;

    newnode = (struct node*)malloc(sizeof(struct node));

    if(newnode == NULL)
    {
        printf("Stack Overflow\n");
        return;
    }

    newnode->data = value;
    newnode->next = top;
    top = newnode;

    printf("%d pushed into stack\n", value);
}

void pop()
{
    struct node *temp;
    int value;

    if(top == NULL)
    {
        printf("Stack Underflow\n");
        return;
    }

    temp = top;
    value = top->data;
    top = top->next;

    free(temp);

    printf("%d popped from stack\n", value);
}

void display()
{
    struct node *ptr;

    if(top == NULL)
    {
        printf("Stack is Empty\n");
        return;
    }

    printf("Stack Elements are:\n");

    ptr = top;

    while(ptr != NULL)
    {
        printf("%d\n", ptr->data);
        ptr = ptr->next;
    }
}

int main()
{
    int choice, value;

    while(1)
    {
        printf("\n--- Stack Menu ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &value);
                push(value);
                break;

            case 2:
                pop();
                break;

            case 3:
                display();
                break;

            case 4:
                exit(0);

            default:
                printf("Invalid Choice\n");
        }
    }

    return 0;
}