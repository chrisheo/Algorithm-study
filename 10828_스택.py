import sys
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.cnt = 0
    def append(self, data):
        new_node = Node()
        new_node.data = data
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        
    def get_node(self, index):
            cnt = 0
            node = self.head
            while cnt < index:
                cnt += 1
                node = node.next
            return node
    def add_node(self, value):
            new_node = Node()
            new_node.data = value
            cur = self.head
            if cur == None:
                self.head = new_node
            else:
                while cur.next is not None:
                    cur = cur.next
                cur.next = new_node
    def delete_node(self):
            if self.cnt == 0:
                pass
            else:
                node = self.get_node(ll.cnt - 1)
                node.next = None
ll = LinkedList()
for _ in range(int(input())):
    cmd = sys.stdin.readline().strip()
    if cmd == "pop":
        temp = Node()
        temp.data = ll.get_node(ll.cnt).data
        ll.delete_node() 
        if temp.data == None:
            print(-1)
        else:
            print(temp.data)
            ll.cnt -= 1
           
    elif cmd == "size":
        print(ll.cnt)
    elif cmd == "empty":
        print(int(ll.cnt == 0))
    elif cmd == "top":
        temp = Node()
        temp.data = ll.get_node(ll.cnt).data
        if temp.data == None:
            print(-1)
        else:
            print(temp.data)
    else:
        X = int(cmd[5:])
        ll.add_node(X)
        ll.cnt += 1

