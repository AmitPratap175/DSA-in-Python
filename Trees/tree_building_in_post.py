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

def search(inorder_, val, left, right):
    for i in range(left, right+1):
        if inorder_[i] == val:
            return i
    return -1

def build_tree(inorder_, postorder_,idx, left, right):
    if left > right or idx <= 0:
        return None
    # print(idx, left, right)
    
    val = postorder_[idx]
    idx -= 1

    root_tmp = Node(val)
    idx_in = search(inorder_, val, left, right)

    root_tmp.right = build_tree(inorder_, postorder_, idx, idx_in +1, right)
    root_tmp.left = build_tree(inorder_, postorder_, idx, left, idx_in-1)
    

    return root_tmp

    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)
# root.right.right.left = Node(7)
# print('Preorder: ',end=" ")
# preorder(root)
# print()

print('Inorder: ',end=" ")
inorder(root)
print()

print('Postorder: ',end=" ")
postorder(root)
print()

preorder_ = [1,2,4,5,3,6]
inorder_ = [4,2,5,1,3,6]
postorder_ = [4,5,2,6,3,1]
print(f"len: {len(preorder_)}")
root_tmp = build_tree(inorder_, postorder_, len(postorder_)-1,0,len(preorder_)-1)

print('Inorder: ',end=" ")
inorder(root)
print()

print('Postorder: ',end=" ")
postorder(root)
print()