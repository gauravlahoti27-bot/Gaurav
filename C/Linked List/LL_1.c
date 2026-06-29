#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};
struct node *head = NULL;

void insert(int value){
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = value;
    new_node->next = head;
    head = new_node;
    printf("Insertion at beginning: %d\n", value);
}
void delete(int pos)
{
    if(head == NULL)
    {
        printf("List is empty\n");
        return;
    }

    struct node *temp, *ptr;

    if(pos == 1)
    {
        temp = head;
        head = head->next;

        printf("Deleted element: %d\n", temp->data);
        free(temp);
        return;
    }

    temp = head;

    for(int i = 1; i < pos - 1 && temp != NULL; i++)
    {
        temp = temp->next;
    }

    if(temp == NULL || temp->next == NULL)
    {
        printf("Position out of bounds\n");
        return;
    }

    ptr = temp->next;
    temp->next = ptr->next;

    printf("Deleted element: %d\n", ptr->data);
    free(ptr);
}

void display(){
    struct node *temp = head;
    if(temp == NULL){
        printf("List is empty\n");
        return;
    }
    printf("List elements: ");
    while(temp != NULL){
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
int main()
{
    int n, value, choice, pos;

    printf("Enter number of elements to insert: ");
    scanf("%d", &n);

    /* Initial creation of list without printing insertion message */
    for(int i = 0; i < n; i++)
    {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &value);

        struct node *new_node = (struct node*)malloc(sizeof(struct node));
        new_node->data = value;
        new_node->next = head;
        head = new_node;
    }

    while(1)
    {
        printf("\n1. Insert at Beginning");
        printf("\n2. Delete at Position");
        printf("\n3. Display");
        printf("\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(value);
                break;

            case 2:
                printf("Enter position to delete: ");
                scanf("%d", &pos);
                delete(pos);
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