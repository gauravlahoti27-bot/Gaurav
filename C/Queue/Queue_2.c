#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};
struct node *front = NULL, *rear = NULL;
    
void enqueue(int value){
    struct node *newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data = value;
    newNode->next = NULL;

    if(rear == NULL){
        front = rear = newNode;
    }
    else{
        rear->next = newNode;
        rear = newNode;
    }
    printf("Enqueued element: %d\n", value);
}

void dequeue(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }
    struct node *temp = front;
    front = front->next;

    if(front == NULL){
        rear = NULL;
    }
    printf("Dequeued element: %d\n", temp->data);
    free(temp);
}

void display(){
    if(front == NULL){
        printf("Queue is empty\n");
        return;
    }
    else{
        struct node *temp = front;
        printf("Queue elements: ");
        while(temp != NULL){
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main(){
    int choice, value;
    while(1){
        printf("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d",&choice);

        switch(choice){
            case 1:
                printf("Enter value to enqueue: ");
                scanf("%d",&value);
                enqueue(value);
                break;

            case 2:
                dequeue();
                break;

            case 3:
                display();
                break;

            case 4:
                exit(0);
                break;

            default:
                printf("Invalid choice\n");
        }
    }
}