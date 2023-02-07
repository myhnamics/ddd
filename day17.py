def is_queue_full():
    global size, queue, front, rear
    if rear != size-1:
        return False
    elif rear == size-1 and front == -1:
        return True
    else:
        for i in range(front+1,size):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def en_queue(data):
    global size,queue,front,rear
    if(is_queue_full()):
        print("큐가 꽉참")
        return
    rear += 1
    queue[rear] = data

def is_queue_empty():
    global size,queue,front,rear
    if(front == rear):
        return True
    else:
        return False

def de_queue():
    global size,queue,front,rear
    if(is_queue_empty()):
        "큐가 비엇어"
        return
    front +=1
    data = queue[front]
    queue[front] = None
    return

def peek():
    global size,queue,front,rear
    if is_queue_empty():
        print("큐가 비어잇어")
        return None
    return queue[front+1]

size = 5
queue = [None for _ in range(0,size)]
front = rear = -1

rear += 1
queue[rear] = '메타몽'
rear += 1
queue[rear] = '꼬부기'
rear += 1
queue[rear] = '모부기'

front += 1
data = queue[front]
queue[front] = None
front += 1
data = queue[front]
queue[front] = None
en_queue("피카류")
en_queue("피류")

print('출구')
for i in range(0,len(queue)):
    print(queue[i])
size = len(queue)
en_queue("vlfb")
print(queue)
