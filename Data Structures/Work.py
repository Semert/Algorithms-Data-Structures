
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        newNode = Node(data)
        curNode = self.head
        while curNode.next!=None:
            curNode = curNode.next
        curNode.next = newNode

    def length(self):
        curNode = self.head
        total = 0
        while curNode.next!=None:
            total += 1
            curNode = curNode.next
        return total

    def display(self):
        elements = []
        curNode = self.head
        while curNode.next!=None:
            curNode = curNode.next
            elements.append(curNode.data)
        print(elements)

    def get(self,index):
        if index >= self.length():
            print("Error Out of Index")
            return None
        curIndex = 0
        curNode = self.head
        while True:
            curNode = curNode.next
            if(curIndex == index):
                return curNode.data
            curIndex += 1


    def erase(self,index):
        if index >= self.length():
            print("Error Out of Index")
            return None
        curIndex = 0
        curNode = self.head
        while True:
            lastNode = curNode
            curNode = curNode.next
            if curIndex==index:
                lastNode.next = curNode.next
                return
            curIndex += 1


myList = LinkedList()

myList.display()

myList.append(1)
myList.append(2)
myList.append(3)

myList.display()
print("element at 2nd index %d" % myList.get(2))

myList.erase(1)
myList.display()
