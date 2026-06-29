#include<stdio.h>
#include<stdlib.h>

struct stack
{
    int size;
    int top;
    int *arr;
};

struct stack *sp;

void create(int n)
{
    sp = (struct stack*)malloc(sizeof(struct stack));
    sp->size = n;
    sp->top = -1;
    sp->arr = (int*)malloc(n * sizeof(int));
}

void push(int value)
{
    if(sp->top == sp->size - 1)
    {
        printf("Stack Overflow\n");
        return;
    }

    sp->top++;
    sp->arr[sp->top] = value;
}

int pop()
{
    if(sp->top == -1)
    {
        printf("Stack Underflow\n");
        return -1;
    }

    return sp->arr[sp->top--];
}

void display(int arr[], int n)
{
    printf("List Elements: ");
    for(int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main()
{
    int n, arr[100];

    printf("Enter number of elements in list: ");
    scanf("%d", &n);

    create(n);

    printf("Enter list elements:\n");
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        push(arr[i]);
    }

    printf("Original List:\n");
    display(arr, n);

    for(int i = 0; i < n; i++)
    {
        arr[i] = pop();
    }

    printf("Reversed List:\n");
    display(arr, n);

    return 0;
}