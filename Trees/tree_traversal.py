from queue import Queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def preorder(currNode):
    
    if currNode == None:
        return
    print(currNode.data, end=" ")
    preorder(currNode.left)
    preorder(currNode.right)

def inorder(currNode):
    if currNode == None:
        return
    inorder(currNode.left)
    print(currNode.data, end=" ")
    inorder(currNode.right)

def postorder(currNode):
    if currNode == None:
        return
    postorder(currNode.left)
    postorder(currNode.right)
    print(currNode.data, end=" ")

def levelorder(root):
    nodes = Queue()
    nodes.put(root)

    while nodes.empty() == False:
        currNode = nodes.get()
        if currNode.left is not None:
            nodes.put(currNode.left)
        if currNode.right is not None:
            nodes.put(currNode.right)
        print(currNode.data, end=" ")
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)
root.right.right.left = Node(7)
print('Preorder: ',end=" ")
preorder(root)
print()

print('Inorder: ',end=" ")
inorder(root)
print()

print('Postorder: ',end=" ")
postorder(root)
print()

print('Level order: ',end=" ")
levelorder(root)
print()