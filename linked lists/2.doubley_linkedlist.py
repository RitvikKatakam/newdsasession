class Node:
    def __init__(self, head):
        self.head = head
        self.prev = None   # FIXED
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, item):
        new_node = Node(item)

        if not self.head:
            self.head = new_node
            return   # FIXED

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
    
    def print_forward(self):   # FIXED
        temp = self.head
        while temp:
            print(temp.head, end=" <=> ")
            temp = temp.next
        print(None)

    def backward(self):
        temp = self.head
        if not temp:
            return

        # go to last node
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.head, end=' <=> ')
            temp = temp.prev
        print(None)


# example
if __name__ == '__main__':
    dll = DoublyLinkedList()

    dll.insert("rakama")
    dll.insert("gundegari galanthiendhey")
    dll.insert("orange army")

    print("Forward:")
    dll.print_forward()

    print("Backward:")
    dll.backward()