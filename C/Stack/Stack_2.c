#include<stdio.h>
#include<stdlib.h>

void insert(int value, int arr[], int *n, int pos)
{
    if(pos < 1 || pos > *n + 1)
    {
        printf("Invalid position\n");
        return;
    }

    for(int i = *n; i >= pos; i--)
    {
        arr[i] = arr[i - 1];
    }

    arr[pos - 1] = value;
    (*n)++;

    printf("Inserted value: %d at position %d\n", value, pos);
}

void delete(int arr[], int *n, int pos)
{
    if(pos < 1 || pos > *n)
    {
        printf("Invalid position\n");
        return;
    }

    int deleteValue = arr[pos - 1];

    for(int i = pos - 1; i < *n - 1; i++)
    {
        arr[i] = arr[i + 1];
    }

    (*n)--;

    printf("Deleted value: %d from position %d\n", deleteValue, pos);
}

void display(int arr[], int n)
{
    printf("Array Elements: ");

    for(int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");
}

int main()
{
    int arr[100], n, pos, choice, value;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter array elements:\n");
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    while(1)
    {
        printf("\n1.Insert\n2.Delete\n3.Display\n4.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);

                printf("Enter position: ");
                scanf("%d", &pos);

                insert(value, arr, &n, pos);
                break;

            case 2:
                printf("Enter position: ");
                scanf("%d", &pos);

                delete(arr, &n, pos);
                break;

            case 3:
                display(arr, n);
                break;

            case 4:
                exit(0);

            default:
                printf("Invalid choice\n");
        }
    }
}