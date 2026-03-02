#MENU DRIVER PROGRAM TO PERFORM ENQUEUE OR DEQUEUE OERATIONS
Queue=[]
def Enqueue(q,e):
    q.append(e)
    print("Element inserted successfully😍")
def Dequeue(q):
    if q!=[]:
        q.pop(0)
    else:
        print("UNDERFLOW⚠️Empty list, No element to remove")
    print("Element removed successfully😍")
def Peek(q):
    if q!=[]:
        print("Element at the front is:🥇",q[0]) 
    else:
        print("UNDERFLOW⚠️Empty list, No element to show")
def Display(Q):
    print("Your Queue is🤗:",Q)

while True:
    print("-----QUEUE OPERATIONS----")
    print("-----1.ENQUEUE----")
    print("-----2.DEQUEUE----")
    print("-----3.PEEK----")
    print("-----4.DISPLAY----")
    print("-----5.EXIT----")
    ch=int(input("Enter your choice between 1-5🤔: "))
    if ch==1:
        elm=int(input("Enter the element to be inserted🥱: "))
        Enqueue(Queue,elm)
    elif ch==2:
        Dequeue(Queue)
    elif ch==3:
        Peek(Queue)
    elif ch==4:
        Display(Queue)
    elif ch==5:
        break
    else:
        print("Wrong choice😣,Enter between 1-5😒")