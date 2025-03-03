class Node:
    '''Create a Linked List Node with a value'''
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    '''Create a Linked List with a node'''
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        # Edge case: the ll is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        temp = self.head
        if self.head is None:
            print("there's nothing to pop because the list is empty")
            return None
        elif self.length == 1:
            node = self.head
            self.length -= 1
            self.head = None
            self.tail = None
            return node
        else:
            for n in range((self.length - 1)):
                if n == (self.length - 2): # penultimo elemento
                    next = temp.next
                    temp.next = None
                    self.tail = temp
                    self.length -= 1
                    return next
                n += 1
                temp = temp.next
                

my_ll = LinkedList(21)
my_ll.append(14)
my_ll.append(7)
print(f"head 1 > {my_ll.head.value}")
print(f"tail 1 > {my_ll.tail.value}")

popped = my_ll.pop()
print(f"popped: {popped.value}")
print(my_ll.tail.value)
print(my_ll.head.value)
