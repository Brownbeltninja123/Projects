global Queue #string 50 elements
global HeadPointer
global TailPointer
#main
Queue = []
HeadPointer = -1
TailPointer = 0


def Enqueue(Input):
    global HeadPointer
    global TailPointer
    global Queue
    if TailPointer == 50:
        print("Error - Queue is Full")
        return "Empty"
    else:
        print("Success")
        Queue.append(Input)
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer-1]


