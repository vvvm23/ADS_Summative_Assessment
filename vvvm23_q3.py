def good_expression(expression):

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
    # Ideally don't have these two expressions
    '''if not ('(' in expression or ')' in expression):
        return True
    if expression[0] == '(' and expression[-1] == ')':
        return False
    if not ('+' in expression):
        return False'''

    expression_stack = Stack()
    expression_level = 0
    expression_index = -1
    expression_list = []
    take_after = False

    for c in expression:
        if c == '(':
            expression_list.append(Expression())
            expression_level += 1
            expression_index += 1
            if expression_stack.isEmpty():
                expression_list[expression_index].before = ''
            else:
                expression_list[expression_index].before = expression_stack.top()
        if c == '+' and expression_level > 0:
            expression_list[expression_index].contains_add = True

        expression_stack.push(c)
        if take_after:
            expression_list[expression_index].after = expression_stack.top()
            take_after = False
            if expression_list[expression_index].before in ['', '+', '(', ')'] and expression_list[expression_index].after in ['', '+', '(', ')']:
                return False

        if c == ')':
            if not expression_list[expression_index].contains_add:
                return False

            take_after = True
            if c == expression[-1] and expression_list[expression_index].before in ['', '+']:
                return False

            expression_level -= 1

    return True

class Expression:
    def __init__(self):
        self.before = ''
        self.after = ''
        self.contains_add = False

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

########################################################################################################################
assert good_expression("1+2+3+4")
assert not good_expression("(1+2+3+4)")
assert good_expression("(1+2)*3+4")
assert not good_expression("((1+2))*3+4")
assert good_expression("1+2*3+4")
assert not good_expression("1+(2*3)+4")
assert good_expression("1*2+3+4")
assert not good_expression("1*2+(3+4)")
print ("all tests passed\n")