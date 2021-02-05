__author__ = "Erik Stroud, 7"
""" 
    Builds and returns a string with all of the values on the Stack from the top of the stack to the bottom 
    of the stack on a single line with no spaces.The first three lines of output would then be:
    1453 16 5AD
    1453 8 2655
    1453 2 10110101101
    :param fileName: 
    :return: a string representation of the stack
"""

def to_string(n,base):
    convert_string = "0123456789ABCDEF"
    if n < base:                 
        rStack.push(convert_string[n])
    else:
        rStack.push(convert_string[n % base])
        to_string(n // base, base)     

def main():
    global rStack
    rStack = Stack()
    data = [(1453, 16), (1453, 8), (1453, 2), (32016, 16), (32016, 8),(32016, 2)]
    for n, base in data:
        to_string(n, base)
        print(n, base, rStack)
        while(not rStack.is_empty()):
            rStack.pop()

class Stack:
    """ A Stack is a LIFO data structure.
        One instance variable:
            stack: A DLL.
        Six methods, all running in constant time:
            constructor
            isEmpty
            push
            pop
            peek
            size
    """

    def __init__(self):
        """
        Initializes the stack with an empty Doubly Linked List.
        :return: The reference for self.
        """
        self.stack = DoublyLinkedList()

    def __str__(self):
        """
        Dunder method used to build and return a string from stack
        :return:
        The string made from the stak data
        """
        newString = ''
        temp = self
        for i in range(temp.size()):
            newString +=str(temp.stack.at_index(i))
        return str(newString)


    def is_empty(self):
        """
        Checks the size of the stack
        :return: True if the stack is empty, False otherwise.
        """
        return self.stack.size == 0

    def push(self, item):
        """
        Places the item onto the top of the stack.
        :param item: the object to be added to the stack
        :return: None
        """
        self.stack.add_front(item)

    def pop(self):
        """
        Removes the object on top of the stack.
        :return: The top object on the stack.
        """
        return self.stack.remove_front()

    def peek(self):
        """
        Looks at the object on top of the stack.
        :return: The top object on the stack.
        """
        return self.stack.tail.data

    def size(self):
        """
        Determines the size of the stack in constant time.
        :return: The size of the stack.
        """
        return self.stack.size


class DoublyLinkedNode:
    """ A single node in a doubly-linked list.
        Contains 3 instance variables:
            data: The value stored at the node.
            prev: A pointer to the previous node in the linked list.
            next: A pointer to the next node in the linked list.
    """

    def __init__(self, value):
        """
        Initializes a node by setting its data to value and
        prev and next to None.
        :return: The reference for self.
        """
        self.data = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    The doubly-linked list class has 3 instance variables:
        head: The first node in the list.
        tail: The last node in the list.
        size: How many nodes are in the list.
    """

    def __init__(self):
        """
        The constructor sets head and tail to None and the size to zero.
        :return: The reference for self.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def add_front(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        front of the list.
        :return: None
        """
        new_node = DoublyLinkedNode(value)
        if (self.size == 0):
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def add_rear(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        rear of the list.
        :return: None
        """
        new_node = DoublyLinkedNode(value)
        if (self.size == 0):
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def remove_front(self):
        """
        Removes the node in the front of the list.
        :return: The data in the deleted node.
        """
        value = self.head.data
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None
        self.size -= 1
        return value

    def remove_rear(self):
        """
        Removes the node in the rear of the list.
        :return: The data in the deleted node.
        """
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None
        self.size -= 1
        return value

    def print_out(self):
        """
        Prints out the list from head to tail all on one line.
        :return: None
        """
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


    def print_reverse(self):
        """
        Prints out the list from tail to head all on one line.
        :return: None
        """
        temp = self.tail
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.prev
        print()


    def at_index(self, index):
        """
        Retrieves the data of the item at index.
        :param index: The index of the item to retrieve.
        :return: Returns the data of the item.
        """
        count = 0
        temp = self.head
        while count < index:
            count += 1
            temp = temp.next
        if not temp:
            return None
        return temp.data


if __name__ == '__main__':
    main()
