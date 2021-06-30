import sys
N = int(sys.stdin.readline())


class Node:

    def __init__(self, data,left = None, right=None):

        self.left = left
        self.right = right
        self.data = data

tree = {}
for i in range(N):
    a,b,c = input().split()
    if b == ".":
        b = None
    if c == ".":
        c = None
    tree[a] = Node(a,b,c)
'''
for i in range(N):
    node = t.root.find(tree[i][0])
    if tree[i][1] != "." and tree[i][2] == ".":
        lnode = Node(tree[i][1])
        node.left = lnode
    elif tree[i][2] != "." and tree[i][1] == ".":
        rnode = Node(tree[i][2])
        node.right = rnode
    elif tree[i][2] != "." and tree[i][1] != ".":
        lnode = Node(tree[i][1])
        node.left = lnode
        rnode = Node(tree[i][2])
        node.right = rnode
'''
def preorder(node):
    print(node.data,end='')
    if node.left != None:
        preorder(tree[node.left])
    if node.right != None:
        preorder(tree[node.right])
def inorder(node):
    if node.left != None:
        inorder(tree[node.left])
    print(node.data,end='')
    if node.right != None:
        inorder(tree[node.right])
def postorder(node):
    if node.left != None:
        postorder(tree[node.left])
    if node.right != None:
        postorder(tree[node.right])
    print(node.data,end='')
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])