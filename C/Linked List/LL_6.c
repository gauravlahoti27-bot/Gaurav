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

/* Deletion from End */
void delete_end()
{
    struct node *temp, *prev;

    if(head == NULL)
    {
        printf("List is Empty\n");
        return;
    }

    /* Only one node */
    if(head->next == NULL)
    {
        printf("%d deleted from end\n", head->data);
        free(head);
        head = NULL;
        return;
    }

    temp = head;
    prev = NULL;

    while(temp->next != NULL)
    {
        prev = temp;
        temp = temp->next;
    }

    prev->next = NULL;

    printf("%d deleted from end\n", temp->data);

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

    /* Initial creation without printing */
    for(int i = 0; i < n; i++)
    {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &value);

        struct node *newnode =(struct node*)malloc(sizeof(struct node));

        newnode->data = value;
        newnode->next = head;
        head = newnode;
    }

    while(1)
    {
        printf("\n1. Insert at Beginning");
        printf("\n2. Delete from End");
        printf("\n3. Display");
        printf("\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                insert_begin(value);
                break;

            case 2:
                delete_end();
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
}