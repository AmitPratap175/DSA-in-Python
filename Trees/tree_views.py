from queue import Queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.orientation = 0


def leftView(root):
    nodes = Queue()
    nodes.put(None)
    nodes.put(root)

    while nodes.empty() == False:
        currNode = nodes.get()
        if currNode == None:
            if nodes.empty() == True:
                break
            nodes.put(None)
            currNode = nodes.get()
            print(currNode.data,end=" ")
        if currNode.left is not None:
            nodes.put(currNode.left)
        if currNode.right is not None:
            nodes.put(currNode.right)

def rightView(root):
    nodes = Queue()
    nodes.put(None)
    nodes.put(root)

    while nodes.empty() == False:
        currNode = nodes.get()

        
        if currNode == None:
            if nodes.empty() == True:
                break
            nodes.put(None)
            continue
        if nodes.queue[0] == None:
            print(currNode.data,end=" ")
        if currNode.left is not None:
            nodes.put(currNode.left)
        if currNode.right is not None:
            nodes.put(currNode.right)
def topView(root):
    nodes = Queue()
    nodes.put(root)

    traversed = dict()

    while nodes.empty() == False:
        currNode = nodes.get()
        currOrientation = currNode.orientation

        if currOrientation not in traversed:
            traversed[currOrientation] = currNode.data
        
        if currNode.left != None:
            currNode.left.orientation = currOrientation - 1
            nodes.put(currNode.left)
        if currNode.right != None:
            currNode.right.orientation = currOrientation + 1
            nodes.put(currNode.right)
    
    for i in sorted(traversed):
        print(traversed[i],end=" ")

def bottomView(root):
    nodes = Queue()
    nodes.put(root)

    traversed = dict()

    while nodes.empty() == False:
        currNode = nodes.get()
        currOrientation = currNode.orientation

        # if currOrientation not in traversed:
        traversed[currOrientation] = currNode.data
        
        if currNode.left != None:
            currNode.left.orientation = currOrientation - 1
            nodes.put(currNode.left)
        if currNode.right != None:
            currNode.right.orientation = currOrientation + 1
            nodes.put(currNode.right)
    
    for i in sorted(traversed):
        print(traversed[i],end=" ")


    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)
root.right.left = Node(7)

print('Left order: ',end=" ")
leftView(root)
print()

print('right order: ',end=" ")
rightView(root)
print()

print('top order: ',end=" ")
topView(root)
print()

print('bottom order: ',end=" ")
bottomView(root)
print()