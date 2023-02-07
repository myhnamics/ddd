class Node():
    def __init__(self):
        self.data = None
        self.data = None

def print_nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
    print()

def find_node(find_data):
    global memory, head, current, pre

    current = head
    if current.data == find_data:
        return current
    while current.link != head :
        current = current.link
        if current.data == find_data:
            return current
    return Node()

memory = []
head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]  # 첫 번째 노드
    head = node
    node.link = head
    memory.append(node)

    for data in data_array[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    print_nodes(head)
    print(find_node("다현").data)


