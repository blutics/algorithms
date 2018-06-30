#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
  int data;
  struct Node* next;
  struct Node* before;
}Node;

typedef struct List{
  Node* head;
  Node* tail;
  int count;
}List;

Node* makeNode(int data){
  Node* new = (Node*)malloc(sizeof(Node));
  new->data=data;
  return new;
}

List* makeList(){
  List* new = (List*)malloc(sizeof(List));
  new->count = 0;
  return new;
}

void addNode(List* mlist, int data){
  List* list = mlist;
  if(list->count==0){
    list->head = makeNode(data);
    list->tail = list->head;
    list->head->next=NULL;
  }else{
    Node* added = makeNode(data);
    list->tail->next = added;
    added->before = list->tail;
    list->tail=added;
    added->next=NULL;
  }
  list->count++;
}

void delNode(List* list, int index){
  int i = 0;
  Node* tmp = list->head;
  while(i<index){
    tmp = tmp->next;
    i++;
  }
  if(tmp==list->head){
    list->head = list->head->next;
    list->head->before = NULL;
  }else if(tmp==list->tail){
    list->tail = list->tail->before;
    list->tail->next = NULL;
  }else{
    tmp->before->next = tmp->next;
    tmp->next->before = tmp->before;
  }
  free(tmp);
}
void displayList(List* list){
  Node* tmp=list->head;
  int i = 0;
  while(1){
    if (tmp==NULL){
      break;
    }
    printf("index[%d] : %d\n",i,tmp->data);
    i+=1;
    tmp=tmp->next;
  }
}

int main(){
  List* list = makeList();
  addNode(list,323);
  addNode(list,33333);
  addNode(list,1211);
  addNode(list,4442);
  addNode(list,41);
  printf("hello world\n");
  delNode(list,2);
  displayList(list);
  system("pause");
  return 0;
}
