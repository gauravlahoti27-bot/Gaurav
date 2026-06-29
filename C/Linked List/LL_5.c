#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head = NULL;

/* Insert at End (for creating list) */
void insert(int value)
{
    struct node *newnode, *temp;

    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;

    if(head == NULL)
    {
        head = newnode;
    }
    else
    {
        temp = head;
        while(temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newnode;
    }
}

/* Search Element */
void search(int key)
{
    struct node *temp = head;
    int pos = 1;

    while(temp != NULL)
    {
        if(temp->data == key)
        {
            printf("Element %d found at position %d\n", key, pos);
            return;
        }

        temp = temp->next;
        pos++;
    }

    printf("Element not found\n");
}

/* Count Nodes */
void count_nodes()
{
    struct node *temp = head;
    int count = 0;

    while(temp != NULL)
    {
        count++;
        temp = temp->next;
    }

    printf("Number of nodes = %d\n", count);
}

/* Display List */
void display()
{
    struct node *temp = head;

    if(head == NULL)
    {
        printf("List is Empty\n");
        return;
    }

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
    int n, value, choice, key;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    for(int i = 0; i < n; i++)
    {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &value);
        insert(value);
    }

    while(1)
    {
        printf("\n1. Search for an Element");
        printf("\n2. Count Number of Nodes");
        printf("\n3. Display");
        printf("\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter element to search: ");
                scanf("%d", &key);
                search(key);
                break;

            case 2:
                count_nodes();
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