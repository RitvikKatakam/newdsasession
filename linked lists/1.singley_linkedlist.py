class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, val):
        new_node = Node(val)   # ✅ properly indented

        if not self.head:
            self.head = new_node
            return 

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def print_arr(self):   # ✅ added function
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# example usage
if __name__ == '__main__':
    ll = SinglyLinkedList()
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)

    print("LinkedList:")
    ll.print_arr()