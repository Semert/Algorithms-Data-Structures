class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data) 7

        if self.head is None:
            self.head = new_node 5
            return

        cur_node = self.head 5
        while cur_node.next != None:
            cur_node = cur_node.next 5
        cur_node.next = new_node 6

    # def print_helper(self, node, name):
    #     if node is None:
    #         print(name + ": None")
    #     else:
    #         print(name + ":" + node.data)



mylist = LinkedList()

mylist.append("A")
mylist.append("B")
mylist.append("C")
mylist.print_list()