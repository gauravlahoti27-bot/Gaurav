#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct stack{
    int size;
    int top;
    char *arr;
};

char stackTop(struct stack* sp)
{
    return sp->arr[sp->top];
}

int precedence(char c)
{
    if(c=='*' || c=='/')
        return 2;
    else if(c=='+' || c=='-')
        return 1;
    else
        return 0;
}

int isOperand(char c)
{
    if((c>='0' && c<='9') ||
       (c>='a' && c<='z') ||
       (c>='A' && c<='Z'))
        return 1;
    else
        return 0;
}

char* InfixToPostfix(char* infix)
{
    struct stack* sp=(struct stack*)malloc(sizeof(struct stack));

    sp->size=strlen(infix);
    sp->top=-1;
    sp->arr=(char*)malloc(sp->size*sizeof(char));

    char* postfix=(char*)malloc((strlen(infix)+1)*sizeof(char));

    int i=0,j=0;

    while(infix[i]!='\0')
    {
        if(isOperand(infix[i]))
        {
            postfix[j++]=infix[i++];
        }
        else
        {
            while(sp->top!=-1 &&
                  precedence(infix[i])<=precedence(stackTop(sp)))
            {
                postfix[j++]=stackTop(sp);
                sp->top--;
            }

            sp->top++;
            sp->arr[sp->top]=infix[i++];
        }
    }

    while(sp->top!=-1)
    {
        postfix[j++]=stackTop(sp);
        sp->top--;
    }

    postfix[j]='\0';

    return postfix;
}

int main()
{
    char infix[100];

    printf("Enter infix expression: ");
    scanf("%s",infix);

    char* postfix=InfixToPostfix(infix);

    printf("Postfix expression: %s\n",postfix);

    return 0;
}