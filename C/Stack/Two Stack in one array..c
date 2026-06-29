#include <stdio.h>
#include <stdlib.h>
#define MAXU  (~0)

const char * const menu="\n\tEnter 0 for check empty\n"
                     " \tEnter 1 Get size\n"
      "\tEnter 2 enqueue\n\tEnter 3 dequeue\n\t Enter 4 Peek\n"
     "\tAny other value for aborting\n\t Enter opcode: ";



typedef struct stack
{
    int * pile;
    unsigned maxnumofelements;
    unsigned top;
} stackobject;

stackobject stack1,stack2;


int isempty(stackobject *msp){
    if (msp->top==MAXU){
        return 1;
    }
    return 0;
}

unsigned getsize()
{
    unsigned size1 = 0;
    unsigned size2 = 0;

    if (!isempty(&stack1))
        size1 = stack1.top + 1;

    if (!isempty(&stack2))
        size2 = stack2.top + 1;

    return size1 + size2;
}

int isfull()
{
    return (getsize() == stack1.maxnumofelements);
}


void push(stackobject *msp,int value){
    if (msp->top == msp->maxnumofelements - 1) {
    printf("Stack overflow\n");
    return;
}

    if (msp->top==MAXU){
        msp->top=0;
    }
    else {
        msp->top+=1;
    }
    msp->pile[msp->top]=value;
}

int pop(stackobject *msp){
    int value;
    if (isempty(msp)) {
    printf("Stack underflow\n");
    return 0;
}
    value=msp->pile[msp->top];
    if (msp->top==0){
        msp->top=MAXU;
    }
    else {
        msp->top-=1;
    }

    return value;
}




void enqueue(int value){
    push(&stack1,value);
}

int dequeue(){
    int temp;
    if (isempty(&stack1) && isempty(&stack2)){
        printf("queue underflow");
        return 0;
    }
    if (isempty(&stack2)){
        while (!isempty(&stack1)){
            temp=pop(&stack1);
            push(&stack2,temp);
        }
    }
    return pop(&stack2);
}

int peek(){
    int temp;
    if (isempty(&stack1) && isempty(&stack2)){
        printf("queue empty");
        return 0;
    }
    if (isempty(&stack2)){
        while (!isempty(&stack1)){
            temp=pop(&stack1);
            push(&stack2,temp);
        }
    }
    return stack2.pile[stack2.top];
}



int main(){
    int value , choice;
    unsigned total;
   printf("\nenter maximum number of elements to be allowed in queue:");
    scanf("%u",&total);
    stack1.maxnumofelements = total;
    stack1.top = MAXU;
    stack1.pile = (int*)malloc(stack1.maxnumofelements * sizeof(int));

    stack2.maxnumofelements = total;
    stack2.top = MAXU;
    stack2.pile = (int*)malloc(stack2.maxnumofelements * sizeof(int));
    int opcode;
    while(1){
        printf(menu);
        scanf("%d",&opcode);
        switch (opcode)
        {
            case 0 :
                if(isempty(&stack1)&&isempty(&stack2)){
                    printf("\nqueue is empty\n");
                }
                else{
                    printf("\nqueue is not empty\n");
                }
                break;

            case 1:
                printf("\nsize of queue in number of elements is:%u",getsize());
                break;

            case 2:
                if (!isfull()){
                printf("\nenter value to be enqueued:");
                scanf("%d",&value);
                enqueue(value);
                }
                else{
                    printf("\ncan not enqueue ..... queue ovrflow!\n");
                }
                break;

            case 3:
                printf("%d",dequeue());
                break;

            case 4:
                printf("%d",peek());
                break;

            default :

                return 0;


        }

    }

    return 0;



}
