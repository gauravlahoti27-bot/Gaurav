#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next; 
};
struct node *head = NULL;

void insert(int key, int value)
{
    struct node *new_node, *temp;

    temp = head;

    while(temp != NULL && temp->data != key)
    {
        temp = temp->next;
    }

    if(temp == NULL)
    {
        printf("Element not found\n");
        return;
    }

    new_node = (struct node*)malloc(sizeof(struct node));

    new_node->data = value;
    new_node->next = temp->next;
    temp->next = new_node;

    printf("Inserted %d after %d\n", value, key);
}
void delete(){
    if(head == NULL)
    {
        printf("List is empty\n");
        return;
    }
    else{
        struct node *temp = head;
        head = head->next;
        printf("Deleted element: %d\n", temp->data);
        free(temp);
    }
}

void display(){
    struct node *temp = head;
    if(temp == NULL){
        printf("List is empty\n");
        return;
    }
    else{
        while(temp != NULL){
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main()
{
    int n, value, choice, key;

    printf("Enter number of elements to insert: ");
    scanf("%d", &n);

    /* Initial creation of list */
    for(int i = 0; i < n; i++)
    {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &value);

        /* Insert without printing message */
        struct node *new_node = (struct node*)malloc(sizeof(struct node));
        new_node->data = value;
        new_node->next = NULL;

        if(head == NULL)
        {
            head = new_node;
        }
        else
        {
            struct node *temp = head;
            while(temp->next != NULL)
            {
                temp = temp->next;
            }
            temp->next = new_node;
        }
    }


    while(1)
    {
        printf("\n1. Insert after Element");
        printf("\n2. Delete from Beginning");
        printf("\n3. Display");
        printf("\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter element to insert after: ");
                scanf("%d", &value);
                printf("Enter value to insert: ");
                scanf("%d", &key);
                insert(value, key);
                break;

            case 2:
                delete();
                break;

            case 3:
                display();
                break;

            case 4:
                exit(0);

            default:
                printf("Invalid choice\n");
        }
    }
}