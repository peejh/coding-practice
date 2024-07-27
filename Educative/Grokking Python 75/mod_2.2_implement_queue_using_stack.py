# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5359382799974400/4603992877432832

from utils.stack import Stack

class MyQueue(object):

    def __init__(self):
        self.stack = Stack()
        # in official solution, stack2 declared here

    def push(self, x):
        if self.stack.is_empty(): # in official solution, this is redundant
            self.stack.push(x)
        else:
            stack2 = Stack() # in official solution, this is declared as an object variable
            while not self.stack.is_empty():
                stack2.push(self.stack.pop())
            self.stack.push(x)
            while not stack2.is_empty():
                self.stack.push(stack2.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.top()

    def empty(self):
        return self.stack.is_empty()