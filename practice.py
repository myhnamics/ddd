def is_queue_full():
    global size, queue, front, rear
    if (rear + 1) % size == front:
        return True
    else:
        return False


def en_queue(data):
    global size, queue, front, rear
    if (is_queue_full()):
        print("큐가 꽉참")
        return
    rear = (rear + 1) % size
    queue[rear] = data


def is_queue_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def de_queue():
    global size, queue, front, rear
    if (is_queue_empty()):
        "큐가 비엇어"
        return
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비어잇어")
        return None
    return queue[(front + 1) % size]


size = 5
queue = [None for _ in range(0, size)]
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
for i in range(0, len(queue)):
    print(queue[i])
size = len(queue)
en_queue("vlfb")

# input
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            en_queue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E' or select == 'e':
            data = de_queue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
