#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head = NULL;

/* Insertion at Specific Position */
void insert_pos(int pos, int value)
{
    struct node *newnode, *temp;

    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;

    if(pos == 1)
    {
        newnode->next = head;
        head = newnode;

        printf("%d inserted at position %d\n", value, pos);
        return;
    }

    temp = head;

    for(int i = 1; i < pos - 1 && temp != NULL; i++)
    {
        temp = temp->next;
    }

    if(temp == NULL)
    {
        printf("Invalid Position\n");
        free(newnode);
        return;
    }

    newnode->next = temp->next;
    temp->next = newnode;

    printf("%d inserted at position %d\n", value, pos);
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
    int choice, pos, value, n;

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
        printf("\n--- Singly Linked List Menu ---\n");
        printf("1. Insert at Specific Position\n");
        printf("2. Delete from End\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter position: ");
                scanf("%d", &pos);

                printf("Enter value: ");
                scanf("%d", &value);

                insert_pos(pos, value);
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

    return 0;
}