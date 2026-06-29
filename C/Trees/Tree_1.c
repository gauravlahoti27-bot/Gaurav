#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *left;
    struct node *right;
};
struct node *root = NULL;

struct node* create_node(int value)
{
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = value;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

struct node *insert(struct node *root , int value)
{
    if(root == NULL){
        return create_node(value);
    }
    else{
        if(value < root->data){
            root->left = insert(root->left, value);
        }
        else if(value > root->data){
            root->right = insert(root->right, value);
        }
    }
    return root;
}

int preorder(struct node *root){
    if(root != NULL){
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }   
}

int height(struct node *root){
    if(root == NULL){
        return -1;
    }
    else{
        int left_height = height(root->left);
        int right_height = height(root->right);
        if(left_height > right_height){
            return left_height + 1;
        }
        else{
            return right_height + 1;
        }       
    }
}

int main()
{
    int choice, value;

    while(1)
    {
        printf("\n--- BST Menu ---\n");
        printf("1. Insertion\n");
        printf("2. Preorder Traversal\n");
        printf("3. Height of Tree\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                root = insert(root, value);
                break;

            case 2:
                printf("Preorder Traversal: ");
                preorder(root);
                printf("\n");
                break;

            case 3:
                printf("Height of Tree = %d\n", height(root));
                break;

            case 4:
                exit(0);

            default:
                printf("Invalid Choice\n");
        }
    }

    return 0;
}