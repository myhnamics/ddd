class tree_node():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = tree_node()
node1.data = "가"

node2 = tree_node()
node2.data = "나"
node1.left = node2

node3 = tree_node()
node3.data = "다"
node1.right = node3

node4 = tree_node()
node4.data = "라"
node2.left = node4

node5 = tree_node()
node5.data = "마"
node2.right = node5

node6 = tree_node()
node6.data = "바"
node3.left = node6

def preorder(node):     #재귀함수
    if node == None:
        return
    print(node.data,end = '->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data,end = '->')
    inorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data,end = '->')

print('preorder')
preorder(node1)
print('end')
print('inorder')
inorder(node1)
print('end')

print('postorder')
postorder(node1)
print('end')