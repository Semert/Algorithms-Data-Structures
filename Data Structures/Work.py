# Arrays
# Linked List
# Stack
# queue
# Tree
# Graph

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
        count = 0
        while curNode.next!=None:
            curNode = curNode.next
            count += 1
        return count

    def display(self):
        array = []
        curNode = self.head
        while curNode.next:
            curNode = curNode.next
            array.append(curNode.data)
        print(array)

    def get(self,index):
        if index >= self.length():
            print("noo")
            return
        curNode = self.head
        curInx = 0
        while True:
            curNode = curNode.next
            if(curInx == index):
                return  curNode.data
            curInx += 1

    def erase(self,index):
        if index >= self.length():
            print("go away")
            return

            curNode = self.head
            curInx = 0

            while True:
                pastNode = curNode
                curNode = curNode.next
                if curInx == index:
                    pastNode = curNode.next
                    return
                curInx += 1

myList = LinkedList()

myList.display()

myList.append(1)
myList.append(2)
myList.append(3)

myList.display()
print("element at 2nd index %d" % myList.get(2))

myList.erase(1)
myList.display()
