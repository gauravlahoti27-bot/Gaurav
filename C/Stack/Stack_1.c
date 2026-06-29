#include<stdio.h>
#include<stdlib.h>

struct stack{
    int size;
    int top;
    int *s;
};

struct stack *sp;

void create(){
    sp = (struct stack*)malloc(sizeof(struct stack));

    printf("Enter the size of stack: ");
    scanf("%d",&sp->size);

    sp->top = -1;
    sp->s = (int*)malloc(sp->size * sizeof(int));
}

void push(int value){
    if(sp->top == sp->size - 1){
        printf("Stack Overflow\n");
    }
    else{
        sp->top++;
        sp->s[sp->top] = value;
        printf("Pushed value: %d\n", value);
    }
}

void pop(){
    if(sp->top == -1){
        printf("Stack Underflow\n");
    }
    else{
        int value = sp->s[sp->top];
        sp->top--;
        printf("Popped value: %d\n", value);
    }
}

void isEmpty(){
    if(sp->top == -1){
        printf("Stack is empty\n");
    }
    else{
        printf("Stack is not empty\n");
    }
}

void peek(){
    if(sp->top == -1){
        printf("Stack is empty\n");
    }
    else{
        printf("Top element: %d\n", sp->s[sp->top]);
    }
}

void isFull(){
    if(sp->top == sp->size -1){
        printf("Stack is full\n");
    }
    else{
        printf("Stack is not full\n");
    }
}

void display(){
    if(sp->top == -1){
        printf("Stack is empty\n");
    }
    else{
        printf("Stack elements: ");
        for(int i = sp->top; i >= 0; i--){
            printf("%d ", sp->s[i]);
        }
        printf("\n");
    }
}

int main(){
    int choice, value;

    create();   

    while(1){
        printf("\n1. Push\n2. Pop\n3. Display\n4. Is Empty\n5. Is Full\n6. Peek\n7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d",&choice);

        switch(choice){
            case 1:
                printf("Enter value to push: ");
                scanf("%d",&value);
                push(value);
                break;

            case 2:
                pop();
                break;

            case 3:
                display();
                break;

            case 4:
                isEmpty();
                break;

            case 5:
                isFull();
                break;

            case 6:
                peek();
                break;
            case 7:
                free(sp->s);
                free(sp);
                printf("Exiting...\n");
                exit(0);
                break;

            default:
                printf("Invalid Choice\n");
        }
    }
}