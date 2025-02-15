class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class stack:
    def __init__(self, val):
        self.head = node(val)
        self.size = 0

    def getSize(self):
        return self.size
    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def push(self, val):
        temp = node(val)
        temp.next = self.head.next
        self.head.next = temp

    def pop(self):
        removed = self.head.next
        self.head.next = self.head.next.next
        return removed
    
