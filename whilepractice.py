#include<stdio.h> 
#include<conio.h> 
#include<stdlib.h> 
typedef struct node //Structure of a node 
{ 
int data; //Data of node 
struct node *next; //Address 
}node; 
display(node *head) //Funcion to display the list 
{ 
node *temp; 
temp=head; 
printf("Traversed List is:\n\t\t"); 
while(temp!=NULL) 
{ 
printf("%d->",temp->data);   	//Print data of current node 
temp=temp->next;			 //Go to next node 
} 
printf("NULL"); 			//Last node points to NULL 
} 
int main() 
{ 
node *prev,*head,*p; 
int n,i; 
printf("Abhishek Sharma \n12314802719\n"); 
printf("Enter number of elements: "); 
scanf("%d",&n); 
head=NULL; 
for(i=0;i<n;i++) 		//Loop for terminating the elements 
{ 
p=(node*)malloc(sizeof(node)); 
printf("Enter %dth element : ",i); 
scanf("%d",&p->data);	 //Inputing elements of nodes from user 
p->next=NULL; 
if(head==NULL) 
head=p; 
else 
prev->next=p; 
prev=p; 
} 
display(head);			 //Funcion call 
return 0; 
}
