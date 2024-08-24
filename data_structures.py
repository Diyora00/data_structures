from collections import deque


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            return
        return Exception('Stack is empty')

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = deque()

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop()
            return
        return Exception('Queue is empty')

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.appendleft(item)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return Exception('Queue is empty')

    def size(self):
        return len(self.queue)


def test_queue():
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(38)
    q1.enqueue(5)
    print(q1.queue)
    q1.dequeue()
    q1.dequeue()
    print(q1.queue)
    print(q1.peek())
    print(q1.size())
    print(q1.is_empty())


def test_stack():
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(7)
    print(s1.stack)
    print(s1.peek())
    print(s1.size())
    print(s1.is_empty())
    s1.pop()
    s1.pop()
    print(s1.stack)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LList:
    def __init__(self):
        self.head = None

    def show_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def add_to_beginning(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def add_to_end(self, new_data):
        node = Node(new_data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def insert(self, prev_node, new_data):
        node = Node(new_data)
        node.next = prev_node.next
        prev_node.next = node

    def delete(self, node):
        prev_node = None
        node_to_delete = None
        current_node = self.head
        while current_node.next:
            if current_node == node:
                node_to_delete = node
                break
            current_node = current_node.next

        if not self.head == node_to_delete:
            current_node = self.head
            while current_node.next:
                if current_node.next == node_to_delete:
                    prev_node = current_node
                    break
                current_node = current_node.next
            prev_node.next = node_to_delete.next
            del node_to_delete


def test_linked_list():
    node1 = Node('sally')
    node2 = Node('vali')
    node3 = Node('ali')

    my_li = LList()
    my_li.head = node1
    node1.next = node2
    node2.next = node3

    my_li.show_all()
    my_li.add_to_beginning('dobby')
    my_li.add_to_end('bobby')
    print('----------------------')
    my_li.show_all()
    print('----------------------')
    my_li.insert(node3, 'alisher')
    my_li.show_all()
    my_li.delete(node3)
    my_li.delete(node2)
    my_li.delete(my_li.head)
    print('----------------------')
    my_li.show_all()
