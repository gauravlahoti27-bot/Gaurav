#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head = NULL;

/* Insertion at Beginning */
void insert_begin(int value)
{
    struct node *newnode;

    newnode = (struct node*)malloc(sizeof(struct node));

    if(newnode == NULL)
    {
        printf("Memory Allocation Failed\n");
        return;
    }

    newnode->data = value;
    newnode->next = head;
    head = newnode;

    printf("%d inserted at beginning\n", value);
}

/* Deletion from Beginning */
void delete_begin()
{
    struct node *temp;

    if(head == NULL)
    {
        printf("List is Empty\n");
        return;
    }

    temp = head;
    head = head->next;

    printf("%d deleted from beginning\n", temp->data);

    free(temp);
}

/* Display List */
void display()
{
    struct node *temp;

    if(head == NULL)
    {
        printf("List is Empty\n");
        return;
    }

    temp = head;

    printf("Linked List: ");

    while(temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    printf("\n");
}

int main()
{
    int choice, value, n;

    printf("Enter number of elements to insert: ");
    scanf("%d", &n);

    /* Initial creation without printing message */
    for(int i = 0; i < n; i++)
    {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &value);

        struct node *newnode =
        (struct node*)malloc(sizeof(struct node));

        newnode->data = value;
        newnode->next = head;
        head = newnode;
    }

    while(1)
    {
        printf("\n--- Singly Linked List Menu ---\n");
        printf("1. Insert at Beginning\n");
        printf("2. Delete from Beginning\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                insert_begin(value);
                break;

            case 2:
                delete_begin();
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
