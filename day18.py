class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(nameAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end='  ')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visitedAry = []  # 방문한 노드

    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(gsize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                    pass
                else:  # 방문한 적이 없으면 다음 정점으로 지정
                    next = vertex
                    break

        if next != None:  # 다음에 방문할 정점이 있는 경우
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:  # 다음에 방문할 정점이 없는 경우
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False

nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산' ]
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

gsize = 6
G1 = Graph(gsize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print('전체 연결도')
printGraph(G1)

edge_array = []
for i in range(gsize):
    for k in range(gsize):
        if G1.graph[i][k] != 0:
            edge_array.append([G1.graph[i][k], i, k])

from operator import itemgetter
edge_array = sorted(edge_array, key = itemgetter(0), reverse=True)

new_array = []
for i in range(0, len(edge_array), 2):
    new_array.append(edge_array[i])

index = 0
print(edge_array)
print(new_array)
while (len(new_array)) > (gsize-1):
    start = new_array[index][1]
    end = new_array[index][2]
    save_cost = new_array[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    start_connect = findVertex(G1, start)
    end_connect = findVertex(G1,end)

    if start_connect and end_connect:
        del(new_array[index])
    else:
        G1.graph[start][end] = save_cost
        G1.graph[end][start] = save_cost
        index += 1
print('최소비용 자전거 도로')
printGraph(G1)
