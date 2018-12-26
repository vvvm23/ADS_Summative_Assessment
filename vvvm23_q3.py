def good_expression(expression):
    good = True
    
    ''' Some rules:
        If the expression contains no brackets it is good.
        If the expression is entirely encompassed in brackets it is not good
        If part of the expression is encompasses in bracket and only contains
        ...multiplication then it is not good
        If part of an expression is also encompassed in brackets then it is
        ..not good eg. ((3+2))
        If part of an expression is encompasses in brackets and contains only
        ..addition and is also surrounded in addition operators then it is
        ..not good. [IS THIS REDUNDANT?]
    '''

    ''' Better ruleset
        Check these rules recursively every time an open bracket is encountered:
        If expression entirely encompasses in brackets then not good
        If entirely consists of multiplication then it is not good
        ..except for highest level
        If expression is surrounded in addition operators or nothing then it is not good.
        ..except for highest level.
        If any of these rules are triggered ignore everything else and return false
        ..at highest level.
    '''

    ''' Implementation Plan

    '''
    return good

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after