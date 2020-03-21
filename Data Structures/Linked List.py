"""
linked List Data Structure.
"""

class Node:   # İlk olarak Node kuruyoruz. LinkedList'in subClass'ı.
    def __init__(self,data=None):  # Eğer data verilmez ise None
        self.data = data
        self.next = None     # Bir Node Data'ya ve Next'e sahip.

class LinkedList:
    def __init__(self):
        self.head = Node()   # Ilk node [Head]

    def append(self,data):  #  Node ekle
        yeni_node = Node(data)   # yeni node için Node class'ını kullanıyoruz.
        cur = self.head          # Ilk node olan head'ı belirleyip ondan sonraki nodelara ekleme yapıyoruz.
        print(self.head.data,self.head.next)
        while cur.next != None:  # Eğer current node'un next'i boş değilse..
            cur = cur.next       # Next node'u current node'a ata.
        cur.next = yeni_node    # Current node'un next'i boş ise, yeni kurduğumuz nodu next'e ata.

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return  total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self,index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.display()


# curNode.next unutma.
# class Node:
#     def __init__(self,data=None):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = Node()
#
#     def append(self,data):
#         newNode = Node(data)
#         curNode = self.head
#         while curNode.next!=None:
#             curNode = curNode.next
#         curNode.next = newNode
#
#     def length(self):
#         curNode = self.head
#         total = 0
#         while curNode.next!=None:
#             total += 1
#             curNode = curNode.next
#         return total

