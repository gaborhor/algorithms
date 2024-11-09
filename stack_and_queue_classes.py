from collections import deque

class MyStack:
    def __init__(self, type):
        self.elemType = type
        self.state = []
    def empty(self):
        return len(self.state) == 0

    def top(self):
        """Returns the top element of a nonempty stack, without removing"""
        if self.empty():
            raise IndexError("Requested top of empty stack")
        else:
            return self.state[-1]

    def push(self, elem):
        """Adds an element to the top of a stack"""
        assert type(elem) == self.elemType
        self.state.append(elem)

    def pop(self):
        """Removes an element from top of a nonempty stack"""
        if not self.empty():
            return self.state.pop()
        else:
            raise IndexError("Cannot pop from empty stack")


class MyQueue:
    def __init__(self, type):
        self.elemType = type
        self.queue = deque()
    def empty(self):
        return len(self.queue) == 0

    def front(self):
        """Returns the Head element of a nonempty queue, without removing. Head is defined as Left side."""
        if self.empty():
            raise IndexError("Requested front of empty queue")
        else:
            return self.queue[0]
    def enqueue(self, elem):
        """Adds an element to the Tail of a queue. Tail is defined as Right side."""
        assert type(elem) == self.elemType
        self.queue.append(elem)

    def dequeue(self):
        """Removes an element from the Head of a nonempty queue. Head is defined as Left side."""
        if not self.empty():
            return self.queue.popleft()
        else:
            raise IndexError("Cannot pop from empty stack")





# Testing code for stack
# s = MyStack(int)    # initialize stack instance containing 'int' type elements
# print(s.empty())    # stack currently empty, should return True
# s.push(5)           # append int '5' to top of stack
# s.push(8)           # append int '8' to top of stack
# print(s.pop())      # pop int '8' from top of stack + print
# s.push(3)           # append int '3' to top of stack
# print(s.empty())    # stack not currently empty -> return False
# print(s.top())      # int '3' currently at top of stack + print
# print(s.pop())      # pop int '3' from top of stack + print
# print(s.pop())      # pop int '5' from top of stack + print
# print(s.pop())      # should generate an error

# Testing code for Queue
# q = MyQueue(int)    # initialize queue instance containing 'int' type elements
# print(q.empty())    # queue currently empty -> return True
# q.enqueue(5)        # append int '5' to Tail of queue (right)
# q.enqueue(8)        # append int '8' to Tail of queue (right)
# print(q.dequeue())  # popleft int '5' from Head of queue (left) + print
# q.enqueue(3)        # append int '3' to Tail of queue (right)
# print(q.empty())    # queue not empty -> return False
# print(q.front())    # int '8' currently at Head of queue + print
# print(q.dequeue())  # popleft int '8' from Head of queue (left) + print
# print(q.dequeue())  # popleft int '3' from Head of queue (left) + print
# print(q.dequeue())  # should generate an error